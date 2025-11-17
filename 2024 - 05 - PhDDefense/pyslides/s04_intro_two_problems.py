import json
import os.path

from PhDDefense.config import *
from lib.utils import MySlide, create_grid_of_colored_rectangles

DOMAIN_STROKE_WIDTH = 2.5
DOMAIN_FILL_OPACITY = 0.4

# =============== =============== =============== =============== #
#              Diffusion equation data and functions              #
# =============== =============== =============== =============== #

path = Path(os.path.join(os.path.abspath(__file__).split("PhDDefense")[0], "PhDDefense", "Material", "DiffEq"))
with open(f"{path}/metadata.json", "r") as f:
    d = json.load(f)
    infty_subdomains = d.pop("infty_subdomains")
    num_snapshots = d.pop("num_snapshots")
    number_of_measures = d.pop("number_of_measures")
    vdim = d.pop("Vdim")
    parameters_ls_dict = d.pop("parameters_ls_dict")
    parameters_inf_dict = d.pop("parameters_inf_dict")
    parameters_dict = d.pop("parameters_dict")
    num_snapshots_optim = d.pop("num_snapshots_optim")
    parameters_optim_dict = d.pop("parameters_optim_dict")
    parameters_se_dict = d.pop("parameters_se_dict")
    parameters_avg_dict = d.pop("parameters_avg_dict")
    num_cells_per_dim = d.pop("num_cells_per_dim")
    sub_sampling = d.pop("sub_sampling")


def get_diff_eq_images(name, i=None, scale=0.8, format="png"):
    solution = ImageMobject(Path(f"{path}/{name}{'_' + str(i) if i is not None else ''}.{format}")).scale(scale)
    return solution


def get_param_matrix(i):
    # param_matrix = IntegerMatrix(parameters_dict[i], left_bracket="(", right_bracket=")")
    # param_matrix = get_sub_objects(param_matrix, list(range(1, count_sub_objects(param_matrix)-1)))
    # create_grid(np.shape(parameters_dict[i]))
    # return param_matrix
    return Group(*create_grid_of_colored_rectangles(np.array(parameters_dict[i]), cmap=COLOR_PARAMS,
                                                    number_color=COLOR_PARAMS,
                                                    stroke_width=1, fill_opacity=0.25))


def get_param_matrix_optim(i):
    # param_matrix = DecimalMatrix(parameters_optim_dict[i], left_bracket="(", right_bracket=")",
    #                              element_to_mobject_config={"num_decimal_places": 2})
    # return param_matrix
    return Group(*create_grid_of_colored_rectangles(np.round(parameters_optim_dict[i], decimals=2), cmap=COLOR_PARAMS,
                                                    number_color=COLOR_PARAMS,
                                                    stroke_width=1, fill_opacity=0.25))


def get_param_matrix_se(i):
    # param_matrix = DecimalMatrix(parameters_se_dict[i], left_bracket="(", right_bracket=")",
    #                              element_to_mobject_config={"num_decimal_places": 2})
    # return param_matrix
    return Group(*create_grid_of_colored_rectangles(np.round(parameters_se_dict[i], decimals=2), cmap=COLOR_PARAMS,
                                                    number_color=COLOR_PARAMS,
                                                    stroke_width=1, fill_opacity=0.25))


def get_param_matrix_avg(i):
    # param_matrix = DecimalMatrix(parameters_avg_dict[i], left_bracket="(", right_bracket=")",
    #                              element_to_mobject_config={"num_decimal_places": 2})
    # return param_matrix
    return Group(*create_grid_of_colored_rectangles(np.round(parameters_avg_dict[i], decimals=2), cmap=COLOR_PARAMS,
                                                    number_color=COLOR_PARAMS,
                                                    stroke_width=1, fill_opacity=0.25))


# =============== =============== =============== =============== #
#                         Other functions                         #
# =============== =============== =============== =============== #
def Yshape(theta):
    r = 0.25 * (2 + 0.5 * (np.sin(2 * theta) + np.cos(3 * theta + 0.22) * 2 / 3))
    # baterfly
    # r = 2 + np.cos(2*theta) + np.sin(5 * theta + 0.22) * 2 / 3
    x = np.cos(theta) * r
    y = np.sin(theta) * r
    return np.array([x, y, 0])


def get_Yshape_object(fill_color=COLOR_PARAMS, fill_opacity=DOMAIN_FILL_OPACITY):
    return ParametricFunction(Yshape, t_range=[0, 2 * PI], fill_color=fill_color, fill_opacity=fill_opacity,
                              stroke_width=DOMAIN_STROKE_WIDTH, stroke_color=COLOR_PARAMS, stroke_opacity=1)


# =============== =============== =============== =============== #
#                              Slides                             #
# =============== =============== =============== =============== #

class TwoProblems(MySlide):
    def construct(self, objects_from_previous_slides):
        buff_main_eq = 0.5

        param_cycle_period = 12
        # =============== =============== =============== #
        # SLIDE 6: Two problems
        # =============== =============== =============== #
        self.next_slide()
        self.remove_old_elements()
        title_2main_problems = Title(r"Two main problems", font_size=STITLE_FS)
        forwmod = Text("Forward modelling", color=FM_COLOR,  # weight=BOLD,
                       font_size=MEDIUM_FS)
        forwmod = forwmod.next_to(title_2main_problems, DOWN, buff=BUFF_ONE, aligned_edge=UP).shift(
            TwoColumns_dx * LEFT)
        invproblem = Text("Inverse problem", color=INV_COLOR,  # weight=BOLD,
                          font_size=MEDIUM_FS)
        invproblem = invproblem.next_to(title_2main_problems, DOWN, buff=BUFF_ONE, aligned_edge=UP).shift(
            TwoColumns_dx * RIGHT)

        self.next_slide()
        self.play(
            FadeIn(forwmod, invproblem),
            self.update_main_title(title_2main_problems),
            self.update_slide_number(),
        )

        # =============== =============== =============== #
        # Forward modelling
        self.next_slide(auto_next=True)
        # TODO: add \mathbb{R}^d
        fmeq = MathTex(r"y \in Y \mapsto u \in V", substrings_to_isolate=["y", "u"],
                       tex_to_color_map={"y": COLOR_PARAMS, "u": COLOR_SOLUTION},
                       font_size=MEDIUM_FS).next_to(forwmod, DOWN, buff=buff_main_eq)
        fmapprox = MathTex(r"\tilde{u} = S(y) \;\; S : \mathbb{R}^d \rightarrow V",
                           substrings_to_isolate=["y", r"\tilde{u}"],
                           tex_to_color_map={"y": COLOR_PARAMS, r"\tilde{u}": COLOR_SOLUTION},
                           font_size=MEDIUM_FS).next_to(fmeq, DOWN, buff=buff_main_eq)

        self.play(
            FadeIn(fmeq)
        )

        # ---------- Add param space ---------- #
        self.next_slide()
        i = 5
        Y = get_Yshape_object(fill_color=COLOR_PARAMS, fill_opacity=DOMAIN_FILL_OPACITY)
        param_matrix = get_param_matrix(i).set_color(COLOR_PARAMS).scale(0.5).next_to(Y, UP)
        yparamgroup = Group(param_matrix, Y)
        solution = get_diff_eq_images(name="solutions", i=i).next_to(yparamgroup, RIGHT, buff=0.75)
        ytextobj = fmeq[0][0]
        t = i / num_snapshots
        Group(yparamgroup, solution).next_to(fmapprox, DOWN, buff=buff_main_eq)
        ydot = Dot(Y.get_center() + 0.5 * Yshape(2 * np.pi * t), radius=0.5 * DEFAULT_DOT_RADIUS,
                   stroke_width=0.5, fill_color=COLOR_PARAMS, color=WHITE)
        solution_coord = solution.get_center()

        param_matrix_coords = param_matrix.get_center()
        Ytextobj = fmeq[1][1]
        self.play(Indicate(Ytextobj), FadeIn(Y, target_position=Ytextobj, scale=0.5))

        # ---------- Add param choice ---------- #
        self.next_slide()
        self.play(
            Indicate(ytextobj),
            FadeIn(ydot, target_position=ytextobj, scale=5),
            FadeIn(param_matrix, target_position=ytextobj, scale=0.1)
        )

        # ---------- Add solution ---------- #
        self.next_slide()
        maptotextobj = fmeq[1][2:]
        utextobj = fmeq[2][0]
        self.play(
            Indicate(maptotextobj, scale_factor=2),
        )
        self.play(
            Indicate(utextobj),
            FadeIn(solution, target_position=utextobj, scale=0.2),
        )

        # ---------- FEM ---------- #
        self.next_slide()
        G = get_diff_eq_images("grid")
        G.move_to(solution)
        fem = Text("FEM mesh", color=autumn_white, font_size=SMALL_FS)
        fem.next_to(G, UP)
        fmeqVN = MathTex(r"y \in Y \mapsto u \in V^N", substrings_to_isolate=["y", "u"],
                         tex_to_color_map={"y": COLOR_PARAMS, "u": COLOR_SOLUTION},
                         font_size=MEDIUM_FS).move_to(fmeq, aligned_edge=DL)
        self.play(
            FadeIn(G, fem),
            FadeIn(fmeqVN)
        )

        # ---------- Multiple queries ---------- #
        self.next_slide()
        self.play(
            FadeOut(G, fem, solution, ydot, fmeqVN)
        )
        MULTIPLE_QUERIES_TIME = 5

        ydots = []
        solutions = list()
        for i in range(num_snapshots):
            t = i / num_snapshots
            solution = get_diff_eq_images(name="solutions", i=i, scale=0.8, format="png")
            new_param_matrix = get_param_matrix(i).set_color(COLOR_PARAMS).scale(0.5).move_to(param_matrix_coords)
            ydots.append(Dot(Y.get_center() + 0.5 * Yshape(2 * np.pi * t), radius=0.5 * DEFAULT_DOT_RADIUS,
                             stroke_width=0.5, fill_color=COLOR_PARAMS, color=WHITE))
            solution.move_to(solution_coord + 2 * Yshape(2 * np.pi * t)).scale(0.25)
            solutions.append(solution)

            self.play(
                FadeOut(param_matrix),
                FadeIn(ydots[-1], scale=5),
                FadeIn(new_param_matrix, target_position=ydots[-1], scale=0.1),
                FadeIn(solution[-1], target_position=ydots[-1], scale=0.1),
                run_time=MULTIPLE_QUERIES_TIME / num_snapshots, rate_func=linear
            )
            param_matrix = new_param_matrix

        # ---------- Optimization ---------- #
        self.next_slide()
        self.play(FadeOut(*solutions), FadeOut(*ydots), FadeOut(param_matrix))

        for i in range(num_snapshots_optim):
            # TODO: the time is kind of Hard Coded
            t = i / num_snapshots_optim
            new_solution = get_diff_eq_images(name="solutions_optim", i=i, scale=0.8, format="png").move_to(
                solution_coord)
            new_param_matrix = get_param_matrix_optim(i).set_color(COLOR_PARAMS).scale(0.5).move_to(param_matrix_coords)
            new_ydot = Dot(Y.get_center() + 0.5 * Yshape(np.pi * t), radius=0.5 * DEFAULT_DOT_RADIUS,
                           stroke_width=0.5, fill_color=COLOR_PARAMS, color=WHITE)

            self.play(
                FadeOut(param_matrix),
                FadeIn(new_param_matrix),
                ReplacementTransform(ydot, new_ydot) if i > 0 else FadeIn(new_ydot),
                ReplacementTransform(solution, new_solution) if i > 0 else FadeIn(new_solution),
                run_time=param_cycle_period / num_snapshots_optim, rate_func=linear
            )
            param_matrix = new_param_matrix
            ydot = new_ydot
            solution = new_solution

        # ---------- reconstruction ---------- #
        self.next_slide()
        self.play(FadeIn(fmapprox))

        # =============== =============== =============== #
        # Inverse problem: measurements pointwise
        tex_z = MathTex(r"\ell(u)+\eta = z \in \mathbb{R}^m",
                        substrings_to_isolate=["z", "u"],
                        tex_to_color_map={"z": COLOR_MEASUREMENTS, "u": COLOR_SOLUTION},
                        font_size=MEDIUM_FS).next_to(invproblem, DOWN, buff=buff_main_eq)
        tex_avg = MathTex(
            r"\ell_i(u) = \int_{I_i} u(x)dx \;\; I_i\in \mathcal{T}_h",
            substrings_to_isolate=["z", "u"],
            tex_to_color_map={"z": COLOR_MEASUREMENTS, "u": COLOR_SOLUTION},
            font_size=MEDIUM_FS).next_to(tex_z, DOWN, buff=buff_main_eq)
        tex_pointwise = MathTex(
            r"\ell_i(u) = u(x_i), \;\; x_i \in \Omega",
            substrings_to_isolate=["z", "u"],
            tex_to_color_map={"z": COLOR_MEASUREMENTS, "u": COLOR_SOLUTION},
            font_size=MEDIUM_FS).move_to(tex_avg)

        def build_barplot(barplot):
            xlab = MathTex("i").next_to(barplot, DOWN, buff=0.1)
            ylab = MathTex("z_i", color=COLOR_MEASUREMENTS).next_to(barplot, LEFT, buff=0.1)
            return Group(barplot, xlab, ylab)

        barplot = build_barplot(get_diff_eq_images(name="barplot_measurements_increase", i=0, scale=0.8, format="png")
                                .next_to(solution, RIGHT)).set_x(tex_avg.get_x())
        # barplot = barplot.shift(barplot.get_x() * LEFT)
        barplot_coords = barplot.get_center()

        # ip = ip.shift(barplot_coords[0] * RIGHT, ip.get_x() * LEFT)

        self.next_slide()
        self.play(FadeIn(tex_z))

        self.next_slide(auto_next=True)
        self.play(FadeIn(tex_pointwise))

        self.remove(solution)
        for i in range(number_of_measures):
            solution = get_diff_eq_images("solutions_point_measurements_increase", i).move_to(solution_coord)
            barplot = build_barplot(get_diff_eq_images(name="barplot_measurements_increase", i=i)).move_to(
                barplot_coords)

            self.add(solution, barplot)
            self.wait(5 / number_of_measures)
            self.remove(solution, barplot)
        self.add(solution, barplot)

        self.next_slide()
        self.remove(param_matrix, ydot, solution, barplot)
        # for i in range(-num_snapshots_optim // 2, num_snapshots_optim // 2):
        for i in list(range(0, num_snapshots_optim // 4)) + list(range(0, num_snapshots_optim // 4))[::-1]:
            i = i % num_snapshots_optim
            t = i / num_snapshots_optim
            param_matrix = get_param_matrix_se(i).set_color(COLOR_PARAMS).scale(0.5).next_to(Y, LEFT).move_to(
                param_matrix_coords)
            ydot = Dot(Y.get_center() + 0.5 * Yshape(2 * np.pi * t), radius=0.5 * DEFAULT_DOT_RADIUS,
                       stroke_width=0.5, fill_color=COLOR_PARAMS, color=WHITE)
            solution = get_diff_eq_images("state_estimation_solutions_points", i).move_to(solution_coord)
            barplot = build_barplot(get_diff_eq_images("state_estimation_barplot_measurements", i)).move_to(
                barplot_coords)

            self.add(param_matrix, ydot, solution, barplot)
            self.wait(param_cycle_period / num_snapshots_optim)
            self.remove(param_matrix, ydot, solution, barplot)
        self.add(param_matrix, ydot, solution, barplot)

        # =============== =============== =============== #
        # Inverse problem: measurements avg
        i = (-num_snapshots_optim // 2) % num_snapshots_optim
        solution_avg = get_diff_eq_images("solution_avg", i).move_to(solution_coord)
        barplot_avg = build_barplot(get_diff_eq_images("barplot_measurements_avg", i)).move_to(barplot_coords)

        self.next_slide()
        self.play(
            FadeOut(tex_pointwise),
            FadeIn(tex_avg),
            ReplacementTransform(solution, solution_avg),
            FadeOut(barplot),
            FadeIn(barplot_avg)
        )

        self.remove(param_matrix, ydot, solution_avg, barplot_avg)
        # for i in range(-num_snapshots_optim // 2, num_snapshots_optim // 2):
        for i in list(range(0, num_snapshots_optim // 4)) + list(range(0, num_snapshots_optim // 4))[::-1]:
            i = i % num_snapshots_optim
            t = i / num_snapshots_optim
            param_matrix = get_param_matrix_avg(i).set_color(COLOR_PARAMS).scale(0.5).next_to(Y, LEFT).move_to(
                param_matrix_coords)
            ydot = Dot(Y.get_center() + 0.5 * Yshape(2 * np.pi * t), radius=0.5 * DEFAULT_DOT_RADIUS,
                       stroke_width=0.5, fill_color=COLOR_PARAMS, color=WHITE)
            solution_avg = get_diff_eq_images("solution_avg", i).move_to(solution_coord)
            barplot_avg = build_barplot(get_diff_eq_images("barplot_measurements_avg", i)).move_to(barplot_coords)

            self.add(param_matrix, ydot, solution_avg, barplot_avg)
            self.wait(param_cycle_period / num_snapshots_optim)
            self.remove(param_matrix, ydot, solution_avg, barplot_avg)
        self.add(param_matrix, ydot, solution_avg, barplot_avg)

        # =============== =============== =============== #
        # State estimation
        i = 0
        se_scale = 0.5

        new_param_matrix = get_param_matrix_se(i).set_color(COLOR_PARAMS).scale(0.5).next_to(Y, LEFT).move_to(
            param_matrix_coords)
        self.next_slide()
        self.remove(ydot)
        ydot = Dot(Y.get_center() + 0.5 * Yshape(np.pi * t), radius=0.5 * DEFAULT_DOT_RADIUS,
                   stroke_width=0.5, fill_color=COLOR_PARAMS, color=WHITE)
        solution = get_diff_eq_images("state_estimation_solutions_points", i).move_to(solution_coord)
        se = Text("State estimation", font_size=SMALL_FS, slant=ITALIC, color=COLOR_SOLUTION,
                  should_center=True).next_to(tex_z, DOWN, buff=buff_main_eq * 1.5)
        seeq = MathTex(r"\tilde{u} = R(z) \;\; R : \mathbb{R}^m \rightarrow V",
                       substrings_to_isolate=["z", r"\tilde{u}"],
                       tex_to_color_map={"z": COLOR_MEASUREMENTS, r"\tilde{u}": COLOR_SOLUTION},
                       font_size=MEDIUM_FS).next_to(se, DOWN)

        pe = Text("Parameter estimation", font_size=SMALL_FS, slant=ITALIC, color=COLOR_PARAMS,
                  should_center=True).next_to(seeq, DOWN, buff=buff_main_eq * 1.5)
        peeq = MathTex(r"\tilde{y} = R(z) \;\; R : \mathbb{R}^m \rightarrow \mathbb{R}^d",
                       substrings_to_isolate=["z", r"\tilde{y}"],
                       tex_to_color_map={"z": COLOR_MEASUREMENTS, "y": COLOR_PARAMS},
                       font_size=MEDIUM_FS).next_to(pe, DOWN)

        state_estimation = get_diff_eq_images("state_estimation", i, scale=se_scale).next_to(seeq, LEFT,
                                                                                             buff=buff_main_eq)
        param_matrix_approx = (get_param_matrix_se(i).set_color(COLOR_PARAMS).scale(se_scale / 0.8 * 0.5)
                               .next_to(peeq, LEFT, buff=buff_main_eq).set_x(state_estimation.get_x()))

        self.play(
            FadeOut(solution_avg, barplot_avg, param_matrix, new_ydot, tex_avg, tex_pointwise),
            FadeIn(se, seeq, new_param_matrix, ydot, solution, state_estimation),
        )

        self.remove(new_param_matrix, ydot, solution, state_estimation)
        for i in range(1, num_snapshots_optim):
            t = i / num_snapshots_optim
            param_matrix = get_param_matrix_se(i).set_color(COLOR_PARAMS).scale(0.5).next_to(Y, LEFT).move_to(
                param_matrix_coords)
            ydot = Dot(Y.get_center() + 0.5 * Yshape(2 * np.pi * t), radius=0.5 * DEFAULT_DOT_RADIUS,
                       stroke_width=0.5, fill_color=COLOR_PARAMS, color=WHITE)
            solution = get_diff_eq_images("state_estimation_solutions_points", i).move_to(solution_coord)
            # barplot = get_diff_eq_images("state_estimation_barplot_measurements", i).move_to(barplot_coords)
            state_estimation = get_diff_eq_images("state_estimation", i, scale=se_scale).move_to(state_estimation)

            self.add(param_matrix, ydot, solution, state_estimation)
            self.wait(param_cycle_period / num_snapshots_optim)
            self.remove(param_matrix, ydot, solution, state_estimation)
        self.add(param_matrix, ydot, solution, state_estimation)

        # =============== =============== =============== #
        # parameter estimation
        self.next_slide()
        self.play(
            FadeIn(peeq, pe, param_matrix_approx)
        )

        self.remove(param_matrix, ydot, solution, state_estimation, param_matrix_approx)
        for i in range(1, num_snapshots_optim):
            t = i / num_snapshots_optim
            param_matrix = get_param_matrix_se(i).set_color(COLOR_PARAMS).scale(0.5).next_to(Y, LEFT).move_to(
                param_matrix_coords)
            ydot = Dot(Y.get_center() + 0.5 * Yshape(2 * np.pi * t), radius=0.5 * DEFAULT_DOT_RADIUS,
                       stroke_width=0.5, fill_color=COLOR_PARAMS, color=WHITE)
            solution = get_diff_eq_images("state_estimation_solutions_points", i).move_to(solution_coord)
            # barplot = get_diff_eq_images("state_estimation_barplot_measurements", i).move_to(barplot_coords)
            state_estimation = get_diff_eq_images("state_estimation", i, scale=se_scale).move_to(state_estimation)
            param_matrix_approx = (
                get_param_matrix_se(i).set_color(COLOR_PARAMS).set_color(COLOR_PARAMS).scale(se_scale / 0.8 * 0.5)
                .next_to(peeq, LEFT, buff=buff_main_eq).set_x(state_estimation.get_x()))
            self.add(param_matrix, ydot, solution, state_estimation, param_matrix_approx)
            self.wait(param_cycle_period / num_snapshots_optim)
            self.remove(param_matrix, ydot, solution, state_estimation, param_matrix_approx)
        self.add(param_matrix, ydot, solution, state_estimation, param_matrix_approx)

        return {"forward_map": fmeq, "Y": Y}
