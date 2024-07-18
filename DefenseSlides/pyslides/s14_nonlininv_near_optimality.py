from DefenseSlides.config import *
from pyslides.s09_intro_objectives_of_thesis import cite_ch2
from lib.utils import MySlide, get_sub_objects

EQ_FONT_SIZE = SMALL_FS

text_near_optimality_property = Tex("Near Optimality property", font_size=EQ_FONT_SIZE, color=INV_COLOR)
near_optimality_property = MathTex(r"\|\uu-\tilde{u} \|_V \leq C \|\uu-P_{V_n} \uu\|_V",
                                   substrings_to_isolate=[r"\tilde{u}"],
                                   tex_to_color_map={r"\tilde{u}": COLOR_APPROXIMATION},
                                   font_size=EQ_FONT_SIZE)
get_sub_objects(near_optimality_property, [1, 10, 15]).set_color(COLOR_SOLUTION)
get_sub_objects(near_optimality_property, [14, 13]).set_color(COLOR_LINEAR)
near_optimality_property_L1 = MathTex(r"\|\uu-\tilde{u} \|_{L^1} \leq C \|\uu-P_{V_n} \uu\|_{L^1}",
                                      substrings_to_isolate=["z", r"\tilde{u}"],
                                      tex_to_color_map={"z": COLOR_MEASUREMENTS, r"\tilde{u}": COLOR_APPROXIMATION},
                                      font_size=EQ_FONT_SIZE)

text_continuity = Tex(r"Lipschitz continuity", font_size=EQ_FONT_SIZE, color=COLOR_SOLUTION)
text_inverse_stability = Tex(r"Inverse stability", font_size=EQ_FONT_SIZE, color=COLOR_APPROXIMATION)
condition_lipschitz = MathTex(r"\|\ell(\uu)-\ell(\vv) \|_Z \leq \alpha_Z \|\uu-\vv\|_V, \;\; \uu,\vv \in V",
                              substrings_to_isolate=[r"\vv", r"\ell", r"\uu"],
                              tex_to_color_map={r"\vv": COLOR_SOLUTION, r"\uu": COLOR_SOLUTION,
                                                r"\ell": COLOR_MEASUREMENTS},
                              font_size=EQ_FONT_SIZE)

condition_inverse = MathTex(r"\|\uu-\vv\|_V \leq \mu_Z \|\ell(\uu)-\ell(\vv) \|_Z, \;\; \uu,\vv \in V_n",
                            substrings_to_isolate=[r"\uu",
                                                   r"\vv", r"\ell"],
                            tex_to_color_map={r"\uu": COLOR_APPROXIMATION,
                                              r"\vv": COLOR_APPROXIMATION,
                                              r"\ell": COLOR_MEASUREMENTS},
                            font_size=EQ_FONT_SIZE)

best_fit_estimator = MathTex(r"\tilde{u}=\argmin_{\vv \in V_n} \|z-\ell(\vv)\|_Z",
                             # r"\tilde{u}=\text{argmin}_{v\in V_n} \|z-\ell(v)\|}",
                             substrings_to_isolate=[r"\tilde{u}", r"\vv", "z"],
                             tex_to_color_map={r"\tilde{u}": COLOR_APPROXIMATION, r"\vv": COLOR_APPROXIMATION,
                                               "z": COLOR_MEASUREMENTS},
                             font_size=EQ_FONT_SIZE)
best_fit_estimator_ell1 = MathTex(r"\tilde{u}=\argmin_{\vv \in V_n} \|z-\ell(\vv)\|_{\ell^1}",
                                  # r"\tilde{u}=\text{argmin}_{v\in V_n} \|z-\ell(v)\|}",
                                  substrings_to_isolate=[r"\tilde{u}", r"\vv", "z"],
                                  tex_to_color_map={r"\tilde{u}": COLOR_APPROXIMATION, r"\vv": COLOR_APPROXIMATION,
                                                    "z": COLOR_MEASUREMENTS},
                                  font_size=EQ_FONT_SIZE)

# best_fit_estimator = MathTex(r"\tilde{u}=R(z)=\underset{v\in V_n}{\text{argmin}} \|z-\ell(v)\|}",
#                              substrings_to_isolate=[r"\tilde{u}", "v", "z"],
#                              tex_to_color_map={r"\tilde{u}": APPROXIMATION_COLOR, "v": APPROXIMATION_COLOR,
#                                                "z": MEASUREMENTS_COLOR},
#                              font_size=EQ_FONT_SIZE)


cite_pbdw = Tex("[Y. Maday, A. T. Patera, J. D. Penn, M. Yano, 2015]",
                font_size=CITATION_FONT_SIZE)

NOP_BUFF = BUFF_HALF / 2


class NearOptimalitySlides(MySlide):

    def construct(self, objects_from_previous_slides):
        title = Title(r"Inverse problem", font_size=STITLE_FS)

        nop = near_optimality_property.copy().next_to(title, DOWN, buff=BUFF_HALF).shift(ThreeColumns_dx / 2 * RIGHT)
        measurements = MathTex(r"\ell(u)+\eta = z \in \mathbb{R}^m",
                               substrings_to_isolate=["z", "u"],
                               tex_to_color_map={"z": COLOR_MEASUREMENTS, "u": COLOR_SOLUTION},
                               font_size=EQ_FONT_SIZE).next_to(title, DOWN, buff=BUFF_HALF).shift(TwoColumns_dx * LEFT)
        rz = MathTex(r"\tilde{u} = R(z) \;\; R : \mathbb{R}^m \rightarrow V",
                     substrings_to_isolate=["z", r"\tilde{u}"],
                     tex_to_color_map={"z": COLOR_MEASUREMENTS, r"\tilde{u}": COLOR_APPROXIMATION},
                     font_size=EQ_FONT_SIZE).next_to(measurements, DOWN, BUFF_HALF)
        best_fit = best_fit_estimator.copy().next_to(rz, DOWN, buff=NOP_BUFF)
        best_fit2 = best_fit.copy()

        # -------------- PBDW vs nonlinear -------------- #
        hilbert_cond = Tex(r"\begin{itemize}"
                           r"\item $V$ Hilbert space."
                           r"\end{itemize}",
                           # tex_environment="flushleft",
                           # tex_to_color_map={"parametric": COLOR_PARAMS, "PDE": PDE_COLOR},
                           # "linear": LINEAR_COLOR, "non-linear": NON_LINEAR_COLOR
                           font_size=EQ_FONT_SIZE).next_to(best_fit, DOWN, buff=BUFF_HALF)
        vnlinear_cond = Tex(r"\begin{itemize}"
                            r"\item $V_n$ a linear space with $\dim(V_n)=n.$"
                            r"\end{itemize}",
                            # tex_environment="flushleft",
                            # tex_to_color_map={"parametric": COLOR_PARAMS, "PDE": PDE_COLOR},
                            # "linear": LINEAR_COLOR, "non-linear": NON_LINEAR_COLOR
                            font_size=EQ_FONT_SIZE).next_to(hilbert_cond, DOWN)
        get_sub_objects(vnlinear_cond, [1, 2, 23, 24]).set_color(COLOR_LINEAR)
        elllinear_cond = Tex(r"\begin{itemize}"
                             r"\item $\ell \in V'$ linear functionals."
                             r"\end{itemize}",
                             # tex_environment="flushleft",
                             # tex_to_color_map={"parametric": COLOR_PARAMS, "PDE": PDE_COLOR},
                             # "linear": LINEAR_COLOR, "non-linear": NON_LINEAR_COLOR
                             font_size=EQ_FONT_SIZE).next_to(vnlinear_cond, DOWN)
        elllinear_cond.align_to(vnlinear_cond, LEFT)
        hilbert_cond.align_to(vnlinear_cond, LEFT)

        banach_cond = Tex(r"\begin{itemize}"
                          r"\item $V$ Banach space."
                          r"\end{itemize}",
                          # tex_environment="flushleft",
                          # tex_to_color_map={"parametric": COLOR_PARAMS, "PDE": PDE_COLOR},
                          # "linear": LINEAR_COLOR, "non-linear": NON_LINEAR_COLOR
                          font_size=EQ_FONT_SIZE).next_to(best_fit, DOWN, buff=BUFF_HALF)
        vnnonlinear_cond = Tex(r"\begin{itemize}"
                               r"\item $V_n$ non-linear n-parameter space."
                               r"\end{itemize}",
                               # tex_environment="flushleft",
                               # tex_to_color_map={"parametric": COLOR_PARAMS, "PDE": PDE_COLOR},
                               # "linear": LINEAR_COLOR, "non-linear": NON_LINEAR_COLOR
                               font_size=EQ_FONT_SIZE).next_to(banach_cond, DOWN)
        get_sub_objects(vnnonlinear_cond, [1, 2]).set_color(NON_LINEAR_COLOR)
        ellnonlinear_cond = Tex(r"\begin{itemize}"
                                r"\item $\ell$ non-linear functionals."
                                r"\end{itemize}",
                                tex_environment="flushleft",
                                # tex_to_color_map={"parametric": COLOR_PARAMS, "PDE": PDE_COLOR},
                                # "linear": LINEAR_COLOR, "non-linear": NON_LINEAR_COLOR
                                font_size=EQ_FONT_SIZE).next_to(vnnonlinear_cond, DOWN)
        banach_cond.align_to(vnlinear_cond, LEFT)
        ellnonlinear_cond.align_to(vnlinear_cond, LEFT)
        vnnonlinear_cond.align_to(vnlinear_cond, LEFT)

        # -------------- PBDW -------------- #
        ljwj = MathTex(r"\ell_j(\uu) = \langle w_j, \uu \rangle_V",
                       substrings_to_isolate=[r"\uu", r"w_j"],
                       tex_to_color_map={r"\uu": COLOR_SOLUTION, r"w_j": COLOR_MEASUREMENTS},
                       font_size=EQ_FONT_SIZE).next_to(elllinear_cond, DOWN, buff=BUFF_HALF)
        Riesz = Tex(r"$w_j \in V$ the Riesz representers of $\ell_j$").next_to(ljwj, DOWN, NOP_BUFF)
        get_sub_objects(Riesz, [0, 1]).set_color(COLOR_MEASUREMENTS)
        Wspace = MathTex(r"W := \text{span} \{w_1, \dots, w_m\}").next_to(Riesz, DOWN, NOP_BUFF)
        get_sub_objects(Wspace, [8, 9, 15, 16, 18, 19]).set_color(COLOR_MEASUREMENTS)
        w_vec = MathTex(r"w = P_W u").next_to(Wspace, DOWN, NOP_BUFF)
        get_sub_objects(w_vec, [0]).set_color(COLOR_MEASUREMENTS)
        get_sub_objects(w_vec, [4]).set_color(COLOR_SOLUTION)

        best_fit_pbdw = MathTex(r"\tilde{u}=\argmin_{\vv \in V_n} \|w-P_W v\|_V",
                                substrings_to_isolate=[r"\tilde{u}", r"\vv", "w"],
                                tex_to_color_map={r"\tilde{u}": COLOR_APPROXIMATION, r"\vv": COLOR_APPROXIMATION,
                                                  "w": COLOR_MEASUREMENTS},
                                font_size=EQ_FONT_SIZE).move_to(best_fit)
        get_sub_objects(best_fit_pbdw, [-3]).set_color(COLOR_APPROXIMATION)
        best_fit_pbdw_correction = MathTex(r"\uu^*=\tilde{u}+(w-P_W\tilde{u})",
                                           substrings_to_isolate=[r"\tilde{u}", r"\vv", "w", r"\uu^*"],
                                           tex_to_color_map={r"\tilde{u}": COLOR_APPROXIMATION,
                                                             r"\vv": COLOR_APPROXIMATION,
                                                             "w": COLOR_MEASUREMENTS, r"\uu^*": COLOR_APPROXIMATION},
                                           font_size=EQ_FONT_SIZE).next_to(best_fit_pbdw, DOWN, buff=NOP_BUFF)
        nop_pbdw_no_noise = MathTex(r"\begin{cases} "
                                    r"\|\uu-\tilde{u} \|_V \\ "
                                    r"\|\uu-\uu^* \|_V "
                                    r"\end{cases} "
                                    r"\leq \mu \|\uu-P_{V_n} \uu\|_V ",
                                    # substrings_to_isolate=[r"\tilde{u}", r"\uu^*"],
                                    # tex_to_color_map={r"\uu^*": APPROXIMATION_COLOR,
                                    #                   r"\tilde{u}": APPROXIMATION_COLOR},
                                    font_size=EQ_FONT_SIZE).move_to(nop, aligned_edge=RIGHT)
        get_sub_objects(nop_pbdw_no_noise, [2, 9, -8, -3]).set_color(COLOR_SOLUTION)
        get_sub_objects(nop_pbdw_no_noise, [4, 5, 11, 12]).set_color(COLOR_APPROXIMATION)
        nop_pbdw = MathTex(r"\begin{cases} "
                           r"\|\uu-\tilde{u} \|_V \\ "
                           r"\|\uu-\uu^* \|_V "
                           r"\end{cases} "
                           r"\leq \mu \|\uu-P_{V_n} \uu\|_V + \mu\beta\epsilon ",
                           # substrings_to_isolate=[r"\tilde{u}", r"\uu^*"],
                           # tex_to_color_map={r"\uu^*": APPROXIMATION_COLOR,
                           #                   r"\tilde{u}": APPROXIMATION_COLOR},
                           font_size=EQ_FONT_SIZE).move_to(nop_pbdw_no_noise, aligned_edge=LEFT)
        cite_pbdw.next_to(nop_pbdw_no_noise, DOWN).set_x(nop.get_x())
        get_sub_objects(nop_pbdw, [2, 9, -8 - 4, -3 - 4]).set_color(COLOR_SOLUTION)
        get_sub_objects(nop_pbdw, [4, 5, 11, 12]).set_color(COLOR_APPROXIMATION)
        mu_def = MathTex(r"\mu=\mu(V_n,W):= \max_{v\in V_n} \frac{\|v\|_V}{\|P_W v\|_V}",
                         substrings_to_isolate=[r"\tilde{u}", r"\vv", "w", r"\uu^*"],
                         tex_to_color_map={r"\tilde{u}": COLOR_APPROXIMATION, r"\vv": COLOR_APPROXIMATION,
                                           "w": COLOR_MEASUREMENTS, r"\uu^*": COLOR_APPROXIMATION},
                         font_size=EQ_FONT_SIZE).next_to(cite_pbdw, DOWN, BUFF_HALF)
        get_sub_objects(mu_def, [4, 5, 16, 17]).set_color(COLOR_LINEAR)
        # get_sub_objects(mu_def, [6]).set_color(COLOR_MEASUREMENTS)
        get_sub_objects(mu_def, [14, 19, 26]).set_color(COLOR_APPROXIMATION)
        beta_def = MathTex(
            r"\|\eta\|_p\leq \epsilon, \quad\quad \beta:=\max_{v\in W} \frac{\|\vv\|_V}{\|\ell(\vv)\|_p}",
            # substrings_to_isolate=[r"\vv"],
            # tex_to_color_map={r"\vv": MEASUREMENTS_COLOR},
            font_size=EQ_FONT_SIZE).next_to(mu_def, DOWN, BUFF_HALF)

        # -------------- Non linear -------------- #
        lip_continuity = text_continuity.copy().next_to(ellnonlinear_cond, DOWN, buff=BUFF_HALF).set_x(best_fit.get_x())
        lip_cond = condition_lipschitz.copy().next_to(lip_continuity, DOWN, buff=NOP_BUFF)
        inv_stab = text_inverse_stability.copy().next_to(lip_cond, DOWN, buff=BUFF_HALF)
        inv_cond = condition_inverse.copy().next_to(inv_stab, DOWN, buff=NOP_BUFF)
        alpha_def = MathTex(r"\alpha_Z = \sup_{\vv,\uu\in V} \frac{\|\ell(\vv) -\ell(\uu)\|_Z}{\|\vv-\uu\|_V}",
                            # substrings_to_isolate=[r"\vv", r"\uu"],
                            # tex_to_color_map={r"\uu": COLOR_SOLUTION, r"\vv": COLOR_SOLUTION},
                            ).next_to(beta_def, DOWN, buff=BUFF_HALF)
        mu_def_2 = MathTex(r"\mu_Z = \sup_{\vv,\uu\in V_n} \frac{\|\vv-\uu\|_V}{\|\ell(\vv) -\ell(\uu)\|_Z}",
                           # substrings_to_isolate=[r"\vv", r"\uu"],
                           # tex_to_color_map={r"\uu": APPROXIMATION_COLOR, r"\vv": APPROXIMATION_COLOR},
                           ).move_to(mu_def)
        get_sub_objects(mu_def_2, [6, 8, 13, 15, 22, 27]).set_color(COLOR_APPROXIMATION)
        get_sub_objects(mu_def_2, [10, 11]).set_color(NON_LINEAR_COLOR)

        nop_noise = MathTex(
            r"\|u-\tilde{u} \|_V \leq (1+2\alpha_Z \mu_Z) \|u-P_{V_n} u\|_V + (1+2\beta \mu_Z) \|\eta\|_p",
            # substrings_to_isolate=[r"\tilde{u}", r"\vv", "z"],
            # tex_to_color_map={r"\tilde{u}": APPROXIMATION_COLOR, r"\vv": APPROXIMATION_COLOR,
            #                   "z": MEASUREMENTS_COLOR},
            font_size=EQ_FONT_SIZE).move_to(nop)
        get_sub_objects(nop_noise, [1, 18, 23]).set_color(COLOR_SOLUTION)
        get_sub_objects(nop_noise, [3, 4]).set_color(COLOR_APPROXIMATION)

        theorem = (Tex(r"\textbf{Theorem} The \textit{best fit estimator} $\tilde{u}$ satisfies"
                       r"$$\|u-\tilde{u} \| \leq C_1 \|u-P_{V_n} u\| + C_2 \|\eta\|_p$$"
                       r"where $C_1=1+2\alpha_Z \mu$ and $C_2=1+2\beta \mu.$",
                       font_size=EQ_FONT_SIZE).next_to(nop, DOWN)
                   .set_y(Group(lip_continuity, inv_cond, inv_stab, lip_cond).get_y()))

        # -------------- -------------- -------------- #
        #   Near optimality property
        self.next_slide()
        self.play(
            self.fade_out_old_elements(),
            self.update_slide_number(),
            self.update_main_title(title),
            FadeIn(measurements, rz)
        )

        title = Title(r"Near optimality property", font_size=STITLE_FS)
        self.next_slide()
        self.play(
            self.update_main_title(title),
            Write(nop)
        )

        # sol = Dot(ORIGIN, color=COLOR_SOLUTION)
        # nopradius = Circle(radius=1.5, color=COLOR_SOLUTION, fill_opacity=0.25).move_to(sol)
        # vn_radius = 5
        # vn_shift = 0.75
        # vn = Arc(arc_center=(vn_radius + vn_shift) * UL, radius=vn_radius, start_angle=-PI / 2 - PI / 8,
        #          angle=PI / 2 + PI / 4, color=NON_LINEAR_COLOR)
        # best_approx = Dot(ORIGIN, color=NON_LINEAR_COLOR).move_to(sol).shift(vn_shift * UL)
        # approx = Dot(best_approx.get_center(), color=COLOR_APPROXIMATION)
        # validity_arc = Arc(arc_center=(vn_radius + vn_shift) * UL, radius=vn_radius, start_angle=-PI / 4 - PI / 8,
        #                    angle=PI / 4,
        #                    color=NON_LINEAR_COLOR)
        # Group(sol, nopradius, vn, approx, validity_arc, best_approx).scale(0.25).next_to(nop, DOWN, buff=BUFF_ONE)
        #
        # self.next_slide()
        # self.play(
        #     Create(sol),
        #     Create(nopradius),
        #     Create(vn),
        #     Create(best_approx),
        #     Create(approx)
        # )
        #
        # self.next_slide()
        # self.play(
        #     MoveAlongPath(approx, validity_arc),
        #     rate_func=there_and_back,
        # )
        # MoveAlongPath(dot, circle)

        # -------------- -------------- -------------- #
        #   Best fit estimator
        title = Title(r"Best fit estimator", font_size=STITLE_FS)
        self.next_slide()
        self.play(self.update_main_title(title), Write(best_fit))

        # -------------- -------------- -------------- #
        #   PBDW
        title = Title(r"Parameterized Background Data Weak", font_size=STITLE_FS)
        self.next_slide()
        self.play(self.update_main_title(title), FadeIn(hilbert_cond))
        self.next_slide()
        self.play(FadeIn(vnlinear_cond))
        self.next_slide()
        self.play(FadeIn(elllinear_cond))

        self.next_slide()
        self.play(Write(ljwj))

        self.next_slide()
        self.play(Write(Riesz), Write(Wspace), Write(w_vec))

        self.next_slide()
        best_fit.save_state()
        self.play(ReplacementTransform(best_fit, best_fit_pbdw))

        self.next_slide()
        self.play(Write(best_fit_pbdw_correction),
                  Group(hilbert_cond, vnlinear_cond, elllinear_cond, ljwj, Riesz, Wspace, w_vec).animate.shift(
                      best_fit_pbdw_correction.height * DOWN))

        self.next_slide()
        new_nop = nop.copy()
        self.play(Unwrite(nop, reverse=False), Write(nop_pbdw_no_noise),
                  FadeIn(cite_pbdw))

        self.next_slide()
        self.play(Write(mu_def))

        self.next_slide()
        self.play(Unwrite(nop_pbdw_no_noise, reverse=False), Write(nop_pbdw), run_time=1)

        self.next_slide()
        self.play(Write(beta_def))

        # -------------- -------------- -------------- #
        #   Conditions
        self.next_slide()
        title = Title(r"Towards non-linearity", font_size=STITLE_FS)
        self.play(self.update_main_title(title), self.update_slide_number(),
                  Unwrite(nop_pbdw, reverse=False),
                  FadeIn(new_nop),
                  # Group(hilbert_cond, vnlinear_cond, elllinear_cond, ljwj, Riesz, Wspace).animate.next_to(
                  #     best_fit_pbdw, DOWN, BUFF_HALF),
                  FadeOut(best_fit_pbdw_correction, cite_pbdw),
                  ReplacementTransform(best_fit_pbdw, best_fit2),
                  Unwrite(Riesz, reverse=False), Unwrite(ljwj, reverse=False), Unwrite(Wspace, reverse=False),
                  Unwrite(w_vec, reverse=False))

        self.next_slide()
        self.play(ReplacementTransform(hilbert_cond, banach_cond))
        self.next_slide()
        self.play(ReplacementTransform(vnlinear_cond, vnnonlinear_cond))
        self.next_slide()
        self.play(ReplacementTransform(elllinear_cond, ellnonlinear_cond))

        self.next_slide()
        title = Title(r"Sufficient conditions", font_size=STITLE_FS)
        self.play(self.update_main_title(title), Write(lip_continuity), Write(inv_stab))

        self.next_slide()
        self.play(Write(lip_cond))

        self.next_slide()
        self.play(Write(alpha_def))

        self.next_slide()
        self.play(Write(inv_cond))

        mutext = get_sub_objects(inv_cond, num_chars=[7, 8])
        self.next_slide()
        self.play(
            Indicate(mutext, 2),
            Indicate(mu_def),
            FadeOut(mutext.copy(), target_position=mu_def.get_center())
        )
        self.play(FadeOut(mu_def), FadeIn(mu_def_2))

        title = Title(r"Near optimality property for non-linear spaces", font_size=STITLE_FS)
        self.next_slide()
        self.play(self.update_main_title(title), self.update_slide_number(),
                  Write(nop_noise), FadeOut(new_nop), FadeIn(cite_ch2.next_to(nop_noise, DOWN)))
