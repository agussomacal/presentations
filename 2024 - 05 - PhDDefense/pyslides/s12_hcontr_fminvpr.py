from PhDDefense.config import *
from PhDDefense.pyslides.s10_hcontr_uea import INFTY_COLOR
from lib.utils import MySlide, get_sub_objects


class FmInvPSlides(MySlide):

    def construct(self, objects_from_previous_slides):
        title = Title(r"Forward and inverse problems", font_size=STITLE_FS)
        xax = objects_from_previous_slides["xax"]
        yax = objects_from_previous_slides["yax"]
        Ybox = objects_from_previous_slides["Ybox"]
        dot_us = objects_from_previous_slides["dot_us"]
        dy_v2 = objects_from_previous_slides["dy_v2"]
        dy_h2 = objects_from_previous_slides["dy_h2"]
        dy_h1 = objects_from_previous_slides["dy_h1"]
        dy_v1 = objects_from_previous_slides["dy_v1"]

        yspace_group = Group(xax, yax, Ybox, *dot_us, dy_v2, dy_h2, dy_h1, dy_v1)

        title_fm = (Tex(r"Forward modelling", font_size=EQ_FONT_SIZE, color=FM_COLOR)
                    .next_to(title, DOWN, buff=BUFF_HALF).shift(TwoColumns_dx * LEFT))
        title_ip = (Tex(r"Inverse problem", font_size=EQ_FONT_SIZE, color=INV_COLOR)
                    .next_to(title, DOWN, buff=BUFF_HALF).shift(TwoColumns_dx * RIGHT))

        # ------ forward modelling ------ #
        fm_rate = (MathTex(r"\|u(y) - P^y_{V_n}u(y) \| \leq C \exp(-cn^{\frac{1}{2d-2}})",
                           tex_to_color_map={r"u": COLOR_SOLUTION, r"y": COLOR_PARAMS})
                   .next_to(title_fm, DOWN, buff=BUFF_HALF))
        fm_norm = (MathTex(r"\|u \|^2_y = \sum^d_{j=1} \yj \int_{\Omega_j} |\nabla u|^2",
                           # tex_to_color_map={r"u": SOLUTION_COLOR, r"\yj": PARAMS_COLOR}
                           ).next_to(fm_rate, DOWN, buff=BUFF_HALF))
        get_sub_objects(fm_norm, [1, -3]).set_color(COLOR_SOLUTION)
        get_sub_objects(fm_norm, [-9, -10]).set_color(COLOR_PARAMS)
        galerkin_problem = (MathTex(
            r"\int_{\Omega_j} \yj \nabla v_i \nabla v_j \xrightarrow[\yj \to \infty]{} \infty",
            tex_to_color_map={r"v_j": COLOR_APPROXIMATION, r"v_i": COLOR_APPROXIMATION}
        ).move_to(fm_norm))
        get_sub_objects(galerkin_problem, [3, 4, -5, -4]).set_color(COLOR_PARAMS)
        get_sub_objects(galerkin_problem, [-1, -2]).set_color(INFTY_COLOR)

        # ------ Inverse problmes ------ #
        txt_se = Tex(r"State estimation", color=COLOR_SOLUTION).next_to(title_ip, DOWN, buff=BUFF_HALF)
        iv_rate = (MathTex(r"\|\uu - \tilde{u} \| \leq C \exp(-cn^{\frac{1}{2d-2}}) \|\uu \|_{H^1_0}",
                           # tex_to_color_map={r"\tilde{u}": APPROXIMATION_COLOR, r"\uu": SOLUTION_COLOR}
                           ).next_to(txt_se, DOWN, buff=BUFF_HALF))
        get_sub_objects(iv_rate, [1, -5]).set_color(COLOR_SOLUTION)
        get_sub_objects(iv_rate, [3, 4]).set_color(COLOR_APPROXIMATION)

        txt_pe = Tex(r"Parameter estimation", color=COLOR_PARAMS).next_to(iv_rate, DOWN, buff=BUFF_HALF)
        # tex_to_color_map = {r"\tilde{u}": APPROXIMATION_COLOR, r"\uu": SOLUTION_COLOR, r"\yj": PARAMS_COLOR,
        #                     r"\yji": PARAMS_COLOR}
        eq_1 = (MathTex(r"f=-\text{div} (y \tilde{u})_{|\Omega_j}",
                        # tex_to_color_map={r"\tilde{u}": APPROXIMATION_COLOR, r"y": PARAMS_COLOR}
                        ).next_to(txt_pe, DOWN, buff=BUFF_HALF))
        equations = [
            MathTex(r"f=-\text{div} (\yj \tilde{u})",
                    # tex_to_color_map={r"\tilde{u}": APPROXIMATION_COLOR, r"\yj": PARAMS_COLOR}
                    ).move_to(eq_1),
            MathTex(r"\frac{f}{\yj}=-\text{div} (\tilde{u})",
                    # tex_to_color_map={r"\tilde{u}": APPROXIMATION_COLOR, r"\yj": PARAMS_COLOR}
                    ).move_to(eq_1),
            MathTex(r"\frac{f}{\yj}=-\text{div} \left( \sum_{i=1}^n c_i u_i \right)",
                    # tex_to_color_map={r"\left( \sum_{i=1}^n c_i u_i \right)": APPROXIMATION_COLOR,
                    #                   r"\yj": PARAMS_COLOR}
                    ).move_to(eq_1),
            MathTex(r"\frac{f}{\yj}= \sum_{i=1}^n c_i \frac{f}{\yji}",
                    # tex_to_color_map={r"\sum_{i=1}^n c_i \frac{f}{\yji}": APPROXIMATION_COLOR,
                    #                   r"\yj": PARAMS_COLOR}
                    ).move_to(eq_1),
            MathTex(r"\frac{1}{\yj}=\sum_{i=1}^n c_i \frac{1}{\yji}", ).move_to(eq_1),
            MathTex(r"\yj^*=\left(\sum_{i=1}^n \frac{c_i}{\yji}\right)^{-1}", ).move_to(eq_1),
        ]

        ivpe_rate = (MathTex(
            r"\Big\|\frac{1}{y^*} - \frac{1}{y} \Big\|_\infty \leq C \exp(-cn^{\frac{1}{2d-2}}) \Big\|\frac{1}{y} \Big\|_\infty", )
                     .next_to(eq_1, DOWN, buff=BUFF_HALF))
        get_sub_objects(ivpe_rate, [10, -5]).set_color(COLOR_PARAMS)
        get_sub_objects(ivpe_rate, [5, 6]).set_color(COLOR_APPROXIMATION)

        # ------ Three titles ------ #
        self.next_slide()
        self.play(
            self.fade_out_old_elements(),
            self.update_slide_number(),
            self.update_main_title(title),
            Write(title),
            Write(title_fm),
            Write(title_ip),
        )

        # ------ Three results ------ #
        yspace_group.next_to(fm_norm, DOWN, buff=BUFF_HALF)
        self.next_slide()
        self.play(
            Write(fm_rate),
            Write(txt_se),
            Write(txt_pe),
            Write(iv_rate),
            Write(ivpe_rate),
            Write(equations[-1])
        )

        self.next_slide()
        self.play(
            Write(fm_norm),
        )

        self.next_slide()
        self.play(
            ReplacementTransform(fm_norm, galerkin_problem)
        )

        self.next_slide()
        self.play(
            Create(xax),
            Create(yax),
            Create(Ybox),
            Create(dy_h1),
            Create(dy_h2),
            Create(dy_v2),
            Create(dy_v1),
        )

        self.next_slide()
        self.play(
            *[Create(d) for d in dot_us]
        )
