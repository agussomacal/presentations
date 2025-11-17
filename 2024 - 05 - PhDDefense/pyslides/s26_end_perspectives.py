from PhDDefense.config import *
from pyslides.s09_intro_objectives_of_thesis import get_objectives_of_the_thesis_elements
from lib.utils import MySlide, get_sub_objects


class PerspectivesSlides(MySlide):
    def construct(self, objects_from_previous_slides):
        (title, linear_approaches, nl_approaches, ch1, ch2, ch3, ch4, ch5, ch6, rec_ch1, rec_ch23, rec_ch4, rec_ch5,
         rec_ch6, cite_ch1, cite_ch2, cite_ch3, cite_ch4, cite_ch5, cite_ch6) = get_objectives_of_the_thesis_elements()
        title = Title(r"Perspectives", font_size=STITLE_FS)

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
            Indicate(ch5),
        )

        self.next_slide()
        self.play(
            Indicate(ch6),
        )

        ch1_blist = Tex("Avoid geometrical assumption").move_to(ch1)
        self.next_slide()
        self.play(
            Indicate(ch1),
        )
        self.play(
            ReplacementTransform(ch1, ch1_blist)
        )

        ch2_blist = Tex(r"Reconstruction from cell averages \\ for piece-wise regular functions").move_to(ch2)
        ch3_blist = Tex(
            r"Accelerate the choice between \\ alternative reconstruction strategies \\ by surrogates").move_to(ch3)
        self.next_slide()
        self.play(
            Indicate(ch2),
            Indicate(ch3),
        )
        self.play(
            ReplacementTransform(ch2, ch2_blist),
            ReplacementTransform(ch3, ch3_blist),
        )

        ch4_blist = Tex(r"Apply to \\ parametric PDE").move_to(ch4)
        self.next_slide()
        self.play(
            Indicate(ch4),
        )
        self.play(
            ReplacementTransform(ch4, ch4_blist),
        )

        ch5_blist = Tex(r"Curriculum learning").move_to(ch5)
        self.next_slide()
        self.play(
            Indicate(ch5),
        )
        self.play(
            ReplacementTransform(ch5, ch5_blist),
        )

        ch6_blist = Tex(r"Other cities \\ Measurement campaign").move_to(ch6)
        self.next_slide()
        self.play(
            Indicate(ch6),
        )
        self.play(
            ReplacementTransform(ch6, ch6_blist),
        )
        # git1 = (Text("https://github.com/agussomacal/ROMHighContrastCity", font_size=CITATION_FONT_SIZE)
        #         .next_to(ch1_blist, DOWN))
        # git2 = (Text("https://github.com/agussomacal/SubCellResolution", font_size=CITATION_FONT_SIZE)
        #         .next_to(ch2_blist, DOWN))
        # git3 = (Text("https://github.com/agussomacal/NonLinearRBA4PDEs", font_size=CITATION_FONT_SIZE)
        #         .next_to(ch4, DOWN))
        # git4 = Text("https://github.com/agussomacal/ConDiPINN", font_size=CITATION_FONT_SIZE).next_to(ch5, DOWN)
        # git5 = (Text("https://github.com/agussomacal/PollutionModeling", font_size=CITATION_FONT_SIZE)
        #         .next_to(ch6, DOWN))
        # git6 = (Text("https://github.com/agussomacal/PerplexityLab", font_size=CITATION_FONT_SIZE)
        #         .next_to(Group(git4, git5), DOWN, buff=BUFF_ONE))
        open_source = Tex(r"Codes are open sourced in GitHub")
        perplexity = Tex("Perplexity Lab: reproducible research").next_to(open_source, DOWN, buff=BUFF_HALF)
        get_sub_objects(perplexity, list(range(0, len("Perplexity")))).set_color(BLUE)
        get_sub_objects(perplexity, list(range(len("Perplexity"), len("PerplexityLab")))).set_color(GREEN)
        Group(open_source, perplexity).next_to(rec_ch6, LEFT).set_x(linear_approaches.get_x())
        self.next_slide()
        self.play(
            Write(open_source)
            # Write(git1),
            # Write(git2),
            # Write(git3),
            # Write(git4),
            # Write(git5),
        )

        self.next_slide()
        self.play(
            Write(perplexity)
        )

        self.next_slide()
        self.play(
            self.fade_out_old_elements(),
            FadeOut(title),
            Write(Tex("Thanks", font_size=STITLE_FS)),
        )
