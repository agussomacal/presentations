from config import *
from lib.utils import MySlide


class TitleSlide(MySlide):
    def construct(self, *args, **kwargs):
        slide_number = Integer(number=self.counter, font_size=SMALL_FS, color=SLIDE_NUM_COLOR).to_corner(DR)
        main_title = Title(
            r"Model reduction for\\forward simulation and inverse problems:\\towards non-linear approaches",
            font_size=STITLE_FS)
        self.add_to_canvas(slide_number=slide_number, main_title=main_title)

        authors = Tex(r"Agust\'in Somacal", font_size=BIG_FS)
        authors.shift(1.5 * DOWN)
        supervisors = Tex(r"Supervisors: Albert Cohen and Olga Mula", font_size=SMALL_FS)
        supervisors.shift(2.5 * DOWN)

        self.play(
            FadeIn(authors),
            FadeIn(supervisors),
            FadeIn(main_title)
        )

        return dict()
