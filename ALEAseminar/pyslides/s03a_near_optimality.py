from pathlib import Path

from ALEAseminar.Concepts.NOPProof.NOPProof import ConceptNOPProof
from ALEAseminar.config import *
from lib.utils import MySlide, get_sub_objects
from ALEAseminar.support_data import path_subcell, min_n, subdivisions

# ------ style objects ------ #
font_size = EQ_FONT_SIZE
style_dict = {
    "tex_to_color_map": {
        r"\uu": COLOR_SOLUTION,
        r"\tu": COLOR_APPROXIMATION,
        r"\vv": COLOR_APPROXIMATION,
        "z": COLOR_MEASUREMENTS
    },
    "substrings_to_isolate": [r"\uu", r"\tu", r"v"],
    "font_size": font_size
}

EQ_FONT_SIZE = SMALL_FS
cite_ch2 = Tex("[A. Cohen, M. Dolbeault, O. Mula, A. Somacal, 2023]", font_size=CITATION_FONT_SIZE)

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

cite_pbdw = Tex("[Y. Maday, A. T. Patera, J. D. Penn, M. Yano, 2015]",
                font_size=CITATION_FONT_SIZE)

NOP_BUFF = BUFF_HALF / 2


class NearOptimalitySlides(MySlide):

    def construct(self, objects_from_previous_slides):
        title = Title(r"Inverse problem", font_size=STITLE_FS)

        nop = near_optimality_property.copy().next_to(title, DOWN, buff=BUFF_HALF).shift(ThreeColumns_dx / 2 * RIGHT)

        # ----- from previous slides ----- #
        if len(objects_from_previous_slides):
            tex_z = objects_from_previous_slides.pop("tex_z")
            seeq = objects_from_previous_slides.pop("seeq")
            yoda_rec_img_old = objects_from_previous_slides.pop("rec_image")
            yoda_img_old = objects_from_previous_slides.pop("yoda_img")
            yoda_pointwise_old = objects_from_previous_slides.pop("yoda_pointwise")
            # yoda_avg_old = objects_from_previous_slides.pop("yoda_avg")
        else:
            yoda_rec_img_old = ImageMobject(Path(f"{path_subcell}/yoda_approx_{min_n}.png")).scale_to_fit_height(1.5)
            yoda_img_old = ImageMobject(Path(f"{path_subcell}/yoda.png")).scale_to_fit_height(1.5)
            yoda_pointwise_old = ImageMobject(Path(f"{path_subcell}/yoda_pointwise")).scale_to_fit_height(1.5)
            # yoda_avg_old = ImageMobject(Path(f"{path_subcell}/yoda_avg20.png")).scale_to_fit_height(1.5)
            tex_z = MathTex(r"\ell(u)+\eta = z \in \mathbb{R}^m",
                            substrings_to_isolate=["z", "u"],
                            tex_to_color_map={"z": COLOR_MEASUREMENTS, "u": COLOR_SOLUTION},
                            font_size=MEDIUM_FS)
            seeq = MathTex(r"\tilde{u} = R(z) \;\; R : \mathbb{R}^m \rightarrow V",
                           substrings_to_isolate=["z", r"\tilde{u}"],
                           tex_to_color_map={"z": COLOR_MEASUREMENTS, r"\tilde{u}": COLOR_APPROXIMATION},
                           font_size=MEDIUM_FS)

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

        height_of_img = BUFF_HALF
        yoda_rec = ImageMobject(Path(f"{path_subcell}/yoda_approx_{min_n}.png")).scale_to_fit_height(height_of_img)
        yoda_img = ImageMobject(Path(f"{path_subcell}/yoda.png")).scale_to_fit_height(height_of_img)
        yoda_pointwise = ImageMobject(Path(f"{path_subcell}/yoda_pointwise")).scale_to_fit_height(height_of_img)
        # yoda_avg = ImageMobject(Path(f"{path_subcell}/yoda_avg20.png")).scale_to_fit_height(height_of_img)

        yoda_img.next_to(measurements, LEFT, buff=3 / 2 * BUFF_HALF)
        yoda_pointwise.next_to(measurements, RIGHT, buff=3 / 2 * BUFF_HALF)
        # yoda_avg.next_to(yoda_pointwise, LEFT, buff=BUFF_QUARTER)
        (yoda_rec.next_to(Group(rz, best_fit), LEFT, buff=BUFF_QUARTER)
         .set_y((rz.get_y(DOWN) + best_fit.get_y(UP)) / 2).set_x(yoda_img.get_x()))

        yoda_rec_pointwise = ImageMobject(
            Path(f"{path_subcell}/yoda_approx_pointwise_{min_n}.png")).scale_to_fit_height(
            height_of_img)
        yoda_diff_pointwise = ImageMobject(
            Path(f"{path_subcell}/yoda_approx_diff_pointwise_{min_n}.png")).scale_to_fit_height(
            height_of_img)
        yoda_diff = ImageMobject(Path(f"{path_subcell}/yoda_approx_diff_{min_n}.png")).scale_to_fit_height(
            height_of_img)

        yoda_rec_pointwise.set_x(yoda_pointwise.get_x()).set_y(yoda_rec.get_y())
        yoda_diff_pointwise.next_to(get_sub_objects(best_fit, [-9, -1]).get_center(), DOWN, BUFF_HALF)
        yoda_diff.next_to(get_sub_objects(nop, [0, 6]).get_center(), DOWN, BUFF_HALF)

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
                         font_size=EQ_FONT_SIZE).next_to(cite_pbdw, DOWN, BUFF_QUARTER)
        get_sub_objects(mu_def, [4, 5, 16, 17]).set_color(COLOR_LINEAR)
        # get_sub_objects(mu_def, [6]).set_color(COLOR_MEASUREMENTS)
        get_sub_objects(mu_def, [14, 19, 26]).set_color(COLOR_APPROXIMATION)
        beta_def = MathTex(
            r"\|\eta\|_p\leq \epsilon, \quad\quad \beta:=\max_{v\in W} \frac{\|\vv\|_V}{\|\ell(\vv)\|_p}",
            # substrings_to_isolate=[r"\vv"],
            # tex_to_color_map={r"\vv": MEASUREMENTS_COLOR},
            font_size=EQ_FONT_SIZE).next_to(mu_def, DOWN, BUFF_QUARTER)

        # -------------- Non linear -------------- #
        lip_continuity = text_continuity.copy().next_to(ellnonlinear_cond, DOWN, buff=BUFF_HALF).set_x(best_fit.get_x())
        lip_cond = condition_lipschitz.copy().next_to(lip_continuity, DOWN, buff=NOP_BUFF)
        inv_stab = text_inverse_stability.copy().next_to(lip_cond, DOWN, buff=BUFF_HALF)
        inv_cond = condition_inverse.copy().next_to(inv_stab, DOWN, buff=NOP_BUFF)
        alpha_def = MathTex(r"\alpha_Z = \sup_{\vv,\uu\in V} \frac{\|\ell(\vv) -\ell(\uu)\|_Z}{\|\vv-\uu\|_V}",
                            # substrings_to_isolate=[r"\vv", r"\uu"],
                            # tex_to_color_map={r"\uu": COLOR_SOLUTION, r"\vv": COLOR_SOLUTION},
                            ).next_to(beta_def, DOWN, buff=BUFF_QUARTER)
        mu_def_2 = MathTex(r"\mu_Z = \sup_{\vv,\uu\in V_n} \frac{\|\vv-\uu\|_V}{\|\ell(\vv) -\ell(\uu)\|_Z}",
                           # substrings_to_isolate=[r"\vv", r"\uu"],
                           # tex_to_color_map={r"\uu": APPROXIMATION_COLOR, r"\vv": APPROXIMATION_COLOR},
                           ).move_to(mu_def)
        get_sub_objects(mu_def_2, [6, 8, 13, 15, 22, 27]).set_color(COLOR_APPROXIMATION)
        get_sub_objects(mu_def_2, [10, 11]).set_color(NON_LINEAR_COLOR)

        nop_noise = MathTex(
            r"\|u-\tu \|_V \leq (1+2\alpha_Z \mu_Z) \|\uu-P_{V_n} \uu\|_V + (1+2\beta \mu_Z) \|\eta\|_p",
            font_size=EQ_FONT_SIZE).move_to(nop)
        get_sub_objects(nop_noise, [1, 18, 23]).set_color(COLOR_SOLUTION)
        get_sub_objects(nop_noise, [20, 21, 22, 23]).set_color(COLOR_LINEAR)
        get_sub_objects(nop_noise, [3, 4]).set_color(COLOR_APPROXIMATION)

        # -------------- -------------- -------------- #
        #   near optimality plot

        m_lin = Line(np.array([0, 0, 0]), np.array([1, 0.5, 0]), color=COLOR_LINEAR, stroke_width=3).scale(3)
        Vn = MathTex("V_n", color=COLOR_LINEAR).next_to(m_lin, UR)
        map_group = VDict({"tex Vn space": Vn, "linear space": m_lin})

        radius = DEFAULT_DOT_RADIUS * 0.5
        # VT_dict = {c: ValueTracker(v) for c, v in zip("xyz", map_group.get_center())}
        # VT_dict["x"] -= 1
        # VT_dict["y"] += 1
        # upos = get_values_from_VTracker_dict(VT_dict, ["x", "y", "z"], return_np_array=True)
        upos = map_group.get_center() + np.array([-1, 1, 0])
        udot = Dot(upos, radius=radius, color=COLOR_SOLUTION)
        Group(udot, m_lin, Vn).next_to(alpha_def, DOWN, BUFF_QUARTER)
        upos = udot.get_center()

        vdot = Dot(m_lin.get_projection(upos), radius=radius, color=COLOR_LINEAR)
        utdot = Dot(m_lin.get_projection(upos + np.array([-0.5, 0, 0])), radius=radius,
                    color=COLOR_APPROXIMATION)

        utex = SingleStringMathTex("u", color=COLOR_SOLUTION).next_to(udot)
        vtex = SingleStringMathTex("P_{V_n}u", color=COLOR_LINEAR).next_to(vdot, DR)
        uttex = SingleStringMathTex(r"\tilde u", color=COLOR_APPROXIMATION).next_to(utdot, UL, buff=0.1)

        line_dist = DashedLine(udot.get_center(), vdot.get_center(), color=[COLOR_SOLUTION, COLOR_LINEAR],
                               stroke_width=1).set_color_by_gradient(COLOR_SOLUTION, COLOR_LINEAR)

        line_dist2tu = DashedLine(udot.get_center(), utdot.get_center(), color=[COLOR_SOLUTION, COLOR_APPROXIMATION],
                                  stroke_width=1).set_color_by_gradient(COLOR_SOLUTION, COLOR_APPROXIMATION)

        # circ = Circle(radius=1.2 * np.sqrt(np.sum((udot.get_center() - utdot.get_center()) ** 2))).move_to(udot)
        # circ = (radius=1.2 * np.sqrt(np.sum((udot.get_center() - utdot.get_center()) ** 2))).move_to(udot)
        circ = Arc(arc_center=udot.get_center(),
                   radius=1.1 * np.sqrt(np.sum((udot.get_center() - utdot.get_center()) ** 2)),
                   start_angle=-PI / 2 - PI / 8,
                   angle=PI / 2, color=COLOR_APPROXIMATION,
                   stroke_width=1,
                   # fill_opacity=0.2
                   )
        # circ = VGroup(udot.copy(), circ).set_fill(color=COLOR_APPROXIMATION, opacity=0.2)

        line_c = Line(udot.get_center(), circ.get_corner(UR), color=[COLOR_APPROXIMATION, COLOR_APPROXIMATION],
                      stroke_width=1).set_color_by_gradient(COLOR_APPROXIMATION, COLOR_APPROXIMATION)

        c_text = SingleStringMathTex("C", color=COLOR_APPROXIMATION).move_to(line_c).shift(0.15 * UR)

        # -------------- -------------- -------------- #
        #   inverse problem
        self.next_slide()
        self.play(
            self.fade_out_old_elements(
                exept=[seeq, tex_z, yoda_img_old, yoda_pointwise_old, yoda_rec_img_old]),
            self.update_slide_number(),
            self.update_main_title(title),
            ReplacementTransform(seeq, rz),
            ReplacementTransform(tex_z, measurements),
            # ReplacementTransform(yoda_avg_old, yoda_avg),
            ReplacementTransform(yoda_pointwise_old, yoda_pointwise),
            ReplacementTransform(yoda_rec_img_old, yoda_rec),
            ReplacementTransform(yoda_img_old, yoda_img),
            # FadeIn(measurements, rz)
        )

        # -------------- -------------- -------------- #
        #   Best fit estimator
        title = Title(r"Best fit estimator", font_size=STITLE_FS)
        self.next_slide()
        self.play(
            self.update_main_title(title),
            Write(best_fit),
        )

        self.next_slide()
        self.play(
            FadeIn(yoda_rec_pointwise)
        )

        self.next_slide()
        self.play(
            FadeIn(yoda_diff_pointwise)
        )

        self.next_slide()
        imcpy = yoda_img.copy()
        self.add(imcpy)
        self.play(
            Create(udot),
            Create(utex),
        )
        self.play(
            FadeOut(imcpy, target_position=udot.get_center(), scale=0.2),
        )

        self.next_slide()
        imcpy = yoda_rec.copy()
        self.add(imcpy)
        self.play(
            Create(m_lin),
            Create(map_group["tex Vn space"]),
        )
        self.play(
            Create(utdot),
            Create(uttex),
        )
        self.play(
            FadeOut(imcpy, target_position=utdot.get_center(), scale=0.2),
        )

        # for n in subdivisions[1:]:
        #     yoda_rec_new = ImageMobject(Path(f"{path_subcell}/yoda_approx_{n}.png")).scale_to_fit_height(
        #         height_of_img).move_to(yoda_rec)
        #     yoda_rec_pointwise_new = ImageMobject(
        #         Path(f"{path_subcell}/yoda_approx_pointwise_{n}.png")).scale_to_fit_height(
        #         height_of_img).move_to(yoda_rec_pointwise)
        #     yoda_diff_pointwise_new = ImageMobject(
        #         Path(f"{path_subcell}/yoda_approx_diff_pointwise_{n}.png")).scale_to_fit_height(
        #         height_of_img).move_to(yoda_diff_pointwise)
        #     yoda_diff_new = ImageMobject(Path(f"{path_subcell}/yoda_approx_diff_{n}.png")).scale_to_fit_height(
        #         height_of_img).move_to(yoda_diff)
        #
        #     # self.next_slide()
        #     self.play(
        #         ReplacementTransform(yoda_rec, yoda_rec_new),
        #         ReplacementTransform(yoda_diff, yoda_diff_new),
        #         ReplacementTransform(yoda_rec_pointwise, yoda_rec_pointwise_new),
        #         ReplacementTransform(yoda_diff_pointwise, yoda_diff_pointwise_new),
        #     )
        #
        #     yoda_rec = yoda_rec_new
        #     yoda_rec_pointwise = yoda_rec_pointwise_new
        #     yoda_diff_pointwise = yoda_diff_pointwise_new
        #     yoda_diff = yoda_diff_new

        # -------------- -------------- -------------- #
        #   Near optimality property
        title = Title(r"Near optimality property", font_size=STITLE_FS)
        self.next_slide()
        self.play(
            self.update_main_title(title),
            Write(nop)
        )

        self.next_slide()
        self.play(
            FadeIn(yoda_diff)
        )

        self.next_slide()
        self.play(
            Create(line_dist2tu),
            FadeOut(yoda_diff, target_position=line_dist2tu.get_center(), scale=0.2),
        )

        self.next_slide()
        self.play(
            Create(vdot),
            Create(vtex),
            Create(line_dist),
        )

        self.next_slide()
        self.play(
            Create(circ),
            Create(line_c),
            Write(c_text)
        )

        # -------------- -------------- -------------- #
        #   PBDW
        title = Title(r"Parameterized Background Data Weak", font_size=STITLE_FS)
        self.next_slide()
        self.play(self.update_main_title(title), FadeIn(hilbert_cond), FadeOut(yoda_diff_pointwise))
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

        def points2circle(a, b, c):
            a, b, c = list(map(np.array, [a, b, c]))
            matrix = np.array([b - a,
                               c - a,
                               c - b])

            x0, y0, _ = np.linalg.lstsq(matrix,
                                        [(a + b) / 2 @ (b - a),
                                         (a + c) / 2 @ (c - a),
                                         (c + b) / 2 @ (c - b)],
                                        rcond=None)[0].tolist()
            return x0, y0, \
                (np.sqrt((a[0] - x0) ** 2 + (a[1] - y0) ** 2) +
                 np.sqrt((b[0] - x0) ** 2 + (b[1] - y0) ** 2) +
                 np.sqrt((c[0] - x0) ** 2 + (c[1] - y0) ** 2)) / 3

        # new_utdot_center = utdot.get_center()
        new_vdot_center = vdot.get_center() + 0.025 * (udot.get_center() - vdot.get_center())
        x0, y0, r = points2circle(new_vdot_center, utdot.get_center(),
                                  utdot.get_center() + 2 * (vdot.get_center() - utdot.get_center()))

        m_nnonlin = Arc(arc_center=np.array([x0, y0, 0]),
                        radius=r,
                        start_angle=PI / 2,
                        angle=2 * PI / 8 + PI / 16, color=NON_LINEAR_COLOR,
                        stroke_width=3,
                        # fill_opacity=0.2
                        )
        line_dist2 = DashedLine(udot.get_center(), new_vdot_center, color=[COLOR_SOLUTION, COLOR_APPROXIMATION],
                                stroke_width=1).set_color_by_gradient(COLOR_SOLUTION, COLOR_APPROXIMATION)

        self.play(
            ReplacementTransform(vnlinear_cond, vnnonlinear_cond),
            ReplacementTransform(m_lin, m_nnonlin),
            vdot.animate.move_to(new_vdot_center),
            ReplacementTransform(line_dist, line_dist2),
            vtex.animate.next_to(vdot, UP),
            Vn.animate.next_to(m_nnonlin, RIGHT, aligned_edge=UP),
        )
        # self.play(
        #     vtex.animate.next_to(vdot, RIGHT)
        # )
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
        # ========== ========== NOP proof ========== ========== #
        title = Title(r"Near optimality property for non-linear spaces", font_size=STITLE_FS)
        nop_plot = Group(m_lin, m_nnonlin, Vn, udot, vdot, utdot, uttex, uttex, vtex, line_dist2, line_dist2tu, circ,
                         line_c, c_text)
        manim_constants = Group(mu_def_2, alpha_def, beta_def)
        cite_ch2.next_to(nop_noise, DOWN)
        nopproof = ConceptNOPProof()
        nopproof.group.next_to(cite_ch2, DOWN).set_x(nop_noise.get_x(LEFT), direction=LEFT)

        # ------ auxiliary objects ------ #
        vertical_buffer = BUFF_QUARTER
        v_norm = get_sub_objects(new_nop, num_chars=list(range(7)))
        v_norm_new_line = get_sub_objects(list(nopproof.nop_proof_mobjs.values())[0], num_chars=list(range(7)))
        braceline_up = Line(v_norm.get_corner(DL), v_norm.get_corner(DR),
                            color=COLOR_SOLUTION, stroke_width=1).shift(
            vertical_buffer / 4 * DOWN)
        braceline_down = Line(v_norm_new_line.get_corner(UL),
                              v_norm_new_line.get_corner(UR), color=COLOR_SOLUTION,
                              stroke_width=1).shift(vertical_buffer / 4 * UP)

        self.next_slide()
        self.play(
            self.update_main_title(title), self.update_slide_number(),
            nop_plot.animate.shift(UL),
            manim_constants.animate.scale(0.75).move_to(Vn.get_corner(RIGHT), aligned_edge=LEFT).shift(UP),
            Create(braceline_up),
            Create(braceline_down),
        )
        self.play(
            *nopproof.get_action_001_start_nop_proof()
        )
        self.next_slide()
        self.play(
            *nopproof.get_action_002_triangular_inequality_in_V()
        )
        self.next_slide()
        self.play(
            *nopproof.get_action_003_inverse_stability()
        )
        self.next_slide()
        self.play(
            *nopproof.get_action_004_triangular_inequality_in_Z()
        )
        self.next_slide()
        self.play(
            *nopproof.get_action_005_best_fit_estimator_property()
        )
        self.next_slide()
        self.play(
            *nopproof.get_action_006_definition_of_z()
        )
        self.next_slide()
        self.play(
            *nopproof.get_action_007_lipschitz()
        )

        self.next_slide()
        self.play(Write(nop_noise), FadeOut(new_nop), FadeIn(cite_ch2),
                  braceline_up.animate.set_x(nop_noise.get_x(direction=LEFT), direction=LEFT),)
