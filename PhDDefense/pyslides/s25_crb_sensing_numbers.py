import json
import os

from PhDDefense.config import *
from pyslides.s07_intro_main_questions import kolmowidth
from lib.utils import MySlide, get_sub_objects

path_crb = Path(os.path.join(os.path.abspath(__file__).split("PhDDefense")[0], "PhDDefense", "Material", "CRB"))

with open(f"{path_crb}/metadata.json", "r") as file:
    info = json.load(file)


class SensingSlides(MySlide):

    def construct(self, objects_from_previous_slides):
        title = Title(r"Non-linear reduced basis", font_size=STITLE_FS)

        # -------------- -------------- -------------- #
        tex_kolmo = Tex("Kolmogorov n-width").next_to(title, DOWN, buff=BUFF_HALF).shift(TwoColumns_dx * LEFT)
        kolmowidth.next_to(tex_kolmo, DOWN, buff=BUFF_QUARTER)

        tex_sensing = Tex("Sensing numbers").next_to(title, DOWN, buff=BUFF_HALF).shift(TwoColumns_dx * RIGHT)
        sensing_numbers = MathTex(
            "s_n(\cM)_V:=\inf_{R,\ell_1,\dots,\ell_n} \max_{u\in\cM} \|u-R(\ell_1(u),\dots,\ell_n(u))\|_V,")
        sensing_numbers.next_to(tex_sensing, DOWN, buff=BUFF_QUARTER)
        get_sub_objects(sensing_numbers, [25, 29]).set_color(COLOR_SOLUTION)
        get_sub_objects(sensing_numbers, [33, 34, 35, 36, 37, 43, 44, 45, 46, 47, 13, 14, 20, 21]).set_color(
            COLOR_MEASUREMENTS)

        non_linear_space = MathTex(
            r"u_\mu (x) := "
            r"\Big\{"
            r"    \begin{array}{ll}"
            r"        b & \mbox{ for } x\in (a, a+\ell) \mbox{ (mod 1)} \\"
            r"        0 & \mbox{ for } x\in (a+\ell, a) \mbox{ (mod 1)} "
            r"    \end{array}"
            r", \quad \quad \mu=(a,\ell,b)"
        ).next_to(kolmowidth, DOWN, BUFF_HALF)

        fourier = MathTex(r"u_\mu=\sum_{k\in\N} \alpha_k \cos(2\pi k x) +  \sum_{k\in\N^*} \beta_k\sin(2\pi k x)",
                          tex_to_color_map={r"\alpha_k": COLOR_MEASUREMENTS, r"\beta_k": COLOR_MEASUREMENTS,
                                            r"\cos(2\pi k x)": COLOR_APPROXIMATION,
                                            r"\sin(2\pi k x)": COLOR_APPROXIMATION}, )
        fourier.next_to(sensing_numbers, DOWN, BUFF_HALF)
        non_linear_param_rec = MathTex(
            r" \left\{"
            r"\begin{array}{ll}"
            r"a+\frac \ell 2 &= -\frac 1 {\pi} {\rm arctan}(\frac {\beta_1}{\alpha_1})\\"
            r"\pi  b\sin(\pi\ell) &=(\alpha_1^2+\beta_1^2)^{1/2}\\"
            r"b\ell&= \alpha_0"
            r"    \end{array}"
            r"\right.",
            # tex_to_color_map={r"\beta_1": COLOR_MEASUREMENTS, r"\alpha_0": COLOR_MEASUREMENTS,
            #                   r"\alpha_1": COLOR_MEASUREMENTS, }
        ).next_to(fourier, DOWN, BUFF_HALF)
        get_sub_objects(non_linear_param_rec, [20, 21, 23, 24, 37, 39, 41, 43, -1, -2]).set_color(COLOR_MEASUREMENTS)

        linear_space = MathTex(
            r"R(\uu) &= P_{V_n} \uu \\",
            r"&= \sum_{i=1}^n \ell_i(u)\vi",
            tex_to_color_map={r"\uu": COLOR_SOLUTION, r"\vi": COLOR_APPROXIMATION, r"\ell_i(u)": COLOR_MEASUREMENTS}
        )
        # linear_space.next_to(Group(ci, non_linear_param_rec), DOWN, buff=BUFF_HALF)
        linear_space.next_to(non_linear_param_rec, DOWN, buff=BUFF_HALF)
        autoencoder_like = MathTex(
            r"R(\uu) &= P_{V_n} \uu + P_{V_{N-n}} \uu \\",
            r"&= \sum_{i=1}^n \ell_i(u)\vi + \sum_{j=1}^{N-n} \tilde \ell_{n+j}(u) v_j",
            tex_to_color_map={r"\uu": COLOR_SOLUTION, r"\vi": COLOR_APPROXIMATION, r"\ell_i(u)": COLOR_MEASUREMENTS,
                              # "\ell_{n+j}(u)": COLOR_MEASUREMENTS, r"v_j": COLOR_APPROXIMATION
                              }
        )
        autoencoder_like.move_to(linear_space, aligned_edge=LEFT)
        get_sub_objects(autoencoder_like, [-1, -2]).set_color(COLOR_APPROXIMATION)

        a = ValueTracker(0.2)
        b = ValueTracker(0.25)
        l = ValueTracker(0.4)
        x_range = (0, 1)
        scale = 3
        f = lambda x: b.get_value() * (
                sigmoid(1000 * (x - a.get_value())) -
                sigmoid(1000 * (x - l.get_value() * x_range[-1] - a.get_value())) +
                sigmoid(1000 * (x_range[-1] + x - a.get_value())) -
                sigmoid(1000 * (x_range[-1] + x - l.get_value() * x_range[-1] - a.get_value()))
        )
        ci = FunctionGraph(f, color=COLOR_PARAMS, x_range=x_range).next_to(non_linear_space, DOWN, BUFF_HALF).scale(
            scale)
        function_down = ci.get_edge_center(DOWN)
        ci.add_updater(
            lambda m: m.become(
                FunctionGraph(f, color=COLOR_PARAMS, x_range=x_range).scale(
                    scale).move_to(function_down, aligned_edge=DOWN)
            )
        )
        machin_lenin = MathTex(
            r"\tilde \ell_{n+j}(u) = \psi_\theta(\ell_1(u), \dots, \ell_n(u))").next_to(
            autoencoder_like, DOWN, BUFF_QUARTER)
        get_sub_objects(machin_lenin, list(range(8))).set_color([COLOR_APPROXIMATION, COLOR_MEASUREMENTS])
        get_sub_objects(machin_lenin, list(range(-6, -1)) + list(range(-16, -11))).set_color(COLOR_MEASUREMENTS)
        ltilda = get_sub_objects(autoencoder_like, [-10, -9, -8, -7, -6, -5, -4, -3])
        ltilda.set_color(COLOR_MEASUREMENTS)

        # ------ reminder of equation ------ #
        self.next_slide()
        self.play(
            self.fade_out_old_elements(),
            self.update_slide_number(),
            self.update_main_title(title),
        )

        self.next_slide()
        self.play(
            FadeIn(tex_kolmo),
            FadeIn(kolmowidth),
        )

        self.next_slide()
        self.play(
            FadeIn(tex_sensing),
            FadeIn(sensing_numbers),
        )

        self.next_slide()
        self.play(
            FadeIn(non_linear_space),
            FadeIn(ci),
        )

        self.next_slide()
        self.play(
            a.animate.set_value(0.4)
        )

        self.next_slide()
        self.play(
            b.animate.set_value(0.15)
        )

        self.next_slide()
        self.play(
            l.animate.set_value(0.5)
        )

        self.next_slide()
        self.play(
            FadeIn(fourier),
        )

        self.next_slide()
        self.play(
            FadeIn(non_linear_param_rec),
        )

        self.next_slide()
        self.play(
            FadeIn(linear_space),
        )

        self.next_slide()
        self.play(
            FadeOut(linear_space),
            FadeIn(autoencoder_like),
        )

        self.next_slide()
        self.play(
            Indicate(ltilda, 2),
        )
        self.play(
            ltilda.animate.set_color([COLOR_APPROXIMATION, COLOR_MEASUREMENTS]),
            FadeIn(machin_lenin, target_position=ltilda.get_center(), scale=0.25)
        )

        # -------------- Reconstructions -------------- #
        scale = 3.75
        kplotNull = (ImageMobject(f"{path_crb}/Null_vn_familya_0_1_b_0_1_n_train1000_m3")
                     .scale_to_fit_height(scale).next_to(non_linear_space, DOWN, BUFF_QUARTER))
        kplot1000 = (ImageMobject(f"{path_crb}/k_plot_vn_familya_0_1_b_0_1_n_train1000_m3")
                     .scale_to_fit_height(scale).move_to(kplotNull))
        kplot10000 = (ImageMobject(f"{path_crb}/k_plot_vn_familya_0_1_b_0_1_n_train10000_m3")
                      .scale_to_fit_height(scale).move_to(kplotNull))

        self.next_slide()
        self.play(
            FadeOut(ci),
        )
        self.play(
            FadeIn(kplotNull)
        )

        self.next_slide()
        self.play(
            FadeOut(kplotNull),
            FadeIn(kplot1000)
        )

        self.next_slide()
        self.add(kplot10000)
        self.play(
            FadeOut(kplot1000),
            # FadeIn(kplot10000)
        )

        # scale = 3.0
        # rf_color = RED
        # null_color = YELLOW
        # nx = len(info["null"][0])
        # mo_ground_truth = Group(
        #     *[Dot(np.array([i / nx, s, 0]) * scale, radius=0.01, color=WHITE) for i, s in
        #       enumerate(info["ground_truth"][0])])
        # mo_null = Group(
        #     *[Dot(np.array([i / nx, s, 0]) * scale, radius=0.01, color=null_color) for i, s in
        #       enumerate(info["null"][0])])
        # mo_tree = Group(
        #     *[Dot(np.array([i / nx, s, 0]) * scale, radius=0.01, color=rf_color) for i, s in
        #       enumerate(info["RF"]["1000"][0])])
        # group = Group(mo_ground_truth, mo_null, mo_tree).set_y(autoencoder_like.get_y(DOWN), DOWN).set_x(ci.get_x())
        #
        # self.play(
        #     FadeIn(group),
        # )

        # [Line(s, e) for s, e in zip(info["null"][0][:-1], info["null"][0][:-1])]

        # fourier_coefs = [ValueTracker(v) for v in info["null"][0]]
        #
        # # print(info["Null"]["1000"][0])
        # f_tree = lambda x: np.sum(
        #     [v.get_value() * ((np.cos if j % 2 else np.sin)(2 * np.pi * x * j) if j > 0 else 1) for j, v in
        #      enumerate(fourier_coefs)])
        # mo_tree = FunctionGraph(f_tree, color=COLOR_PARAMS, x_range=x_range).next_to(ci, DOWN, BUFF_ONE).scale(scale)
        # tree_down = mo_tree.get_edge_center(DOWN)
        # mo_tree.add_updater(
        #     lambda m: m.become(
        #         FunctionGraph(f_tree, color=COLOR_PARAMS, x_range=x_range).scale(
        #             scale).move_to(tree_down, aligned_edge=DOWN)
        #     )
        # )

        # who2animate = [None, 0, 2, 1]
        # for i, values in enumerate(zip(info["a"], info["b"], info["delta"])):
        #     self.next_slide()
        #     if who2animate[i] is not None:
        #         self.play(
        #             [a, b, l][who2animate[i]].animate.set_value(values[who2animate[i]]),
        #         )
        #     else:
        #         self.play(
        #             FadeIn(group),
        #         )

        # l.animate.set_value(lval),

        # self.next_slide()
        # self.play(FadeIn(Dot(100*UP)))

        # alpha = [ValueTracker(0.2) for ]
        # beta = ValueTracker(0.25)
        # l = ValueTracker(0.4)
        # x_range = (0, 1)
        # scale = 3
        # f = lambda x: b.get_value() * (
        #         sigmoid(1000 * (x - a.get_value())) -
        #         sigmoid(1000 * (x - l.get_value() * x_range[-1] - a.get_value())) +
        #         sigmoid(1000 * (x_range[-1] + x - a.get_value())) -
        #         sigmoid(1000 * (x_range[-1] + x - l.get_value() * x_range[-1] - a.get_value()))
        # )
        # ci = FunctionGraph(f, color=COLOR_PARAMS, x_range=x_range).next_to(non_linear_space, DOWN, BUFF_HALF).scale(
        #     scale)
        # function_down = ci.get_edge_center(DOWN)
        # ci.add_updater(
        #     lambda m: m.become(
        #         FunctionGraph(f, color=COLOR_PARAMS, x_range=x_range).scale(
        #             scale).move_to(function_down, aligned_edge=DOWN)
        #     )
        # )

        # family_ab3 = ImageMobject(f"{path_crb}/k_plot_vn_familya_0_1_b_0_1_n_train1000_m3").scale_to_fit_height(2)
        # family_ab3.next_to(ci, DOWN, buff=BUFF_HALF)
        # family_ab4 = ImageMobject(f"{path_crb}/k_plot_vn_familya_0_1_b_0_1_n_train10000_m3").scale_to_fit_height(2)
        # family_ab4.move_to(family_ab3)
        # self.next_slide()
        # self.play(
        #     FadeIn(family_ab3)
        # )
        # self.next_slide()
        # self.play(
        #     FadeOut(family_ab3),
        #     FadeIn(family_ab4),
        #     self.update_slide_number()
        # )
