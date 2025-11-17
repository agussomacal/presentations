from ALEASeminar.config import *
from lib.utils import MySlide


class EndSlides(MySlide):
    def construct(self, objects_from_previous_slides):
        self.next_slide()
        self.play(
            self.fade_out_old_elements(),
            self.update_slide_number(),
            FadeOut(self.get_title_mobject())
        )

        open_source = Tex(
            r"All code available open source at: \underline{https://github.com/agussomacal/SubCellResolution}").set_y(
            H / 2)
        presentation = Tex(
            r"Code for presentation at: \\ \underline{https://github.com/agussomacal/presentations}")
        banner = ManimBanner().scale_to_fit_height(0.5)

        references = Tex("References")
        cite_template = TexTemplate(
            documentclass=fr"\documentclass[preview, varwidth={W / 2 * 1.5 * pixels_per_width_point}px]" + "{standalone}"
        )
        cite_ch1 = Tex(
            "[A. Cohen, M. Dolbeault, O. Mula, A. Somacal, Nonlinear approximation spaces for inverse problems, Analysis and Applications, 2023]",
            font_size=CITATION_FONT_SIZE, tex_template=cite_template)
        cite_ch2 = Tex(
            "[A. Cohen, O. Mula, A. Somacal, High order recovery of geometric interfaces from cell-average data, 2024]",
            font_size=CITATION_FONT_SIZE, tex_template=cite_template)
        cite_pbdw = Tex(
            "PBDW [Y. Maday, A. T. Patera, J. D. Penn, M. Yano, A parameterized‐background data‐weak approach to variational data assimilation: formulation, analysis, and application to acoustics, International Journal for Numerical Methods in Engineering, 2015]",
            font_size=CITATION_FONT_SIZE, tex_template=cite_template)
        cite_depres = Tex(
            "ML corners [B. Després, H. Jourdren, Machine Learning design of Volume of Fluid schemes for compressible flows, Journal of Computational Physics, 2020]",
            font_size=CITATION_FONT_SIZE, tex_template=cite_template)
        cite_lvira = Tex(
            r"LVIRA [E.G. Puckett, A volume-of-fluid interface tracking algorithm with applications to computing shock wave refraction, 1991]",
            font_size=CITATION_FONT_SIZE, tex_template=cite_template)
        cite_elvira = Tex(
            "ELVIRA [J. E. Pillod, E.G. Puckett, Second-order accurate volume-of-fluid algorithms for tracking material interfaces, Journal of Computational Physics, 2004]",
            font_size=CITATION_FONT_SIZE, tex_template=cite_template)

        references.next_to(open_source, DOWN, buff=BUFF_ONE)
        open_source.next_to(references, 1.5 * UP, buff=BUFF_ONE)
        references.set_x(open_source.get_x(LEFT), LEFT)
        presentation.next_to(open_source, DOWN, buff=BUFF_QUARTER).set_x(open_source.get_x(LEFT), LEFT)
        banner.next_to(presentation, RIGHT, buff=3 / 2 * BUFF_HALF)
        cite_lvira.next_to(references, DOWN, buff=BUFF_QUARTER).set_x(open_source.get_x(LEFT), LEFT)
        cite_elvira.next_to(cite_lvira, DOWN, buff=BUFF_QUARTER).set_x(open_source.get_x(LEFT), LEFT)
        cite_pbdw.next_to(cite_elvira, DOWN, buff=BUFF_QUARTER).set_x(open_source.get_x(LEFT), LEFT)
        cite_depres.next_to(cite_pbdw, DOWN, buff=BUFF_QUARTER).set_x(open_source.get_x(LEFT), LEFT)
        cite_ch1.next_to(cite_depres, DOWN, buff=BUFF_QUARTER).set_x(open_source.get_x(LEFT), LEFT)
        cite_ch2.next_to(cite_ch1, DOWN, buff=BUFF_QUARTER).set_x(open_source.get_x(LEFT), LEFT)
        Group(cite_lvira, cite_elvira, cite_pbdw, cite_depres, cite_ch1, cite_ch2).set_x(0)

        self.next_slide()
        self.play(
            Write(open_source),
        )

        self.next_slide()
        self.play(
            open_source.animate.set_color(GRAY),
            Write(presentation),
            banner.create(),
        )
        self.play(banner.expand())

        self.next_slide()
        self.play(
            # Write(Tex("Thanks", font_size=STITLE_FS)),
            presentation.animate.set_color(GRAY),
            Write(references),
            Write(cite_ch1),
            Write(cite_ch2),
            Write(cite_depres),
            Write(cite_pbdw),
            Write(cite_lvira),
            Write(cite_elvira)
        )
