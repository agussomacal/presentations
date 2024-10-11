from pathlib import Path

from ALEAseminar.config import *
from ALEAseminar.support_data import path_subcell
from lib.utils import MySlide, shift_to, move_and_scale

num_cells_per_dim = 10


class ConvergencePLotLayout:
    def __init__(self, title, shift=0 * UP):
        self.m_tex = MathTex("blabla", font_size=SMALL_FS)
        self.m_measurements = Rectangle(fill_opacity=0, stroke_opacity=0, height=1.5, width=1.5)
        self.m_ground_truth = self.m_measurements.copy()

        self.m_measurements.next_to(title, DOWN, buff=3 / 2 * BUFF_ONE).shift(5 * LEFT)
        self.m_tex = self.m_tex.next_to(self.m_measurements, UP, buff=4 / 5 * BUFF_ONE)
        self.m_ground_truth.next_to(self.m_measurements, DOWN, buff=BUFF_HALF)
        self.center_y = (self.m_measurements.get_y() + self.m_ground_truth.get_y()) / 2

        self.dx_grid_space = (W - self.m_measurements.get_x(direction=RIGHT))
        self.center_x_grid = (W + self.m_measurements.get_x(direction=RIGHT)) / 2
        self.center_x_grid_two_columns_a = self.center_x_grid - self.dx_grid_space / 4
        self.center_x_grid_two_columns_b = self.center_x_grid + self.dx_grid_space / 4

        self.m_measurements_a = Rectangle(fill_opacity=0, stroke_opacity=0, height=1.5, width=1.5)
        self.m_measurements_b = Rectangle(fill_opacity=0, stroke_opacity=0, height=1.5, width=1.5).next_to(
            self.m_measurements_a, RIGHT, buff=0.25)
        Group(self.m_measurements_a, self.m_measurements_b).move_to(self.m_measurements)
        self.m_ground_truth_a = Rectangle(fill_opacity=0, stroke_opacity=0, height=1.5, width=1.5)
        self.m_ground_truth_b = Rectangle(fill_opacity=0, stroke_opacity=0, height=1.5, width=1.5).next_to(
            self.m_ground_truth_a, RIGHT, buff=0.25)
        Group(self.m_ground_truth_a, self.m_ground_truth_b).move_to(self.m_ground_truth)
        self.m_ground_truth_down = Rectangle(fill_opacity=0, stroke_opacity=0, height=1.5, width=1.5).next_to(
            Group(self.m_ground_truth_a, self.m_ground_truth_b), DOWN, buff=BUFF_HALF)

        Group(self.m_ground_truth_down, self.m_ground_truth, self.m_ground_truth_a, self.m_ground_truth_b,
              self.m_measurements_a, self.m_measurements_b, self.m_measurements).shift(shift)


def get_original_data_and_ground_truth(layout):
    ground_truth = move_and_scale(
        ImageMobject(Path(f"{path_subcell}/zoomed_true_image_")),
        layout.m_ground_truth_down)
    original_avg_10 = move_and_scale(
        ImageMobject(Path(f"{path_subcell}/OriginalData_num_cells_per_dim10_modelspiecewise_constant")),
        layout.m_measurements_a)
    original_avg_20 = move_and_scale(
        ImageMobject(Path(f"{path_subcell}/OriginalData_num_cells_per_dim20_modelspiecewise_constant")),
        layout.m_measurements_b)
    return ground_truth, original_avg_10, original_avg_20


def get_reconstructions(layout, model_name):
    reconstruction_avg_10 = move_and_scale(
        ImageMobject(Path(f"{path_subcell}/NoOriginalImage_num_cells_per_dim10_models{model_name}")),
        layout.m_ground_truth_a)
    reconstruction_avg_20 = move_and_scale(
        ImageMobject(Path(f"{path_subcell}/NoOriginalImage_num_cells_per_dim20_models{model_name}")),
        layout.m_ground_truth_b)
    return reconstruction_avg_10, reconstruction_avg_20


latex4average_measurements = MathTex(
    r"\ell_i(u) = \int_{I_i} u(x)dx \;\; I_i\in \mathcal{T}_h",
    substrings_to_isolate=["z", "u"],
    tex_to_color_map={"z": COLOR_MEASUREMENTS, "u": COLOR_SOLUTION},
    font_size=SMALL_FS)


class InterfaceReconstructionSlides(MySlide):

    def construct(self, objects_from_previous_slides):
        title = Title(r"Interface reconstruction from cell averages", font_size=STITLE_FS)
        layout = ConvergencePLotLayout(title)

        # -------------- -------------- -------------- #
        #
        # solution = move_and_scale(get_diff_eq_images(name="solutions_optim", i=0), layout.m_measurements)
        # solution_avg = move_and_scale(get_diff_eq_images("solution_avg", i=25), layout.m_measurements)
        solution = move_and_scale(ImageMobject(Path(f"{path_subcell}/solution")), layout.m_measurements)
        solution_avg = move_and_scale(ImageMobject(Path(f"{path_subcell}/solution_avg")), layout.m_measurements)
        # solution_avg = move_and_scale(get_diff_eq_images("solution_avg", i=25), layout.m_measurements)
        avg = latex4average_measurements.copy().move_to(layout.m_tex)
        harrow = DoubleArrow(ORIGIN, solution_avg.get_width() / num_cells_per_dim * RIGHT)
        tex_h = SingleStringMathTex("h").next_to(harrow, UP, buff=0.1)
        hgroup = Group(harrow, tex_h).next_to(solution_avg, UP, buff=0.1)

        self.next_slide()
        self.play(
            self.fade_out_old_elements(),
            self.update_slide_number(),
            self.update_main_title(title),
            FadeIn(solution)
        )

        self.next_slide()
        self.play(
            FadeOut(solution),
            FadeIn(solution_avg),
            Write(avg),
            FadeIn(hgroup)
        )

        self.next_slide()
        solution.move_to(layout.m_ground_truth)
        self.play(
            FadeIn(solution),
        )

        # -------------- -------------- -------------- #
        #   two applications
        self.next_slide()
        motivation_2 = Tex(r"Application\\"
                           r'\begin{enumerate}'
                           '\item Image superresolution.'
                           '\item Finite Volumes PDE Solvers'
                           '\end{enumerate}',
                           tex_environment="flushleft",
                           font_size=EQ_FONT_SIZE).set_y(layout.center_y)
        motivation_2 = shift_to(motivation_2, position=layout.center_x_grid, coordinate="x")
        motivation_1 = Tex(r"Application\\"
                           r'\begin{enumerate}'
                           '\item Image superresolution.'
                           # '\item Finite Volumes PDE Solvers'
                           '\end{enumerate}',
                           tex_environment="flushleft",
                           font_size=EQ_FONT_SIZE).move_to(motivation_2, aligned_edge=UL)

        # TODO: Replace with true circles
        circ_avg_10 = move_and_scale(ImageMobject(Path(f"{path_subcell}/CircleAvg10_0")), layout.m_measurements_a)
        circ_avg_20 = move_and_scale(ImageMobject(Path(f"{path_subcell}/CircleAvg20_0")), layout.m_measurements_b)
        circle_reconstructed = move_and_scale(ImageMobject(Path(f"{path_subcell}/Circle_0")), layout.m_ground_truth)

        harrow_10 = DoubleArrow(ORIGIN, circ_avg_10.get_width() / 10 * RIGHT)
        tex_h_10 = SingleStringMathTex("h").next_to(harrow_10, UP, buff=0.1)
        hgroup_10 = (Group(harrow_10, tex_h_10).next_to(circ_avg_10, UP, buff=0.1)
                     .shift(circ_avg_10.get_width() / 20 * RIGHT))

        harrow_20 = DoubleArrow(ORIGIN, circ_avg_20.get_width() / 20 * RIGHT)
        tex_h_20 = SingleStringMathTex("h").next_to(harrow_20, UP, buff=0.1)
        hgroup_20 = (Group(harrow_20, tex_h_20).next_to(circ_avg_20, UP, buff=0.1)
                     .shift(circ_avg_20.get_width() / 40 * RIGHT))

        self.play(
            FadeOut(solution_avg, solution, hgroup),
            FadeIn(motivation_1, circ_avg_10, circ_avg_20, circle_reconstructed, hgroup_10, hgroup_20),
        )

        self.next_slide()
        # TODO: create animation for circle moving in FV fashion
        self.play(
            FadeOut(motivation_1),
            FadeIn(motivation_2)
        )
        seconds_in_sequence = 5
        N = 40  # TODO: extract this number from file instead of harcoding it.
        for i in (np.arange(N + 1, dtype=int) % N):
            self.remove(circ_avg_10, circ_avg_20, circle_reconstructed)
            circ_avg_10 = move_and_scale(ImageMobject(Path(f"{path_subcell}/CircleAvg10_{i}")), layout.m_measurements_a)
            circ_avg_20 = move_and_scale(ImageMobject(Path(f"{path_subcell}/CircleAvg20_{i}")), layout.m_measurements_b)
            circle_reconstructed = move_and_scale(ImageMobject(Path(f"{path_subcell}/Circle_{i}")),
                                                  layout.m_ground_truth)
            # self.play(FadeIn(circ_avg_10, circ_avg_20, circle_reconstructed), run_time=seconds_in_sequence / N)
            self.add(circ_avg_10, circ_avg_20, circle_reconstructed)
            self.wait(seconds_in_sequence / N)

        # -------------- -------------- -------------- #
        #   Regular case
        self.next_slide()
        title = Title(r"Regular case", font_size=STITLE_FS)
        fit_poly = Tex(r"$u$ smooth locally fit polynomials",
                       # tex_environment="flushleft",
                       font_size=EQ_FONT_SIZE).set_y(layout.center_y)
        fit_poly = shift_to(fit_poly, position=layout.center_x_grid, coordinate="x")
        regular = Tex(r"$u$ smooth",
                      # tex_environment="flushleft",
                      font_size=EQ_FONT_SIZE).move_to(fit_poly, aligned_edge=UL)
        solution = move_and_scale(solution, layout.m_ground_truth_a)
        self.play(
            self.update_main_title(title),
            self.update_slide_number(),
            FadeOut(motivation_2),
            FadeOut(circ_avg_10, circ_avg_20, circle_reconstructed, hgroup_10, hgroup_20),
            FadeIn(regular, solution_avg, solution, hgroup),
        )

        poly_approximation = move_and_scale(ImageMobject(Path(f"{path_subcell}/solution_avg_25_reconstructed")),
                                            layout.m_ground_truth_b)
        self.next_slide()
        self.play(
            FadeOut(regular),
            FadeIn(fit_poly, poly_approximation),
        )

        # -------------- -------------- -------------- #
        #   Singular case
        self.next_slide()
        title = Title(r"Interface reconstruction", font_size=STITLE_FS)
        singular = Tex(r"$u$ presents jump discontinuities",
                       # tex_environment="flushleft",
                       font_size=EQ_FONT_SIZE).set_y(layout.center_y)
        singular = shift_to(singular, position=layout.center_x_grid, coordinate="x")

        # TODO: Show a reconstruction for polynomials that fails
        self.play(
            self.update_slide_number(),
            self.update_main_title(title),
            FadeOut(fit_poly),
            FadeOut(poly_approximation, solution, solution_avg, hgroup),
            FadeIn(singular, circ_avg_10, circ_avg_20, circle_reconstructed, hgroup_10, hgroup_20),
        )

        return {"singular": singular}
