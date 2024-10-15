from PhDDefense.config import *
from pyslides.s09_intro_objectives_of_thesis import get_objectives_of_the_thesis_elements
from lib.utils import MySlide


class ThesisObjective2sSlides(MySlide):

    def construct(self, objects_from_previous_slides):
        (title, linear_approaches, nl_approaches, ch1, ch2, ch3, ch4, ch5, ch6, rec_ch1, rec_ch23, rec_ch4, rec_ch5,
         rec_ch6, cite_ch1, cite_ch2, cite_ch3, cite_ch4, cite_ch5, cite_ch6) = get_objectives_of_the_thesis_elements()

        self.next_slide()
        self.play(
            self.fade_out_old_elements(),
            self.update_slide_number(),
            self.update_main_title(title),
        )

        self.play(
            Write(linear_approaches),
            Write(nl_approaches),
            Create(rec_ch1),
            Create(rec_ch23),
            Create(rec_ch4),
            Create(rec_ch5),
            Create(rec_ch6),
            Write(ch1),
            Write(ch2),
            Write(ch3),
            Write(ch4),
            Write(ch5),
            Write(ch6),
            Write(cite_ch1),
            Write(cite_ch2),
            Write(cite_ch3),
            Write(cite_ch4),
            Write(cite_ch5),
            Write(cite_ch6),
        )

        self.next_slide()
        self.play(
            ch1.animate.set_color(COLOR_SHADOW),
            Indicate(ch2),
            ch3.animate.set_color(COLOR_SHADOW),
            ch4.animate.set_color(COLOR_SHADOW),
            ch5.animate.set_color(COLOR_SHADOW),
            ch6.animate.set_color(COLOR_SHADOW),
        )

        return dict()
