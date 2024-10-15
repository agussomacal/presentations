from functools import partial

from PhDDefense.config import *
from PhDDefense.pyslides.s04_intro_two_problems import get_Yshape_object, DOMAIN_FILL_OPACITY
from PhDDefense.pyslides.s05_intro_solution_manifold import buff_images, solution_manifold, \
    linear_approx
from lib.utils import get_info2color_from_dict, MySlide

kolmowidth = MathTex(
    r"d_n(\cM)_V = \inf_{V_n, \; \dim(V_n)=n} \text{dist}(\cM, V_n)_V",
    **get_info2color_from_dict({r"\vv": COLOR_APPROXIMATION, r"V_n": COLOR_LINEAR})
)
kolmowidth[0][3].set_color(COLOR_SOLUTION)
kolmowidth[-3][8].set_color(COLOR_SOLUTION)

class MainQuestionsSlides(MySlide):

    def construct(self, objects_from_previous_slides):
        title = Title(r"Main questions", font_size=STITLE_FS)
        # "map_group": VGroup(fmeqcM, Y, manifold, m_lin, Vn, cM)
        if "map_group" in objects_from_previous_slides:
            map_group = objects_from_previous_slides["map_group"]
            linear_combination = objects_from_previous_slides["linear_combination"]
            vnspace = objects_from_previous_slides["vnspace"]
        else:
            fmeq = MathTex(r"y \in Y \mapsto u \in V", substrings_to_isolate=["y", "u"],
                           tex_to_color_map={"y": COLOR_PARAMS, "u": COLOR_SOLUTION},
                           font_size=MEDIUM_FS).next_to(title, DOWN)
            Y = get_Yshape_object(fill_color=COLOR_PARAMS, fill_opacity=DOMAIN_FILL_OPACITY).next_to(fmeq, DOWN,
                                                                                                     buff=buff_images).shift(
                2 * LEFT)
            manifold = (ParametricFunction(solution_manifold, t_range=np.array([0, 1]), fill_opacity=0.5)
            .set_color(COLOR_SOLUTION).set_stroke(width=0.5).next_to(Y, ORIGIN, buff=0).shift(
                2 * Y.get_x() * LEFT))
            m_lin = ParametricFunction(function=partial(linear_approx, p=np.array([0, 0]), v=np.array([1, 2])),
                                       t_range=[-0.5, 2.5], color=COLOR_LINEAR).move_to(manifold)
            map_group = VGroup(fmeq, Y, manifold, m_lin).shift(ThreeColumns_dx * LEFT).scale(0.8)
            self.remove_old_elements()
            self.add(map_group)

        # -------------- -------------- -------------- #
        #   main questions
        questions_1 = Tex(r'For a given problem (parametric PDE):',
                          r'\begin{enumerate}'
                          '\item What can we achieve with optimally chosen \\ linear spaces?'
                          '\item Is it enough?'
                          '\item Can we do better with non-linear spaces?'
                          '\end{enumerate}',
                          tex_environment="flushleft",
                          tex_to_color_map={"parametric": COLOR_PARAMS, "PDE": PDE_COLOR},
                          # "linear": LINEAR_COLOR, "non-linear": NON_LINEAR_COLOR
                          font_size=EQ_FONT_SIZE)
        # self.add(*list(map(index_labels, questions_1)))
        questions_1.next_to(vnspace, RIGHT, buff=BUFF_ONE)

        tex_to_color_dict = {r"\vv": COLOR_APPROXIMATION, r"\uu": COLOR_SOLUTION, r"V_n": COLOR_LINEAR,
                             r"\cM": PDE_COLOR}

        projection = MathTex(r"\|\uu-P_{V_n} \uu\|_V = \min_{\vv\in V_n} \|\uu-\vv\|_V",
                             **get_info2color_from_dict(tex_to_color_dict))
        projection.next_to(title, DOWN, buff=BUFF_HALF).set_x(ThreeColumns_dx / 2)

        tex_to_color_dict = {r"\vv": COLOR_APPROXIMATION, r"V_n": COLOR_LINEAR}
        manifold_distance = MathTex(
            r"\dist(\cM, V_n)_V = \max_{\uu \in \cM } \min_{\vv \in V_n} \|\uu-\vv\|_V",
            **get_info2color_from_dict(tex_to_color_dict),
        ).next_to(projection, DOWN, buff=BUFF_HALF)
        manifold_distance[0][5].set_color(COLOR_SOLUTION)
        manifold_distance[2][6].set_color(COLOR_SOLUTION)
        manifold_distance[2][8].set_color(COLOR_SOLUTION)
        manifold_distance[-3][1].set_color(COLOR_SOLUTION)


        kolmowidth.next_to(manifold_distance, DOWN, buff=BUFF_HALF)

        Group(projection, manifold_distance, kolmowidth).set_y(CENTER_Y)

        # -------------- -------------- -------------- #
        #   main questions
        self.next_slide()
        self.play(
            self.fade_out_old_elements(exept=[map_group, linear_combination, vnspace]),
            self.update_slide_number(),
            self.update_main_title(title)
        )
        self.play(
            FadeIn(questions_1),
        )

        # self.add(*list(map(index_labels, manifold_distance)))
        # self.add(*list(map(index_labels, kolmowidth)))
        # -------------- -------------- -------------- #
        #   Manifold distance: Vn space
        title = Title(r"Distance to manifold", font_size=STITLE_FS)
        radius = DEFAULT_DOT_RADIUS * 0.5
        VT_dict = {c: ValueTracker(v) for c, v in zip("xyz", map_group["tex cM"].get_center())}
        VT_dict["x"] -= 1
        VT_dict["y"] += 1
        upos = get_values_from_VTracker_dict(VT_dict, ["x", "y", "z"], return_np_array=True)

        udot = Dot(upos, radius=radius, color=COLOR_SOLUTION)
        udot.add_updater(
            lambda dot: dot.become(
                Dot(
                    get_values_from_VTracker_dict(VT_dict, ["x", "y", "z"], return_np_array=True)
                    , radius=radius, color=COLOR_SOLUTION
                )
            )
        )

        vdot = Dot(map_group["linear space"].get_projection(upos), radius=radius, color=COLOR_APPROXIMATION)
        vdot.add_updater(
            lambda dot: dot.become(
                Dot(
                    map_group["linear space"].get_projection(
                        get_values_from_VTracker_dict(VT_dict, ["x", "y", "z"], return_np_array=True)),
                    radius=radius, color=COLOR_APPROXIMATION,
                )
            )
        )

        utex = SingleStringMathTex("u", color=COLOR_SOLUTION).next_to(udot)
        utex.add_updater(lambda u: u.become(SingleStringMathTex("u", color=COLOR_SOLUTION).next_to(udot)))
        vtex = SingleStringMathTex("v", color=COLOR_APPROXIMATION).next_to(vdot)
        vtex.add_updater(lambda u: u.become(SingleStringMathTex("v", color=COLOR_APPROXIMATION).next_to(vdot)))
        line_dist = DashedLine(udot.get_center(), vdot.get_center(), color=[COLOR_SOLUTION, COLOR_APPROXIMATION],
                               stroke_width=1).set_color_by_gradient(COLOR_SOLUTION, COLOR_APPROXIMATION)
        line_dist.add_updater(lambda u: u.become(
            DashedLine(udot.get_center(), vdot.get_center(), color=[COLOR_SOLUTION, COLOR_APPROXIMATION],
                       stroke_width=1).set_color_by_gradient(COLOR_SOLUTION, COLOR_APPROXIMATION)))
        tex_dist = MathTex(r"\dist(\cM, V_n)_V",
                           tex_to_color_map={r"\cM": COLOR_SOLUTION, r"V_n": COLOR_LINEAR},
                           substrings_to_isolate=[r"\cM", r"V_n"]).next_to(line_dist, LEFT)
        tex_dist.add_updater(
            lambda u: u.become(MathTex(r"\dist(\cM, V_n)_V",
                                       tex_to_color_map={r"\cM": COLOR_SOLUTION, r"V_n": COLOR_LINEAR},
                                       substrings_to_isolate=[r"\cM", r"V_n"]).next_to(vdot, LEFT).shift(
                (udot.get_center() - vdot.get_center()) / 2)))
        map_group["tex Vn space"].add_updater(
            lambda u: u.become(SingleStringMathTex("V_n", color=COLOR_LINEAR).next_to(map_group["linear space"], UR))
        )

        # -------------- -------------- -------------- #
        #   Manifold distance: projection
        self.next_slide()
        self.play(
            self.update_slide_number(),
            self.update_main_title(title),
            FadeOut(questions_1),
        )
        self.play(Write(projection))

        i = 5
        se_scale = 0.37
        # solution = get_diff_eq_images("state_estimation_solutions_points", i, scale=se_scale).move_to(solution_coord)
        # state_estimation = get_diff_eq_images("state_estimation", i, scale=se_scale).move_to(state_estimation)
        self.next_slide()
        self.play(
            Create(udot),
            Write(utex),
        )

        self.next_slide()
        self.play(
            Create(vdot),
            Write(vtex),
        )

        self.next_slide()
        self.play(
            VT_dict["x"].animate.increment_value(-1),
            VT_dict["y"].animate.increment_value(-0.5),
            Create(line_dist),
        )

        # -------------- -------------- -------------- #
        #   Manifold distance
        ls_center = map_group["linear space"].get_center()
        ls_lenght = map_group["linear space"].width
        theta = ValueTracker(np.arctan(0.5))
        Vn_y = ValueTracker(0)
        map_group["linear space"].add_updater(
            lambda dot: dot.become(
                Line(start=np.array([0, 0, 0]), end=ls_lenght / 0.8 * np.array([1, np.tan(theta.get_value()), 0]),
                     color=COLOR_LINEAR).scale(0.8).move_to(ls_center).shift(Vn_y.get_value() * UP)
            )
        )
        map_group["tex Vn space"].add_updater(
            lambda u: u.become(SingleStringMathTex("V_n", color=COLOR_LINEAR).next_to(map_group["linear space"], (
                UR if theta.get_value() > 0 else DR)))
        )

        T = np.linspace(0, 1, num=1000)
        boundary = [Dot(solution_manifold(t, 1)) for t in T]
        Group(*boundary).scale(0.8).move_to(map_group["solution manifold"])
        boundary_projection = lambda line: boundary[
            np.argmax([np.sum((dot.get_center() - line.get_projection(dot.get_center())) ** 2) for dot in
                       boundary])].get_center()
        udot_mdist = Dot(boundary_projection(map_group["linear space"]), radius=radius, color=COLOR_APPROXIMATION)
        udot_mdist.add_updater(
            lambda dot: dot.become(
                Dot(
                    boundary_projection(map_group["linear space"]),
                    radius=radius, color=COLOR_SOLUTION,
                )
            )
        )

        self.next_slide()
        self.play(
            Write(manifold_distance),
            VT_dict["x"].animate.set_value(udot_mdist.get_x()),
            VT_dict["y"].animate.set_value(udot_mdist.get_y()),
            ReplacementTransform(udot, udot_mdist),
            Write(tex_dist),
        )

        utex.add_updater(lambda u: u.become(SingleStringMathTex("u", color=COLOR_SOLUTION).next_to(udot_mdist)))
        vdot.add_updater(
            lambda dot: dot.become(
                Dot(
                    map_group["linear space"].get_projection(udot_mdist.get_center()),
                    radius=radius, color=COLOR_APPROXIMATION,
                )
            )
        )

        line_dist.add_updater(lambda u: u.become(
            DashedLine(udot_mdist.get_center(), vdot.get_center(),
                       stroke_width=1).set_color_by_gradient(COLOR_SOLUTION, COLOR_APPROXIMATION)))
        tex_dist.add_updater(
            lambda u: u.become(MathTex(r"\dist(\cM, V_n)_V",
                                       tex_to_color_map={r"\cM": COLOR_SOLUTION, r"V_n": COLOR_LINEAR},
                                       substrings_to_isolate=[r"\cM", r"V_n"]).next_to(vdot, LEFT).shift(
                (udot_mdist.get_center() - vdot.get_center()) / 2)))

        self.next_slide()
        self.play(
            theta.animate.increment_value(-20 / 180 * np.pi),
            # Vn_y.animate.increment_value(0.5),
            run_time=2
        )

        # -------------- -------------- -------------- #
        #   Kolmogorov width
        self.next_slide()
        title = Title(r"Kolmogorov width", font_size=STITLE_FS)

        # N = 1000
        # minx, miny = np.min([dot.get_center()[:2] for dot in boundary], axis=0)
        # maxx, maxy = np.max([dot.get_center()[:2] for dot in boundary], axis=0)
        # [(x, y) for x, y in itertools.product(np.linspace(minx, maxx, num=N), np.linspace(miny, maxy, num=N)) if ]

        # boundary = [Dot(solution_manifold(t, 1)) for t in T]

        self.play(
            self.update_main_title(title),
            Write(kolmowidth),
        )

        self.next_slide()
        self.play(
            theta.animate.increment_value(30 / 180 * np.pi),
            Vn_y.animate.increment_value(-0.05),
            run_time=1.5
        )
        self.play(
            theta.animate.increment_value(-10 / 180 * np.pi),
            Vn_y.animate.increment_value(0.05),
            run_time=1.5
        )
        self.play(
            theta.animate.increment_value(5 / 180 * np.pi),
            Vn_y.animate.increment_value(0.05),
            run_time=1.5
        )

        tex_kolmo = MathTex(r"d_n(\cM)_V",
                            tex_to_color_map={r"\cM": COLOR_SOLUTION},
                            substrings_to_isolate=[r"\cM"]).move_to(tex_dist)
        line_dist_undash = Line(udot_mdist.get_center(), vdot.get_center(), color=[COLOR_SOLUTION, COLOR_APPROXIMATION],
                                stroke_width=2).set_color_by_gradient(COLOR_SOLUTION, COLOR_APPROXIMATION)
        self.play(
            Unwrite(tex_dist),
            Write(tex_kolmo),
            ReplacementTransform(line_dist, line_dist_undash),

        )

        return {"kolmowidth": kolmowidth}
