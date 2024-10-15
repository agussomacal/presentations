from ALEAseminar.config import *
from ALEAseminar.pyslides.s03_near_optimality import best_fit_estimator, nop_non_linear
from lib.utils import MySlide


class PerspectivesSlides(MySlide):
    def construct(self, objects_from_previous_slides):
        title = Title(r"Summary and perspectives", font_size=STITLE_FS)

        self.next_slide()
        self.play(
            self.update_main_title(title),
            self.fade_out_old_elements(),
            self.update_slide_number(),
        )

        separation = 3 / 2 * BUFF_HALF
        texts = [
            Tex("Near optimality property for non-linear spaces and best-fit estimator"),
            Tex("LVIRA: application to interface reconstruction"),
            Tex("OBERA: more general interfaces"),
            Tex("AEROS: addressing computational complexity problem"),
            Tex("Vertices: when domains present corners"),
            Tex("PDEs by Finite Volumes Schemes"),
        ]
        bfe = best_fit_estimator.copy()
        nop = nop_non_linear.copy()
        nop.next_to(bfe, RIGHT, buff=BUFF_HALF)
        representers = [
            Group(bfe, nop),
            ImageMobject(f"{material_dir}/LVIRArepresentation.png").scale_to_fit_height(1.25 * separation),
            ImageMobject(f"{material_dir}/OBERArepresentation.png").scale_to_fit_height(1.25 * separation),
            ImageMobject(f"{material_dir}/AEROSrepresentation.png").scale_to_fit_height(1.25 * separation),
            ImageMobject(f"{material_dir}/Cornersrepresentation.png").scale_to_fit_height(1.25 * separation),
            ImageMobject(f"{material_dir}/FVrepresentation.png").scale_to_fit_height(1.25 * separation),
        ]

        group = VGroup(*texts[1:]).arrange(DOWN, buff=BUFF_HALF).shift(2 * LEFT).shift(DOWN)
        [rep.next_to(text, RIGHT) for rep, text in zip(representers[1:], texts[1:])]
        rgroup = Group(*representers[1:]).shift(2 * RIGHT)
        rgroupx = rgroup.get_x(RIGHT)
        representers[0].next_to(texts[1], UP, buff=BUFF_HALF)
        texts[0].next_to(representers[0], UP)
        representers[0].set_x(texts[0].get_x(LEFT), LEFT)  # left alignment

        Group(*texts, *representers).set_x(0).set_y(-BUFF_HALF)

        for i, (rep, text) in enumerate(zip(representers, texts)):
            self.next_slide()
            text.set_x(group.get_x(LEFT), LEFT)  # left alignment
            if i > 0:
                rep.set_x(rgroupx, RIGHT).shift(((-1) ** i) * 1.1 * RIGHT)  # right alignment
            self.play(
                Write(text),
                FadeIn(rep)
            )
