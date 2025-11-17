from config import *
from pyslides.s03a_near_optimality import best_fit_estimator
from pyslides.s04_recontrucrion_from_cell_averages import ConvergencePLotLayout
from pyslides.s08_aeros import STENCIL_COLOR
from pyslides.s10_corners import path_corners_images
from lib.utils import MySlide


class CornerReconstructionSlides(MySlide):

    def construct(self, objects_from_previous_slides):
        title = Title(r"Reconstructing corners", font_size=STITLE_FS)
        layout = ConvergencePLotLayout(title)

        bfe = best_fit_estimator.copy().next_to(title, DOWN, buff=BUFF_HALF)
        best_fit_estimator_elvira = MathTex(r"\tilde{u}=\argmin_{\vv \in S} \|z-\ell(\vv)\|_Z",
                                            substrings_to_isolate=[r"\tilde{u}", r"\vv", "z"],
                                            tex_to_color_map={r"\tilde{u}": COLOR_APPROXIMATION,
                                                              r"\vv": COLOR_APPROXIMATION,
                                                              "z": COLOR_MEASUREMENTS},
                                            font_size=EQ_FONT_SIZE).move_to(bfe)

        s_definition = MathTex(r"S = \{\vv_{AEROS-P2}, \vv_{AEROS-V}, \vv_{TEM} \}",
                               substrings_to_isolate=[r"\tilde{u}", r"\vv", "z"],
                               tex_to_color_map={r"\tilde{u}": COLOR_APPROXIMATION, r"\vv": COLOR_APPROXIMATION,
                                                 "z": COLOR_MEASUREMENTS},
                               font_size=EQ_FONT_SIZE).next_to(best_fit_estimator_elvira, RIGHT, buff=BUFF_HALF)
        citation_elvira = Text("ELVIRA method: [J. E. Pilliod, E. G. Puckett, Journal of Computational Physics, 2004]",
                               font_size=CITATION_FONT_SIZE, color=STENCIL_COLOR).next_to(best_fit_estimator_elvira,
                                                                                          DOWN)
        example_reconstruction = [
            (ImageMobject(
                Path(
                    f"{path_corners_images}/plot_reconstruction_imageShapesVertexjpg_modelsoriginal_data_num_cells_per_dim30")).scale_to_fit_height(
                4)
             .next_to(best_fit_estimator_elvira, DOWN, buff=BUFF_ONE)),
            (ImageMobject(
                Path(
                    f"{path_corners_images}/plot_reconstruction_imageShapesVertexjpg_modelselvira_num_cells_per_dim30")).scale_to_fit_height(
                4)
             .next_to(best_fit_estimator_elvira, DOWN, buff=BUFF_ONE)),
            (ImageMobject(
                Path(
                    f"{path_corners_images}/plot_reconstruction_imageShapesVertexjpg_modelsaero_qelvira_vertex_num_cells_per_dim30")).scale_to_fit_height(
                4)
             .next_to(best_fit_estimator_elvira, DOWN, buff=BUFF_ONE))
        ]
        # -------------- -------------- -------------- #
        #   Corners
        self.next_slide()
        self.play(
            self.fade_out_old_elements(),
            self.update_main_title(title),
            self.update_slide_number(),
        )
        self.play(FadeIn(bfe))

        self.next_slide()
        self.play(
            ReplacementTransform(bfe, best_fit_estimator_elvira)
        )
        self.next_slide()
        self.play(
            Write(s_definition),
            Write(citation_elvira)
        )

        self.next_slide()
        self.play(
            FadeIn(example_reconstruction[0])
        )

        self.next_slide()
        self.play(
            FadeOut(example_reconstruction[0]),
            FadeIn(example_reconstruction[1])
        )

        self.next_slide()
        self.add(example_reconstruction[2])
        self.play(
            FadeOut(example_reconstruction[1]),
            # FadeIn(example_reconstruction[2])
        )
        self.wait(0.01)
