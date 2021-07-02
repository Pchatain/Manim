from typing import Text
from manim import *

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


# Exmaple of usign VGRoups. problem is that the center is in the wrong spot
  #  bit_group1 = VGroup()
  #   bit_group1.add(*Dot([-4, 0, 0]))
  #   bit_group2 = VGroup().add(*Dot([-4, -1, 0]))
  #   dot = Dot([-4, 0, 0])
  #   dot2 = Dot([-4, -1, 0])
  #   bit_group1.add(*Text("0").next_to(dot, UP).scale(0.7))
  #   bit_group2.add(*Text("1").next_to(dot2, UP).scale(0.7))
  #   self.play(Write(bit_group1))
  #   self.play(Write(bit_group2))
  #   self.wait(1)
  #   d1_text = Text("0").next_to(dot, UP).scale(0.7)
  #   d2_text = Text("1").next_to(dot2, UP).scale(0.7)

  #   time = 0.0
  #   line1 = Line([-4, 0, 0], [4, 0, 0])
  #   line2 = Line([-4, -1, 0], [4, -1, 0])
  #   on_screen_time = Variable(time, Text("t"), num_decimal_places=2).shift(UP)
  #   self.play(Write(line1), Write(line2))
  #   self.wait(1)
  #   self.play(Write(on_screen_time))

class classical_circuit(Scene):
  def construct(self):

    bit_group1 = VGroup()
    bit_group1.add(*Dot([-4, 0, 0]))
    bit_group2 = VGroup().add(*Dot([-4, -1, 0]))
    dot = Dot([-4, 0, 0])
    dot2 = Dot([-4, -1, 0])
    bit_group1.add(*Text("0").next_to(dot, UP).scale(0.7))
    bit_group2.add(*Text("1").next_to(dot2, UP).scale(0.7))
    self.play(Write(bit_group1))
    self.play(Write(bit_group2))
    self.wait(1)
    d1_text = Text("0").next_to(dot, UP).scale(0.7)
    d2_text = Text("1").next_to(dot2, UP).scale(0.7)

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

    self.play(MoveAlongPath(bit_group1, line1), MoveAlongPath(bit_group2, line2), Transform(d1_text, d1_text_moved), Transform(d2_text, d2_text_moved), time_tracker.animate.set_value(t2), run_time=2, rate_func=linear)
    self.wait()

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