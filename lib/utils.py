from pathlib import Path
from typing import List, Union

import numpy as np
from manim import FadeOut, Integer, ReplacementTransform, Title, RIGHT, UP, index_labels, Group, VGroup, \
    Dot, Line, Rectangle, ManimColor, WHITE, MathTex, DecimalNumber, DOWN, TexTemplate
from manim_slides.slide import Slide
from matplotlib import pyplot as plt


# ---------------------- Latex template ---------------------- #
def add_latex_file2preample(latex_timeplate: TexTemplate, source_dir: Union[Path, str]):
    with open(f"{source_dir}/config_latex.tex", "r") as f:
        for line in f:
            if line[0] != "%":
                latex_timeplate.add_to_preamble(line)
    return latex_timeplate


# ---------------------- Colors ---------------------- #
def get_info2color_from_dict(tex_to_color_dict):
    return {
        "substrings_to_isolate": list(tex_to_color_dict.keys()),
        "tex_to_color_map": tex_to_color_dict
    }


def cmap_value2manimcolor(value, cmap="coolwarm"):
    if isinstance(cmap, str):
        return ManimColor(getattr(plt.cm, cmap)(value))
    elif isinstance(cmap, ManimColor):
        return cmap
    else:
        raise Exception("cmap must be str or ManimColor")


# ---------------------- My Slides class ---------------------- #
class MySlide(Slide):
    def __init__(self, title_font_size=50, num_slide_font_size=25, num_slide_color=WHITE):
        super().__init__()
        self.num_slide_font_size = num_slide_font_size
        self.num_slide_color = num_slide_color
        self.title_font_size = title_font_size

    def setup(self):
        self.counter = 0

    def remove_old_elements(self):
        self.remove(
            *[mobj for mobj in self.mobjects if
              mobj not in [self.canvas.get("slide_number"), self.canvas.get("main_title")]])

    def fade_out_old_elements(self, exept=[]):
        return FadeOut(*[mobj for mobj in self.mobjects if
                         mobj not in [self.canvas.get("slide_number"), self.canvas.get("main_title")] +
                         (exept if isinstance(exept, list) else [exept])])

    def update_slide_number(self, counter_update=1):
        self.counter += counter_update
        old_slide_number = self.canvas["slide_number"]
        new_slide_number = Integer(number=self.counter, font_size=self.num_slide_font_size,
                                   color=self.num_slide_color).move_to(
            old_slide_number)
        self.remove(old_slide_number)
        self.canvas["slide_number"] = new_slide_number
        return ReplacementTransform(old_slide_number, new_slide_number)

    def update_main_title(self, title):
        old_main_title = self.canvas["main_title"]
        if isinstance(title, str):
            new_main_title = Title(title, font_size=self.title_font_size)
        else:
            new_main_title = title
        self.remove(old_main_title)
        self.canvas["main_title"] = new_main_title
        return ReplacementTransform(old_main_title, new_main_title)

    def get_title_mobject(self):
        return self.canvas["main_title"]


# ---------------------- Moving objects ---------------------- #
def get_shift_from_xy_coordinate(mobject, position, coordinate):
    """

    :param mobject:
    :param position: x or y coordinates
    :param coordinate: "x" or "y"
    :return:
    """
    if coordinate not in ["x", "y"]: raise Exception("Coordinate must be x or y")
    return (position - getattr(mobject, f"get_{coordinate}")()) * (RIGHT if coordinate == "x" else UP)


def shift_to(mobject, position, coordinate):
    """

    :param mobject:
    :param position: x or y coordinates
    :param coordinate: "x" or "y"
    :return:
    """
    if coordinate not in ["x", "y"]: raise Exception("Coordinate must be x or y")
    mobject.shift(get_shift_from_xy_coordinate(mobject, position, coordinate))
    return mobject


def move_and_scale(mobject, target_mobject):
    return mobject.scale_to_fit_height(target_mobject.height).move_to(target_mobject)


# ---------------------- Pointing to specific subobjects ---------------------- #
def show_nested_labels(self, mobject):
    self.add(*list(map(index_labels, mobject)))


def find_substring_indexes(mobject, substring, return_indices=True):
    # i = mobject.index_of_part_by_tex(substring)
    # j = mobject[i].get_tex_string()
    # # Cconst = nopL1.get_parts_by_tex(r"C", substring=True, case_sensitive=True)
    # Cconst = nopL1[i].get_tex_string()[j]

    for i, subtext in enumerate(mobject):
        string = subtext.get_tex_string()
        for j in range(len(string) - len(substring)):
            print(string[j:j + len(substring)], substring)
            if str(string[j:j + len(substring)]) == substring:
                print(i, j)
                if return_indices:
                    yield i, j
                else:
                    yield mobject[i][j:j + len(substring)]


def count_sub_objects(mobject):
    counter = 0
    for submobj_i in mobject:
        for _ in submobj_i:
            counter += 1
    return counter


def get_sub_objects(mobject, num_chars: List[int]):
    num_objects = count_sub_objects(mobject)
    num_chars = [n if n >= 0 else num_objects + n for n in num_chars]
    subobj = []
    counter = 0
    for i, submobj_i in enumerate(mobject):
        for j, submobj_j in enumerate(submobj_i):
            if counter in num_chars:
                subobj.append(submobj_j)
            counter += 1
    return Group(*subobj)


# ---------------------- Grids ---------------------- #
def create_grid(shape, **kwargs):
    new_shape = (shape[0] + 1, shape[1] + 1)
    dots = []
    d = VGroup()
    for i in range(new_shape[0]):
        dots.append([])
        for j in range(new_shape[1]):
            dots[i].append(Dot(radius=0))
            d.add(dots[i][j])
    d.arrange_in_grid(*new_shape, buff=1)

    l = VGroup()
    # build horizontal lines
    for i in range(new_shape[0]):
        l.add(Line(dots[i][0].get_center(), dots[i][-1].get_center(), **kwargs))
    # build vertical lines
    for j in range(new_shape[1]):
        l.add(Line(dots[0][j].get_center(), dots[-1][j].get_center(), **kwargs))

    return l.set_y(0).set_x(0)


def create_column_grid(shape, rows=False, **kwargs):
    new_shape = (shape[0] + 1, shape[1] + 1)
    dots = []
    d = VGroup()
    for i in range(new_shape[0]):
        dots.append([])
        for j in range(new_shape[1]):
            dots[i].append(Dot(radius=0))
            d.add(dots[i][j])
    d.arrange_in_grid(*new_shape, buff=1)

    l = VGroup()
    # build horizontal lines
    for i in range(new_shape[0]):
        if rows or (i in [0, shape[0]]):
            l.add(Line(dots[i][0].get_center(), dots[i][-1].get_center(), **kwargs))
    # build vertical lines
    for j in range(new_shape[1]):
        if not rows or (j in [0, shape[1]]):
            l.add(Line(dots[0][j].get_center(), dots[-1][j].get_center(), **kwargs))

    if "fill_opacity" in kwargs:
        l.add(Rectangle(height=shape[0], width=shape[1], **kwargs))

    return l.set_y(0).set_x(0)


def create_grid_of_colored_rectangles(values, cmap="coolwarm", number_color=WHITE, **kwargs):
    r = VGroup()
    for value in values.reshape(-1):
        r.add(Rectangle(height=1, width=1, color=cmap_value2manimcolor(value, cmap), **kwargs))
    r.arrange_in_grid(*np.shape(values), buff=0)
    r.set_y(0).set_x(0)

    t = VGroup()
    for i, value in enumerate(values.reshape(-1)):
        if isinstance(value, MathTex):
            t.add(value)
        else:
            t.add(DecimalNumber(value, num_decimal_places=1, color=number_color).move_to(r[i]))
    return r, t


def create_column_rectangles(values, cmap="coolwarm", **kwargs):
    r = VGroup()
    for value in values:
        r.add(Rectangle(height=value, width=1,
                        color=cmap_value2manimcolor(value, cmap) if isinstance(cmap, str) else cmap, **kwargs))
    r.arrange_in_grid(rows=1, cols=len(values), buff=0, center=0, cell_alignment=DOWN)
    r.set_y(0).set_x(0)

    t = VGroup()
    for i, value in enumerate(values):
        t.add(DecimalNumber(value, num_decimal_places=1).next_to(r[i], UP))
    return r, t
