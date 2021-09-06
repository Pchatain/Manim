from sys import setdlopenflags
from typing import Text, get_origin
from manim import *
import numpy as np

# TODO: define quanta in a class

WIRE1_START = [-4, 0, 0]
WIRE1_END = [3, 0, 0]
WIRE2_START = [-4, -2, 0]
WIRE2_END = [3, -2, 0]


class qcIntro(Scene):
    def construct(self):
        quantum = Text("Quantum Computing:", color=BLUE).shift(UP).scale(1.5)
        create = Text("How to entangle two qubits").shift(DOWN)
        self.play(Write(quantum))
        self.wait(1)
        self.play(Write(create))
        self.wait(1)


class prereq(Scene):
    def construct(self):
        knowledge = Text("Prerequisite Knowledge").shift(UP).shift(LEFT)
        self.play(Write(knowledge))
        self.wait(1)
        list_of_content = MathTex(
            r"&\text{1.  Linear algebra}\\",
            r"&\text{2.  Basic circuits (computer science)}\\",
            r"&\text{3.  Complex numbers}\\",
            r"&\text{4.  Quantum Superposition}",
        ).shift(DOWN)
        self.play(Write(list_of_content))
        self.wait(1)
        # knowledge = Text("Prerequisite Knowledge").shift(UP).shift(LEFT)
        # self.play(Write(knowledge))
        # p1 = Text("1.  Basic Linear algebra").scale(0.5).shift(LEFT)
        # self.play(Write(p1))
        # p2 = Text("2.  Basic circuit computer science").scale(0.5).shift(DOWN)
        # self.play(Write(p2))


class testingStuff(Scene):
    def construct(self):
        q1 = QubitReal(0, [0, 0, 0])
        hgate = Cnot(DOWN, [0, 0, 0])
        line = Line(WIRE1_START, WIRE1_END)
        self.add_foreground_mobjects(hgate)
        self.add(q1, hgate, line)
        self.play(q1.hadamard_gate(), hgate.use())
        # color_map = {r"|0\rangle": BLUE, r"|1\rangle": RED}
        # label = (
        #     Tex(r"$(a + bi)$", r"$|0\rangle$", r"$+ (c + di)$", r"$|1\rangle$")
        #     .move_to([0, 1, 0])
        #     .scale(2)
        # )
        # label.set_color_by_tex_to_color_map(color_map)

        # m0 = 0.0
        # m1 = 1.0
        # color_map = {".": BLUE, " ": RED}
        # l1 = Tex(r"(", str(m0) + ",", " " + str(m1), ")")
        # l1.set_color_by_tex_to_color_map(color_map)
        # self.add(l1)
        # self.wait()
        # q1 = Mgate().shift(DOWN)
        # self.add(q1)
        # self.wait(0.5)
        # self.play(q1.animate.set_opacity(0.5))


class bug(Scene):
    def construct(self):
        q1 = QubitReal(0, [0, 0, 0])
        q1.add_coord()
        q2 = QubitReal(0, [2, 0, 0])
        self.add(q1, q2)

        # self.play(q1.update_qubit(1), q1.update_coord())
        # self.play(q1.update_qubit(1), q1.update_coord())
        # self.play(q1.update_qubit(1), q1.update_coord())
        # self.play(q1.update_qubit(1), q1.update_coord())
        self.play(q1.update_qubit(0.5), q1.update_coord())
        print(f"Values are {q1.get_values(3)}")
        self.play(q2.hadamard_gate(), q2.update_coord())
        print(f"Values are hadamard {q2.get_values(3)}")
        # self.wait(1)
        self.play(q1.update_qubit(1), q1.update_coord())
        print(f"Values are {q1.get_values(3)}")
        self.play(q1.update_qubit(0.5), q1.update_coord())
        print(f"Values are {q1.get_values(3)}")
        self.wait(1)


class helpTest(Scene):
    def construct(self):
        dot = Dot([-4, 0, 0])
        d1_text = Text("0").next_to(dot, UP).scale(0.7)

        bit_group1 = VGroup()
        bit_group1.add(*Dot([-4, 0, 0]))

        bit_group1.add(*Text("0").next_to(dot, UP).scale(0.7))
        line1 = Line([-4, 0, 0], [4, 0, 0])
        self.add(line1)
        self.play(MoveAlongPath(bit_group1, line1), run_time=2, rate_func=linear)
        points = d1_text.get_points()
        print(len(points))
        print("length of points ^")
        circ = Circle().next_to(points[len(points) / 2])
        self.add(circ)
        self.wait(1)


class classical_circuit(Scene):
    def construct(self):

        dot1 = Dot(WIRE1_START)
        dot2 = Dot(WIRE2_START)

        line1 = Line(WIRE1_START, WIRE1_END + RIGHT)
        line2 = Line(WIRE2_START, WIRE2_END + RIGHT)
        dot1.move_to(line1.get_start())
        dot2.move_to(line2.get_start())
        text1 = Tex("0").next_to(dot1, UP).scale(0.7)
        text2 = Tex("1").next_to(dot2, UP).scale(0.7)

        bit_group1 = VGroup(dot1, text1)
        bit_group2 = VGroup(dot2, text2)
        self.play(Create(line1), Create(line2))
        self.wait(1)
        self.play(Write(bit_group1))
        self.wait(1)
        self.play(Write(bit_group2))
        self.wait(1)
        self.play(
            bit_group1.animate.shift(RIGHT * 8),
            bit_group2.animate.shift(RIGHT * 8),
            run_time=2,
            rate_func=linear,
        )
        self.wait(1)


class wire_classical_2(Scene):
    def construct(self):
        dot1 = Dot([0, 0, 0])
        dot2 = Dot([0, -2, 0])

        line1 = Line([0, 0, 0], [8, 0, 0])
        line2 = Line([0, -2, 0], [8, -2, 0])
        text1 = Tex("0").next_to(dot1, UP).scale(0.7)
        text2 = Tex("1").next_to(dot2, UP).scale(0.7)

        bit_group1 = VGroup(dot1, text1)
        bit_group2 = VGroup(dot2, text2)
        self.play(Create(line1), Create(line2))
        self.wait(1)
        self.play(Write(bit_group1), Write(bit_group2))
        self.wait(1)

        time = 0.0
        on_screen_time = Variable(time, Text("t"), num_decimal_places=2).shift(UP * 2)
        self.wait(1)
        self.play(Write(on_screen_time))

        t2 = 2.0
        time_tracker = on_screen_time.tracker
        self.wait(2)

        self.play(
            line1.animate.shift(LEFT * 8),
            line2.animate.shift(LEFT * 8),
            time_tracker.animate.set_value(t2),
            run_time=2,
            rate_func=linear,
        )
        self.wait(1)


class wire_classical(Scene):
    def construct(self):
        dot1 = Dot(WIRE1_START)
        dot2 = Dot(WIRE2_START)

        line1 = Line(WIRE1_START, WIRE1_END)
        line2 = Line(WIRE2_START, WIRE2_END)
        dot1.move_to(line1.get_start())
        dot2.move_to(line2.get_start())
        text1 = Tex("0").next_to(dot1, UP).scale(0.7)
        text2 = Tex("1").next_to(dot2, UP).scale(0.7)

        bit_group1 = VGroup(dot1, text1)
        bit_group2 = VGroup(dot2, text2)
        self.play(Create(line1), Create(line2))
        self.wait(1)
        self.play(Write(bit_group1), Write(bit_group2))
        self.wait(1)

        t1 = ValueTracker(line1.get_start()[0])
        t2 = ValueTracker(line2.get_start()[0])
        time = 0.0
        on_screen_time = Variable(time, Text("t"), num_decimal_places=2).shift(UP)
        self.play(Write(on_screen_time))
        time_tracker = on_screen_time.tracker
        time2 = 2.0
        bit_group1.add_updater(lambda x: x.set_x(t1.get_value()))
        bit_group2.add_updater(lambda x: x.set_x(t2.get_value()))
        self.wait(1)
        self.play(
            t1.animate.set_value(line1.get_end()[0]),
            t2.animate.set_value(line2.get_end()[0]),
            time_tracker.animate.set_value(time2),
            rate_func=linear,
            run_time=2.0,
        )
        self.wait(1)


class QubitReal(VGroup):
    def __init__(self, magnitude_1, loc):
        super().__init__()
        self.magnitude_0 = np.sqrt(1 - magnitude_1 * magnitude_1)
        self.magnitude_1 = magnitude_1
        arrow = Vector([1 / 2, 0, 0], color=GREEN)
        self.label = Text("")
        zero = Tex(r"$|0\rangle$", color=BLUE).scale(0.5)
        one = Tex(r"$|1\rangle$", color=RED).scale(0.5)
        # myTemplate = TexTemplate()
        # myTemplate.add_to_preamble(r"\usepackage{mathtools}")
        # myTemplate.add_to_preamble(r"\DeclarePairedDelimiter\bra{\langle}{\rvert}")
        # one = Tex(r"\ket{1}", tex_template = myTemplate).scale(0.5)

        self.circle = Circle(0.5, color=WHITE).move_to(loc + UP * 3 / 4)
        self.add(self.circle, arrow)
        center = self.circle.get_center()
        arrow.move_to(center + RIGHT / 4)
        arrow.rotate(angle=magnitude_1 * np.pi, about_point=center)
        self.arrow = arrow
        self.add(zero.move_to(center + RIGHT * 4 / 5))
        self.add(one.move_to(center + LEFT * 4 / 5))
        dot = Dot(center + DOWN * 3 / 4)
        self.add(dot)
        self.color_map = {".": BLUE, " ": RED}

    def rotate_vec(self, m0, m1, ang):
        angle = ang * np.pi / 2
        cos = np.cos(angle)
        sin = np.sin(angle)
        rotate_matrix = np.array([[cos, -sin], [sin, cos]])
        rotated = np.matmul(rotate_matrix, np.array([m0, m1]))
        return rotated

    def update_qubit(self, ang):
        arrow_points = self.arrow.get_points()
        anim = Rotate(
            self.arrow,
            angle=ang * np.pi,
            about_point=arrow_points[0],
            axis=([0, 0, 1]),
        )
        rotated = self.rotate_vec(self.magnitude_0, self.magnitude_1, ang)

        self.magnitude_0, self.magnitude_1 = rotated[0], rotated[1]

        return anim

    def hadamard_gate(self):
        # In my basis, z coresponds to RIGHT, x coresponds to UP, y coresponds to out of page
        arrow_points = self.arrow.get_points()
        anim = Rotate(
            self.arrow,
            angle=180 * DEGREES,
            about_point=arrow_points[0],
            axis=([1, 1, 0]),
        )
        # self.update_qubit(2)
        m0 = self.magnitude_0 * np.array([1 / np.sqrt(2), 1 / np.sqrt(2)])
        m1 = self.magnitude_1 * np.array([1 / np.sqrt(2), -1 / np.sqrt(2)])
        m_total = m0 + m1
        self.magnitude_0, self.magnitude_1 = m_total[0], m_total[1]
        return anim

    def get_values(self, precision):
        return np.around((self.magnitude_0, self.magnitude_1), decimals=precision)

    def measure(self):
        value1, value2 = self.get_values(5)
        self.chart = (
            BarChart((value1 ** 2, value2 ** 2), bar_names=["0", "1"])
            .scale(0.4)
            .move_to(self.get_center() + [2.4, 0, 0])
        )
        anim = Transform(self.copy(), self.chart)
        return anim

    def add_coord(self):
        m0, m1 = self.get_values(2)
        pts = self.arrow.get_points()

        self.label = (
            Tex(r"(", str(m0) + ",", " " + str(m1), ")")
            .move_to(pts[0] + UP * 3 / 4)
            .scale(0.5)
        )
        self.label.set_color_by_tex_to_color_map(self.color_map)
        self.add(self.label)

    def update_coord(self):
        m0, m1 = self.get_values(2)
        pts = self.arrow.get_points()
        label = (
            Tex(r"(", str(m0) + ",", " " + str(m1), ")")
            .move_to(pts[0] + UP * 3 / 4)
            .scale(0.5)
        )
        label.set_color_by_tex_to_color_map(self.color_map)
        return Transform(self.label, label)

    # def clear_arrow(self):
    #     self.remove(self.arrow)
    #     self.arrow = None

    # @override_animate(clear_arrow)
    # def _clear_arrow_animation(self, anim_args=None):
    #     if anim_args is None:
    #         anim_args = {}
    #     anim = Uncreate(self.arrow, **anim_args)
    #     self.clear_arrow()
    #     return anim


class Hgate(VGroup):
    def __init__(self):
        super().__init__()
        outline = Square(0.5).set_fill(BLACK, opacity=1.0)
        self.label = Text("H").scale(0.75).move_to(outline.get_center())
        self.add(outline)
        self.add(self.label)

    def use(self):
        return self.label.animate.set_color(GREY)


class Mgate(VGroup):
    def __init__(self):
        super().__init__()
        outline = Square(0.5).set_fill(BLACK, opacity=1.0)
        self.label = Text("M").scale(0.75).move_to(outline.get_center())
        self.add(outline)
        self.add(self.label)

    def use(self):
        return self.label.animate.set_color(GREY)


class Cnot(VGroup):
    def __init__(self, direction, start):
        super().__init__()
        self.outline = Circle(0.25).set_fill(BLUE, opacity=1.0).move_to(start)
        self.label = Text("+", width=1).scale(0.25).move_to(self.outline.get_center())
        self.dot = Dot(self.outline.get_center() + direction * 2)
        self.line = Line(self.outline.get_center(), self.dot.get_center())
        self.add(self.outline)
        self.add(self.label)
        self.add(self.dot)
        self.add(self.line)

    def use(self):
        return VGroup(self.label, self.dot, self.line).animate.set_color(GREY)


class quantum_bit(Scene):
    def construct(self):
        dot1 = Dot([0, 0, 0])
        dot2 = Dot([0, 0, 0])

        text1 = Tex("1").next_to(dot1, UP).scale(0.7)
        text2 = Tex("0").next_to(dot2, UP).scale(0.7)

        bit_group2 = VGroup(dot1, text1)
        bit_group1 = VGroup(dot2, text2)
        self.add(bit_group1)
        self.wait(1)
        self.play(ReplacementTransform(bit_group1, bit_group2))
        self.wait(1)
        # Depricated
        q1 = QubitReal(1, [2, 0, 0])
        q1.add_coord()
        question = Text("?", color=YELLOW).move_to([-2, 0.25, 0])

        self.play(bit_group2.animate.shift(LEFT * 2), Write(q1))
        bg1 = VGroup(Dot([-2, 0, 0]), Tex("0").next_to([-2, 0, 0], UP).scale(0.7))
        self.wait(1)
        arrow = DoubleArrow([-1.5, 0, 0], [1.5, 0, 0], color=BLUE)
        self.play(Write(arrow))
        self.wait(1)
        self.play(
            q1.update_qubit(1), q1.update_coord(), ReplacementTransform(bit_group2, bg1)
        )
        self.wait(0.5)
        self.play(
            q1.update_qubit(0.5),
            q1.update_coord(),
            ReplacementTransform(bg1, question),
        )
        self.wait(0.5)
        self.play(
            q1.update_qubit(-1), q1.update_coord()
        )  # TODO: Figure out why there is a bug with -1.25
        self.wait(0.5)
        self.play(q1.update_qubit(1.5), q1.update_coord())
        self.play(q1.hadamard_gate(), q1.update_coord())

        self.wait(1)


class quantum_amplitude(Scene):
    def construct(self):
        q1 = QubitReal(0, [0, -1, 0])
        # self.play(Write(q1))
        # myTemplate = TexTemplate()
        # myTemplate.add_to_preamble(r"\usepackage{mathtools}")
        # myTemplate.add_to_preamble(r"\DeclarePairedDelimiter\bra{\langle}{\rvert}")
        # one = Tex(r"$|1\rangle$").scale(0.5)
        color_map = {r"|0\rangle": BLUE, r"|1\rangle": RED}
        label = (
            Tex(r"$(a + bi)$", r"$|0\rangle$", r"$+$", "$(c + di)$", r"$|1\rangle$")
            .move_to([0, 1, 0])
            .scale(2)
        )
        label0 = Tex(r"$|0\rangle$", r"$+$", r"$|1\rangle$").move_to([0, 1, 0]).scale(2)
        label0.set_color_by_tex_to_color_map(color_map)
        label.set_color_by_tex_to_color_map(color_map)
        self.play(Write(label0))
        self.wait(1)
        self.play(ReplacementTransform(label0, label))
        self.wait(1)
        amplitude_box = VGroup(
            SurroundingRectangle(label[0]), SurroundingRectangle(label[3])
        )
        self.play(Create(amplitude_box))
        self.wait(1)


class probability(Scene):
    def construct(self):
        q1 = QubitReal(0, [0, -1, 0])
        # self.play(Write(q1))
        # myTemplate = TexTemplate()
        # myTemplate.add_to_preamble(r"\usepackage{mathtools}")
        # myTemplate.add_to_preamble(r"\DeclarePairedDelimiter\bra{\langle}{\rvert}")
        # one = Tex(r"$|1\rangle$").scale(0.5)
        color_map = {r"|0\rangle": BLUE, r"|1\rangle": RED}
        label = (
            Tex(r"$(a + bi)$", r"$|0\rangle$", r"$+$", r"$(c + di)$", r"$|1\rangle$")
            .move_to([0, 1, 0])
            .scale(2)
        )
        label.set_color_by_tex_to_color_map(color_map)
        label2 = (
            Tex(
                r"$(1/\sqrt{2})$",
                r"$|0\rangle$",
                r"$+$",
                r"$(1/\sqrt{2})$",
                r"$|1\rangle$",
            )
            .move_to([0, 1, 0])
            .scale(2)
        )
        label2.set_color_by_tex_to_color_map(color_map)
        amplitude_box1 = VGroup(
            SurroundingRectangle(label[0]), SurroundingRectangle(label[3])
        )
        amplitude_box2 = VGroup(
            SurroundingRectangle(label2[0]), SurroundingRectangle(label2[3])
        )
        self.add(label, amplitude_box1)
        self.wait(1)
        self.play(
            ReplacementTransform(label, label2),
            ReplacementTransform(amplitude_box1, amplitude_box2),
        )

        amplitude = Tex(r"$|1/\sqrt{2}|^2 = $", r"$1/2$").move_to([-2, -1.5, 0])
        amplitude2 = amplitude.copy()
        amplitude2.shift(RIGHT * 4)
        # amplitude2 = Tex(
        #     r"$|i/\sqrt{2}|^2 =i /\sqrt{2} \times (-i/\sqrt{2}) = 1/2$"
        # ).move_to([3, -1.5, 0])
        self.wait(1)
        framebox1 = SurroundingRectangle(amplitude[1])
        framebox2 = SurroundingRectangle(amplitude2[1])
        self.play(Write(amplitude))
        self.wait(0.25)
        self.play(ReplacementTransform(amplitude_box2[0], framebox1))
        self.wait(1)
        self.play(Write(amplitude2), ReplacementTransform(amplitude_box2[1], framebox2))

        chart = BarChart((1 / 2, 1 / 2), bar_names=[r"|0\rangle", r"|1\rangle"])
        self.wait(3)
        self.play(
            ReplacementTransform(
                VGroup(framebox1, amplitude, label2, amplitude2, framebox2), chart
            )
        )

        self.wait(1)


class hadamard_0(Scene):
    def construct(self):
        line1 = Line([-4, 0, 0], [4, 0, 0])
        line2 = Line([-4, -2, 0], [4, -2, 0])

        h_gate = Hgate().move_to([0, 1, 0])
        self.play(Write(h_gate))
        self.add_foreground_mobjects(h_gate)
        self.wait()

        q1 = QubitReal(0, [-4, 0, 0])
        q2 = QubitReal(1, [-4, -2, 0])

        self.play(Write(line1), Write(line2), h_gate.animate.move_to([-2, 0, 0]))
        self.wait(0.25)
        self.play(Write(q1), Write(q2))
        self.wait(1)

        self.play(q2.animate.shift(RIGHT * 2), q1.animate.shift(RIGHT * 2))
        # q1_new = QubitReal(0.5).move_to(q1_loc + RIGHT * 2) + d1
        reflection_line = Line([-2.35, 0.4, 0], [-1.65, 1.1, 0], color=YELLOW)
        self.wait(1)
        self.play(FadeIn(reflection_line))
        self.wait(1)
        self.play(q1.hadamard_gate(), run_time=2, rate_func=linear)
        self.wait(1)
        self.play(FadeOut(reflection_line), h_gate.use())
        self.wait(1)

        self.play(q1.animate.shift(RIGHT * 6), q2.animate.shift(RIGHT * 6))

        self.wait(1)


class hadamard_1(Scene):
    def construct(self):
        line1 = Line([-4, 0, 0], [4, 0, 0])
        line2 = Line([-4, -2, 0], [4, -2, 0])

        h_gate = Hgate().move_to([0, 1, 0])
        self.play(Write(h_gate))
        self.add_foreground_mobjects(h_gate)
        self.wait()

        q1_loc = [-4, 0, 0]
        q2_loc = [-4, -2, 0]
        q1 = QubitReal(0, q1_loc)
        q2 = QubitReal(1, q2_loc)

        self.play(Write(line1), Write(line2), h_gate.animate.move_to([-2, -2, 0]))
        self.play(Write(q1), Write(q2))
        self.wait(1)

        self.play(q2.animate.shift(RIGHT * 2), q1.animate.shift(RIGHT * 2))
        # q1_new = QubitReal(0.5).move_to(q1_loc + RIGHT * 2) + d1
        reflection_line = Line([-2.35, -1.6, 0], [-1.65, -0.9, 0], color=YELLOW)
        self.play(FadeIn(reflection_line))
        self.play(q2.hadamard_gate())
        self.play(FadeOut(reflection_line), h_gate.use())

        self.play(q1.animate.shift(RIGHT * 6), q2.animate.shift(RIGHT * 6))

        self.wait(2)
        self.wait()


class storage(Scene):
    def construct(self):
        q1 = QubitReal(0, [0, 0, 0])
        q2 = QubitReal(0.1, [0, 0, 0])
        q1.add_coord()
        q2.add_coord()
        self.play(Write(q1))
        self.wait(1)
        self.play(q1.hadamard_gate(), q1.update_coord())
        self.wait(1)
        self.play(q1.update_qubit(1), q1.update_coord())
        self.play(q1.update_qubit(0.5), q1.update_coord())
        self.play(q1.update_qubit(-0.25), q1.update_coord())
        self.play(q1.update_qubit(1), q1.update_coord())
        self.play(q1.update_qubit(-1.75), q1.update_coord())
        self.play(q1.update_qubit(-0.25), q1.update_coord())

        text = Tex(r"0.9012345678", r"$|0\rangle$").move_to([0, -2, 0])
        color_map = {r"|0\rangle": BLUE, r"|1\rangle": RED}
        text.set_color_by_tex_to_color_map(color_map)
        self.play(ReplacementTransform(q1, q2), Write(text))

        self.wait(1)


class measure_scene(Scene):
    def construct(self):
        line1 = Line([-4, 0, 0], [3, 0, 0])
        line2 = Line([-4, -2, 0], [3, -2, 0])

        m_gate_old = Mgate().move_to([0, 2, 0])
        self.play(Write(m_gate_old))
        h_gate = Hgate().move_to([-2, 0, 0])
        q1_loc = [-4, 0, 0]
        q2_loc = [-4, -2, 0]
        q1 = QubitReal(0, q1_loc)
        q2 = QubitReal(0, q2_loc)
        m_gate = VGroup(Mgate().move_to([3, 0, 0]), Mgate().move_to([3, -2, 0]))

        self.wait(1)
        self.play(
            Write(line1),
            Write(line2),
            Write(h_gate),
            ReplacementTransform(m_gate_old, m_gate),
        )
        self.add_foreground_mobjects(h_gate, m_gate)
        self.wait(1)
        self.play(Write(q1), Write(q2))
        self.wait(1)

        self.play(q2.animate.shift(RIGHT * 2), q1.animate.shift(RIGHT * 2))
        self.wait(1)
        self.play(q1.hadamard_gate(), run_time=0.5)
        self.wait(1)
        self.play(q1.animate.shift(RIGHT * 5), q2.animate.shift(RIGHT * 5))
        self.wait(1)
        self.play(q1.measure())
        self.wait(1)

        self.play(q2.measure())
        self.wait()


class fourAmplitudes(VGroup):
    def __init__(self, zero0, zero1, one0, one1):
        super().__init__()
        color_map = {"0": BLUE, "1": RED}
        color_map2 = {r"|": WHITE}
        HEIGHT = -3
        zerozero = Tex(zero0 + r"$|$", r"$0$", r"$0$", r"$\rangle$").move_to(
            [-4.5, HEIGHT, 0]
        )
        zeroone = Tex(zero1 + r"$|$", r"$0$", r"$1$", r"$\rangle$").move_to(
            [-1.5, HEIGHT, 0]
        )
        onezero = Tex(one0 + r"$|$", r"$1$", r"$0$", r"$\rangle$").move_to(
            [1.5, HEIGHT, 0]
        )
        oneone = Tex(one1 + r"$|$", r"$1$", r"$1$", r"$\rangle$").move_to(
            [4.5, HEIGHT, 0]
        )
        zerozero.set_color_by_tex_to_color_map(color_map)
        zeroone.set_color_by_tex_to_color_map(color_map)
        onezero.set_color_by_tex_to_color_map(color_map)
        oneone.set_color_by_tex_to_color_map(color_map)
        zerozero.set_color_by_tex_to_color_map(color_map2)
        zeroone.set_color_by_tex_to_color_map(color_map2)
        onezero.set_color_by_tex_to_color_map(color_map2)
        oneone.set_color_by_tex_to_color_map(color_map2)
        self.add(zerozero)
        self.add(zeroone)
        self.add(onezero)
        self.add(oneone)


class twoAmplitudes(VGroup):
    def __init__(self, zero0, one1):
        super().__init__()
        color_map = {"0": BLUE, "1": RED}
        color_map2 = {r"|": WHITE}
        HEIGHT = -3
        zero = Tex(zero0 + r"$|$", r"$0$", r"$\rangle$").move_to([-1.5, HEIGHT, 0])
        one = Tex(one1 + r"$|$", r"$1$", r"$\rangle$").move_to([1.5, HEIGHT, 0])

        zero.set_color_by_tex_to_color_map(color_map)
        one.set_color_by_tex_to_color_map(color_map)
        zero.set_color_by_tex_to_color_map(color_map2)
        one.set_color_by_tex_to_color_map(color_map2)
        self.add(zero)
        self.add(one)


class four_amplitudes(Scene):
    def construct(self):
        line1 = Line([-4, 0, 0], [3, 0, 0])
        line2 = Line([-4, -2, 0], [3, -2, 0])

        h_gate = Hgate().move_to([-2, 0, 0])
        q1_loc = [-4, 0, 0]
        q2_loc = [-4, -2, 0]
        q1 = QubitReal(0, q1_loc)
        q2 = QubitReal(0, q2_loc)
        m_gate = VGroup(Mgate().move_to([3, 0, 0]), Mgate().move_to([3, -2, 0]))
        self.add_foreground_mobjects(h_gate, m_gate)

        self.add(line1, line2, h_gate, m_gate, q1, q2)
        self.wait(1)
        amps1 = fourAmplitudes(r"$1$", r"$0$", r"$0$", r"$0$")
        self.play(Write(amps1))
        self.wait(1)

        self.play(q2.animate.shift(RIGHT * 2), q1.animate.shift(RIGHT * 2))
        self.wait(1)
        amps2 = fourAmplitudes(
            r"$\frac{1}{\sqrt{2}}$", r"$0$", r"$\frac{1}{\sqrt{2}}$", r"$0$"
        )
        self.play(q1.hadamard_gate(), ReplacementTransform(amps1, amps2))
        self.wait(1)
        self.play(q1.animate.shift(RIGHT * 5), q2.animate.shift(RIGHT * 5))
        self.wait(1)
        self.play(q1.measure(), q2.measure())
        self.wait(1)


# might not need but could be good to see for prep for final bell state
class four_amplitudes2(Scene):
    def construct(self):
        line1 = Line([-4, 0, 0], [3, 0, 0])
        line2 = Line([-4, -2, 0], [3, -2, 0])

        h_gate = VGroup(Hgate().move_to([-2, 0, 0]), Hgate().move_to([-2, -2, 0]))
        m_gates = VGroup(Mgate().move_to([3, 0, 0]), Mgate().move_to([3, -2, 0]))
        q1_loc = [-4, 0, 0]
        q2_loc = [-4, -2, 0]
        q1 = QubitReal(0, q1_loc)
        q2 = QubitReal(0, q2_loc)
        self.add_foreground_mobjects(h_gate, m_gates)

        self.add(line1, line2, h_gate, m_gates, q1, q2)
        self.wait(1)
        amps1 = fourAmplitudes(r"$0$", r"$1$", r"$0$", r"$0$")
        self.play(Write(amps1))
        self.wait(1)

        self.play(q2.animate.shift(RIGHT * 2), q1.animate.shift(RIGHT * 2))
        self.wait(1)
        amps2 = fourAmplitudes(
            r"$\frac{1}{2}$", r"$\frac{1}{2}$", r"$\frac{1}{2}$", r"$\frac{1}{2}$"
        )
        self.play(
            q1.hadamard_gate(),
            q2.hadamard_gate(),
            RotateTransform(amps1, amps2),
            run_time=1.5,
        )
        self.wait(2)
        self.play(q1.animate.shift(RIGHT * 5), q2.animate.shift(RIGHT * 5))
        self.wait(1)
        self.play(q1.measure(), q2.measure())
        self.wait(1)


class cnot_classical(Scene):
    def construct(self):
        # TODO:
        line1 = Line(WIRE1_START, WIRE1_END + RIGHT)
        line2 = Line(WIRE2_START, WIRE2_END + RIGHT)
        c_not = Cnot(UP, [0, -2, 0])
        grp = VGroup(line1, line2, c_not)
        self.play(Write(grp))
        self.wait(1)
        self.play(FadeOut(grp))
        self.wait(1)

        q1 = QubitReal(0, [0, 0, 0])
        q2 = QubitReal(1, [0, 0, 0])
        amps1 = twoAmplitudes(r"$1$", r"$0$")
        q3 = q1.copy()
        self.play(Write(q1), Write(amps1))
        self.wait(1)
        self.play(ReplacementTransform(q1, q2), Swap(amps1[0][0], amps1[1][0]))
        self.wait(1)
        self.play(ReplacementTransform(q2, q3), Swap(amps1[0][0], amps1[1][0]))

        self.wait(1)


class cnot_no_amp(Scene):
    def construct(self):
        line1 = Line([-4, 0, 0], [3, 0, 0])
        line2 = Line([-4, -2, 0], [3, -2, 0])
        self.play(Write(line1), Write(line2))
        c_not = Cnot(UP, [0, -2, 0])
        m_gate = VGroup(Mgate().move_to([3, 0, 0]), Mgate().move_to([3, -2, 0]))

        self.add_foreground_mobjects(c_not, m_gate)
        self.play(Write(c_not), Write(m_gate))
        q1 = QubitReal(1, [-4, 0, 0])
        q2 = QubitReal(0, [-4, -2, 0])
        self.wait(1)
        control_box = SurroundingRectangle(c_not[2])
        self.play(Create(control_box))
        self.wait(1)
        target_box = SurroundingRectangle(c_not[0])
        self.play(ReplacementTransform(control_box, target_box))
        self.wait(1)
        self.play(FadeIn(q1, q2), FadeOut(target_box))
        self.wait(1)
        self.play(q1.animate.shift(RIGHT * 4), q2.animate.shift(RIGHT * 4))
        self.play(q2.update_qubit(1), c_not.use())
        self.wait(1)
        self.play(q1.animate.shift(RIGHT * 3), q2.animate.shift(RIGHT * 3))
        self.wait(1)
        self.play(q1.measure(), q2.measure(), m_gate[0].use(), m_gate[1].use())
        self.wait(1)


class cnot_scene(Scene):
    def construct(self):
        line1 = Line([-4, 0, 0], [3, 0, 0])
        line2 = Line([-4, -2, 0], [3, -2, 0])
        self.play(Write(line1), Write(line2))
        c_not = Cnot(UP, [0, -2, 0])
        m_gate = VGroup(Mgate().move_to([3, 0, 0]), Mgate().move_to([3, -2, 0]))

        self.add_foreground_mobjects(c_not, m_gate)
        self.play(Write(c_not), Write(m_gate))
        q1 = QubitReal(1, [-4, 0, 0])
        q2 = QubitReal(0, [-4, -2, 0])
        self.wait(1)
        control_box = SurroundingRectangle(c_not[2])
        self.play(Create(control_box))
        self.wait(1)
        target_box = SurroundingRectangle(c_not[0])
        self.play(ReplacementTransform(control_box, target_box))
        self.wait(1)
        amps1 = fourAmplitudes(r"$0$", r"$0$", r"$1$", r"$0$")
        self.play(FadeIn(q1, q2), FadeOut(target_box), FadeIn(amps1))
        self.wait(1)
        self.play(q1.animate.shift(RIGHT * 4), q2.animate.shift(RIGHT * 4))
        self.wait(1)
        self.play(q2.update_qubit(1), Swap(amps1[2][0], amps1[3][0]), c_not.use())
        self.wait(1)
        self.play(q1.animate.shift(RIGHT * 3), q2.animate.shift(RIGHT * 3))
        self.wait(1)
        self.play(q1.measure(), q2.measure(), m_gate[0].use(), m_gate[1].use())
        self.wait(1)


class cnot_no_amp2(Scene):
    def construct(self):
        line1 = Line([-4, 0, 0], [3, 0, 0])
        line2 = Line([-4, -2, 0], [3, -2, 0])
        self.play(Write(line1), Write(line2))
        c_not = Cnot(UP, [0, -2, 0])
        m_gate = VGroup(Mgate().move_to([3, 0, 0]), Mgate().move_to([3, -2, 0]))

        self.add_foreground_mobjects(c_not, m_gate)
        self.play(Write(c_not), Write(m_gate))
        q1 = QubitReal(0, [-4, 0, 0])
        q2 = QubitReal(1, [-4, -2, 0])
        self.wait(1)
        self.play(FadeIn(q1, q2))
        self.wait(1)
        self.play(q1.animate.shift(RIGHT * 4), q2.animate.shift(RIGHT * 4))
        self.wait(1)
        self.play(c_not.use())
        self.wait(1)
        self.play(q1.animate.shift(RIGHT * 3), q2.animate.shift(RIGHT * 3))
        self.wait(1)
        self.play(q1.measure(), q2.measure(), m_gate[0].use(), m_gate[1].use())
        self.wait(1)


class cnot_quick1(Scene):
    def construct(self):
        line1 = Line([-4, 0, 0], [3, 0, 0])
        line2 = Line([-4, -2, 0], [3, -2, 0])
        c_not = Cnot(UP, [0, -2, 0])
        m_gate = VGroup(Mgate().move_to([3, 0, 0]), Mgate().move_to([3, -2, 0]))

        self.add_foreground_mobjects(c_not, m_gate)
        self.add(line1, line2, c_not, m_gate)
        q1 = QubitReal(0, [-4, 0, 0])
        q2 = QubitReal(1, [-4, -2, 0])
        self.wait(1)
        amps1 = fourAmplitudes(r"$0$", r"$1$", r"$0$", r"$0$")
        self.play(FadeIn(q1, q2), FadeIn(amps1))
        self.wait(1)
        self.play(q1.animate.shift(RIGHT * 4), q2.animate.shift(RIGHT * 4))
        self.wait(1)
        self.play(Swap(amps1[2][0], amps1[3][0]), c_not.use())
        self.wait(1)
        self.play(q1.animate.shift(RIGHT * 3), q2.animate.shift(RIGHT * 3))
        self.wait(1)
        self.play(q1.measure(), q2.measure(), m_gate[0].use(), m_gate[1].use())
        self.wait(1)


class bell_state_intro(Scene):  # intro scene
    def construct(self):
        line1 = Line([-4, 0, 0], [3, 0, 0])
        line2 = Line([-4, -2, 0], [3, -2, 0])
        self.play(Write(line1), Write(line2))
        c_not = Cnot(UP, [0, -2, 0])
        h_gate = Hgate().move_to([-2, 0, 0])
        m_gate = VGroup(Mgate().move_to([3, 0, 0]), Mgate().move_to([3, -2, 0]))

        self.add_foreground_mobjects(c_not, h_gate, m_gate)
        self.play(Write(c_not), Write(h_gate), Write(m_gate))
        q1 = QubitReal(0, [-4, 0, 0])
        q2 = QubitReal(0, [-4, -2, 0])
        self.wait(5)  # 7s
        self.play(FadeIn(q1, q2))  # 8s
        self.wait(3)  # 9s
        self.play(q1.animate.shift(RIGHT * 2), q2.animate.shift(RIGHT * 2))  # 10s
        self.play(q1.hadamard_gate(), run_time=0.75)  # 11s
        self.play(q1.animate.shift(RIGHT * 2), q2.animate.shift(RIGHT * 2))  # 12s
        self.play(q2.update_qubit(1 / 2), run_time=0.75)  # 13s

        self.play(q1.animate.shift(RIGHT * 3), q2.animate.shift(RIGHT * 3))  # 14s
        self.play(q1.measure(), q2.measure())  # 15
        chart = (
            BarChart((1 / 2, 1 / 2), bar_names=["00", "11"])
            .scale(0.7)
            .move_to([4, -1, 0])
        )
        bell_text = Text("Bell State").move_to([4, 1.5, 0])
        self.play(
            VGroup(q1, q2, line1, line2, h_gate, c_not, m_gate).animate.shift(LEFT * 2)
        )
        self.play(Transform((q1 + q2), chart))
        self.wait(3.5)  # 23s
        self.play(Write(bell_text))
        self.wait(3)  # 27
        framebox1 = SurroundingRectangle(
            chart[4][0], buff=0.1
        )  # x-axis components, first of the components
        self.play(Create(framebox1))  # 28
        framebox2 = SurroundingRectangle(
            chart[4][1], buff=0.1
        )  # x-axis components, first of the com.
        self.wait(2)
        self.play(ReplacementTransform(framebox1, framebox2))  # 31
        self.wait(3)


class bell_state_quick(Scene):  # intro scene
    def construct(self):
        TIME = 0.1
        line1 = Line([-4, 0, 0], [3, 0, 0])
        line2 = Line([-4, -2, 0], [3, -2, 0])
        self.play(Write(line1), Write(line2))
        c_not = Cnot(UP, [0, -2, 0])
        h_gate = Hgate().move_to([-2, 0, 0])
        m_gate = VGroup(Mgate().move_to([3, 0, 0]), Mgate().move_to([3, -2, 0]))
        self.wait(1)
        self.play(Write(h_gate), Write(c_not), Write(m_gate))
        self.add_foreground_mobjects(c_not, h_gate, m_gate)
        q1 = QubitReal(0, [-4, 0, 0])
        q2 = QubitReal(0, [-4, -2, 0])
        amps1 = fourAmplitudes(r"$1$", r"$0$", r"$0$", r"$0$")
        amps2 = fourAmplitudes(
            r"$\frac{1}{\sqrt{2}}$", r"$0$", r"$\frac{1}{\sqrt{2}}$", r"$0$"
        )
        self.wait(TIME)
        self.play(FadeIn(q1, q2, amps1))
        self.wait(TIME)
        self.play(q1.animate.shift(RIGHT * 2), q2.animate.shift(RIGHT * 2))
        self.wait(TIME)
        self.play(q1.hadamard_gate(), h_gate.use(), run_time=2)
        self.wait(TIME)
        self.play(ReplacementTransform(amps1, amps2))
        self.wait(TIME)
        self.play(q1.animate.shift(RIGHT * 2), q2.animate.shift(RIGHT * 2))
        self.wait(TIME)
        arc = ArcBetweenPoints(
            [4.15, -3, 0], [1.4, -2.97, 0], angle=np.pi
        )  # [4.15, -3, 0], [-1.65, -2.97, 0] old points
        self.play(q2.update_qubit(1 / 2), c_not.use())
        self.wait(TIME)
        self.play(
            amps2[2][0].animate.shift(RIGHT * 2.85), MoveAlongPath(amps2[3][0], arc)
        )
        self.wait(TIME)
        self.play(q1.animate.shift(RIGHT * 3), q2.animate.shift(RIGHT * 3))
        self.wait(TIME)
        self.play(q1.measure(), q2.measure(), m_gate[0].use(), m_gate[1].use())
        self.wait(TIME)
        chart = (
            BarChart((1 / 2, 0, 0, 1 / 2), bar_names=["00", "01", "10", "11"])
            .scale(0.7)
            .move_to([-2, -0.5, 0])
        )
        bell_text = Text("Bell State").move_to([0, 1.5, 0])
        self.play(FadeIn(bell_text))
        self.wait(TIME)
        self.play(
            ReplacementTransform(VGroup(line2, line1, h_gate, m_gate, c_not), chart)
        )


class bell_state_final(Scene):  # intro scene
    def construct(self):
        line1 = Line([-4, 0, 0], [3, 0, 0])
        line2 = Line([-4, -2, 0], [3, -2, 0])
        self.play(Write(line1), Write(line2))
        c_not = Cnot(UP, [0, -2, 0])
        h_gate = Hgate().move_to([-2, 0, 0])
        m_gate = VGroup(Mgate().move_to([3, 0, 0]), Mgate().move_to([3, -2, 0]))

        self.play(Write(h_gate))
        self.wait(1)
        self.play(Write(c_not))
        self.wait(1)
        self.play(Write(m_gate))
        self.add_foreground_mobjects(c_not, h_gate, m_gate)
        q1 = QubitReal(0, [-4, 0, 0])
        q2 = QubitReal(0, [-4, -2, 0])
        amps1 = fourAmplitudes(r"$1$", r"$0$", r"$0$", r"$0$")
        amps2 = fourAmplitudes(
            r"$\frac{1}{\sqrt{2}}$", r"$0$", r"$\frac{1}{\sqrt{2}}$", r"$0$"
        )
        self.wait(1)
        self.play(FadeIn(q1, q2, amps1))
        self.wait(1)
        self.play(q1.animate.shift(RIGHT * 2), q2.animate.shift(RIGHT * 2))
        self.wait(1)
        self.play(q1.hadamard_gate(), h_gate.use(), run_time=2)
        self.wait(0.5)
        self.play(ReplacementTransform(amps1, amps2))
        self.wait(1)
        self.play(q1.animate.shift(RIGHT * 2), q2.animate.shift(RIGHT * 2))
        self.wait(1)
        arc = ArcBetweenPoints(
            [4.15, -3, 0], [1.4, -2.97, 0], angle=np.pi
        )  # [4.15, -3, 0], [-1.65, -2.97, 0] old points
        self.play(q2.update_qubit(1 / 2), c_not.use(), run_time=2)
        self.wait(0.5)
        self.play(
            amps2[2][0].animate.shift(RIGHT * 2.85), MoveAlongPath(amps2[3][0], arc)
        )
        self.wait(1)
        self.play(q1.animate.shift(RIGHT * 3), q2.animate.shift(RIGHT * 3))
        self.wait(1)
        self.play(q1.measure(), q2.measure(), m_gate[0].use(), m_gate[1].use())
        self.wait(1)
        chart = (
            BarChart((1 / 2, 0, 0, 1 / 2), bar_names=["00", "01", "10", "11"])
            .scale(0.7)
            .move_to([-2, -0.5, 0])
        )
        bell_text = Text("Bell State").move_to([0, 1.5, 0])
        self.play(FadeIn(bell_text))
        self.wait(2)
        self.play(
            ReplacementTransform(VGroup(line2, line1, h_gate, m_gate, c_not), chart)
        )
        self.wait(1)
        b1 = SurroundingRectangle(chart[4][0])
        b2 = SurroundingRectangle(chart[4][3])
        self.play(Write(b1))
        self.play(Write(b2))
        self.wait(1)
        self.play(FadeOut(b1, b2))
        meas1 = SurroundingRectangle(q1.chart[4][1])
        self.play(Write(meas1))
        meas2 = SurroundingRectangle(q2.chart[4][1])
        meas3 = SurroundingRectangle(chart[4][3])
        self.wait(1)
        self.play(Write(meas2))
        self.wait(1)
        self.play(Write(meas3))
        self.wait(1)
        self.play(q2.animate.shift(LEFT * 8 + UP * 8), run_time=4, rate_func=linear)
        self.wait(1)


class outro(Scene):
    def construct(self):
        goodbye = Text("https://qiskit.org/textbook").move_to([0, 1, 0])
        self.play(Write(goodbye))
        image = ImageMobject("qiskit-logo").move_to([0, -2, 0]).scale(0.5)
        self.play(FadeIn(image))
        self.wait(2)


class image_test(Scene):
    def construct(self):
        image = ImageMobject("test_image").scale(0.5)
        self.play(FadeIn(image))
        self.wait()
