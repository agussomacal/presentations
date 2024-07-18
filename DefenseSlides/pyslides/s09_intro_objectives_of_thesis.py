from DefenseSlides.config import *
from lib.utils import MySlide

COLOR_LINEAR = ORANGE
COLOR_CH23 = YELLOW
COLOR_CH4 = BLUE
COLOR_CH5 = PURPLE
COLOR_CH6 = GREEN

cite_ch1 = Tex(
    # r"[A. Cohen, W. Dahmen, M. Dolbeault, A. Somacal, ESAIM: Mathematical Modelling and Numerical Analysis, 2023]",
    r"[A. Cohen, W. Dahmen, M. Dolbeault, A. Somacal, 2023]", font_size=CITATION_FONT_SIZE)
cite_ch2 = Tex("[A. Cohen, M. Dolbeault, O. Mula, A. Somacal, 2023]", font_size=CITATION_FONT_SIZE)
cite_ch3 = Tex("[A. Cohen, O. Mula, A. Somacal, ArXiv, 2024]", font_size=CITATION_FONT_SIZE)
cite_ch4 = Tex("[A. Cohen, C. Farhat, Y. Maday, A. Somacal, 2023]", font_size=CITATION_FONT_SIZE)
cite_ch5 = Tex("[A. Beguinet, V. Ehrlacher, R. Flenghi, M. Fuente, O. Mula, A. Somacal, 2023]",
               font_size=CITATION_FONT_SIZE)
cite_ch6 = Tex("[M. Dolbeault, O. Mula, A. Somacal, 2024]", font_size=CITATION_FONT_SIZE)


def get_objectives_of_the_thesis_elements():
    title = Title(r"Contributions of the thesis", font_size=STITLE_FS)

    # -------------- -------------- -------------- #
    #   Objective: chapter 1
    linear_approaches = (Tex("Linear approaches", color=COLOR_LINEAR, font_size=MEDIUM_FS)
    .next_to(title, DOWN, buff=BUFF_HALF).shift(
        ThreeColumns_dx * LEFT))
    nl_approaches = (Tex("Non-linear approaches", color=NON_LINEAR_COLOR, font_size=MEDIUM_FS)
    .next_to(title, DOWN, buff=BUFF_HALF).shift(
        ThreeColumns_dx / 2 * RIGHT))

    # In Chapter 2 we extend the approximation guarantees offered by linear spaces in the context of the linear
    # elliptic Equation (1.1) when the parameter space Y is allowed to be unbounded, or equivalently, when extreme
    # levels of contrast in the diffusivity constants are possible.
    ch1 = Tex(r"Extend approximation guarantees\\"
              r'Diffusion equation with \\ unbounded parameter space Y',
              # tex_environment="flushleft",
              # tex_template=TexTemplate(documentclass=r"\documentclass[preview, varwidth=285px]{standalone}"),
              tex_to_color_map={"parameter space Y": COLOR_PARAMS},
              font_size=EQ_FONT_SIZE).next_to(linear_approaches, DOWN, buff=BUFF_HALF)
    cite_ch1.next_to(ch1, DOWN, buff=BUFF_HALF)
    rec_ch1 = SurroundingRectangle(Group(ch1, cite_ch1), buff=.1, corner_radius=0.1,
                                   color=COLOR_LINEAR, stroke_opacity=0.5)

    ch2 = (Tex(r"Theoretical framework \\ to analyse \\ non-linear strategies", font_size=EQ_FONT_SIZE)
           .next_to(nl_approaches, DOWN, buff=BUFF_HALF).shift(ThreeColumns_dx / 2 * LEFT))
    cite_ch2.next_to(ch2, DOWN, buff=BUFF_HALF)
    ch3 = (
        Tex(r"Implementation of non-linear strategies \\ to reconstruct step-functions \\ out of cell average data",
            font_size=EQ_FONT_SIZE).next_to(ch2, DOWN, buff=BUFF_ONE))
    cite_ch3.next_to(ch3, DOWN, buff=BUFF_HALF)
    rec_ch23 = SurroundingRectangle(Group(ch2, ch3, cite_ch2, cite_ch3), buff=.1, corner_radius=0.1,
                                    color=COLOR_CH23, stroke_opacity=0.5)

    ch4 = (Tex(r"Reconstruct step-functions \\ combining \\ linear and learning techniques",
               font_size=EQ_FONT_SIZE).next_to(nl_approaches, DOWN, buff=BUFF_HALF).shift(
        ThreeColumns_dx / 2 * RIGHT))
    cite_ch4.next_to(ch4, DOWN, buff=BUFF_HALF)
    rec_ch4 = SurroundingRectangle(Group(ch4, cite_ch4), buff=.1, corner_radius=0.1,
                                   color=COLOR_CH4, stroke_opacity=0.5)

    ch6 = Tex(r"Real case study: \\ estimation of pollution in a city", font_size=EQ_FONT_SIZE)
    cite_ch6.next_to(ch6, DOWN, buff=BUFF_HALF)
    rec_ch6 = SurroundingRectangle(Group(ch6, cite_ch6), buff=.1, corner_radius=0.1,
                                   color=COLOR_CH6, stroke_opacity=0.5)
    Group(ch6, rec_ch6, cite_ch6).next_to(rec_ch23, DOWN, buff=BUFF_QUARTER)

    ch5 = Tex(r"Comparing traditional and \\ physics informed "
              r"learning strategies \\ for transport-diffusion equations", font_size=EQ_FONT_SIZE)
    cite_ch5.next_to(ch5, DOWN, buff=BUFF_HALF)
    rec_ch5 = SurroundingRectangle(Group(ch5, cite_ch5), buff=.1, corner_radius=0.1,
                                   color=COLOR_CH5, stroke_opacity=0.5)
    Group(ch5, rec_ch5, cite_ch5).next_to(rec_ch4, DOWN, BUFF_QUARTER)

    return (title, linear_approaches, nl_approaches, ch1, ch2, ch3, ch4, ch5, ch6, rec_ch1, rec_ch23, rec_ch4, rec_ch5,
            rec_ch6, cite_ch1, cite_ch2, cite_ch3, cite_ch4, cite_ch5, cite_ch6)


class ThesisObjectivesSlides(MySlide):

    def construct(self, objects_from_previous_slides):
        (title, linear_approaches, nl_approaches, ch1, ch2, ch3, ch4, ch5, ch6, rec_ch1, rec_ch23, rec_ch4, rec_ch5,
         rec_ch6, cite_ch1, cite_ch2, cite_ch3, cite_ch4, cite_ch5, cite_ch6) = get_objectives_of_the_thesis_elements()

        self.next_slide()
        self.play(
            self.fade_out_old_elements(),
            self.update_slide_number(),
            self.update_main_title(title),
        )

        self.next_slide()
        self.play(Write(linear_approaches), Write(ch1), Write(cite_ch1))
        self.play(Create(rec_ch1))

        # -------------- -------------- -------------- #
        #   Objective: chapter 2
        self.next_slide()
        self.play(Write(nl_approaches))

        self.next_slide()
        self.play(Write(ch2), Write(cite_ch2))

        # -------------- -------------- -------------- #
        #   Objective: chapter 3
        self.next_slide()
        self.play(Write(ch3), Write(cite_ch3))
        self.play(Create(rec_ch23))

        # -------------- -------------- -------------- #
        #   Objective: chapter 4
        self.next_slide()
        self.play(Write(ch4), Write(cite_ch4))
        self.play(Create(rec_ch4))

        # -------------- -------------- -------------- #
        #   Objective: chapter 5
        self.next_slide()
        self.play(Write(ch5), Write(cite_ch5))
        self.play(Create(rec_ch5))

        # -------------- -------------- -------------- #
        #   Objective: chapter 6
        self.next_slide()
        self.play(Write(ch6), Write(cite_ch6))
        self.play(Create(rec_ch6))

        self.next_slide()
        self.play(
            Indicate(ch1),
            ch2.animate.set_color(COLOR_SHADOW),
            ch3.animate.set_color(COLOR_SHADOW),
            ch4.animate.set_color(COLOR_SHADOW),
            ch5.animate.set_color(COLOR_SHADOW),
            ch6.animate.set_color(COLOR_SHADOW),
        )

        return dict()
