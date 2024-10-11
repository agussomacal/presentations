from pathlib import Path

from ALEAseminar.config import *
from ALEAseminar.support_data import path_subcell, min_n
from lib.utils import MySlide, get_sub_objects

PDE_COLOR = BLUE
IMAGE_COLOR = TEAL


def get_h_group(image, num_cells_per_dim):
    harrow_sol = DoubleArrow(ORIGIN, image.get_width() / num_cells_per_dim * RIGHT)
    tex_h_sol = SingleStringMathTex("h").next_to(harrow_sol, UP, buff=0.1)
    hgroup_sol = Group(harrow_sol, tex_h_sol).next_to(image, UP, buff=0.1)
    return hgroup_sol


class InvPrbExamplesSlides(MySlide):

    def construct(self, objects_from_previous_slides):
        # -------------- -------------- -------------- #
        # Create objects

        # --------- u column ---------- #
        utex = MathTex(r"u \in V \quad \text{Banach}", font_size=MEDIUM_FS)
        get_sub_objects(utex, [0]).set_color(COLOR_SOLUTION)
        uelement = get_sub_objects(utex, [0])
        text_pdes = Tex("Parametric PDEs", font_size=MEDIUM_FS)
        pdetex = MathTex(r"u:\mathcal{P}(u, y)=0",
                         tex_to_color_map={"y": COLOR_PARAMS, "u": COLOR_SOLUTION})
        ytex = MathTex(r"\y:=\{y_1, \dots, y_d\} \in \R^d",
                       substrings_to_isolate=[r"\y", r"y_1", r"y_d"],
                       tex_to_color_map={r"\y": COLOR_PARAMS, r"y_1": COLOR_PARAMS, r"y_d": COLOR_PARAMS})

        text_diffusion = Tex("Diffusion PDE")
        diffusion = MathTex(r"-\text{div} (\diffcoef(y) \nabla u)=f")
        get_sub_objects(diffusion, [-7]).set_color(COLOR_PARAMS)
        get_sub_objects(diffusion, [-4]).set_color(COLOR_SOLUTION)
        pde_rectangle = RoundedRectangle(color=PDE_COLOR)

        text_image = Tex("Image", font_size=MEDIUM_FS)
        # uimage = MathTex(r"u\in \R^{s\times k}", font_size=MEDIUM_FS)
        # get_sub_objects(uimage, [0]).set_color(COLOR_SOLUTION)
        image_rectangle = RoundedRectangle(color=IMAGE_COLOR)

        # --------- second column ---------- #
        title = Title("Inverse problem", font_size=STITLE_FS)
        solution = ImageMobject(Path(f"{path_subcell}/solution")).scale_to_fit_height(1.5)
        yoda_img = ImageMobject(Path(f"{path_subcell}/yoda.png")).scale_to_fit_height(1.5)

        # --------- measurements column ---------- #
        tex_z = MathTex(r"\ell(u)+\eta = z \in \mathbb{R}^m",
                        substrings_to_isolate=["z", "u"],
                        tex_to_color_map={"z": COLOR_MEASUREMENTS, "u": COLOR_SOLUTION},
                        font_size=MEDIUM_FS)
        tex_avg = MathTex(
            r"\ell_i(u) = \int_{I_i} u(x)dx \;\; I_i\in \mathcal{T}_h",
            substrings_to_isolate=["z", "u"],
            tex_to_color_map={"z": COLOR_MEASUREMENTS, "u": COLOR_SOLUTION},
            font_size=SMALL_FS)
        tex_pointwise = MathTex(
            r"\ell_i(u) = u(x_i), \;\; x_i \in \Omega",
            substrings_to_isolate=["z", "u"],
            tex_to_color_map={"z": COLOR_MEASUREMENTS, "u": COLOR_SOLUTION},
            font_size=SMALL_FS)
        solution_pointwise = ImageMobject(Path(f"{path_subcell}/solution_pointwise")).scale_to_fit_height(1.5)
        yoda_pointwise = ImageMobject(Path(f"{path_subcell}/yoda_pointwise")).scale_to_fit_height(1.5)
        solution_avg = ImageMobject(Path(f"{path_subcell}/solution_avg")).scale_to_fit_height(1.5)
        yoda_avg = ImageMobject(Path(f"{path_subcell}/yoda_avg20.png")).scale_to_fit_height(1.5)

        # --------- reconstruction column ---------- #
        se = Text("State estimation", font_size=SMALL_FS, slant=ITALIC, color=COLOR_SOLUTION, should_center=True)
        seeq = MathTex(r"\tilde{u} = R(z) \;\; R : \mathbb{R}^m \rightarrow V",
                       substrings_to_isolate=["z", r"\tilde{u}"],
                       tex_to_color_map={"z": COLOR_MEASUREMENTS, r"\tilde{u}": COLOR_APPROXIMATION},
                       font_size=MEDIUM_FS)
        pe = Text("Parameter estimation", font_size=SMALL_FS, slant=ITALIC, color=COLOR_PARAMS,
                  should_center=True)
        peeq = MathTex(r"\tilde{y} = R(z) \;\; R : \mathbb{R}^m \rightarrow \mathbb{R}^d",
                       substrings_to_isolate=["z", r"\tilde{y}"],
                       tex_to_color_map={"z": COLOR_MEASUREMENTS, "y": COLOR_APPROXIMATION},
                       font_size=MEDIUM_FS)
        rec_solution = ImageMobject(Path(f"{path_subcell}/solution")).scale_to_fit_height(1.5)
        rec_image = ImageMobject(Path(f"{path_subcell}/yoda_approx_{min_n}.png")).scale_to_fit_height(1.5)

        # -------------- -------------- -------------- #
        # Position objects
        buff_horizontal = 0.25

        utex.next_to(title, DOWN, buff=BUFF_HALF).shift(ThreeColumns_dx * LEFT)

        # pdes
        text_pdes.next_to(utex, DOWN, buff=BUFF_HALF)
        pdetex.next_to(text_pdes, DOWN, buff=BUFF_QUARTER)
        ytex.next_to(pdetex, DOWN, buff=BUFF_QUARTER)
        diffusion.next_to(text_diffusion, DOWN, buff=BUFF_QUARTER)
        solution.next_to(Group(diffusion, text_diffusion), RIGHT, buff=buff_horizontal)
        group_diffusion = Group(text_diffusion, diffusion, solution)
        group_diffusion.next_to(ytex, DOWN, buff=BUFF_HALF)
        pde_rectangle = SurroundingRectangle(Group(text_pdes, pdetex, ytex, group_diffusion), color=PDE_COLOR,
                                             corner_radius=0.2)

        # image
        # uimage.next_to(text_image, DOWN, buff=BUFF_HALF)
        # image.next_to(Group(text_image, uimage), RIGHT, buff=buff_horizontal)
        # image_group = Group(uimage, image, text_image)
        yoda_img.next_to(text_image, RIGHT, buff=buff_horizontal)
        image_group = Group(yoda_img, text_image)
        image_group.next_to(group_diffusion, DOWN, buff=BUFF_HALF)
        image_rectangle = SurroundingRectangle(image_group, color=IMAGE_COLOR, corner_radius=0.2)

        # measurements
        tex_z.next_to(title, DOWN, buff=BUFF_HALF)

        solution_pointwise.next_to(tex_pointwise, DOWN, buff=BUFF_QUARTER).shift((buff_horizontal / 2 + 0.75) * LEFT)
        yoda_pointwise.next_to(tex_pointwise, DOWN, buff=BUFF_QUARTER).shift((buff_horizontal / 2 + 0.75) * RIGHT)
        # yoda_pointwise.next_to(solution_pointwise, RIGHT, buff=buff_horizontal)
        # Group(yoda_pointwise, solution_pointwise).next_to(tex_pointwise, DOWN, buff=BUFF_QUARTER)
        print("height", yoda_pointwise.height)
        yoda_pointwise.set_y(solution_pointwise.get_y() + 1.325)

        tex_avg.next_to(Group(yoda_pointwise, solution_pointwise), DOWN, buff=BUFF_HALF)
        yoda_avg.next_to(solution_avg, RIGHT, buff=buff_horizontal)
        Group(yoda_avg, solution_avg).next_to(tex_avg, DOWN, buff=BUFF_HALF)

        (Group(tex_pointwise, solution_pointwise, tex_avg, yoda_avg, solution_avg)
         .next_to(tex_z, DOWN, buff=BUFF_HALF))

        hsol = get_h_group(solution_avg, 10)
        himg = get_h_group(yoda_avg, 20)

        # inverse problems
        se.next_to(title, DOWN, buff=BUFF_HALF).shift(ThreeColumns_dx * RIGHT)
        seeq.next_to(se, DOWN, buff=BUFF_HALF)

        rec_image.next_to(rec_solution, RIGHT, buff=buff_horizontal)
        Group(rec_solution, rec_image).next_to(seeq, DOWN, buff=BUFF_HALF)

        pe.next_to(Group(rec_solution, rec_image), DOWN, buff=BUFF_ONE)
        peeq.next_to(pe, DOWN, buff=BUFF_HALF)

        Group(se, seeq, rec_image, rec_solution, pe, peeq).set_y(CENTER_Y)

        # -------------- -------------- -------------- #
        # Slides
        self.next_slide()
        self.play(
            self.update_slide_number(),
            self.update_main_title(title),
            self.fade_out_old_elements()
        )
        self.play(
            Write(utex)
        )

        self.next_slide()
        self.play(
            Write(text_pdes),
            Write(pdetex)
        )

        self.next_slide()
        self.play(
            Write(ytex)
        )

        self.next_slide()
        self.play(
            Write(text_diffusion),
            Indicate(pdetex),
            FadeIn(diffusion, target_position=pdetex.get_center(), scale=0.25)
        )

        self.next_slide()
        uelement = get_sub_objects(diffusion, [-4])
        self.play(
            Indicate(uelement),
            FadeIn(solution, target_position=uelement.get_center(), scale=0.25),
            Create(pde_rectangle)
        )

        self.next_slide()
        self.play(
            Write(text_image),
            # Write(uimage),
        )

        self.next_slide()
        # uelement = get_sub_objects(uimage, [0])
        self.play(
            # FadeIn(image, target_position=uelement.get_center(), scale=0.25),
            FadeIn(yoda_img),
            Create(image_rectangle)
        )

        self.next_slide()
        self.play(
            Write(tex_z),
        )

        self.next_slide()
        self.play(
            Write(tex_pointwise),
        )

        self.next_slide()
        self.play(
            FadeIn(solution_pointwise),
            FadeIn(yoda_pointwise),
        )

        self.next_slide()
        self.play(
            Write(tex_avg),
        )

        self.next_slide()
        self.play(
            FadeIn(solution_avg),
            FadeIn(yoda_avg),
            FadeIn(hsol, himg)
        )

        self.next_slide()
        self.play(
            Write(se),
            Write(seeq),
        )

        self.next_slide()
        self.play(
            FadeIn(rec_solution),
            FadeIn(rec_image),
        )

        self.next_slide()
        self.play(
            Write(pe),
            Write(peeq),
        )

        return {"tex_z": tex_z, "seeq": seeq, "rec_image": rec_image, "yoda_img": yoda_img,
                "yoda_pointwise": yoda_pointwise, "yoda_avg": yoda_avg}
