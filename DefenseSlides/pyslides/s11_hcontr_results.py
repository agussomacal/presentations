from DefenseSlides.config import *
from DefenseSlides.pyslides.s10_hcontr_uea import INFTY_COLOR, y_space_box, disjoint_inclusions_domain, expeq, expeq_us
from pyslides.s04_intro_two_problems import num_snapshots, get_diff_eq_images, parameters_ls_dict, infty_subdomains
from pyslides.s09_intro_objectives_of_thesis import cite_ch1
from lib.utils import MySlide, get_sub_objects, create_grid_of_colored_rectangles

COLOR_EXTREME_PARTITION = RED

BUFF_thorems = 0.25

FONT_SCALE = 0.8
EQ_FONT_SIZE_HC_RESULTS = EQ_FONT_SIZE * FONT_SCALE
BUFF_EQ_HC_RESULTS = BUFF_HALF * FONT_SCALE

params_shape = np.shape(parameters_ls_dict[0])


class ResultsSlides(MySlide):

    def construct(self, objects_from_previous_slides):
        title = Title(r"Three main results", font_size=STITLE_FS)

        title_compactness = Tex(r"Compactness", font_size=EQ_FONT_SIZE).next_to(title, DOWN,
                                                                                buff=BUFF_EQ_HC_RESULTS).shift(
            ThreeColumns_dx * LEFT)
        title_convergence = Tex(r"Convergence", font_size=EQ_FONT_SIZE).next_to(title, DOWN, buff=BUFF_EQ_HC_RESULTS)
        title_quantification = Tex(r"Convergence rate", font_size=EQ_FONT_SIZE).next_to(title, DOWN,
                                                                                        buff=BUFF_EQ_HC_RESULTS).shift(
            ThreeColumns_dx * RIGHT)

        tex_convergence = Tex(r"Theorem: There exists a sequence of linear spaces $(V_n)_{n>1}$ "
                              r"and a zero converging sequence $(\varepsilon_n)_{n>1}$ for all $y \in Y'$ "
                              r"such that $$\| u(y) - P_{V_n} u(y) \| \leq \varepsilon_n\| u(y) \|_{H^1_0}.$$",
                              # tex_to_color_map={r"y": PARAMS_COLOR, r"\uu": SOLUTION_COLOR}
                              tex_template=add_latex_file2preample(
                                  TexTemplate(
                                      documentclass=fr"\documentclass[preview, varwidth={1.65 * pixels_per_width_point}px]" + "{standalone}"),
                                  source_dir),
                              font_size=EQ_FONT_SIZE_HC_RESULTS
                              ).next_to(title_convergence, DOWN, buff=BUFF_thorems)
        get_sub_objects(tex_convergence, [-9, -18, -26]).set_color(COLOR_SOLUTION)
        get_sub_objects(tex_convergence, [-7, -16, -39, -24]).set_color(COLOR_PARAMS)
        get_sub_objects(tex_convergence, [-19, -20, 43, 44]).set_color(COLOR_LINEAR)

        # ------ Three main steps ------ #
        self.next_slide()
        self.play(
            self.fade_out_old_elements(),
            self.update_slide_number(),
            self.update_main_title(title),
        )
        self.play(
            Write(title_compactness),
            Write(title_convergence),
            Write(title_quantification),
        )

        # ------ compactness ------ #
        tex_compact = Tex(r"$\cM' := \{ \uu (y): y \in Y' \}$ is a compact set of $H^1_0(\Omega )$",
                          # tex_to_color_map={r"y": PARAMS_COLOR, r"\uu": SOLUTION_COLOR}
                          tex_template=add_latex_file2preample(
                              TexTemplate(
                                  documentclass=fr"\documentclass[preview, varwidth={pixels_per_width_point}px]" + "{standalone}"),
                              source_dir),
                          font_size=EQ_FONT_SIZE_HC_RESULTS
                          ).next_to(title_compactness, DOWN, buff=BUFF_thorems)
        get_sub_objects(tex_compact, [5]).set_color(COLOR_SOLUTION)
        get_sub_objects(tex_compact, [7, 10]).set_color(COLOR_PARAMS)
        tex_limiting_solutions = Tex(r"Limiting solutions: $u_S \in V_S$\\ "
                                     r"$V_S:=\{v \in H^1_0; \nabla v_{|\Omega_j}=0; j\in S \subset \{1,2,\dots,d\}\}$",
                                     font_size=EQ_FONT_SIZE_HC_RESULTS).next_to(tex_compact, DOWN,
                                                                                buff=BUFF_EQ_HC_RESULTS)
        get_sub_objects(tex_limiting_solutions, [-18, -19, -20, -21, -22, -23, -24]).set_color(INFTY_COLOR)
        tex_lemma_lim_sol = Tex(r"Lemma: $!\exists$ $u_S(y_{S^c})\in V_S$ the limit of $u(y_S^c,y_S)$ "
                                r"as $y_j \rightarrow \infty$ with $j\in S$",
                                tex_template=add_latex_file2preample(
                                    TexTemplate(
                                        documentclass=fr"\documentclass[preview, varwidth={1.65 * pixels_per_width_point}px]" + "{standalone}"),
                                    source_dir),
                                font_size=EQ_FONT_SIZE_HC_RESULTS
                                ).next_to(tex_limiting_solutions, DOWN, buff=BUFF_thorems)
        get_sub_objects(tex_lemma_lim_sol, [-3 - 7, -4 - 7]).set_color(COLOR_PARAMS)
        get_sub_objects(tex_lemma_lim_sol, [-1 - 7]).set_color(INFTY_COLOR)

        self.next_slide()
        self.play(
            Write(tex_compact),
        )

        self.next_slide()
        self.play(
            Write(tex_limiting_solutions),
        )

        def get_diffusion_param_limit_solutions(i, ls=False):
            matrix = np.array(parameters_ls_dict[i])
            max_index = np.where(matrix == np.max(matrix))
            r, t = create_grid_of_colored_rectangles(np.array(matrix), cmap=COLOR_PARAMS,
                                                     number_color=COLOR_PARAMS,
                                                     stroke_width=1, fill_opacity=0.25)
            if i == num_snapshots - 1:
                for k, l in zip(*max_index):
                    if ls:
                        tex_val = MathTex(r"\nabla u_{S}\\=0", font_size=DEFAULT_FONT_SIZE * 3 / 4)
                    else:
                        tex_val = MathTex(r"\infty", font_size=DEFAULT_FONT_SIZE)
                    ix = l + np.shape(matrix)[0] * k
                    t[ix] = tex_val.move_to(t[ix])
            new_param_matrix = VDict({"rectangles": r, "entries": t})

            # if i == num_snapshots - 1:
            #     matrix = matrix.tolist()
            #     for k, l in zip(*max_index):
            #         if ls:
            #             matrix[k][l] = r"\nabla u_{S}=0"
            #         else:
            #             matrix[k][l] = r"+\infty"
            # param_matrix = Matrix(matrix, left_bracket="(", right_bracket=")", element_alignment_corner=ORIGIN,
            #                       element_to_mobject_config={"font_size": STITLE_FS})
            new_param_matrix = new_param_matrix.set_color(COLOR_PARAMS).scale(0.37 * 0.75)
            new_solution = (get_diff_eq_images(name="solutions_lim_sol", i=i)
                            .scale(0.6 * 0.75).next_to(new_param_matrix, RIGHT, buff=0.2))
            return new_param_matrix, new_solution

        param_matrix, solution = get_diffusion_param_limit_solutions(0)
        param_matrix_ls, solution_ls = get_diffusion_param_limit_solutions(num_snapshots - 1, ls=True)
        Group(param_matrix_ls, solution_ls).next_to(Group(param_matrix, solution), DOWN, buff=0.2)
        # param_matrix_ls.next_to(param_matrix, DOWN, buff=0.2, aligned_edge=RIGHT)
        us_text = MathTex("u_S").next_to(solution_ls, RIGHT, buff=BUFF_thorems)
        v_text = MathTex(r"u(y_S^c,y_S)").next_to(solution, RIGHT, buff=BUFF_thorems)
        group_inf_sol = (Group(us_text, v_text, param_matrix_ls, solution_ls, param_matrix, solution)
                         .next_to(tex_lemma_lim_sol, DOWN, buff=BUFF_EQ_HC_RESULTS))

        self.next_slide()
        self.play(
            Write(us_text),
            Write(v_text),
            FadeIn(param_matrix),
            FadeIn(solution),
            FadeIn(param_matrix_ls),
            FadeIn(solution_ls)
        )

        # limit solutions
        self.next_slide()
        param_cycle_period = 2
        for i in range(1, num_snapshots):
            new_param_matrix, new_solution = get_diffusion_param_limit_solutions(i)
            new_param_matrix.move_to(param_matrix, aligned_edge=RIGHT)
            new_solution.move_to(solution)
            self.play(
                FadeOut(param_matrix),
                FadeIn(new_param_matrix),
                ReplacementTransform(solution, new_solution),
                run_time=param_cycle_period / num_snapshots, rate_func=linear
            )
            param_matrix = new_param_matrix
            solution = new_solution

        self.play(
            Write(tex_lemma_lim_sol),
            *[Indicate(param_matrix["entries"][subdomain[1] + params_shape[0] * subdomain[0]]) for subdomain in
              infty_subdomains],
            *[Indicate(param_matrix_ls["entries"][subdomain[1] + params_shape[0] * subdomain[0]]) for subdomain in
              infty_subdomains],
            *[Indicate(param_matrix["rectangles"][subdomain[1] + params_shape[0] * subdomain[0]]) for subdomain in
              infty_subdomains],
            *[Indicate(param_matrix_ls["rectangles"][subdomain[1] + params_shape[0] * subdomain[0]]) for subdomain in
              infty_subdomains],
            # *[param_matrix.get_columns()[subdomain[1]][subdomain[0]].animate.scale(1.2).set_color(INFTY_COLOR) for
            #   subdomain in infty_subdomains],
            # *[param_matrix_ls.get_columns()[subdomain[1]][subdomain[0]].animate.scale(1.2).set_color(INFTY_COLOR) for
            #   subdomain in infty_subdomains]
        )
        self.play(
            *[param_matrix["entries"][subdomain[1] + params_shape[0] * subdomain[0]].animate.set_color(INFTY_COLOR) for
              subdomain in infty_subdomains],
            *[param_matrix_ls["entries"][subdomain[1] + params_shape[0] * subdomain[0]].animate.set_color(INFTY_COLOR)
              for subdomain in infty_subdomains],
            *[param_matrix["rectangles"][subdomain[1] + params_shape[0] * subdomain[0]].animate.set_color(INFTY_COLOR)
              for
              subdomain in infty_subdomains],
            *[param_matrix_ls["rectangles"][subdomain[1] + params_shape[0] * subdomain[0]].animate.set_color(
                INFTY_COLOR)
                for subdomain in infty_subdomains],
            # *[param_matrix.get_columns()[subdomain[1]][subdomain[0]].animate.scale(1.2).set_color(INFTY_COLOR) for
            #   subdomain in infty_subdomains],
            # *[param_matrix_ls.get_columns()[subdomain[1]][subdomain[0]].animate.scale(1.2).set_color(INFTY_COLOR) for
            #   subdomain in infty_subdomains]
        )

        # ------ convergence ------ #
        self.next_slide()
        self.play(
            Write(tex_convergence),
        )

        # ------ convergence rate ------ #
        r = 0.1
        scaling = 0.75
        R = 1
        R, Ybox, xax, yax = y_space_box(r, R)
        Ybox.set_stroke_width(0).set_height(scaling * R).set_width(scaling * R).shift(0.25 / 2 * R * UR)
        xinf_line = DashedLine(ORIGIN, scaling * R * RIGHT, stroke_width=2.5, stroke_color=COLOR_PARAMS,
                               stroke_opacity=1).move_to(Ybox, aligned_edge=DL)
        yinf_line = DashedLine(ORIGIN, scaling * R * UP, stroke_width=2.5, stroke_color=COLOR_PARAMS,
                               stroke_opacity=1).move_to(Ybox, aligned_edge=DL)

        (Group(Ybox, xax, yax, xinf_line, yinf_line)
         .next_to(tex_convergence, DOWN, buff=BUFF_EQ_HC_RESULTS + 1))

        yj = MathTex(r"y_j", color=COLOR_PARAMS).next_to(xax, DOWN, buff=BUFF_thorems)
        yjp = MathTex(r"y_{j+1}", color=COLOR_PARAMS).next_to(yax, LEFT, buff=BUFF_thorems)
        zj = MathTex(r"1/y_j", color=COLOR_PARAMS).next_to(xax, DOWN, buff=BUFF_thorems)
        zjp = MathTex(r"1/y_{j+1}", color=COLOR_PARAMS).next_to(yax, LEFT, buff=BUFF_thorems)

        self.next_slide()
        self.play(
            FadeIn(Ybox, xax, yax, xinf_line, yinf_line),
            Write(yj),
            Write(yjp)
        )

        self.next_slide()
        self.play(
            ReplacementTransform(yj, zj),
            ReplacementTransform(yjp, zjp),
            Ybox.animate.set_height(scaling * R).set_width(scaling * R).move_to(xax.get_edge_center(LEFT),
                                                                                aligned_edge=DL),
            FadeOut(xinf_line),
            FadeOut(yinf_line),
        )

        dot_zj = Dot(Ybox.get_edge_center(DR), radius=DEFAULT_DOT_RADIUS * 0.5, color=COLOR_PARAMS)
        dot_zjp = Dot(Ybox.get_edge_center(UL), radius=DEFAULT_DOT_RADIUS * 0.5, color=COLOR_PARAMS)
        # dot_11 = Dot(Ybox.get_edge_center(UR), radius=DEFAULT_DOT_RADIUS * 0.5, color=COLOR_PARAMS)
        dot_inf = Dot(Ybox.get_edge_center(DL), radius=DEFAULT_DOT_RADIUS * 0.5, color=COLOR_PARAMS)

        solution_j = (get_diff_eq_images(name="solutions_lim_sol", i="_".join(map(str, infty_subdomains[0])))
                      .scale(0.3).next_to(dot_zj, DR, buff=0.2))
        solution_jp = (get_diff_eq_images(name="solutions_lim_sol", i="_".join(map(str, infty_subdomains[3])))
                       .scale(0.3).next_to(dot_zjp, UL, buff=0.2))
        # solution_11 = (get_diff_eq_images(name="solutions_lim_sol", i="11")
        #                .scale(0.3).next_to(dot_11, UR, buff=0.2))
        solution_infinf = (get_diff_eq_images(name="solutions_lim_sol", i="infinf")
                           .scale(0.3).next_to(dot_inf, DL, buff=0.2))
        self.next_slide()
        self.play(
            Create(dot_zj),
            FadeIn(solution_j),
        )

        self.next_slide()
        self.play(
            Create(dot_zjp),
            FadeIn(solution_jp),
        )

        # self.next_slide()
        # self.play(
        #     Create(dot_11),
        #     # FadeIn(solution_11),
        # )

        self.next_slide()
        self.play(
            Create(dot_inf),
            FadeIn(solution_infinf),
        )

        # ------ dyadic partition ------ #
        self.next_slide()
        self.play(
            FadeOut(solution_j, solution_jp,  # solution_11,
                    solution_infinf),
            FadeOut(  # dot_11,
                dot_zj, dot_zjp, dot_inf),
            Ybox.animate.set_height(1.5).set_width(1.5).move_to(xax.get_edge_center(LEFT), aligned_edge=DL),
            xax.animate.set_width(2).shift(0.25 * RIGHT),
            yax.animate.set_height(2).shift(0.25 * UP),
            zj.animate.shift(0.25 * RIGHT),
            zjp.animate.shift(0.25 * UP),
        )

        tex_dyadic = (Tex("Dyadic partition", font_size=EQ_FONT_SIZE_HC_RESULTS)
                      .next_to(Ybox, UP, buff=BUFF_EQ_HC_RESULTS))
        dy_v1 = DashedLine(Ybox.get_edge_center(DOWN), Ybox.get_edge_center(UP), stroke_width=2)
        dy_h1 = DashedLine(Ybox.get_edge_center(LEFT), Ybox.get_edge_center(RIGHT), stroke_width=2)
        self.next_slide()
        self.play(
            Write(tex_dyadic),
            Create(dy_v1),
            Create(dy_h1),
        )

        w, h, _ = (Ybox.get_edge_center(UR) - Ybox.get_center()).tolist()
        region = Rectangle(height=h, width=w, color=COLOR_PARAMS, fill_opacity=0.5).move_to(Ybox.get_center(),
                                                                                            aligned_edge=DL)
        self.next_slide()
        self.play(
            Indicate(region),
        )
        parametric_expansion = MathTex(r"u(y)=\sum_{\nu \in \N^d} u_\nu y^\nu", font_size=EQ_FONT_SIZE_HC_RESULTS)
        get_sub_objects(parametric_expansion, [0]).set_color(COLOR_SOLUTION)
        get_sub_objects(parametric_expansion, [2, -2]).set_color(COLOR_PARAMS)
        parametric_truncation = (MathTex(r"\tilde u=u_{b,k}(y)=\sum_{|\nu| \leq k} u_{b,\nu} y^\nu",
                                         font_size=EQ_FONT_SIZE_HC_RESULTS)
                                 .next_to(parametric_expansion, RIGHT, BUFF_thorems))
        get_sub_objects(parametric_truncation, [0, 1]).set_color(COLOR_APPROXIMATION)
        get_sub_objects(parametric_truncation, [8, -2]).set_color(COLOR_PARAMS)
        gpexp = Group(parametric_truncation, parametric_expansion).next_to(yj, DOWN, buff=BUFF_EQ_HC_RESULTS)
        citation = (Tex("[M. Bachmayr and A. Cohen., Mathematics of Computation, 2017]",
                        font_size=CITATION_FONT_SIZE, color=COLOR_APPROXIMATION)
                    .next_to(gpexp, DOWN, BUFF_thorems))
        self.next_slide()
        self.play(
            Write(parametric_truncation),
            Write(parametric_expansion),
        )

        expeq_copy = expeq.copy().next_to(region, RIGHT, buff=BUFF_thorems).set_color(COLOR_APPROXIMATION)
        self.next_slide()
        self.play(
            region.animate.scale(1.5).set_color(COLOR_APPROXIMATION),
            Write(citation),
            Write(expeq_copy)
        )

        dy_v2 = DashedLine(Ybox.get_edge_center(DOWN) + Ybox.width / 4 * LEFT,
                           Ybox.get_edge_center(UP) + Ybox.width / 4 * LEFT, stroke_width=2)
        dy_h2 = DashedLine(Ybox.get_edge_center(LEFT) + Ybox.height / 4 * DOWN,
                           Ybox.get_edge_center(RIGHT) + Ybox.height / 4 * DOWN, stroke_width=2)
        self.next_slide()
        self.play(
            region.animate.scale(2 / 3),
            Write(tex_dyadic),
            Create(dy_v2),
            Create(dy_h2),
        )

        regions = [
            (Rectangle(height=h / 2, width=w, color=COLOR_PARAMS, fill_opacity=0.5)
             .move_to(region.get_edge_center(DL), aligned_edge=DL).shift(h / 2 * DOWN)),
            (Rectangle(height=h, width=w / 2, color=COLOR_PARAMS, fill_opacity=0.5)
             .move_to(region.get_edge_center(DL), aligned_edge=DL).shift(w / 2 * LEFT)),
            (Rectangle(height=h / 2, width=w / 2, color=COLOR_PARAMS, fill_opacity=0.5)
             .move_to(region.get_edge_center(DL), aligned_edge=DL).shift(h / 2 * DOWN, w / 2 * LEFT))
        ]
        for region_i in regions:
            self.next_slide()
            self.play(
                Indicate(region_i),
            )
            self.play(
                region_i.animate.scale(1.5).set_color(COLOR_APPROXIMATION),
            )
            self.play(
                region_i.animate.scale(2 / 3),
            )

        regions_us = [
            (Rectangle(height=h / 2, width=w, color=COLOR_PARAMS, fill_opacity=0.5)
             .move_to(regions[0].get_edge_center(DL), aligned_edge=DL).shift(h / 2 * DOWN)),
            (Rectangle(height=h / 2, width=w / 2, color=COLOR_PARAMS, fill_opacity=0.5)
             .move_to(regions[2].get_edge_center(DL), aligned_edge=DL).shift(h / 2 * DOWN)),
            (Rectangle(height=h / 2, width=w / 2, color=COLOR_PARAMS, fill_opacity=0.5)
             .move_to(regions[2].get_edge_center(DL), aligned_edge=DL).shift(h / 2 * DOWN, w / 2 * LEFT)),
            (Rectangle(height=h / 2, width=w / 2, color=COLOR_PARAMS, fill_opacity=0.5)
             .move_to(regions[2].get_edge_center(DL), aligned_edge=DL).shift(w / 2 * LEFT)),
            (Rectangle(height=h, width=w / 2, color=COLOR_PARAMS, fill_opacity=0.5)
             .move_to(regions[1].get_edge_center(DL), aligned_edge=DL).shift(w / 2 * LEFT)),
        ]

        dot_us = [
            Dot(regions_us[0].get_edge_center(DOWN), radius=DEFAULT_DOT_RADIUS * 0.5, color=COLOR_EXTREME_PARTITION),
            Dot(regions_us[1].get_edge_center(DOWN), radius=DEFAULT_DOT_RADIUS * 0.5, color=COLOR_EXTREME_PARTITION),
            Dot(regions_us[2].get_edge_center(DL), radius=DEFAULT_DOT_RADIUS * 0.5, color=COLOR_EXTREME_PARTITION),
            Dot(regions_us[3].get_edge_center(LEFT), radius=DEFAULT_DOT_RADIUS * 0.5, color=COLOR_EXTREME_PARTITION),
            Dot(regions_us[4].get_edge_center(LEFT), radius=DEFAULT_DOT_RADIUS * 0.5, color=COLOR_EXTREME_PARTITION),
        ]
        for region_i, d in zip(regions_us, dot_us):
            self.next_slide()
            self.play(
                Indicate(region_i),
                run_time=0.5,
            )
            self.play(
                Create(d),
                region_i.animate.set_color(COLOR_EXTREME_PARTITION),
                run_time=0.5,
            )

        self.next_slide()
        disjoint_inclusions = Tex(r"Geometrical assumption", font_size=EQ_FONT_SIZE_HC_RESULTS,
                                  tex_template=LatexTemplate,
                                  color=COLOR_EXTREME_PARTITION).next_to(title_quantification, DOWN, BUFF_thorems)
        fig1, fig2, fig3, fig4, fig5, omega = disjoint_inclusions_domain()
        disjoint_inclusions_example = VGroup(
            fig1, fig2, fig3, fig4, fig5, omega
        ).next_to(disjoint_inclusions, DOWN, buff=BUFF_HALF)
        fig2.shift(0.2 * UL),
        fig3.shift(0.2 * UR),
        fig4.shift(0.2 * DR),
        fig5.shift(0.2 * DL)
        expeq_us_copy = expeq_us.copy().next_to(disjoint_inclusions_example, DOWN,
                                                buff=BUFF_thorems).set_color(COLOR_EXTREME_PARTITION)
        cite_ch1.next_to(expeq_us_copy, DOWN, buff=BUFF_thorems).set_color(COLOR_EXTREME_PARTITION)
        Group(disjoint_inclusions, disjoint_inclusions_example, expeq_us_copy, cite_ch1).set_y(expeq_copy.get_y())

        self.play(FadeIn(disjoint_inclusions_example))
        self.play(Write(disjoint_inclusions))
        self.next_slide()
        self.play(
            Write(expeq_us_copy),
            Write(cite_ch1)
        )

        return {"xax": xax, "yax": yax, "Ybox": Ybox, "dot_us": dot_us, "dy_v2": dy_v2, "dy_h2": dy_h2, "dy_h1": dy_h1,
                "dy_v1": dy_v1}
