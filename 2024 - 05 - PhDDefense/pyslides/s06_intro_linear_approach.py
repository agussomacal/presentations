from functools import partial

from PhDDefense.config import *
from PhDDefense.pyslides.s04_intro_two_problems import get_Yshape_object, DOMAIN_FILL_OPACITY
from PhDDefense.pyslides.s05_intro_solution_manifold import buff_images, solution_manifold, \
    linear_approx
from lib.utils import MySlide, get_sub_objects

COLOR_MATRIX = YELLOW
COLOR_VECTOR = PURPLE


class LinearApproachSlides(MySlide):

    def construct(self, objects_from_previous_slides):
        title = Title(r"Linear approaches", font_size=STITLE_FS)
        if "map_group" in objects_from_previous_slides:
            map_group = objects_from_previous_slides["map_group"]
        else:
            fmeq = MathTex(r"y \in Y \mapsto u \in V", substrings_to_isolate=["y", "u"],
                           tex_to_color_map={"y": COLOR_PARAMS, "u": COLOR_SOLUTION},
                           font_size=MEDIUM_FS).next_to(title, DOWN)
            Y = (get_Yshape_object(fill_color=COLOR_PARAMS, fill_opacity=DOMAIN_FILL_OPACITY)
                 .next_to(fmeq, DOWN, buff=buff_images).shift(2 * LEFT))
            manifold = (ParametricFunction(solution_manifold, t_range=np.array([0, 1]), fill_opacity=0.5)
            .set_color(COLOR_SOLUTION).set_stroke(width=0.5).next_to(Y, ORIGIN, buff=0).shift(
                2 * Y.get_x() * LEFT))
            m_lin = ParametricFunction(function=partial(linear_approx, p=np.array([0, 0]), v=np.array([1, 2])),
                                       t_range=[-0.5, 2.5], color=COLOR_LINEAR).move_to(manifold)
            map_group = VDict(
                {"map_eq": fmeq, "Y space": Y, "solution manifold": manifold, "linear space": m_lin, })

        # -------------- -------------- -------------- #
        # parametric_expansion = MathTex(r"\tilde u=\sum_{|\nu| \leq k} u_\nu y^\nu", font_size=MEDIUM_FS)
        # parametric_expansion = MathTex(r"\tilde u=\sum_{\mu \in \mathcal{A}}^n u_\mu y^\mu", font_size=MEDIUM_FS)
        # parametric_expansion = (parametric_expansion
        #                         .next_to(title, DOWN, buff=BUFF_SUBTITLES)).shift(ThreeColumns_dx / 6 * RIGHT)
        tex_to_color_dict = {r"\tu": COLOR_APPROXIMATION, r"\vi": COLOR_APPROXIMATION, r"\vk": COLOR_APPROXIMATION,
                             r"\zj": COLOR_MEASUREMENTS, r"\ci": COLOR_LINEAR, r"\y": COLOR_PARAMS}
        tex_to_color_map = {"tex_to_color_map": tex_to_color_dict}
        vnspace = MathTex(r"V_n:=\text{span}\{ v_1, \dots, v_n \}",
                          substrings_to_isolate=[r"v_1", r"v_n", r"v_i", r"V_n"],
                          tex_to_color_map={r"v_1": COLOR_APPROXIMATION, r"v_n": COLOR_APPROXIMATION,
                                            r"v_i": COLOR_APPROXIMATION, r"V_n": COLOR_LINEAR},
                          font_size=EQ_FONT_SIZE)
        linear_combination = MathTex(r"\tu =\sum_{i=1}^n \ci \vi", font_size=MEDIUM_FS, **tex_to_color_map,
                                     substrings_to_isolate=list(tex_to_color_dict.keys()))
        linear_combination.next_to(vnspace, DOWN, buff=BUFF_HALF)

        # -------------- -------------- -------------- #
        galerkin_proj = Tex(r"Forward modelling: \\ Galerkin projection", font_size=EQ_FONT_SIZE,
                            color=FM_COLOR).next_to(title, DOWN, buff=BUFF_ONE * 3 / 4).shift(
            ThreeColumns_dx / 2 * RIGHT)
        gproj_eq1 = MathTex(r"\int_\Omega a(x,\y) \nabla u \nabla v dx = \int_\Omega fv dx",
                            font_size=EQ_FONT_SIZE).next_to(galerkin_proj, DOWN)
        get_sub_objects(gproj_eq1, [6]).set_color(COLOR_PARAMS)
        galerkin_u = get_sub_objects(gproj_eq1, [9]).set_color(COLOR_SOLUTION)
        gproj_eq2 = (MathTex(
            r"\int_\Omega a(x,\y) \nabla \left(\sum_{i=1}^n \ci \vi \right) \nabla \vk dx = \int_\Omega f\vk dx",
            font_size=EQ_FONT_SIZE, **tex_to_color_map, substrings_to_isolate=list(tex_to_color_dict.keys()))
                     .next_to(galerkin_proj, DOWN))
        gproj_eq3 = MathTex(r"\sum_{i=1}^n \ci \int_\Omega a(x,\y) \nabla \vi \nabla \vk dx = \int_\Omega f\vk dx",
                            font_size=EQ_FONT_SIZE, **tex_to_color_map,
                            substrings_to_isolate=list(tex_to_color_dict.keys())).next_to(galerkin_proj, DOWN)
        tex_to_color_dict_galerking = {r"\int_\Omega a(x,": COLOR_MATRIX,
                                       r") \nabla \vi \nabla \vk dx": COLOR_MATRIX, r"\y": COLOR_PARAMS,
                                       r"\int_\Omega f\vk dx": COLOR_VECTOR, r"\ci": COLOR_LINEAR}
        gproj_eq3_bis = MathTex(r"\sum_{i=1}^n \ci \int_\Omega a(x,\y) \nabla \vi \nabla \vk dx = \int_\Omega f\vk dx",
                                font_size=EQ_FONT_SIZE,
                                tex_to_color_map=tex_to_color_dict_galerking,
                                substrings_to_isolate=list(tex_to_color_dict_galerking.keys())).next_to(galerkin_proj,
                                                                                                        DOWN)

        tex_to_color_dict_galerking = {r"A": COLOR_MATRIX, r"\y": COLOR_PARAMS,
                                       r"b": COLOR_VECTOR, "c": COLOR_LINEAR}
        gproj_eq4 = (MathTex(r"A(\y)c=b, \quad A(\y)\in \R^{N\times N}", font_size=EQ_FONT_SIZE,
                             tex_to_color_map=tex_to_color_dict_galerking,
                             substrings_to_isolate=list(tex_to_color_dict_galerking.keys()))
                     .next_to(gproj_eq3, DOWN))
        gproj_eq4_nxn = (MathTex(r"A(\y)c=b, \quad A(\y)\in \R^{n\times n}", font_size=EQ_FONT_SIZE,
                                 tex_to_color_map=tex_to_color_dict_galerking,
                                 substrings_to_isolate=list(tex_to_color_dict_galerking.keys()))
                         .next_to(gproj_eq3, DOWN))
        rom = Tex("ROM $n \ll N$ FEM", font_size=EQ_FONT_SIZE).next_to(gproj_eq4, RIGHT, buff=0.25)
        fem = Tex("$1 \ll N$ FEM", font_size=EQ_FONT_SIZE).move_to(rom, aligned_edge=RIGHT)

        # -------------- -------------- -------------- #
        ell2proj = Tex(r"State estimation: \\ best fit estimator", font_size=EQ_FONT_SIZE,
                       color=INV_COLOR).next_to(gproj_eq4, DOWN, buff=BUFF_ONE * 3 / 4)
        iproj_eq1 = MathTex(r"\ell_j(\tu ) \approx \zj", **tex_to_color_map,
                            substrings_to_isolate=list(tex_to_color_dict.keys()),
                            font_size=EQ_FONT_SIZE).next_to(ell2proj, DOWN, buff=BUFF_HALF)
        iproj_eq2 = MathTex(r"\ell_j \left(\sum_{i=1}^n \ci \vi \right) \approx \zj", **tex_to_color_map,
                            substrings_to_isolate=list(tex_to_color_dict.keys()),
                            font_size=EQ_FONT_SIZE).move_to(iproj_eq1)
        iproj_eq3 = MathTex(r"\sum_{i=1}^n \ci\ell_j( \vi )\approx \zj", **tex_to_color_map,
                            substrings_to_isolate=list(tex_to_color_dict.keys()),
                            font_size=EQ_FONT_SIZE).move_to(iproj_eq2)

        tex_to_color_dict_galerking = {r"\ell_j( \vi )": COLOR_MATRIX,
                                       r"\zj": COLOR_MEASUREMENTS, r"\ci": COLOR_LINEAR}
        iproj_eq3_bis = MathTex(r"\sum_{i=1}^n \ci\ell_j( \vi )\approx \zj",
                                tex_to_color_map=tex_to_color_dict_galerking,
                                substrings_to_isolate=list(tex_to_color_dict_galerking.keys()),
                                font_size=EQ_FONT_SIZE).move_to(iproj_eq2)
        iproj_eq4 = MathTex(r"Lc \approx z, \quad L\in \R^{m\times n}",
                            tex_to_color_map={"z": COLOR_MEASUREMENTS, "L": COLOR_APPROXIMATION, "c": COLOR_LINEAR},
                            substrings_to_isolate=["z", "L"], font_size=EQ_FONT_SIZE).next_to(iproj_eq3, DOWN)
        iproj_eq5 = (MathTex(r"L^TLc = L^Tz",
                             tex_to_color_map={r"L^Tz": COLOR_VECTOR, r"L^TL": COLOR_MATRIX, "c": COLOR_LINEAR},
                             substrings_to_isolate=[r"L^Tz", "L^TL", "c"], font_size=EQ_FONT_SIZE)
                     .next_to(iproj_eq4, DOWN, BUFF_HALF))

        # -------------- -------------- -------------- #
        # SLIDE: Linear method presentation
        # -------------- -------------- -------------- #
        self.next_slide()
        self.play(
            self.fade_out_old_elements(),
            map_group.animate.shift(ThreeColumns_dx * LEFT).scale(0.8),
            self.update_slide_number(),
            self.update_main_title(title)
        )

        Group(vnspace, linear_combination).next_to(map_group, DOWN,
                                                   buff=BUFF_HALF)  # .set_x(-ThreeColumns_dx).set_y(-H / 2)
        self.next_slide()
        self.play(
            Write(vnspace),
            Write(linear_combination)
        )
        # map_group = map_group.add(vnspace, linear_combination)

        # -------------- -------------- -------------- #
        # galerkin projection
        self.next_slide()
        self.play(
            Write(galerkin_proj),
            Write(gproj_eq1)
        )

        self.next_slide()
        self.play(
            Indicate(galerkin_u),
            FadeOut(linear_combination.copy(), target_position=galerkin_u.get_center())
        )
        self.play(
            ReplacementTransform(gproj_eq1, gproj_eq2)
        )

        self.next_slide()
        self.play(
            ReplacementTransform(gproj_eq2, gproj_eq3)
        )

        self.next_slide()
        self.play(
            ReplacementTransform(gproj_eq3, gproj_eq3_bis),
            Write(gproj_eq4),
            Write(fem)
        )

        self.next_slide()
        self.play(
            ReplacementTransform(fem, rom),
            ReplacementTransform(gproj_eq4, gproj_eq4_nxn),
        )

        # -------------- -------------- -------------- #
        # ell2 projection
        self.next_slide()
        self.play(
            Write(ell2proj),
            Write(iproj_eq1)
        )

        self.next_slide()
        uinvpr = get_sub_objects(iproj_eq1, [4])
        self.play(
            Indicate(uinvpr),
            FadeOut(linear_combination.copy(), target_position=uinvpr.get_center())
        )
        self.play(
            ReplacementTransform(iproj_eq1, iproj_eq2)
        )

        self.next_slide()
        self.play(
            ReplacementTransform(iproj_eq2, iproj_eq3)
        )

        self.next_slide()
        self.play(
            ReplacementTransform(iproj_eq3, iproj_eq3_bis),
            Write(iproj_eq4)
        )

        self.next_slide()
        self.play(
            Write(iproj_eq5),
        )

        return {"map_group": map_group, "linear_combination": linear_combination, "vnspace": vnspace}

# # -------------- -------------- -------------- #
# # SLIDE 8: Projections
# # -------------- -------------- -------------- #
# self.next_slide()
#
# linear_model = (MathTex(r"u\approx \tilde u=\sum_{i=1}^n c_iv_i", font_size=MEDIUM_FS)
#                 .next_to(self.get_title_mobject(), DOWN, buff=1, aligned_edge=UP))
# self.play(
#     self.fade_out_old_elements(),
#     FadeIn(solution, target_position=previous_slide_solution),
#     FadeIn(linear_model),
#     self.update_slide_number(),
#     self.update_main_title(r"Linear approach"),
# )
#
# solutions_vi = []
# for i in range(2, num_snapshots - 2):
#     solutions_vi.append(get_diff_eq_images(name="solutions", i=i, scale=0.8, format="png"))
#     vi = linear_model[-1]
#     self.play(Indicate(vi), FadeIn(solutions_vi[-1], target_position=Ytextobj, scale=0.5))
#
# # -------------- -------------- -------------- #
# # V projection
# self.next_slide()
# vproj = Tex(r"$V$ projection", font_size=MEDIUM_FS, color=PDE_COLOR).next_to(linear_model, DOWN, buff=1,
#                                                                              aligned_edge=UP).shift(
#     ThreeColumnsCenter * LEFT)
# # vproj_eq = Tex("\\justifying{$\\tilde u=P_{V_n}u$\\\ $P_{V_n}=\sum_{i=1}^n \\langle u, v_i \\rangle_V v_i$ }",
# #                font_size=MEDIUM_FS, tex_template=myBaseTemplate).next_to(vproj, DOWN)
# vproj_eq = MathTex(r"\ci=\langle u, v_i \rangle_V",
#                    font_size=EQ_FONT_SIZE).next_to(vproj, DOWN)
#
# self.play(
#     FadeIn(vproj, vproj_eq)
# )
