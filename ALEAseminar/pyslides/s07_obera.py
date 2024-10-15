from ALEAseminar.config import *
from ALEAseminar.pyslides.s03_near_optimality import best_fit_estimator
from ALEAseminar.pyslides.s04_recontrucrion_from_cell_averages import ConvergencePLotLayout, \
    get_original_data_and_ground_truth, get_reconstructions
from ALEAseminar.pyslides.s05_piecewise_constant import LVIRA_COLOR, \
    create_convergence_plot_objects, QUADRATIC_COLOR, CIRCLE_COLOR, VERTEX_COLOR, QUARTIC_COLOR, OBERA_DATA
from ALEAseminar.pyslides.s06_lvira import grid_curve_and_averages, drop_cell_T
from lib.utils import MySlide, get_sub_objects

OBERA_COLOR = LVIRA_COLOR


class OBERASlides(MySlide):

    def construct(self, objects_from_previous_slides):
        title = Title(r"Higher order", font_size=STITLE_FS)
        layout = ConvergencePLotLayout(title, shift=UP)

        # # -------------- -------------- -------------- #
        # #   OBERA
        obera = Tex(r"Optimization Based Edge Reconstruction Algorithm", font_size=STITLE_FS,
                    substrings_to_isolate=["O", "B", "E", "R", "A"],
                    tex_to_color_map={"O": OBERA_COLOR, "B": OBERA_COLOR, "E": OBERA_COLOR, "R": OBERA_COLOR,
                                      "A": OBERA_COLOR})
        self.next_slide()
        self.play(
            self.fade_out_old_elements(),
            self.update_main_title(title),
            self.update_slide_number(),
            Write(obera)
        )

        self.next_slide()
        title = Title(r"Higher order: OBERA", font_size=STITLE_FS)
        vn_space = MathTex(
            r"V_n := \{ v_{\mu}: \mu \in \R^n \}",
            font_size=EQ_FONT_SIZE).next_to(title, DOWN, buff=BUFF_HALF)
        best_fit = best_fit_estimator.copy().next_to(vn_space, DOWN, buff=BUFF_HALF)

        txt_quadratic = Tex(r"Quadratic", font_size=EQ_FONT_SIZE, color=QUADRATIC_COLOR)
        txt_quartic = Tex(r"Quartic", font_size=EQ_FONT_SIZE, color=QUARTIC_COLOR)
        txt_circle = Tex(r"Circle", font_size=EQ_FONT_SIZE, color=CIRCLE_COLOR)
        txt_vertex = Tex(r"Vertex", font_size=EQ_FONT_SIZE, color=VERTEX_COLOR)

        example_vn_quadratic = drop_cell_T(
            grid_curve_and_averages(
                best_fit.get_edge_center(DOWN) + BUFF_HALF * DOWN,
                lambda x: -0.1 + 0.5 * x - 0.5 * x ** 2,
                grid_shape=(3, 3), cmap="coolwarm", width=1.5, add_updater=False)[0]
        )
        example_vn_quartic = drop_cell_T(
            grid_curve_and_averages(
                best_fit.get_edge_center(DOWN) + BUFF_HALF * DOWN,
                lambda x: -0.1 + 0.5 * x - 0.5 * x ** 2 + 0.5 * x ** 3 - 0.05 * x ** 4,
                grid_shape=(5, 5), cmap="coolwarm", width=1.5, add_updater=False)[0]
        )
        example_vn_circle = drop_cell_T(
            grid_curve_and_averages(
                best_fit.get_edge_center(DOWN) + BUFF_HALF * DOWN,
                lambda x: np.sqrt(4 ** 2 - (x - 2) ** 2) - 3,
                grid_shape=(3, 3), cmap="coolwarm", width=1.5, add_updater=False)[0]
        )
        example_vn_vertex = drop_cell_T(
            grid_curve_and_averages(
                best_fit.get_edge_center(DOWN) + BUFF_HALF * DOWN,
                lambda x: 0.1 + (0.7 * x) * (x < 0) + (-0.2 * x) * (x >= 0),
                grid_shape=(5, 5), cmap="coolwarm", width=1.5, add_updater=False)[0]
        )

        example_vn_quartic.next_to(example_vn_quadratic, RIGHT, buff=BUFF_HALF)
        (Group(example_vn_quadratic, example_vn_quartic)
         .next_to(best_fit, DOWN, buff=1.5 * BUFF_HALF))
        example_vn_circle.next_to(example_vn_quadratic, DOWN, buff=1.5 * BUFF_HALF)
        example_vn_vertex.next_to(example_vn_quartic, DOWN, buff=1.5 * BUFF_HALF)
        Group(vn_space, best_fit, example_vn_quadratic, example_vn_quartic, example_vn_circle,
              example_vn_vertex).set_y(-BUFF_HALF)

        txt_quadratic.next_to(example_vn_quadratic, UP)
        txt_quartic.next_to(example_vn_quartic, UP)
        txt_circle.next_to(example_vn_circle, UP)
        txt_vertex.next_to(example_vn_vertex, UP)

        self.play(
            self.update_main_title(title),
            FadeOut(obera, target_position=best_fit.get_center(), scale=0.1),
            Write(best_fit)
        )

        self.next_slide()
        self.play(
            Write(vn_space)
        )

        self.next_slide()
        self.play(
            FadeIn(example_vn_quadratic),
            Write(txt_quadratic)

        )

        self.next_slide()
        self.play(
            FadeIn(example_vn_quartic),
            Write(txt_quartic)
        )

        self.next_slide()
        self.play(
            FadeIn(example_vn_circle),
            Write(txt_circle)
        )

        self.next_slide()
        self.play(
            FadeIn(example_vn_vertex),
            Write(txt_vertex)
        )

        # -------------- convergence rate -------------- #
        plot_group_lvira = create_convergence_plot_objects("LVIRA", layout=layout)

        exp_citation = Text("[A. Cohen, O. Mula, A. Somacal, ArXiv, 2024]",
                            font_size=CITATION_FONT_SIZE, color=OBERA_DATA.color).set_x(plot_group_lvira.get_x()).set_y(
            -H + BUFF_HALF)

        layout = ConvergencePLotLayout(title, shift=UP)
        ground_truth, original_avg_10, original_avg_20 = get_original_data_and_ground_truth(layout)
        lvira_reconstruction_avg_10, lvira_reconstruction_avg_20 = get_reconstructions(layout, "linear_obera_w")

        self.next_slide()
        self.play(
            self.fade_out_old_elements(),
            FadeIn(original_avg_10, original_avg_20, lvira_reconstruction_avg_10, lvira_reconstruction_avg_20,
                   ground_truth),
            FadeIn(plot_group_lvira),
        )

        plot_group_obera = create_convergence_plot_objects("OBERA", layout=layout)
        obera2_reconstruction_avg_10, obera2_reconstruction_avg_20 = (
            get_reconstructions(layout, "quadratic_obera_non_adaptive"))
        self.next_slide()
        self.play(
            FadeOut(lvira_reconstruction_avg_10, lvira_reconstruction_avg_20),
            FadeIn(obera2_reconstruction_avg_10, obera2_reconstruction_avg_20),
            FadeOut(plot_group_lvira),
            FadeIn(plot_group_obera),
            Write(exp_citation),
        )

        # ---------- OBERA problems ---------- #
        self.next_slide()
        best_fit.set_x(0)
        problem = Tex("Practical problem: long computation time", font_size=MEDIUM_FS)
        problem2 = Tex("Theoretical problem: difficult to prove $\mu_Z \leq \infty$", font_size=MEDIUM_FS)
        problem.next_to(best_fit, DOWN, buff=BUFF_ONE)
        problem2.next_to(problem, DOWN, buff=BUFF_ONE, aligned_edge=LEFT)
        Group(problem, problem2).set_x(0)

        self.play(
            self.fade_out_old_elements(),
        )
        self.play(Write(problem2))

        self.next_slide()
        self.play(Write(problem))

        self.next_slide()
        self.play(
            FadeIn(best_fit, target_position=problem.get_center(), scale=0.1),
        )

        self.next_slide()
        self.play(
            Indicate(get_sub_objects(best_fit, list(range(3, 9))).copy()),
        )
        self.play(
            get_sub_objects(best_fit, list(range(3, 9))).animate.set_color(RED)
        )

        self.next_slide()
        self.play(
            Indicate(get_sub_objects(best_fit, list(range(-6, -2))).copy()),
        )
        self.play(
            get_sub_objects(best_fit, list(range(-6, -2))).animate.set_color(RED)
        )
        return dict()
