# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 13:32:58 2018

@author: simcha
"""

from big_ol_pile_of_manim_imports import *
 
class Shapes(Scene):
    #A few simple shapes
    def construct(self):
        circle = Circle().move_to(np.array([3,0,0]))
        square = Square()
        line=Line(np.array([1.5,0,0]),np.array([5,0,0]))
        triangle=Polygon(np.array([0,0,0]),np.array([1,1,0]),np.array([1,-1,0]))
         
        
                
        self.play(ShowCreation(circle))
        self.add(Arrow(line))
        self.play(FadeOut(circle))
        self.play(GrowFromCenter(square))
        self.play(Transform(square,triangle))
        self.play(Transform(square, line.rotate(np.pi).move_to(np.array([-5, 0, 0]))))
        self.play(FadeOut(square))
        
class MoreShapes(Scene):
    #A few more simple shapes
    def construct(self):
        circle = Circle(color=PURPLE_A)
        square = Square(fill_color=GOLD_B, fill_opacity=1, color=GOLD_A)
        square.move_to(UP+LEFT)
        circle.surround(square)
        rectangle = Rectangle(height=2, width=3)
        ellipse=Ellipse(width=3, height=1, color=RED)
        ellipse.shift(2*DOWN+2*RIGHT)
        pointer = CurvedArrow(2*RIGHT,5*RIGHT,color=MAROON_C)
        arrow = Arrow(LEFT,UP)
        arrow.next_to(circle,DOWN+LEFT)
        rectangle.next_to(arrow,DOWN+LEFT)
        ring=Annulus(inner_radius=.5, outer_radius=1, color=BLUE)
        ring.next_to(ellipse, RIGHT)
#         
        self.add(pointer)
        self.play(FadeIn(square))
        self.play(Rotating(square),FadeIn(circle))
        self.play(GrowArrow(arrow))
        self.play(GrowFromCenter(rectangle), GrowFromCenter(ellipse), GrowFromCenter(ring))
        
        hexagon = Polygon(np.array([1, 0, 0]), np.array([0.75, -0.5, 0]), np.array([-0.75, -0.5, 0]), np.array([-1, 0, 0]), np.array([-0.75, 0.5, 0]), np.array([0.75, 0.5, 0]))
        hexagon2 = hexagon.copy()
        bigHexagon = hexagon2.scale(1.5)
        bigHexagon.surround(hexagon)
#        
        self.play(FadeIn(hexagon), FadeIn(bigHexagon))
        self.play(Rotating(hexagon), Rotating(bigHexagon))
        
class AddingText(Scene):
    #Adding text on the screen
    def construct(self):
        my_first_text=TextMobject("Writing with manim is fun")
        second_line=TextMobject("and easy to do!")
        second_line.next_to(my_first_text,DOWN)
        third_line=TextMobject("for me and you!")
        third_line.next_to(my_first_text,DOWN)
         
        self.add(my_first_text, second_line)
        self.wait(2)
        self.play(Transform(second_line,third_line))
        self.wait(2)
        second_line.shift(3*DOWN)
        self.play(ApplyMethod(my_first_text.shift,3*UP))       