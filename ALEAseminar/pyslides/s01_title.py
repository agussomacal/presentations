"""
High order recovery of geometric interfaces from cell-average data

In image processing edge-adapted methods are used to reconstruct high-resolution images from coarser cell averages.
When images are piecewise smooth functions, interfaces can be approximated by a pre-specified functional class through
optimization LVIRA or specific pre-processing ENO-EA. First we present a framework to analyze the reconstruction
capabilities of non-linear families and use it to prove that LVIRA is a second order method. Then we show how to build
fast higher order methods to reconstruct interfaces as well as two strategies to deal with non-smooth interfaces
presenting corners.
"""
from manim import Title, DOWN

from ALEAseminar.config import *
from ALEAseminar.config import STITLE_FS, H
from lib.utils import MySlide

CENTER_Y = (Title("bla", font_size=STITLE_FS).get_y(DOWN) - H) / 2


class TitleSlide(MySlide):
    def construct(self, *args, **kwargs):
        slide_number = Integer(number=self.counter, font_size=SMALL_FS, color=SLIDE_NUM_COLOR).to_corner(DR)
        main_title = Title(
            r"Non-linear inverse problems\\applications to image reconstruction",
            font_size=STITLE_FS)
        self.add_to_canvas(slide_number=slide_number, main_title=main_title)

        conference = Tex(r"Séminaire de Mathématiques Appliquées du LMJL", font_size=BIG_FS)
        authors = Tex(r"Agust\'in Somacal", font_size=MEDIUM_FS).next_to(conference, DOWN, buff=1)
        # authors.shift(1.5 * DOWN)
        collaborators = Tex(r"Collaborators: Albert Cohen, Matthieu Dolbeault, Olga Mula", font_size=SMALL_FS)
        collaborators.next_to(authors, DOWN).set_y(1 - H)

        self.play(
            FadeIn(authors),
            FadeIn(conference),
            FadeIn(collaborators),
            FadeIn(main_title)
        )

        return dict()
