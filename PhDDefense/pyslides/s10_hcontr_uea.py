from PhDDefense.config import *
from PhDDefense.config import COLOR_SHADOW
from pyslides.s04_intro_two_problems import parameters_inf_dict, num_snapshots, get_diff_eq_images, get_Yshape_object
from pyslides.s08_intro_kolmogorov_width_decay import kolmo_decay_plot
from pyslides.s09_intro_objectives_of_thesis import cite_ch1
from lib.utils import cmap_value2manimcolor, MySlide, get_sub_objects, create_grid_of_colored_rectangles

INFTY_COLOR = YELLOW
COLOR_UEA = ORANGE

expeq = MathTex(r'd_n(\mathcal{M})_V \leq Ce^{-cn^\frac{1}{d}', color=COLOR_UEA, font_size=EQ_FONT_SIZE)
expeq_us = MathTex(r'd_n(\mathcal{M})_V \leq Ce^{-cn^\frac{1}{2d-2}}', color=INFTY_COLOR, font_size=EQ_FONT_SIZE)


def y_space_box(r, R):
    xax = Arrow(ORIGIN, (r + R) * RIGHT, buff=0, stroke_width=1.5, tip_length=0.1)
    yax = Arrow(ORIGIN, (r + R) * UP, buff=0, stroke_width=1.5, tip_length=0.1)
    Ybox = Rectangle(height=R, width=R, fill_color=COLOR_PARAMS, fill_opacity=0.5,
                     stroke_width=2.5, stroke_color=COLOR_PARAMS, stroke_opacity=1).move_to(ORIGIN,
                                                                                            aligned_edge=DL).shift(
        r * RIGHT, r * UP)
    return R, Ybox, xax, yax


def disjoint_inclusions_domain():
    fig1 = Rectangle(height=1.6, width=1.6, color=cmap_value2manimcolor(0.5, cmap="Blues"), fill_opacity=0.5,
                     stroke_width=0)
    fig2 = Circle(radius=0.25, color=cmap_value2manimcolor(0.7, cmap="Blues"), fill_opacity=0.5, stroke_width=0)
    fig3 = Circle(radius=0.2, color=cmap_value2manimcolor(0.8, cmap="Blues"), fill_opacity=0.5,
                  stroke_width=0).next_to(fig2, RIGHT, buff=0)
    fig4 = Rectangle(height=0.2, width=0.43, color=cmap_value2manimcolor(0.9, cmap="Blues"),
                     fill_opacity=0.5, stroke_width=0).rotate(30).next_to(fig3, DOWN, buff=0)
    fig5 = Ellipse(width=0.4, height=0.2, fill_opacity=0.5, stroke_width=0,
                   color=cmap_value2manimcolor(0.35, cmap="Blues")).rotate(-30).next_to(fig4, LEFT, buff=0)
    Group(fig2, fig3, fig4, fig5).move_to(fig1)
    omega = MathTex(r"\Omega", font_size=EQ_FONT_SIZE).move_to(fig1, aligned_edge=DL).shift(0.2 * UR)
    return fig1, fig2, fig3, fig4, fig5, omega


class UEASlides(MySlide):

    def construct(self, objects_from_previous_slides):
        title = Title(r"High contrast diffusivity", font_size=STITLE_FS)

        # -------------- -------------- -------------- #
        #   UEA
        tex_to_color_map = {r"\uu": COLOR_SOLUTION, "\diffcoef": COLOR_PARAMS,
                            "y_j": COLOR_PARAMS}
        text_diffusion = (Text("Diffusion PDE", font_size=EQ_FONT_SIZE, t2c={"PDE": PDE_COLOR})
                          .next_to(title, DOWN, buff=BUFF_HALF).shift(3 * LEFT))
        diffusion = (MathTex(r"-\text{div} (\diffcoef \nabla \uu)=f",
                             font_size=EQ_FONT_SIZE,
                             tex_to_color_map={"\diffcoef": COLOR_PARAMS, r"\uu": COLOR_SOLUTION})
                     .next_to(text_diffusion, DOWN, buff=BUFF_HALF))

        piecewiseconstat = MathTex(r"\diffcoef =\overline{a}(x) + \sum_{j=1}^d y_j \chi_{\Omega_j}(x)",
                                   font_size=EQ_FONT_SIZE,
                                   tex_to_color_map={"\diffcoef": COLOR_PARAMS, "y_j": COLOR_PARAMS}).next_to(
            diffusion, DOWN, buff=BUFF_HALF)
        get_sub_objects(piecewiseconstat, [5]).set_color(COLOR_PARAMS)
        kappa = piecewiseconstat[0][:6]
        variational_formulation = MathTex(r"\int_\Omega a(x,y) \nabla \uu \nabla \vv dx = \int_\Omega f\vv dx",
                                          font_size=EQ_FONT_SIZE, tex_to_color_map=tex_to_color_map).move_to(diffusion)
        get_sub_objects(variational_formulation, [2, 6]).set_color(COLOR_PARAMS)
        variational_pwc = MathTex(
            r"\int_\Omega \sum_{j=1}^d y_j \chi_{\Omega_j}(x) \nabla \uu \nabla \vv dx = \int_\Omega f\vv dx",
            font_size=EQ_FONT_SIZE, tex_to_color_map=tex_to_color_map).move_to(diffusion)
        variational_pwc_factored = MathTex(
            r"\sum_{j=1}^d y_j \int_{\Omega_j} \nabla \uu \nabla \vv dx = \int_\Omega f\vv dx",
            font_size=EQ_FONT_SIZE, tex_to_color_map=tex_to_color_map).move_to(diffusion)

        ueatex = (Tex(r"Uniform Ellipticity Assumption (UEA)", font_size=EQ_FONT_SIZE, color=COLOR_UEA)
                  .next_to(variational_pwc_factored, DOWN, buff=BUFF_HALF))
        ueaeq = (MathTex(r"0<r \leq a(x,y) \leq R < \infty", font_size=EQ_FONT_SIZE)
                 .next_to(ueatex, DOWN, buff=BUFF_HALF))
        get_sub_objects(ueaeq, [4, 8]).set_color(COLOR_PARAMS)
        ueaeq_y = MathTex(r"0<r \leq y_j \leq R < \infty", font_size=EQ_FONT_SIZE,
                          tex_to_color_map={r"y_j": COLOR_PARAMS, r"+\infty": INFTY_COLOR}).move_to(ueaeq)
        not_ueaeq = MathTex(r"0<r \leq a(x,y) \leq +\infty", font_size=EQ_FONT_SIZE,
                            tex_to_color_map={r"+\infty": INFTY_COLOR}).move_to(ueaeq)
        get_sub_objects(not_ueaeq, [5, 9]).set_color(COLOR_PARAMS)
        not_ueatex = (
            Tex(r"\sout{Uniform Ellipticity Assumption (UEA)}", font_size=EQ_FONT_SIZE, tex_template=LatexTemplate)
            .move_to(ueatex))
        not_ueaeq_y = MathTex(r"0 < y_j \leq +\infty", font_size=EQ_FONT_SIZE,
                              tex_to_color_map={r"y_j": COLOR_PARAMS, r"+\infty": INFTY_COLOR}).move_to(not_ueaeq)

        Yspace = MathTex(r"Y = ]0, \infty]^d", font_size=EQ_FONT_SIZE,
                         tex_to_color_map={r"\infty": INFTY_COLOR})
        tex_homogeneity = MathTex(r"u(ty)=\frac{u(y)}{t}").next_to(Yspace)
        get_sub_objects(tex_homogeneity, [0, 6]).set_color(COLOR_SOLUTION)
        get_sub_objects(tex_homogeneity, [3, 8]).set_color(COLOR_PARAMS)
        Group(Yspace, tex_homogeneity).move_to(ueaeq)
        Yspace_prima = MathTex(r"Y' = [1, \infty]^d", font_size=EQ_FONT_SIZE,
                               tex_to_color_map={r"\infty": INFTY_COLOR})

        n_max = 7
        expdecay_graph, expdecay_points, grid, stepfuncdecay_graph, stepfuncdecay_points, x_label, y_label = kolmo_decay_plot(
            n_max)
        expgroup = VGroup(grid, expdecay_graph, expdecay_points, stepfuncdecay_graph, stepfuncdecay_points, y_label,
                          x_label)
        expgroup.scale(0.3).next_to(ueatex, RIGHT, buff=BUFF_HALF)
        expeq_copy = expeq.copy().next_to(expdecay_points, RIGHT, aligned_edge=DOWN)
        expeq_us_copy = expeq_us.copy().next_to(expdecay_points, RIGHT, aligned_edge=DOWN)

        # citation1 = (Tex(
        #     r"[J. Bäck, F. Nobile, L. Tamellini, R. Tempone., Spectral and High Order Methods for Partial Differential Equations, 2011]",
        #     color=COLOR_UEA, font_size=CITATION_FONT_SIZE)
        #              .next_to(expgroup, DOWN, buff=BUFF_EQ))
        citation1 = (Tex(
            r"[J. Bäck, F. Nobile, L. Tamellini, R. Tempone., 2011]",
            color=COLOR_UEA, font_size=CITATION_FONT_SIZE)
                     .next_to(Group(expgroup, expeq_copy), DOWN, buff=BUFF_HALF))
        citation2 = (Tex(r"[H. Tran, C. G. Webster, G. Zhang., Numerische Mathematik, 2017]",
                         color=COLOR_UEA, font_size=CITATION_FONT_SIZE)
                     .next_to(citation1, DOWN, aligned_edge=RIGHT, buff=0.05))
        citation_us_copy = cite_ch1.copy().move_to(citation1, aligned_edge=RIGHT).set_color(INFTY_COLOR)

        disjoint_inclusions = (
            Tex(r"Disjoint inclusions geometrical assumption", font_size=EQ_FONT_SIZE, tex_template=LatexTemplate,
                color=INFTY_COLOR)
            .move_to(not_ueatex))

        fig1, fig2, fig3, fig4, fig5, omega = disjoint_inclusions_domain()
        disjoint_inclusions_example = VGroup(
            fig1, fig2, fig3, fig4, fig5, omega
        ).next_to(citation_us_copy, DOWN, buff=BUFF_HALF)
        # omegas = [MathTex(r"\Omega_{{{i}}}", FONT_SIZE=CITATION_FONT_SIZE).move_to(fig) for fig in [fig2, fig3, fig4, fig5]]

        # ------ reminder of equation ------ #
        self.next_slide()
        self.play(
            self.fade_out_old_elements(),
            self.update_slide_number(),
            self.update_main_title(title),
            FadeIn(text_diffusion),
            FadeIn(diffusion),
        )

        self.next_slide()
        ypos = diffusion[-4]
        self.play(
            Indicate(ypos),
            FadeIn(kappa, target_position=ypos, scale=0.25)
        )
        self.play(
            FadeOut(kappa),
            Write(piecewiseconstat)
        )

        self.next_slide()

        def get_diffusion_param_solutions_inf(i):
            matrix = np.array(parameters_inf_dict[i])
            max_index = np.where(matrix == np.max(matrix))
            r, t = create_grid_of_colored_rectangles(np.array(matrix), cmap=COLOR_PARAMS,
                                                     number_color=COLOR_PARAMS,
                                                     stroke_width=1, fill_opacity=0.25)
            if i == num_snapshots - 1:
                t[max_index[1][0] + np.shape(matrix)[0] * max_index[0][0]] = (
                    MathTex(r"\infty", font_size=DEFAULT_FONT_SIZE).move_to(
                        t[max_index[1][0] + np.shape(matrix)[0] * max_index[0][0]]))
            new_param_matrix = VDict({"rectangles": r, "entries": t})
            new_param_matrix.set_color(COLOR_PARAMS).scale(0.37)
            new_solution = (get_diff_eq_images(name="solutions_inf", i=i)
                            .scale(0.6).next_to(new_param_matrix, RIGHT, buff=0.2))
            Group(new_param_matrix, new_solution).next_to(ueaeq, DOWN, buff=BUFF_ONE)
            return new_param_matrix, new_solution

        u = diffusion[-2][-1]
        yj = piecewiseconstat[-2]
        param_matrix, solution = get_diffusion_param_solutions_inf(0)
        self.play(
            Indicate(yj),
            FadeIn(param_matrix, target_position=yj.get_center(), scale=0.2),
        )
        self.play(
            Indicate(u),
            FadeIn(solution, target_position=u.get_center(), scale=0.2),
        )

        # ------ Variational formulation ------ #
        self.next_slide()
        self.play(
            ReplacementTransform(diffusion, variational_formulation)
        )
        self.next_slide()
        self.play(
            Indicate(piecewiseconstat),
            FadeOut(piecewiseconstat, target_position=variational_formulation.get_center(), scale=0.2),
            ReplacementTransform(variational_formulation, variational_pwc)
        )

        self.next_slide()
        self.play(
            ReplacementTransform(variational_pwc, variational_pwc_factored)
        )

        # ------ UEA ------ #
        self.next_slide()
        Y = get_Yshape_object(fill_color=COLOR_PARAMS, fill_opacity=0.5).next_to(param_matrix, LEFT, buff=2 * BUFF_HALF)
        r = 0.2
        R = max((Y.get_height(), Y.get_width()))
        R, Ybox, xax, yax = y_space_box(r, R)
        Group(xax, yax, Ybox).move_to(Y, aligned_edge=UR)
        self.play(
            Write(ueatex),
            Write(ueaeq),
            FadeIn(Y),
            Create(xax),
            Create(yax)
        )

        self.play(
            Create(expdecay_graph),
            Create(expdecay_points),
            Create(grid),
            # Create(stepfuncdecay_graph),
            # Create(stepfuncdecay_points),
            Create(x_label),
            Create(y_label),
        )

        self.play(
            Write(expeq_copy),
            Write(citation1),
            Write(citation2)
        )

        self.next_slide()
        self.play(
            ReplacementTransform(Y, Ybox),
            ReplacementTransform(ueaeq, ueaeq_y),
        )

        # ------ Not UEA ------ #
        self.next_slide()
        param_cycle_period = 2
        for i in range(1, num_snapshots):
            new_param_matrix, new_solution = get_diffusion_param_solutions_inf(i)
            self.play(
                FadeOut(param_matrix),
                FadeIn(new_param_matrix),
                ReplacementTransform(solution, new_solution),
                run_time=param_cycle_period / num_snapshots, rate_func=linear
            )
            param_matrix = new_param_matrix
            solution = new_solution

        zero_dot = Dot(xax.get_edge_center(LEFT), radius=0.05, color=config["background_color"])
        dr = Ybox.get_edge_center(DL) - xax.get_edge_center(LEFT)
        xinf_line = DashedLine(ORIGIN, 1.5 * R * RIGHT, stroke_width=2.5, stroke_color=COLOR_PARAMS,
                               stroke_opacity=1).move_to(Ybox, aligned_edge=DL)
        yinf_line = DashedLine(ORIGIN, 1.5 * R * UP, stroke_width=2.5, stroke_color=COLOR_PARAMS,
                               stroke_opacity=1).move_to(Ybox, aligned_edge=DL)
        self.play(
            ReplacementTransform(ueaeq_y, not_ueaeq_y),
            ReplacementTransform(ueatex, not_ueatex),
            # param_matrix.get_columns()[1][1].animate.scale(1.2).set_color(INFTY_COLOR),
            Indicate(new_param_matrix["entries"][-1]),
            Indicate(new_param_matrix["rectangles"][-1]),
            # Indicate(param_matrix.get_columns()[1][1])
        )
        self.play(
            # param_matrix.get_columns()[1][1].animate.scale(1.2).set_color(INFTY_COLOR),
            new_param_matrix["entries"][-1].animate.set_color(INFTY_COLOR),
            new_param_matrix["rectangles"][-1].animate.set_color(INFTY_COLOR),
            # Indicate(param_matrix.get_columns()[1][1])
        )

        self.play(
            not_ueatex.animate.set_color(COLOR_SHADOW),
            Create(xinf_line),
            Create(yinf_line),
            Ybox.animate.set_stroke_width(0).set_height(1.5 * R).set_width(1.5 * R).shift(0.25 * R * UR)
        )
        self.play(
            Ybox.animate.shift(-dr / 2).set_height(Ybox.get_height() + dr[1]).set_width(Ybox.get_width() + dr[0]),
            xinf_line.animate.shift(-dr, dr[0] / 2 * RIGHT).set_width(xinf_line.get_width() + dr[0]),
            yinf_line.animate.shift(-dr, dr[1] / 2 * UP).set_height(yinf_line.get_height() + dr[1]),
            FadeIn(zero_dot)
        )

        self.next_slide()
        self.play(
            ReplacementTransform(not_ueaeq_y, Yspace),
        )

        self.next_slide()
        self.play(
            Write(tex_homogeneity)
        )

        self.next_slide(auto_next=True)
        Yspace_prima.next_to(Yspace, RIGHT, buff=BUFF_HALF)
        self.play(
            Unwrite(tex_homogeneity),
            # Group(Yspace, Yspace_prima).animate.move_to(ueaeq),
        )
        self.play(
            Write(Yspace_prima),
            Ybox.animate.shift(dr / 2).set_height(Ybox.get_height() - dr[1]).set_width(Ybox.get_width() - dr[0]),
            xinf_line.animate.shift(dr, dr[0] / 2 * LEFT).set_width(xinf_line.get_width() - dr[0]),
            yinf_line.animate.shift(dr, dr[1] / 2 * DOWN).set_height(yinf_line.get_height() - dr[1]),
            FadeOut(zero_dot),
        )

        # -------- Our result --------- #
        self.next_slide()
        self.play(
            FadeOut(citation1),
            FadeOut(citation2),
            FadeIn(citation_us_copy),
            ReplacementTransform(expeq_copy, expeq_us_copy),
        )

        # self.next_slide()
        # self.play(
        #     ReplacementTransform(not_ueatex, disjoint_inclusions),
        #     Create(disjoint_inclusions_example),
        #     Write(omega),
        # )
        #
        # self.next_slide()
        # self.play(
        #     fig2.animate.shift(0.2 * UL),
        #     fig3.animate.shift(0.2 * UR),
        #     fig4.animate.shift(0.2 * DR),
        #     fig5.animate.shift(0.2 * DL)
        # )
