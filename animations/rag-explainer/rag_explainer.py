"""How RAG retrieves context: a question lands in embedding space, pulls in
its nearest fragments, and carries them out to the LLM.

Built with 3Blue1Brown's manim (manimgl, https://github.com/3b1b/manim).

Render (headless):
    xvfb-run -a -s "-screen 0 1920x1080x24" manimgl rag_explainer.py RagExplainer -w --hd
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
QUERY = "#ffd166"
ANSWER = "#8ce0b5"

TOPICS = {
    "Cooking": "#ff9f5a",
    "Space": "#6fb3ff",
    "Finance": "#7ed492",
    "Health": "#f48fb1",
}

# (text, topic, x, y, label side)
FRAGMENTS = [
    ("Soft-boil eggs for 6 minutes", "Cooking", -4.75, 2.30, UP),
    ("Hard-boiled eggs need 10 min", "Cooking", -3.30, 1.25, DOWN),
    ("Salt pasta water generously", "Cooking", -5.75, 1.15, DOWN),
    ("Rest steak before slicing", "Cooking", -5.60, 0.15, DOWN),
    ("Iron oxide makes Mars red", "Space", -0.75, 2.15, DOWN),
    ("Mars has two small moons", "Space", 1.10, 1.70, DOWN),
    ("Jupiter is a gas giant", "Space", -0.45, 0.85, DOWN),
    ("Sunlight takes 8 min to reach us", "Space", 0.95, 0.15, DOWN),
    ("Interest earns interest over time", "Finance", -0.70, -1.30, DOWN),
    ("Index funds spread risk", "Finance", 1.10, -2.00, DOWN),
    ("Inflation erodes cash savings", "Finance", -0.40, -2.75, DOWN),
    ("Eggs are rich in protein", "Health", -3.30, -0.95, DOWN),
    ("One egg a day is fine for most", "Health", -4.60, -1.60, DOWN),
    ("Sleep 7 to 9 hours a night", "Health", -5.55, -2.75, DOWN),
    ("Walking lowers blood pressure", "Health", -3.25, -2.80, DOWN),
]

TOPIC_TAGS = {
    "Cooking": (-6.15, 2.70),
    "Space": (1.55, 2.70),
    "Finance": (1.55, -1.05),
    "Health": (-6.15, -0.95),
}

SPACE_X = (-6.85, 2.25)
SPACE_Y = (-3.35, 3.00)
PANEL_X = (2.55, 6.90)


def txt(s, size=20, color=INK, font=FONT, **kw):
    return Text(s, font=font, font_size=size, **kw).set_color(color)


def card(s, accent, width, size=18, fill=CARD):
    t = txt(s, size=size)
    if t.get_width() > width - 0.4:
        t.set_width(width - 0.4)
    box = RoundedRectangle(width=width, height=t.get_height() + 0.32, corner_radius=0.09)
    box.set_fill(fill, 1).set_stroke(accent, 2)
    t.move_to(box)
    return VGroup(box, t)


def similarity(d):
    return float(np.exp(-d / 2.6))


class RagExplainer(Scene):
    def setup(self):
        self.bg = FullScreenRectangle().set_fill(BG, 1).set_stroke(width=0)
        self.add(self.bg)

    # ------------------------------------------------------------------ layout
    def build_space(self):
        w, h = SPACE_X[1] - SPACE_X[0], SPACE_Y[1] - SPACE_Y[0]
        frame = RoundedRectangle(width=w, height=h, corner_radius=0.15)
        frame.move_to([(SPACE_X[0] + SPACE_X[1]) / 2, (SPACE_Y[0] + SPACE_Y[1]) / 2, 0])
        frame.set_fill(PANEL, 1).set_stroke(GRID, 1.5)
        grid = VGroup()
        for x in np.arange(SPACE_X[0] + 0.5, SPACE_X[1], 0.5):
            grid.add(Line([x, SPACE_Y[0], 0], [x, SPACE_Y[1], 0]))
        for y in np.arange(SPACE_Y[0] + 0.5, SPACE_Y[1], 0.5):
            grid.add(Line([SPACE_X[0], y, 0], [SPACE_X[1], y, 0]))
        grid.set_stroke(GRID, 1, opacity=0.45)
        label = txt("embedding space  ·  2D projection", 15, MUTED, MONO)
        label.next_to(frame.get_corner(DR), UL, buff=0.12)
        return VGroup(frame, grid, label)

    def build_fragments(self):
        frags = []
        for s, topic, x, y, side in FRAGMENTS:
            p = np.array([x, y, 0.0])
            dot = Dot(p, radius=0.07).set_fill(TOPICS[topic], 1)
            halo = Dot(p, radius=0.14).set_fill(TOPICS[topic], 0.18)
            lab = txt(s, 14, INK).set_opacity(0.78)
            lab.next_to(dot, side, buff=0.08)
            frags.append(dict(text=s, topic=topic, pos=p, dot=dot, halo=halo, label=lab,
                              group=VGroup(halo, dot, lab)))
        tags = VGroup(*[
            txt(t.upper(), 13, TOPICS[t], MONO).move_to([x, y, 0])
            for t, (x, y) in TOPIC_TAGS.items()
        ])
        return frags, tags

    def build_panel(self):
        w, h = PANEL_X[1] - PANEL_X[0], SPACE_Y[1] - SPACE_Y[0]
        frame = RoundedRectangle(width=w, height=h, corner_radius=0.15)
        frame.move_to([(PANEL_X[0] + PANEL_X[1]) / 2, (SPACE_Y[0] + SPACE_Y[1]) / 2, 0])
        frame.set_fill(PANEL, 1).set_stroke(GRID, 1.5)
        head = txt("PROMPT TO THE LLM", 15, MUTED, MONO)
        head.move_to(frame.get_top() + DOWN * 0.3)
        return VGroup(frame, head)

    def set_caption(self, s, run_time=0.6):
        new = txt(s, 19, MUTED).move_to([(SPACE_X[0] + PANEL_X[1]) / 2, -3.72, 0])
        if getattr(self, "caption", None) is None:
            self.caption = new
            self.play(FadeIn(new, shift=UP * 0.1), run_time=run_time)
        else:
            old = self.caption
            self.caption = new
            self.play(FadeOut(old, shift=UP * 0.1), FadeIn(new, shift=UP * 0.1), run_time=run_time)

    # ------------------------------------------------------------------- story
    def construct(self):
        title = txt("How RAG finds its context", 54, INK, weight=BOLD)
        sub = txt("Retrieval-Augmented Generation, one question at a time", 24, MUTED)
        VGroup(title, sub).arrange(DOWN, buff=0.35)
        self.play(Write(title), run_time=1.4)
        self.play(FadeIn(sub, shift=UP * 0.15))
        self.wait(1.2)
        self.play(FadeOut(title, shift=UP * 0.3), FadeOut(sub, shift=UP * 0.3))

        space = self.build_space()
        panel = self.build_panel()
        self.frags, tags = self.build_fragments()
        self.panel = panel
        self.play(FadeIn(space), FadeIn(panel), run_time=1.0)
        self.caption = None
        self.set_caption("Every document fragment is embedded as a point. Similar meaning lands close together.")
        self.play(LaggedStart(*[GrowFromCenter(VGroup(f["halo"], f["dot"])) for f in self.frags],
                              lag_ratio=0.06), run_time=1.6)
        self.play(LaggedStart(*[FadeIn(f["label"]) for f in self.frags], lag_ratio=0.04),
                  FadeIn(tags), run_time=1.6)
        self.wait(1.2)

        self.ask(
            "How long should I boil an egg?", (-4.10, 1.80),
            "Soft-boil about 6 minutes,\nhard-boil about 10.",
            note="Top-k always returns k fragments, even a weak third match.",
        )
        self.ask(
            "Why is Mars red?", (0.25, 2.45),
            "Its surface dust is rich in\niron oxide: Mars is rusty.",
        )
        self.ask(
            "Is eating eggs every day healthy?", (-3.75, -0.35),
            "For most people, yes: one egg\na day is fine, and eggs are\na good source of protein.",
            note="This question sits between two topics, so retrieval pulls from both.",
        )

        steps = VGroup(*[
            txt(s, 30, c, weight=BOLD) for s, c in
            [("Retrieve", QUERY), ("Augment", INK), ("Generate", ANSWER)]
        ]).arrange(RIGHT, buff=1.1)
        arrows = VGroup(*[
            Arrow(steps[i].get_right(), steps[i + 1].get_left(), buff=0.2).set_color(MUTED)
            for i in range(2)
        ])
        expl = VGroup(
            txt("nearest fragments\nto the question", 17, MUTED),
            txt("pasted into\nthe prompt", 17, MUTED),
            txt("the LLM answers\nfrom that context", 17, MUTED),
        )
        for e, s in zip(expl, steps):
            e.next_to(s, DOWN, buff=0.3)
        everything = Group(*[m for m in self.mobjects if m is not self.bg and m is not self.camera.frame])
        self.play(FadeOut(everything), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(VGroup(s, e), shift=UP * 0.2) for s, e in zip(steps, expl)],
                              lag_ratio=0.35),
                  LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.35), run_time=2.2)
        self.wait(2.5)
        self.play(FadeOut(VGroup(steps, arrows, expl)))

    # -------------------------------------------------------------- one query
    def ask(self, question, qxy, answer, k=3, note=None):
        qpos = np.array([qxy[0], qxy[1], 0.0])

        # 1. the question is formulated
        bar = card(question, QUERY, width=SPACE_X[1] - SPACE_X[0] - 1.6, size=24)
        bar.move_to([(SPACE_X[0] + SPACE_X[1]) / 2, 3.55, 0])
        prompt_mark = txt(">", 24, QUERY, MONO).next_to(bar[0].get_left(), RIGHT, buff=0.2)
        bar[1].next_to(prompt_mark, RIGHT, buff=0.18)
        self.set_caption("A user asks a question.")
        self.play(FadeIn(bar[0]), FadeIn(prompt_mark))
        self.play(Write(bar[1]), run_time=1.0 + 0.03 * len(question))
        self.wait(0.4)

        # 2. it is embedded into the same space
        self.set_caption("The question is embedded with the same model, so it becomes a point too.")
        qdot = GlowDot(qpos, radius=0.45, color=QUERY, glow_factor=1.6)
        qcore = Dot(qpos, radius=0.09).set_fill(QUERY, 1)
        qlabel = txt(question, 15, QUERY, weight=BOLD).next_to(qcore, UP, buff=0.14)
        if qlabel.get_left()[0] < SPACE_X[0] + 0.1:
            qlabel.shift(RIGHT * (SPACE_X[0] + 0.1 - qlabel.get_left()[0]))
        if qlabel.get_right()[0] > SPACE_X[1] - 0.1:
            qlabel.shift(LEFT * (qlabel.get_right()[0] - SPACE_X[1] + 0.1))
        qlabel.set_backstroke(BG, 4)
        flying = bar[1].copy()
        self.play(Transform(flying, qlabel, path_arc=-PI / 5), FadeIn(qdot), GrowFromCenter(qcore),
                  run_time=1.5)
        self.remove(flying)
        self.add(qlabel)
        self.play(FadeOut(VGroup(bar[0], bar[1], prompt_mark), shift=UP * 0.2), run_time=0.5)

        # 3. measure distance to every fragment
        self.set_caption("Distance in this space stands for difference in meaning.")
        ranked = sorted(self.frags, key=lambda f: np.linalg.norm(f["pos"] - qpos))
        lines = VGroup()
        for f in self.frags:
            d = np.linalg.norm(f["pos"] - qpos)
            ln = Line(qpos, f["pos"]).set_stroke(QUERY, 1.2, opacity=0.15 + 0.6 * similarity(d))
            lines.add(ln)
        self.add(lines, qdot, qcore, qlabel)
        self.play(LaggedStart(*[ShowCreation(l) for l in lines], lag_ratio=0.04), run_time=1.4)

        top = ranked[:k]
        rest = ranked[k:]
        r_k = np.linalg.norm(top[-1]["pos"] - qpos) + 0.18
        ring = Circle(radius=0.05).move_to(qpos).set_stroke(QUERY, 2, opacity=0.9)
        self.add(ring)
        self.set_caption(f"Keep the {k} nearest fragments (top-k), drop the rest.")
        self.play(ring.animate.set_width(2 * r_k).set_stroke(opacity=0.6), run_time=1.3,
                  rate_func=smooth)
        keep_lines = VGroup(*[lines[self.frags.index(f)] for f in top])
        drop_lines = VGroup(*[lines[self.frags.index(f)] for f in rest])
        sims = VGroup()
        for f in top:
            d = np.linalg.norm(f["pos"] - qpos)
            s = txt(f"{similarity(d):.2f}", 14, QUERY, MONO, weight=BOLD).set_backstroke(BG, 4)
            mid = qpos + 0.62 * (f["pos"] - qpos)
            normal = np.array([-(f["pos"] - qpos)[1], (f["pos"] - qpos)[0], 0])
            normal = normal / (np.linalg.norm(normal) + 1e-9)
            s.move_to(mid + normal * 0.18)
            sims.add(s)
        self.play(
            FadeOut(drop_lines),
            keep_lines.animate.set_stroke(QUERY, 3, opacity=1),
            *[f["dot"].animate.set_opacity(0.3) for f in rest],
            *[f["halo"].animate.set_opacity(0.05) for f in rest],
            *[f["label"].animate.set_opacity(0.22) for f in rest],
            *[f["dot"].animate.scale(1.6) for f in top],
            *[f["label"].animate.set_opacity(1) for f in top],
            FadeIn(sims),
            run_time=1.2,
        )
        if note and "weak" in note:
            self.set_caption(note)
            self.play(Indicate(sims[-1], color=WHITE, scale_factor=1.4), run_time=1.0)
            self.wait(0.6)
        self.wait(0.5)

        # 4. the nearest fragments attach to the question
        self.set_caption("The nearest fragments attach to the question.")
        chip_w = 2.5
        chips = VGroup(*[card(f["text"], TOPICS[f["topic"]], chip_w, size=14) for f in top])
        chips.arrange(DOWN, buff=0.08)
        side = RIGHT if qpos[0] < -2.0 else LEFT
        chips.next_to(qcore, side + DOWN * 0.6, buff=0.28)
        tethers = VGroup()
        for c in chips:
            t = Line(qpos, c.get_center()).set_stroke(QUERY, 2.2, opacity=0.9)
            t.add_updater(lambda m, c=c: m.put_start_and_end_on(qcore.get_center(),
                                                                c.get_corner(UL if side is RIGHT else UR)))
            tethers.add(t)
        sources = [f["label"].copy() for f in top]
        self.play(
            *[Transform(src, chip) for src, chip in zip(sources, chips)],
            FadeOut(keep_lines), FadeOut(sims), FadeOut(ring),
            *[f["label"].animate.set_opacity(0.22) for f in top],
            run_time=1.4,
        )
        for src in sources:
            self.remove(src)
        self.add(tethers, chips, qdot, qcore, qlabel)
        self.wait(0.6)

        # 5. the question flies out of the space, dragging the snippets along
        self.set_caption("The question leaves the space and drags its snippets into the prompt.")
        pw = PANEL_X[1] - PANEL_X[0] - 0.4
        q_final = card("Q: " + question, QUERY, pw, size=17)
        ctx_final = VGroup(*[card(f["text"], TOPICS[f["topic"]], pw, size=16) for f in top])
        ctx_head = txt("CONTEXT", 13, MUTED, MONO)
        stack = VGroup(q_final, ctx_head, *ctx_final).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        ctx_head.shift(RIGHT * 0.05)
        stack.next_to(self.panel[1], DOWN, buff=0.3)
        stack.set_x((PANEL_X[0] + PANEL_X[1]) / 2)

        target_spot = q_final.get_left() + LEFT * 0.05
        glow = Group(qdot, qcore)
        anims = [
            Transform(glow, Group(
                GlowDot(target_spot, radius=0.35, color=QUERY, glow_factor=1.6),
                Dot(target_spot, radius=0.09).set_fill(QUERY, 1),
            ), path_arc=-PI / 4),
            FadeTransform(qlabel, q_final, path_arc=-PI / 4),
        ]
        for i, (c, cf) in enumerate(zip(chips, ctx_final)):
            anims.append(Transform(c, cf, path_arc=-PI / 4,
                                   rate_func=squish_rate_func(smooth, 0.12 * (i + 1), 1.0)))
        self.play(*anims, run_time=2.4)
        tethers.clear_updaters()
        self.play(FadeOut(tethers), FadeOut(glow), run_time=0.4)
        self.add(ctx_head)
        self.play(FadeIn(ctx_head), run_time=0.3)

        # 6. generation
        self.set_caption("The LLM answers from the retrieved context.")
        llm = card("LLM", INK, 1.3, size=20)
        llm.next_to(stack, DOWN, buff=0.45).set_x((PANEL_X[0] + PANEL_X[1]) / 2)
        arr = Arrow(stack.get_bottom(), llm.get_top(), buff=0.06).set_color(MUTED)
        ans = card(answer, ANSWER, pw, size=17, fill=CARD)
        ans.next_to(llm, DOWN, buff=0.35).set_x((PANEL_X[0] + PANEL_X[1]) / 2)
        arr2 = Arrow(llm.get_bottom(), ans.get_top(), buff=0.06).set_color(MUTED)
        self.play(GrowArrow(arr), FadeIn(llm, scale=0.8), run_time=0.7)
        self.play(GrowArrow(arr2), FadeIn(ans[0]), run_time=0.5)
        self.play(Write(ans[1]), run_time=1.6)
        if note and "weak" not in note:
            self.set_caption(note)
        self.wait(2.0)

        # 7. reset for the next question
        self.play(
            FadeOut(VGroup(q_final, chips, ctx_head, llm, arr, arr2, ans)),
            *[f["dot"].animate.set_opacity(1) for f in rest],
            *[f["dot"].animate.scale(1 / 1.6) for f in top],
            *[f["label"].animate.set_opacity(0.78) for f in self.frags],
            *[f["halo"].animate.set_opacity(0.18) for f in rest],
            run_time=1.0,
        )
        self.wait(0.3)
