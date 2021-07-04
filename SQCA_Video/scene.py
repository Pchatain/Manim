from typing import Text, get_origin
from manim import *
import numpy as np

# TODO: define quanta in a class

class prereq(Scene):
  def construct(self):
    knowledge = Text("Prerequisite Knowledge").shift(UP).shift(LEFT)
    self.play(Write(knowledge))
    list_of_content = MathTex(
            r'&\text{1.  Linear algebra}\\',
            r'&\text{2.  Basic circuits computer science}\\',
            r'&\text{3.  Complex numbers}',
        ).shift(DOWN)
    self.play(Write(list_of_content))
    # knowledge = Text("Prerequisite Knowledge").shift(UP).shift(LEFT)
    # self.play(Write(knowledge))
    # p1 = Text("1.  Basic Linear algebra").scale(0.5).shift(LEFT)
    # self.play(Write(p1))
    # p2 = Text("2.  Basic circuit computer science").scale(0.5).shift(DOWN)
    # self.play(Write(p2))



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
    circ = Circle().next_to(points[len(points)/2])
    self.add(circ)
    self.wait(1)

class classical_circuit(Scene):
  def construct(self):

    dot1 = Dot([-4, 0, 0])
    dot2 = Dot([-4, -1, 0])
    
    line1 = Line([-4, 0, 0], [4, 0, 0])
    line2 = Line([-4, -1, 0], [4, -1, 0])
    dot1.move_to(line1.get_start())
    dot2.move_to(line2.get_start())
    text1=Tex("0").next_to(dot1, UP).scale(0.7)
    text2=Tex("1").next_to(dot2, UP).scale(0.7)

    bit_group1 = VGroup(dot1, text1)
    bit_group2 = VGroup(dot2, text2)
    self.play(Create(line1), Create(line2))
    self.play(Write(bit_group1), Write(bit_group2))

    t1 = ValueTracker(line1.get_start()[0])
    t2 = ValueTracker(line2.get_start()[0])
    time = 0.0
    on_screen_time = Variable(time, Text("t"), num_decimal_places=2).shift(UP)
    self.play(Write(on_screen_time))
    time_tracker = on_screen_time.tracker
    time2 = 2.0
    bit_group1.add_updater(lambda x: x.set_x(t1.get_value()))
    bit_group2.add_updater(lambda x: x.set_x(t2.get_value()))

    self.play(t1.animate.set_value(line1.get_end()[0]), t2.animate.set_value(line2.get_end()[0]), time_tracker.animate.set_value(time2),rate_func=linear,run_time=2.0)
 

class wire_classical(Scene):
  def construct(self):    
    d1 = Dot([-4, 0, 0])
    d2 = Dot([-4, -1, 0])
    d1_moved = Dot([4, 0, 0])
    d2_moved = Dot([4, -1, 0])

    d1_text = Text("0").next_to(d1, UP).scale(0.7)
    d2_text = Text("1").next_to(d2, UP).scale(0.7)
    d1_text_moved = Text("0").next_to(d1_moved, UP).scale(0.7)
    d2_text_moved = Text("1").next_to(d2_moved, UP).scale(0.7)
    # In classical, everyday bits, they can either be a 0, or a 1. 
    self.play(Write(d1), Write(d2), Write(d1_text), Write(d2_text))
    self.wait(1)

    time = 0.0
    line1 = Line([-4, 0, 0], [4, 0, 0])
    line2 = Line([-4, -1, 0], [4, -1, 0])
    on_screen_time = Variable(time, Text("t"), num_decimal_places=2).shift(UP)
    self.play(Write(line1), Write(line2))
    self.wait(1)
    self.play(Write(on_screen_time))

    t2 = 2.0
    time_tracker = on_screen_time.tracker
    self.wait(2)

    self.play(MoveAlongPath(d1, line1), MoveAlongPath(d2, line2), Transform(d1_text, d1_text_moved), Transform(d2_text, d2_text_moved), time_tracker.animate.set_value(t2), run_time=2, rate_func=linear)
    self.wait()


class QubitReal(VGroup):
    def __init__(self, magnitude_1, loc):
        super().__init__()
        self.magnitude_0 = np.sqrt(1 - magnitude_1 * magnitude_1)
        self.magnitude_1 = magnitude_1
        arrow = Vector([1/2, 0, 0])

        zero = Text("0").scale(0.5)
        one = Text("1").scale(0.5)
        # myTemplate = TexTemplate()
        # myTemplate.add_to_preamble(r"\usepackage{mathtools}")
        # myTemplate.add_to_preamble(r"\DeclarePairedDelimiter\bra{\langle}{\rvert}")
        # one = Tex(r"\ket{1}", tex_template = myTemplate).scale(0.5)

        self.circle = Circle(0.5).move_to(loc + UP * 3/4)
        self.add(self.circle, arrow)
        center = self.circle.get_center()
        arrow.move_to(center + RIGHT/4)
        arrow.rotate(angle=magnitude_1 * np.pi, about_point=center)
        self.arrow = arrow
        self.add(zero.move_to(center + RIGHT * 4/5))
        self.add(one.move_to(center + LEFT * 4/5))
        dot = Dot(center + DOWN * 3/4)
        self.add(dot)


    def update_qubit(self, magnitude_1):
        arrow_points = self.arrow.get_points()
        anim = Rotate(self.arrow, angle=magnitude_1 * np.pi, about_point=arrow_points[0], axis=([0, 0, 1]))
        angle = magnitude_1 * np.pi/2
        cos = np.cos(angle)
        sin = np.sin(angle)
        rotate_matrix = np.array([[cos, sin], [-sin, cos]])
        rotated = np.matmul(rotate_matrix, np.array([self.magnitude_0, self.magnitude_1]))
        # print("_________________")
        # print(f"prev was {np.array([self.magnitude_0, self.magnitude_1])} and now is {rotated}")
        # print("____________")
        self.magnitude_0 = rotated[0]
        self.magnitude_1 = rotated[1]
        return anim

    def hadamard_gate(self):
        arrow_points = self.arrow.get_points()
        anim = Rotate(self.arrow, angle=180 * DEGREES, about_point=arrow_points[0], axis=([1, 1, 0]))
        m0 = self.magnitude_0 * np.array([1/np.sqrt(2), 1/np.sqrt(2)])
        m1 = self.magnitude_1 * np.array([1/np.sqrt(2), -1/np.sqrt(2)])
        m_total = m0 + m1
        self.magnitude_0, self.magnitude_1 = m_total[0], m_total[1]
        return anim

    def get_values(self, precision):
        # print(f"Values are {(self.magnitude_0, self.magnitude_1)}")
        return np.around((self.magnitude_0, self.magnitude_1), decimals=precision)

    def measure(self):
      value1, value2 = self.get_values(5)
      text1 = Text(str(value1)).move_to(self.get_center() + [1, 0, 0]).scale(0.5) # TODO: change to 2 decimal places
      text2 = Text(str(value2)).move_to(self.get_center() + [2, 0, 0]).scale(0.5)
      output = VGroup(text1, text2)
      chart = BarChart((value1**2, value2**2), bar_names = ["0", "1"]).scale(0.4).move_to(self.get_center() + [2, -0.5, 0])
      anim = Transform(self, chart)
      return anim

    def clear_arrow(self):
        self.remove(self.arrow)
        self.arrow = None

    @override_animate(clear_arrow)
    def _clear_arrow_animation(self, anim_args=None):
        if anim_args is None:
            anim_args = {}
        anim = Uncreate(self.arrow, **anim_args)
        self.clear_arrow()
        return anim

class Hgate(VGroup):
  def __init__(self):
    super().__init__()
    outline = Square(0.5).set_fill(BLACK, opacity=1.0)
    label = Text("H").scale(0.75).move_to(outline.get_center())
    self.add(outline) 
    self.add(label)

class Mgate(VGroup):
  def __init__(self):
    super().__init__()
    outline = Square(0.5).set_fill(BLACK, opacity=1.0)
    label = Text("M").scale(0.75).move_to(outline.get_center())
    self.add(outline) 
    self.add(label)

class Cnot(VGroup):
  def __init__(self, direction, start):
    super().__init__()
    outline = Circle(0.25).set_fill(BLUE, opacity=1.0).move_to(start)
    label = Text("+", width=1).scale(0.25).move_to(outline.get_center())
    dot = Dot(outline.get_center() + direction*2)
    line = Line(outline.get_center(), dot.get_center())
    self.add(outline)
    self.add(label)
    self.add(dot)
    self.add(line)

class quantum_bit(Scene):
  def construct(self):

    # Depricated
    # q1 = QubitReal(0, [-4, 1, 0])
    # q_new = QubitReal(1).move_to([-4, 1, 0])
    # self.add(q1)
    # self.play(Transform(q1 - d1, q_new))
    
    self.wait()

class hadamard_0(Scene):
  def construct(self):
    line1 = Line([-4, 0, 0], [4, 0, 0])
    line2 = Line([-4, -2, 0], [4, -2, 0])

    h_gate = Hgate().move_to([0,1,0])
    self.play(Write(h_gate))
    self.add_foreground_mobjects(h_gate)
    self.wait()

    q1 = QubitReal(0, [-4, 0, 0])
    q2 = QubitReal(1, [-4, -2, 0])

    self.play(Write(line1), Write(line2), h_gate.animate.move_to([-2,0,0]))
    self.play(Write(q1), Write(q2))
    self.wait(1)

    self.play(q2.animate.shift(RIGHT * 2), q1.animate.shift(RIGHT * 2))
    # q1_new = QubitReal(0.5).move_to(q1_loc + RIGHT * 2) + d1
    reflection_line = Line([-2.35, 0.4, 0], [-1.65, 1.1, 0], color=YELLOW)
    self.play(FadeIn(reflection_line))
    self.play(q1.hadamard_gate())
    self.play(FadeOut(reflection_line))

    self.play(q1.animate.shift(RIGHT * 6), q2.animate.shift(RIGHT * 6))

    self.wait(2)
    self.wait()

class hadamard_1(Scene):
  def construct(self):
    line1 = Line([-4, 0, 0], [4, 0, 0])
    line2 = Line([-4, -2, 0], [4, -2, 0])

    h_gate = Hgate().move_to([0,1,0])
    self.play(Write(h_gate))
    self.add_foreground_mobjects(h_gate)
    self.wait()

    q1_loc = [-4, 0, 0]
    q2_loc = [-4, -2, 0]
    q1 = QubitReal(0, q1_loc)
    q2 = QubitReal(1, q2_loc)

    self.play(Write(line1), Write(line2), h_gate.animate.move_to([-2,-2,0]))
    self.play(Write(q1), Write(q2))
    self.wait(1)

    self.play(q2.animate.shift(RIGHT * 2), q1.animate.shift(RIGHT * 2))
    # q1_new = QubitReal(0.5).move_to(q1_loc + RIGHT * 2) + d1
    reflection_line = Line([-2.35, -1.6, 0], [-1.65, -0.9, 0], color=YELLOW)
    self.play(FadeIn(reflection_line))
    self.play(q2.hadamard_gate())
    self.play(FadeOut(reflection_line))

    self.play(q1.animate.shift(RIGHT * 6), q2.animate.shift(RIGHT * 6))

    self.wait(2)
    self.wait()


class measure_scene(Scene):
  def construct(self):
    line1 = Line([-4, 0, 0], [3, 0, 0])
    line2 = Line([-4, -2, 0], [3, -2, 0])

    h_gate = Hgate().move_to([-2,0,0])
    q1_loc = [-4, 0, 0]
    q2_loc = [-4, -2, 0]
    q1 = QubitReal(0, q1_loc)
    q2 = QubitReal(1, q2_loc)
    self.add_foreground_mobjects(h_gate)
    self.play(Write(line1), Write(line2), Write(h_gate))
    q1.get_values(5)
    q2.get_values(5)
    self.play(Write(q1), Write(q2))
    self.wait(1)

    self.play(q2.animate.shift(RIGHT * 2), q1.animate.shift(RIGHT * 2))

    self.play(q1.hadamard_gate(), run_time=0.5)
    self.wait(2)
    m_gate = VGroup(Mgate().move_to([3, 0, 0]), Mgate().move_to([3, -2, 0]))
    self.play(Write(m_gate))
    self.wait(1)
    self.play(q1.animate.shift(RIGHT * 5), q2.animate.shift(RIGHT * 5))
    self.play(q1.measure())

    self.play(q2.measure())
    self.wait()

class cnot_scene(Scene):
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
    self.play(FadeIn(q1, q2))
    self.play(q1.animate.shift(RIGHT * 4), q2.animate.shift(RIGHT * 4))
    print(f"values are {q1.get_values(3)}")

    self.play(q1.update_qubit(1))
    print(f"values are {q1.get_values(3)}")
    print()
    self.play(q1.animate.shift(RIGHT * 3), q2.animate.shift(RIGHT * 3))

    self.wait()

class bell_state(Scene):
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
    q2 = QubitReal(1, [-4, -2, 0])
    # print(f"values {q2.get_values(3)}")
    # print()
    self.play(FadeIn(q1, q2))
    self.play(q1.animate.shift(RIGHT * 2), q2.animate.shift(RIGHT * 2))
    self.play(q1.hadamard_gate())
    self.play(q1.animate.shift(RIGHT * 2), q2.animate.shift(RIGHT * 2))
    self.play(q2.update_qubit(-1/2))
    # print(f"Values now {q2.get_values(3)}")
    # print()
    self.play(q1.animate.shift(RIGHT * 3), q2.animate.shift(RIGHT * 3))
    self.play(q1.measure(), q2.measure())
    self.wait(1)
    chart = BarChart((1/2, 1/2), bar_names = ["00", "11"]).scale(0.7).move_to([4, -1, 0])
    self.play(VGroup(q1, q2, line1, line2, h_gate, c_not, m_gate).animate.shift(LEFT * 2))
    self.play(Transform((q1 + q2), chart))

class image_test(Scene):
  def construct(self):
    image = ImageMobject("test_image").scale(0.5)
    self.play(FadeIn(image))
    self.wait()
