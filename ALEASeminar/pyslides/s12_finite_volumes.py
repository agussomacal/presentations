from pathlib import Path

from ALEASeminar.config import *
from ALEASeminar.support_data import path_subcell
from lib.utils import MySlide

path_fv_images = Path(path_subcell, "finite_volumes")

names_dict = {
    "aero_qelvira_vertex": "All together",

    "elvira": "ELVIRA",
    "elvira_w_oriented": "ELVIRA-WO",

    "linear_obera": "OBERA Linear",
    "linear_obera_w": "OBERA-W Linear",

    "quadratic_obera_non_adaptive": "OBERA Quadratic",
    "quadratic_aero": "AEROS Quadratic",

    "upwind": "UpWind",
}

titles = ["smooth shape", "shape with corners", "Zalesak notched circle"]  # Zalesak notched circle
shapes = ["batata", "ShapesVertex", "zalesak_notched_circle"]  # zalesak_notched_circle
models = ["upwind", "elvira_w_oriented", "quadratic_aero", "aero_qelvira_vertex"]
num_cells_per_dim_s = [30]
num_cells_per_dim = 30


def get_evol_image(shape, num_cells_per_dim, i, height=4):
    filename = f"ReconstructionErrorInTimex{i}_num_cells_per_dim{num_cells_per_dim}_image{shape}jpg_angular_velocity0_velocity0_025"
    return ImageMobject(Path(f"{path_fv_images}/{filename}")).scale_to_fit_height(height)


def get_rec_image(shape, model, num_cells_per_dim, height=4):
    filename = f"plot_{'upwind_' if model == 'upwind' else ''}reconstruction_init_final_num_cells_per_dim{num_cells_per_dim}_angular_velocity0_image{shape}jpg_velocity0_025_models{model}"
    return ImageMobject(Path(f"{path_fv_images}/{filename}")).scale_to_fit_height(height)


class FiniteVolumesSlides(MySlide):

    def construct(self, objects_from_previous_slides):
        for tit, shape in zip(titles, shapes):
            title = Title(fr"Finite volumes: {tit}", font_size=STITLE_FS)
            evol_images = [
                get_evol_image(shape, num_cells_per_dim, i, height=3.3).shift(TwoColumns_dx * RIGHT + DOWN / 2) for
                i, model in enumerate(models)]
            models_img = [get_rec_image(shape, model, num_cells_per_dim, height=2.5) for model in models]
            models_img[0].next_to(models_img[1], LEFT)
            models_img[2].next_to(models_img[0], DOWN)
            models_img[3].next_to(models_img[2], RIGHT)
            Group(*models_img).move_to(ORIGIN).shift(TwoColumns_dx * LEFT + DOWN / 2)
            models_names = [Tex(names_dict[model]).next_to(models_img[i], UP if i < 2 else DOWN) for i, model in
                            enumerate(models)]

            for i, (evol_img, model_img, model_name) in enumerate(zip(evol_images, models_img, models_names)):
                self.next_slide()
                if i == 0:
                    self.play(
                        self.fade_out_old_elements(),
                        self.update_main_title(title),
                        self.update_slide_number(),
                    )
                    self.play(FadeIn(evol_img), FadeIn(model_img), Write(model_name))
                else:
                    self.play(FadeOut(evol_images[i - 1]), FadeIn(evol_img), FadeIn(model_img), Write(model_name))
            self.wait(0.01)
