from config import *
from pyslides.s04_recontrucrion_from_cell_averages import ConvergencePLotLayout, \
    get_original_data_and_ground_truth, get_reconstructions
from pyslides.s05_piecewise_constant import create_convergence_plot_objects, \
    AEROS_4_DATA, AEROS_2_DATA
from pyslides.s08_aeros import AEROS_COLOR
from lib.utils import MySlide


class AEROSConvergenceSlides(MySlide):

    def construct(self, objects_from_previous_slides):
        title = Title(r"AEROS convergence", font_size=STITLE_FS)
        layout = ConvergencePLotLayout(title)

        # -------------- -------------- -------------- #
        #   AEROS
        # grid, x_label, y_label, points, graphs, order, plot_group = create_convergence_plot_objects(
        #     models=[PIECEWISE_DATA, LVIRA_DATA, OBERA_DATA, AEROS_2_DATA, AEROS_4_DATA], layout=layout)
        plot_group_obera = create_convergence_plot_objects("OBERA", layout=layout)

        citation = Text("[A. Cohen, O. Mula, A. Somacal, ArXiv, 2024]",
                        font_size=CITATION_FONT_SIZE, color=AEROS_2_DATA.color).set_x(plot_group_obera.get_x()).set_y(
            -H + BUFF_HALF)

        # aa = Text("OBERA", font_size=EQ_FONT_SIZE)
        # ab = MathTex(r"3\cdot 10^{-1}\text{s}", font_size=EQ_FONT_SIZE).next_to(aa, RIGHT, buff=BUFF_HALF)
        # ba = Text("AEROS", font_size=EQ_FONT_SIZE).next_to(aa, DOWN, buff=BUFF_HALF / 2)
        # bb = MathTex(r"3\cdot 10^{-3}\text{s}", font_size=EQ_FONT_SIZE).next_to(ab, DOWN, buff=BUFF_HALF / 2,
        #                                                                         aligned_edge=LEFT)
        # computation_time = Group(aa, ab, ba, bb).move_to(citation, UP).set_y(
        #     (plot_group_obera.get_y(DOWN) + citation.get_y(UP)) / 2)

        # computation_time = MobjectTable(
        #     [[Text("OBERA (s)", font_size=SMALL_FS), MathTex("3\cdot 10^{-1}", font_size=SMALL_FS)],
        #      [Text("AEROS (s)", font_size=SMALL_FS), MathTex("3\cdot 10^{-3}", font_size=SMALL_FS)]]
        # ).move_to(citation, UP).set_y((x_label.get_y(DOWN) + citation.get_y(UP)) / 2)
        faster_time = (MathTex(r"\tau_{AEROS} \lesssim \frac{\tau_{OBERA}}{100}", font_size=EQ_FONT_SIZE)
                       .move_to(citation, UP).set_y((plot_group_obera.get_y(DOWN) + citation.get_y(UP)) / 2))
        faster_time = Group(SurroundingRectangle(faster_time, color=AEROS_COLOR, fill_opacity=0.1), faster_time)

        layout2 = ConvergencePLotLayout(title, shift=UP)
        ground_truth, original_avg_10, original_avg_20 = get_original_data_and_ground_truth(layout2)
        obera_reconstruction_avg_10, obera_reconstruction_avg_20 = get_reconstructions(layout2,
                                                                                       "quadratic_obera_non_adaptive")

        self.next_slide()
        self.play(
            self.fade_out_old_elements(),
            self.update_main_title(title),
            self.update_slide_number(),
            # FadeIn(grid, x_label, y_label),
            # Create(points["Piecewise constant"]),
            # Create(graphs["Piecewise constant"]),
            # Write(order["Piecewise constant"]),
            # Create(points["LVIRA"]),
            # Create(graphs["LVIRA"]),
            # Write(order["LVIRA"]),
            # Create(points["OBERA"]),
            # Create(graphs["OBERA"]),
            # Write(order["OBERA"]),
        )
        self.play(
            FadeIn(ground_truth, original_avg_10, original_avg_20, obera_reconstruction_avg_10,
                   obera_reconstruction_avg_20),
            FadeIn(plot_group_obera),
        )

        self.next_slide()
        title = Title(r"AEROS convergence: Quadratic", font_size=STITLE_FS)
        plot_group_aeros2 = create_convergence_plot_objects("AEROS2", layout=layout)
        aeros2_reconstruction_avg_10, aeros2_reconstruction_avg_20 = get_reconstructions(layout2, "quadratic_aero")
        self.play(
            self.update_main_title(title),
            self.update_slide_number(),
            FadeIn(aeros2_reconstruction_avg_10, aeros2_reconstruction_avg_20),
            FadeOut(obera_reconstruction_avg_10, obera_reconstruction_avg_20),
            # Create(points["AEROS2"]),
            # Create(graphs["AEROS2"]),
            # Write(order["AEROS2"]),
            Write(citation),
            FadeOut(plot_group_obera),
            FadeIn(plot_group_aeros2)
        )

        self.next_slide()
        self.play(FadeIn(faster_time))

        # self.next_slide()
        # self.play(
        #     self.update_slide_number(),
        #     FadeIn(computation_time)
        # )
        #
        # self.next_slide()
        # self.play(
        #     ReplacementTransform(computation_time, faster_time)
        # )

        title = Title(r"AEROS convergence: Quartic", font_size=STITLE_FS)
        self.next_slide()
        plot_group_aeros4 = create_convergence_plot_objects("AEROS4", layout=layout)
        aeros4_reconstruction_avg_10, aeros4_reconstruction_avg_20 = get_reconstructions(layout2, "quartic_aero")
        self.play(
            self.update_main_title(title),
            self.update_slide_number(),
            FadeOut(aeros2_reconstruction_avg_10, aeros2_reconstruction_avg_20),
            FadeIn(aeros4_reconstruction_avg_10, aeros4_reconstruction_avg_20),
            # Create(points["AEROS4"]),
            # Create(graphs["AEROS4"]),
            # Write(order["AEROS4"]),
            FadeIn(plot_group_aeros4),
            FadeOut(plot_group_aeros2),
            citation.animate.set_color(AEROS_4_DATA.color),
        )

        return dict()
