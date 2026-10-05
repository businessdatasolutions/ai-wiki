"""How an LLM Wiki works: the LLM compiles raw sources into a persistent,
interlinked wiki, keeps it current on every ingest, answers questions from it
(plus the raw sources), files good answers back, and lints it.

Companion to animations/rag-explainer. Based on Karpathy's LLM Wiki pattern
(llm-wiki.md in this repo) and SmartScope's "LLM Wiki Architecture" article.

Built with 3Blue1Brown's manim (manimgl, https://github.com/3b1b/manim).

Render (headless):
    xvfb-run -a -s "-screen 0 1920x1080x24" manimgl llm_wiki_explainer.py LlmWikiExplainer -w --hd
"""
from manimlib import *
import numpy as np

FONT = "IBM Plex Sans"
MONO = "IBM Plex Mono"

BG = "#0d1117"
PANEL = "#151b23"
CARD = "#1b232d"
GRID = "#2a3440"
INK = "#e6edf3"
MUTED = "#7d8a99"
LINK = "#4f5d6d"
QUERY = "#ffd166"
ANSWER = "#8ce0b5"
ALERT = "#ff7b72"
AMBER = "#f2b04c"

KINDS = {
    "source": ("SOURCE", "#a7b3c0"),
    "entity": ("ENTITY", "#6fb3ff"),
    "concept": ("CONCEPT", "#ff9f5a"),
    "synthesis": ("SYNTHESIS", "#8ce0b5"),
}

RAW_X = (-6.90, -4.25)
WIKI_X = (-2.35, 6.90)
PANEL_Y = (-3.35, 2.95)
GRAPH_RIGHT = 4.45          # pages live left of this; index/log column to the right
LLM_POS = np.array([-3.30, -0.30, 0.0])
BAR_Y = 3.55

# wiki pages: key -> (kind, title, x, y)
PAGES = {
    "S1": ("source", "Mars dust survey", -1.25, 2.20),
    "C1": ("concept", "Iron oxide", -1.25, 0.75),
    "C4": ("concept", "Perchlorates", -1.25, -0.70),
    "S2": ("source", "Perseverance samples", -1.25, -2.15),
    "E1": ("entity", "Mars", 1.10, 1.45),
    "E2": ("entity", "Perseverance", 1.10, -1.40),
    "C2": ("concept", "Habitability", 3.40, -0.35),
    # added later
    "S3": ("source", "Subsurface ice radar", 3.40, 2.20),
    "C3": ("concept", "Subsurface ice", 3.40, 1.15),
    "Y1": ("synthesis", "Life on Mars today?", 3.40, -2.15),
}
INITIAL = ["S1", "C1", "C4", "S2", "E1", "E2", "C2"]
INITIAL_LINKS = [("S1", "E1"), ("S1", "C1"), ("C1", "E1"), ("S2", "E2"),
                 ("E2", "E1"), ("E2", "C2"), ("E1", "C2")]


def txt(s, size=20, color=INK, font=FONT, **kw):
    return Text(s, font=font, font_size=size, **kw).set_color(color)


def fit(m, width):
    if m.get_width() > width:
        m.set_width(width)
    return m


def chip(s, accent, size=14, fill=CARD, pad=0.16):
    t = txt(s, size)
    box = RoundedRectangle(width=t.get_width() + 2 * pad, height=t.get_height() + 0.22,
                           corner_radius=0.08)
    box.set_fill(fill, 1).set_stroke(accent, 1.8)
    t.move_to(box)
    return VGroup(box, t)


def page_card(kind, title, w=1.9, h=0.72):
    label, col = KINDS[kind]
    box = RoundedRectangle(width=w, height=h, corner_radius=0.08)
    box.set_fill(CARD, 1).set_stroke(col, 2)
    lab = txt(label, 10, col, MONO)
    t = fit(txt(title, 15, INK), w - 0.28)
    lab.next_to(box.get_corner(UL), DR, buff=(0.12, 0.1, 0))
    t.next_to(lab, DOWN, aligned_edge=LEFT, buff=0.07)
    return VGroup(box, lab, t)


def doc_icon(name, w=2.35, h=0.5):
    fold = 0.16
    x0, x1, y0, y1 = -w / 2, w / 2, -h / 2, h / 2
    body = Polygon([x0, y0, 0], [x1, y0, 0], [x1, y1 - fold, 0], [x1 - fold, y1, 0], [x0, y1, 0])
    body.set_fill(CARD, 1).set_stroke(KINDS["source"][1], 1.5)
    ear = Polygon([x1 - fold, y1, 0], [x1 - fold, y1 - fold, 0], [x1, y1 - fold, 0])
    ear.set_fill(GRID, 1).set_stroke(KINDS["source"][1], 1.5)
    t = fit(txt(name, 12, INK, MONO), w - 0.45).move_to(body).shift(LEFT * 0.06)
    return VGroup(body, ear, t)


def panel(xr, title, sub):
    w, h = xr[1] - xr[0], PANEL_Y[1] - PANEL_Y[0]
    frame = RoundedRectangle(width=w, height=h, corner_radius=0.15)
    frame.move_to([(xr[0] + xr[1]) / 2, (PANEL_Y[0] + PANEL_Y[1]) / 2, 0])
    frame.set_fill(PANEL, 1).set_stroke(GRID, 1.5)
    head = VGroup(txt(title, 14, INK, MONO), txt(sub, 13, MUTED))
    head.arrange(RIGHT, buff=0.18, aligned_edge=DOWN)
    head.next_to(frame.get_corner(UL), DR, buff=(0.22, 0.16, 0))
    return VGroup(frame, head)


class LlmWikiExplainer(Scene):
    def setup(self):
        self.bg = FullScreenRectangle().set_fill(BG, 1).set_stroke(width=0)
        self.add(self.bg)
        self.caption = None

    # ----------------------------------------------------------------- helpers
    def set_caption(self, s, run_time=0.6):
        new = txt(s, 19, MUTED).move_to([0, -3.72, 0])
        fit(new, 13.6)
        if self.caption is None:
            self.caption = new
            self.play(FadeIn(new, shift=UP * 0.1), run_time=run_time)
        else:
            old, self.caption = self.caption, new
            self.play(FadeOut(old, shift=UP * 0.1), FadeIn(new, shift=UP * 0.1), run_time=run_time)

    def sparks(self, start, targets, color=QUERY, run_time=0.9, lag=0.12):
        dots = [GlowDot(start, radius=0.25, color=color, glow_factor=1.5) for _ in targets]
        self.add(*dots)
        self.play(LaggedStart(*[d.animate.move_to(t) for d, t in zip(dots, targets)], lag_ratio=lag),
                  run_time=run_time)
        self.remove(*dots)

    def pulse(self):
        ring = self.llm[0].copy().set_fill(opacity=0).set_stroke(QUERY, 4)
        return AnimationGroup(
            FadeOut(ring, scale=1.5),
            self.llm[1].animate.set_color(QUERY).set_anim_args(rate_func=there_and_back),
        )

    def link(self, a, b, color=LINK, width=1.6):
        pa, pb = self.cards[a].get_center(), self.cards[b].get_center()
        ln = Line(pa, pb).set_stroke(color, width)
        self.links[(a, b)] = ln
        return ln

    def raise_cards(self):
        mobs = [self.cards[k] for k in PAGES if k in self.shown]
        mobs += [self.index_box, *self.index_lines, self.log_box, *self.log_lines,
                 self.review_box, *self.review_lines]
        if getattr(self, "flag", None) is not None:
            mobs.append(self.flag)
        self.bring_to_front(*mobs)

    def build_bar(self):
        frame = RoundedRectangle(width=13.8, height=0.62, corner_radius=0.12)
        frame.move_to([0, BAR_Y, 0]).set_fill(PANEL, 1).set_stroke(GRID, 1.5)
        lab = txt("CONTEXT WINDOW", 12, MUTED, MONO)
        lab.next_to(frame.get_left(), RIGHT, buff=0.2)
        self.bar_cursor = lab.get_right()[0] + 0.25
        return VGroup(frame, lab)

    def bar_put(self, mob):
        mob.move_to([self.bar_cursor + mob.get_width() / 2, BAR_Y, 0])
        self.bar_cursor += mob.get_width() + 0.12
        return mob

    def bar_reset(self):
        self.bar_cursor = self.bar[1].get_right()[0] + 0.25

    def right_box(self, top, bottom, title):
        x0, x1 = GRAPH_RIGHT + 0.2, WIKI_X[1] - 0.15
        box = RoundedRectangle(width=x1 - x0, height=top - bottom, corner_radius=0.08)
        box.move_to([(x0 + x1) / 2, (top + bottom) / 2, 0]).set_fill(CARD, 1).set_stroke(GRID, 1.5)
        head = txt(title, 12, INK, MONO).next_to(box.get_corner(UL), DR, buff=(0.14, 0.1, 0))
        return VGroup(box, head)

    def build_index(self):
        self.index_box = self.right_box(PANEL_Y[1] - 0.55, 0.22, "index.md")
        self.index_lines = VGroup()
        return self.index_box

    def stack_row(self, lines, box, row, buff=0.05):
        anchor = lines[-1] if len(lines) else box[1]
        row.next_to(anchor, DOWN, aligned_edge=LEFT, buff=buff if len(lines) else 0.1)
        lines.add(row)
        return row

    def index_entry(self, key):
        kind, title, *_ = PAGES[key]
        dot = Dot(radius=0.035).set_fill(KINDS[kind][1], 1)
        row = VGroup(dot, txt(title, 10, INK)).arrange(RIGHT, buff=0.08)
        return self.stack_row(self.index_lines, self.index_box, row, 0.045)

    def build_log(self):
        self.log_box = self.right_box(0.07, -1.42, "log.md")
        self.log_lines = VGroup()
        return self.log_box

    def log_entry(self, op, title, date="10-05"):
        a = txt(f"{date} {op}", 9, AMBER if op == "lint" else MUTED, MONO)
        b = txt(title, 10, INK)
        row = fit(VGroup(a, b).arrange(RIGHT, buff=0.08), 1.85)
        return self.stack_row(self.log_lines, self.log_box, row, 0.06)

    def build_review(self):
        self.review_box = self.right_box(-1.57, PANEL_Y[0] + 0.15, "review queue")
        self.review_lines = VGroup()
        return self.review_box

    def review_entry(self, label, title, color):
        dot = Dot(radius=0.04).set_fill(color, 1)
        body = VGroup(txt(label, 9, color, MONO), txt(title, 10, INK)).arrange(DOWN, aligned_edge=LEFT, buff=0.03)
        row = fit(VGroup(dot, body).arrange(RIGHT, buff=0.08, aligned_edge=UP), 1.85)
        return self.stack_row(self.review_lines, self.review_box, row, 0.1)

    def review_resolve(self, row, label="resolved"):
        new = row.copy()
        new[0].set_fill(ANSWER, 1)
        lab = txt(label, 9, ANSWER, MONO).move_to(new[1][0], aligned_edge=LEFT)
        new[1][0].become(lab)
        new[1][1].set_opacity(0.55)
        return Transform(row, new)

    def flash_rows(self, rows):
        return [AnimationGroup(FadeIn(r, shift=RIGHT * 0.15), r[-1].animate.set_color(QUERY))
                for r in rows]

    # ------------------------------------------------------------------- story
    def construct(self):
        self.intro()
        self.rag_recap()
        self.layers()
        self.ingest()
        self.query()
        self.lint()
        self.wrap()

    def intro(self):
        title = txt("How an LLM Wiki works", 54, INK, weight=BOLD)
        sub = txt("Compile your sources once. Keep the knowledge current.", 24, MUTED)
        VGroup(title, sub).arrange(DOWN, buff=0.35)
        self.play(Write(title), run_time=1.4)
        self.play(FadeIn(sub, shift=UP * 0.15))
        self.wait(1.2)
        self.play(FadeOut(title, shift=UP * 0.3), FadeOut(sub, shift=UP * 0.3))

    def rag_recap(self):
        self.raw = panel(RAW_X, "RAW SOURCES", "read-only")
        self.docs = {
            "R1": doc_icon("mars-dust-survey.pdf"),
            "R2": doc_icon("perseverance-samples.md"),
            "R3": doc_icon("ice-radar-2026.pdf"),
        }
        cx = (RAW_X[0] + RAW_X[1]) / 2
        self.docs["R1"].move_to([cx, 1.95, 0])
        self.docs["R2"].move_to([cx, 1.25, 0])
        self.docs["R3"].move_to([cx, 0.55, 0])
        self.llm = VGroup(
            Circle(radius=0.48).set_fill(CARD, 1).set_stroke(INK, 2),
            txt("LLM", 20, INK, weight=BOLD),
        ).move_to(LLM_POS)
        self.bar = self.build_bar()

        self.play(FadeIn(self.raw), FadeIn(self.docs["R1"]), FadeIn(self.docs["R2"]),
                  FadeIn(self.llm), FadeIn(self.bar), run_time=1.0)
        self.set_caption("First, plain RAG: every question goes back to the raw sources.")

        counter = None
        short = {"R1": "dust-survey", "R2": "perseverance"}
        questions = [
            ("What makes Mars red?", ["R1"], "Iron oxide in the dust."),
            ("Did Perseverance find organics?", ["R2", "R1"], "Yes, in several rock samples."),
            ("What makes Mars red?", ["R1"], "Iron oxide in the dust."),
        ]
        for i, (q, srcs, ans) in enumerate(questions):
            qc = self.bar_put(chip(q, QUERY, 14))
            self.play(FadeIn(qc, shift=DOWN * 0.1), run_time=0.5)
            frags = []
            for s in srcs:
                f = chip("chunk · " + short[s], KINDS["source"][1], 11)
                f.move_to(self.docs[s])
                frags.append(f)
            targets = [self.bar_put(f.copy()).get_center() for f in frags]
            self.play(*[f.animate.move_to(t) for f, t in zip(frags, targets)],
                      self.pulse(), run_time=0.9)
            ac = self.bar_put(chip(ans, ANSWER, 14))
            self.play(FadeIn(ac, shift=LEFT * 0.1), run_time=0.5)
            new_counter = VGroup(txt("rebuilt from scratch", 13, ALERT, MONO),
                                 txt(f"{i + 1}×", 30, ALERT, MONO, weight=BOLD)).arrange(DOWN, buff=0.1)
            new_counter.move_to([cx, -2.4, 0])
            if i == 2:
                self.set_caption("Asked again? Rediscovered again. Nothing accumulates.")
            if counter is None:
                counter = new_counter
                self.play(FadeIn(counter), run_time=0.4)
            else:
                self.play(Transform(counter, new_counter), run_time=0.4)
            self.wait(0.6 if i < 2 else 1.4)
            self.play(FadeOut(VGroup(qc, ac, *frags), shift=UP * 0.2), run_time=0.5)
            self.bar_reset()
        self.play(FadeOut(counter), run_time=0.4)


    def layers(self):
        self.wiki = panel(WIKI_X, "LLM WIKI", "persistent pages for humans and LLMs")
        self.schema = VGroup(
            txt("SCHEMA", 11, AMBER, MONO),
            chip("CLAUDE.md", AMBER, 15),
        ).arrange(DOWN, buff=0.08).move_to(LLM_POS + UP * 2.35)
        rules = DashedLine(self.schema.get_bottom(), self.llm.get_top(), dash_length=0.07)
        rules.set_stroke(AMBER, 1.5)
        self.schema.add(rules)

        y = LLM_POS[1]
        read = Arrow([RAW_X[1] + 0.02, y, 0], [LLM_POS[0] - 0.5, y, 0], buff=0, stroke_width=3,
                      max_tip_length_to_length_ratio=0.35).set_color(KINDS["entity"][1])
        write = Arrow([LLM_POS[0] + 0.5, y, 0], [WIKI_X[0] - 0.02, y, 0], buff=0, stroke_width=3,
                      max_tip_length_to_length_ratio=0.35).set_color(KINDS["concept"][1])
        rl = txt("read", 10, KINDS["entity"][1], MONO).next_to(read, DOWN, buff=0.06)
        wl = txt("write", 10, KINDS["concept"][1], MONO).next_to(write, DOWN, buff=0.06)
        self.flow = VGroup(read, write, rl, wl)

        self.cards = {k: page_card(PAGES[k][0], PAGES[k][1]).move_to([PAGES[k][2], PAGES[k][3], 0])
                      for k in PAGES}
        self.links = {}
        self.shown = set(INITIAL)
        self.flag = None
        index = self.build_index()
        log = self.build_log()
        review = self.build_review()

        self.set_caption("An LLM Wiki adds a persistent layer: pages the LLM writes and keeps current.")
        self.play(FadeIn(self.wiki), FadeIn(self.flow), run_time=0.8)
        links = VGroup(*[self.link(a, b) for a, b in INITIAL_LINKS])
        self.play(LaggedStart(*[GrowFromCenter(self.cards[k]) for k in INITIAL], lag_ratio=0.12),
                  FadeIn(index), FadeIn(log), FadeIn(review), run_time=1.6)
        self.add(links)
        self.raise_cards()
        self.play(LaggedStart(*[ShowCreation(l) for l in links], lag_ratio=0.1), run_time=1.2)
        rows = [self.index_entry(k) for k in INITIAL]
        logs = [self.log_entry("ingest", "Mars dust survey", "09-28"),
                self.log_entry("ingest", "Perseverance samples", "10-01")]
        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.1) for r in rows + logs], lag_ratio=0.08),
                  run_time=1.2)
        ticks = VGroup(*[txt("compiled", 10, ANSWER, MONO).next_to(self.docs[k], DOWN, buff=0.03)
                         .align_to(self.docs[k], RIGHT) for k in ("R1", "R2")])
        self.play(FadeIn(ticks), run_time=0.5)
        self.ticks = ticks
        self.set_caption("Pages link to each other with wikilinks. index.md catalogues them, log.md records every change.")
        self.wait(1.6)

        self.set_caption("The schema is the editorial policy: how to ingest, answer and maintain the wiki.")
        self.play(FadeIn(self.schema, shift=DOWN * 0.15), run_time=0.8)
        self.play(Indicate(self.schema[1], color=AMBER, scale_factor=1.1), run_time=0.9)
        self.set_caption("Raw sources stay the source of truth. The LLM reads them but never modifies them.")
        self.play(Indicate(self.raw[1], color=INK), run_time=1.0)
        self.wait(0.8)

    def stage_list(self, title, items, color):
        head = txt(title, 10, color, MONO)
        rows = VGroup(*[fit(chip(t, c, 11), 1.8) for t, c in items]).arrange(DOWN, buff=0.07)
        g = VGroup(head, rows).arrange(DOWN, buff=0.12)
        g.move_to([LLM_POS[0], -2.0, 0])
        return g

    def ingest(self):
        self.set_caption("Ingest: you add a new source.")
        r3 = self.docs["R3"]
        self.play(FadeIn(r3, shift=DOWN * 0.4), run_time=0.7)
        reading = r3.copy()
        self.play(reading.animate.scale(0.5).move_to(self.llm), run_time=0.8)
        self.play(FadeOut(reading), self.pulse(), run_time=0.5)

        self.set_caption("Stage 1, analysis: extract entities and concepts, link them to the wiki, detect contradictions.")
        s1 = self.stage_list("STAGE 1 · ANALYSIS", [
            ("entity: Mars", KINDS["entity"][1]),
            ("concept: Subsurface ice", KINDS["concept"][1]),
            ("links to: Habitability", LINK),
            ("contradiction found", ALERT),
        ], QUERY)
        self.play(FadeIn(s1[0]), LaggedStart(*[FadeIn(c, shift=DOWN * 0.1) for c in s1[1]], lag_ratio=0.25),
                  run_time=1.6)
        self.wait(1.0)

        s2 = self.stage_list("STAGE 2 · GENERATION", [
            ("source summary", KINDS["source"][1]),
            ("entity + concept pages", KINDS["concept"][1]),
            ("index.md / log.md", GRID),
            ("review item", ALERT),
        ], ANSWER)
        self.set_caption("Stage 2, generation: write the pages. First a summary page for the new source.")
        self.play(FadeTransform(s1, s2), run_time=0.8)
        self.s2 = s2

        def mark(i):
            return s2[1][i][0].animate.set_fill(GRID, 1)

        self.sparks(LLM_POS, [self.cards["S3"].get_center()])
        self.shown.add("S3")
        self.play(GrowFromCenter(self.cards["S3"]), mark(0), run_time=0.6)

        touched = txt("pages touched: 1", 14, QUERY, MONO)
        touched.next_to(self.wiki[0].get_corner(UR), DL, buff=(0.2, 0.16, 0))
        self.add(touched)

        def bump(n):
            new = txt(f"pages touched: {n}", 14, QUERY, MONO).move_to(touched, aligned_edge=RIGHT)
            return Transform(touched, new)

        self.set_caption("Then it updates the pages the source affects, and creates the ones that are missing.")
        self.sparks(LLM_POS, [self.cards["E1"].get_center(), self.cards["C3"].get_center()])
        self.shown.add("C3")
        new_links = VGroup(self.link("S3", "E1"), self.link("S3", "C3"))
        self.add(new_links)
        self.raise_cards()
        self.play(GrowFromCenter(self.cards["C3"]),
                  Indicate(self.cards["E1"], color=QUERY, scale_factor=1.08),
                  ShowCreation(new_links), bump(3), mark(1), run_time=1.0)

        self.set_caption("New data contradicts an old claim. It is flagged for the review queue, not silently overwritten.")
        self.sparks(LLM_POS, [self.cards["C2"].get_center()])
        contra = self.link("C3", "C2", color=ALERT, width=2.4)
        self.add(contra)
        flag = chip("contradiction", ALERT, 11).next_to(self.cards["C2"], DOWN, buff=0.12)
        self.flag = flag
        self.raise_cards()
        self.play(ShowCreation(contra), Indicate(self.cards["C2"], color=ALERT, scale_factor=1.08),
                  FadeIn(flag, shift=UP * 0.1), bump(4), run_time=1.0)
        self.contra_item = self.review_entry("contradiction", "Habitability", ALERT)
        moving = flag.copy()
        self.play(moving.animate.scale(0.6).move_to(self.contra_item), mark(3), run_time=0.8)
        self.play(FadeOut(moving), FadeIn(self.contra_item), run_time=0.4)

        self.set_caption("Finally the index and the log are updated. One source can touch 10 to 15 pages.")
        rows = [self.index_entry("S3"), self.index_entry("C3")]
        lrow = self.log_entry("ingest", "Subsurface ice radar")
        self.sparks(LLM_POS, [self.index_box.get_center(), self.log_box.get_center()])
        self.play(*self.flash_rows(rows + [lrow]), bump(6), mark(2), run_time=0.9)
        tick = txt("compiled", 10, ANSWER, MONO).next_to(r3, DOWN, buff=0.03).align_to(r3, RIGHT)
        self.ticks.add(tick)
        self.play(FadeIn(tick), *[r[-1].animate.set_color(INK) for r in rows + [lrow]], run_time=0.6)
        self.wait(1.0)
        self.play(FadeOut(touched), FadeOut(s2), run_time=0.5)

    def query(self):
        q = "Could Mars support life today?"
        self.set_caption("Query: you ask a question.")
        qc = self.bar_put(chip(q, QUERY, 13))
        self.play(FadeIn(qc, shift=DOWN * 0.1), run_time=0.6)

        self.set_caption("Retrieval still happens. It searches the wiki pages, starting from the index...")
        idx_hl = SurroundingRectangle(self.index_box[0], buff=0.03).set_stroke(QUERY, 2.5)
        picks = ["C2", "C3", "E1"]
        hls = VGroup(*[SurroundingRectangle(self.cards[k], buff=0.05).set_stroke(QUERY, 2.5) for k in picks])
        self.play(ShowCreation(idx_hl), run_time=0.5)
        self.play(ShowCreation(hls), run_time=0.6)
        self.set_caption("...and the raw sources, because the wiki doesn't replace them.")
        raw_hl = SurroundingRectangle(self.docs["R3"], buff=0.05).set_stroke(QUERY, 2.5)
        self.play(ShowCreation(raw_hl), run_time=0.6)

        self.set_caption("The selected wiki pages, log history and raw passages are packed into the context window.")
        packed = [(f"wiki: {PAGES[k][1]}", KINDS[PAGES[k][0]][1], self.cards[k]) for k in picks]
        packed += [("wiki: log history", GRID, self.log_box),
                   ("raw: ice-radar §2", KINDS["source"][1], self.docs["R3"])]
        segs = []
        for label, col, src in packed:
            c = chip(label, col, 11).move_to(src)
            segs.append((c, self.bar_put(c.copy()).get_center()))
        self.play(LaggedStart(*[c.animate.move_to(t) for c, t in segs], lag_ratio=0.15), run_time=1.6)
        self.play(FadeOut(hls), FadeOut(raw_hl), FadeOut(idx_hl),
                  self.pulse(), run_time=0.7)

        ans = chip("Not on the surface, but buried ice keeps it open.", ANSWER, 13)
        ans.next_to(self.bar, DOWN, buff=0.12).align_to(self.bar, RIGHT).shift(LEFT * 0.2)
        self.set_caption("The LLM synthesizes an answer and cites the pages it used.")
        self.play(FadeIn(ans, shift=DOWN * 0.1), run_time=0.6)
        self.wait(1.0)

        self.set_caption("A valuable answer is saved back to the wiki, after review.")
        item = self.review_entry("answer to review", "Life on Mars today?", AMBER)
        self.play(Transform(ans, item, path_arc=-PI / 6), run_time=1.1)
        self.remove(ans)
        self.add(item)
        self.wait(0.4)
        self.play(self.review_resolve(item, "approved"), run_time=0.5)
        y1 = self.cards["Y1"]
        self.play(TransformFromCopy(item, y1, path_arc=PI / 6), run_time=1.0)
        self.shown.add("Y1")
        new_links = VGroup(self.link("Y1", "C2"), self.link("Y1", "E1"))
        self.add(new_links)
        self.raise_cards()
        rows = [self.index_entry("Y1")]
        lrow = self.log_entry("query", "Life on Mars today?")
        self.set_caption("Now the next question starts from a better place. The exploration compounds.")
        self.play(ShowCreation(new_links), *self.flash_rows(rows + [lrow]),
                  FadeOut(VGroup(qc, *[c for c, _ in segs]), shift=UP * 0.2), run_time=1.0)
        self.play(*[r[-1].animate.set_color(INK) for r in rows + [lrow]], run_time=0.4)
        self.bar_reset()
        self.wait(1.2)

    def lint(self):
        self.set_caption("Lint: now and then the LLM health-checks the whole wiki.")
        sweep = Line([WIKI_X[0] + 0.1, PANEL_Y[0] + 0.1, 0], [WIKI_X[0] + 0.1, PANEL_Y[1] - 0.45, 0])
        sweep.set_stroke(AMBER, 3, opacity=0.8)
        self.play(FadeIn(sweep), run_time=0.2)
        self.play(sweep.animate.set_x(GRAPH_RIGHT), run_time=1.6, rate_func=linear)
        self.play(FadeOut(sweep), run_time=0.2)

        self.set_caption("It finds an orphan page with no links, and connects it.")
        orphan = SurroundingRectangle(self.cards["C4"], buff=0.06).set_stroke(AMBER, 2.5)
        otag = chip("orphan: no links", AMBER, 11).next_to(self.cards["C4"], DOWN, buff=0.08)
        self.play(ShowCreation(orphan), FadeIn(otag), run_time=0.6)
        ln = self.link("C4", "C2")
        self.add(ln)
        self.raise_cards()
        self.play(ShowCreation(ln), run_time=0.8)
        self.play(FadeOut(orphan), FadeOut(otag), run_time=0.4)

        self.set_caption("It revises the stale claim the contradiction pointed to, and clears the review item.")
        stale = SurroundingRectangle(self.cards["C2"], buff=0.06).set_stroke(AMBER, 2.5)
        revised = chip("claim revised", ANSWER, 11).move_to(self.flag)
        self.play(ShowCreation(stale), run_time=0.5)
        self.play(Transform(self.flag, revised), self.links[("C3", "C2")].animate.set_stroke(LINK, 1.6),
                  self.review_resolve(self.contra_item), run_time=0.8)
        lrow = self.log_entry("lint", "2 fixes")
        self.play(FadeOut(stale), *self.flash_rows([lrow]), run_time=0.6)
        self.play(lrow[-1].animate.set_color(INK), run_time=0.3)
        self.set_caption("Every ingest, answer and lint pass leaves artifacts behind. That is what compounds.")
        self.wait(2.0)

    def wrap(self):
        self.play(FadeOut(Group(*[m for m in self.mobjects if m is not self.bg and m is not self.camera.frame])),
                  run_time=0.8)
        self.caption = None

        head = txt("PIPELINE COMPARISON", 13, MUTED, MONO)

        def row(label, color, steps):
            lab = fit(txt(label, 20, color, weight=BOLD), 2.4)
            chips = [chip(s, color if i == len(steps) - 1 else GRID, 14) for i, s in enumerate(steps)]
            seq = VGroup()
            for i, c in enumerate(chips):
                seq.add(c)
                if i < len(chips) - 1:
                    seq.add(Arrow(ORIGIN, RIGHT * 0.4, buff=0, stroke_width=2.5).set_color(MUTED))
            seq.arrange(RIGHT, buff=0.12)
            lab.next_to(seq, LEFT, buff=0.4)
            return VGroup(lab, seq)

        rag = row("Query-time RAG", MUTED, ["Question", "Search raw", "Synthesize on the spot",
                                            "Answer only remains"])
        wiki = row("LLM Wiki", ANSWER, ["Add new source", "Incremental wiki update",
                                        "At query time: search wiki + raw", "Artifacts remain"])
        for r, y in ((rag, 0.0), (wiki, -0.85)):
            r[1].move_to([0, y, 0], aligned_edge=LEFT).set_x(-3.9 + r[1].get_width() / 2)
            r[0].next_to(r[1], LEFT, buff=0.35)
        table = VGroup(rag, wiki)
        fit(table, 13.4).move_to(UP * 2.2)
        head.next_to(table, UP, buff=0.3).align_to(table, LEFT)
        self.play(FadeIn(head), FadeIn(rag[0]),
                  LaggedStart(*[FadeIn(m, shift=RIGHT * 0.1) for m in rag[1]], lag_ratio=0.15), run_time=1.6)
        self.play(FadeIn(wiki[0]),
                  LaggedStart(*[FadeIn(m, shift=RIGHT * 0.1) for m in wiki[1]], lag_ratio=0.15), run_time=1.6)
        self.wait(1.0)

        point = txt("Retrieval is essential. Because a wiki exists, raw search is not eliminated.", 20, QUERY)
        fit(point, 13.0).next_to(table, DOWN, buff=0.55)
        self.play(FadeIn(point, shift=UP * 0.1), run_time=0.8)
        self.wait(1.2)

        risks = VGroup(*[chip(s, ALERT, 15) for s in
                         ["Information loss", "Summary drift", "Error cementing", "Non-determinism"]])
        risks.arrange(RIGHT, buff=0.2)
        note = txt("Incorrect summaries remain as Markdown and become context for later questions.", 16, MUTED)
        rg = VGroup(risks, note).arrange(DOWN, buff=0.2).next_to(point, DOWN, buff=0.5)
        self.play(LaggedStart(*[FadeIn(r, shift=UP * 0.1) for r in risks], lag_ratio=0.2), run_time=1.2)
        self.play(FadeIn(note), run_time=0.6)
        self.wait(1.2)

        close = VGroup(
            txt("Not a deterministic knowledge compiler.", 22, INK, weight=BOLD),
            txt("A living draft maintained by an LLM: a map, with the raw sources as the territory.", 18, INK),
        ).arrange(DOWN, buff=0.12)
        fit(close, 13.0).next_to(rg, DOWN, buff=0.5)
        self.play(FadeIn(close, shift=UP * 0.1), run_time=0.8)
        credit = txt("Pattern: Andrej Karpathy, \"LLM Wiki\"  ·  Diagram and analysis: SmartScope", 13, MUTED)
        credit.to_edge(DOWN, buff=0.25)
        self.play(FadeIn(credit), run_time=0.5)
        self.wait(3.5)
        self.play(FadeOut(Group(head, table, point, rg, close, credit)), run_time=0.8)
