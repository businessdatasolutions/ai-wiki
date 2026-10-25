"""Offline tests for the yt-dlp caption fallback in fetch_transcript.py.

Run from the repo root:
    python -m unittest discover -s .claude/skills/youtube-transcript-skill/tests
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import fetch_transcript as ft  # noqa: E402

# A rolling auto (ASR) track as YouTube serves it (copied from the shape of a
# real en-orig file): every real cue repeats the previous line above the new
# one, and each is followed by a ~10 ms hold cue. The FIRST cue's "previous
# line" is a single space, not an empty line; a parser that ends the cue on a
# whitespace-only line drops the opening words (it cost two transcripts their
# first sentence on 2026-10-25). The one-word line "frontier." carries no inline
# timing tag (2026-10-03).
ROLLING_ASR = "\n".join([
    "WEBVTT",
    "Kind: captions",
    "Language: en",
    "",
    "00:00:00.160 --> 00:00:02.310 align:start position:0%",
    " ",
    "we<00:00:00.480><c> are</c><00:00:00.800><c> at</c><00:00:01.120><c> the</c>",
    "",
    "00:00:02.310 --> 00:00:02.320 align:start position:0%",
    "we are at the",
    " ",
    "",
    "00:00:02.320 --> 00:00:04.150 align:start position:0%",
    "we are at the",
    "frontier.",
    "",
    "00:00:04.150 --> 00:00:04.160 align:start position:0%",
    "frontier.",
    " ",
    "",
    "00:00:04.160 --> 00:00:06.000 align:start position:0%",
    "frontier.",
    "&gt;&gt; Next<00:00:04.500><c> speaker</c><00:00:05.000><c> here.</c>",
    "",
])

# A human-written track: a two-line cue holds two NEW lines, not a repeat.
MANUAL_TWO_LINE = """WEBVTT

00:00:00.000 --> 00:00:03.000
Will AI take your job?
Or will it work for you?

00:00:03.000 --> 00:00:05.500
AI can analyze medical scans.
"""


class ParseVtt(unittest.TestCase):
    def test_rolling_track_yields_each_new_line_once(self):
        cues = ft.parse_vtt(ROLLING_ASR, keep_all=False)
        self.assertEqual([text for _, text in cues], ["we are at the", "frontier.", ">> Next speaker here."])

    def test_rolling_track_keeps_cue_start_times(self):
        cues = ft.parse_vtt(ROLLING_ASR, keep_all=False)
        self.assertEqual([start for start, _ in cues], [0.16, 2.32, 4.16])

    def test_manual_track_keeps_both_lines_of_a_two_line_cue(self):
        # The last-line rule dropped 164 lines of a DW Shift report (2026-10-25).
        cues = ft.parse_vtt(MANUAL_TWO_LINE, keep_all=True)
        self.assertEqual(cues, [(0.0, "Will AI take your job? Or will it work for you?"),
                                (3.0, "AI can analyze medical scans.")])


class SegmentsFromCues(unittest.TestCase):
    def test_merges_until_a_sentence_ends_after_four_seconds(self):
        cues = [(0.0, "So the question"), (2.0, "is not which jobs."), (5.0, "It is how"), (9.5, "work changes.")]
        self.assertEqual(ft.segments_from_cues(cues), [
            {"ts": "0:00", "text": "So the question is not which jobs. It is how work changes."},
        ])

    def test_splits_at_a_sentence_end_once_four_seconds_have_passed(self):
        cues = [(0.0, "First point."), (4.0, "Still first."), (6.0, "Second point.")]
        self.assertEqual(ft.segments_from_cues(cues), [
            {"ts": "0:00", "text": "First point. Still first."},
            {"ts": "0:06", "text": "Second point."},
        ])

    def test_caps_a_segment_at_twenty_seconds_without_punctuation(self):
        cues = [(0.0, "and so on"), (10.0, "and so forth"), (20.0, "and then"), (25.0, "more")]
        segs = ft.segments_from_cues(cues)
        self.assertEqual([s["ts"] for s in segs], ["0:00", "0:25"])

    def test_formats_hour_timestamps(self):
        self.assertEqual(ft.segments_from_cues([(3605.4, "Late in the stream.")]),
                         [{"ts": "1:00:05", "text": "Late in the stream."}])


class PickVtt(unittest.TestCase):
    def test_prefers_a_human_track_over_the_original_asr(self):
        files = [Path("x.en-orig.vtt"), Path("x.en.vtt")]
        self.assertEqual(ft.pick_vtt(files), (Path("x.en.vtt"), "manual"))

    def test_falls_back_to_the_original_asr_track(self):
        self.assertEqual(ft.pick_vtt([Path("x.en-orig.vtt")]), (Path("x.en-orig.vtt"), "asr"))

    def test_returns_none_when_there_are_no_tracks(self):
        self.assertIsNone(ft.pick_vtt([]))


class NeedsFallback(unittest.TestCase):
    def _result(self, last_ts, length_seconds=3000):
        segs = [{"ts": "0:00", "text": "a"}] + ([{"ts": last_ts, "text": "b"}] if last_ts else [])
        return {"metadata": {"length_seconds": length_seconds}, "transcript": segs if last_ts else []}

    def test_empty_transcript_needs_fallback(self):
        self.assertTrue(ft.needs_fallback(self._result(None)))

    def test_transcript_ending_more_than_ten_minutes_early_needs_fallback(self):
        # A long panel can come back silently truncated (2026-10-03).
        self.assertTrue(ft.needs_fallback(self._result("39:00")))

    def test_transcript_reaching_the_end_does_not(self):
        self.assertFalse(ft.needs_fallback(self._result("49:30")))


if __name__ == "__main__":
    unittest.main()
