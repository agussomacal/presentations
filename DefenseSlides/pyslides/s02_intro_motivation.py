"""

For airfoil flow see 3blue1brown repository: https://github.com/3b1b/videos/blob/master/_2018/div_curl.py
associated to video: https://www.youtube.com/watch?v=rB83DpBJQsE
"""

from DefenseSlides.config import *
from lib.utils import MySlide, get_sub_objects


# Helper functions
def joukowsky_map(z, r=1):
    if z == 0:
        return 0
    return z + r / z


def inverse_joukowsky_map(w):
    u = 1 if w.real >= 0 else -1
    return (w + u * np.sqrt(w ** 2 - 4)) / 2


def derivative(func, dt=1e-7):
    return lambda z: (func(z + dt) - func(z)) / dt


def airfoil_flow_vector_field(point, airfoil_width=0.0, airfoil_vertical_asymmetry=0, center=(0, 0), radius=1):
    z = R3_to_complex(point - np.array(center + (0,)))
    z = inverse_joukowsky_map(z + airfoil_vertical_asymmetry * 1j) + airfoil_width
    return complex_to_R3(derivative(lambda x: joukowsky_map(x, radius))(z).conjugate())


def create_airfoil_streamlines(x_min, x_max, y_min, y_max, delta_y=0.05, airfoil_width=0.0,
                               airfoil_vertical_asymmetry=0, center=(0, 0), radius=1):
    delta_x = (x_max - x_min) * 2  # only the initial points
    return StreamLines(
        lambda point: airfoil_flow_vector_field(point, airfoil_width=airfoil_width,
                                                airfoil_vertical_asymmetry=airfoil_vertical_asymmetry,
                                                center=center, radius=radius),
        x_range=[x_min, x_max, delta_x],
        y_range=[y_min, y_max, delta_y],
        n_repeats=1,
        noise_factor=delta_y,
        stroke_width=2 * delta_y / 0.1,
        virtual_time=2 * (x_max - x_min),
        dt=0.005,
        padding=0.1
    )


class MotivationSlides(MySlide):

    def construct(self, objects_from_previous_slides):
        # -------------- -------------- -------------- #
        # SLIDE 1: systems examples
        # -------------- -------------- -------------- #
        airfoil_img = ImageMobject(f"{images_dir}/airfoil_real.jpg")  # .shift(UP, W/2*RIGHT)
        airfoil_img.height = H
        windmills_img = ImageMobject(f"{images_dir}/windmills.png")  # .shift(UP, W/2*LEFT)
        windmills_img.width = W
        img_group = Group(windmills_img, airfoil_img)
        img_group.arrange()

        self.next_slide()
        self.remove_old_elements()
        self.play(
            FadeIn(img_group),
            self.update_slide_number(),
            self.update_main_title(r"Introduction: motivation")
        )

        # -------------- -------------- -------------- #
        # SLIDE 2: PDE modelling
        # -------------- -------------- -------------- #
        width = 6
        height = 3
        center = windmills_img.get_center()
        radius = 0.5
        airfoil_params = {
            "x_min": center[0] - width / 2, "x_max": center[0] + width / 2,
            "y_min": center[1] - height / 2, "y_max": center[1] + height / 2,
            "delta_y": 0.1,
            "center": center, "radius": radius
        }
        airfoil_0 = create_airfoil_streamlines(**airfoil_params, airfoil_width=0, airfoil_vertical_asymmetry=0)
        modelled = Text(
            "Modelling through a",
            font_size=SMALL_FS, color=autumn_white,
        ).next_to(img_group, DOWN)
        ppde = Text(
            "parametric PDE (Partial differential equation)",
            font_size=SMALL_FS, color=autumn_white,
            t2s={"parametric": ITALIC},
            t2w={"PDE": BOLD},
            t2c={"parametric": COLOR_PARAMS, "PDE": PDE_COLOR},
        ).next_to(modelled, DOWN)

        wing_img = ImageMobject(f"{images_dir}/airplanewing.png").shift(
            windmills_img.get_center())  # .shift(UP, W/2*LEFT)
        self.next_slide()
        self.play(
            FadeIn(modelled, ppde),
        )

        self.next_slide(auto_next=True)
        self.play(
            FadeOut(windmills_img),
            FadeIn(wing_img),
            self.update_slide_number(),
        )
        self.wait(0.5)
        self.play(
            FadeOut(wing_img),
        )
        self.play(
            FadeIn(airfoil_0),
            # FadeIn(group)
        )

        # airfoil_0.start_animation(warm_up=False, flow_speed=1)
        self.next_slide(loop=True)
        airfoil_1 = create_airfoil_streamlines(**airfoil_params, airfoil_width=0.5, airfoil_vertical_asymmetry=0)
        airfoil_2 = create_airfoil_streamlines(**airfoil_params, airfoil_width=0, airfoil_vertical_asymmetry=0)
        # airfoil_3 = create_airfoil_streamlines(x_min=-6, x_max=6, y_min=-3.1, y_max=2.1, delta_y=0.1,
        #                                        airfoil_width=0, airfoil_vertical_asymmetry=0,
        #                                        center=center, radius=radius)
        # self.play(FadeIn(airfoil_0))
        self.play(
            ReplacementTransform(airfoil_0, airfoil_1),
        )
        self.play(
            ReplacementTransform(airfoil_1, airfoil_2),
        )

        # -------------- -------------- -------------- #
        # SLIDE 3: PDE math
        # -------------- -------------- -------------- #
        pdetex = MathTex(r"\mathcal{P}(u, y)=0", font_size=BIG_FS,
                         substrings_to_isolate=[r"y", r"u"],
                         tex_to_color_map={"y": COLOR_PARAMS, "u": COLOR_SOLUTION})
        Ptex = Tex(r"$\mathcal{P}$: Differential operator", tex_to_color_map={r"y": COLOR_PARAMS},
                   font_size=MEDIUM_FS, ).next_to(pdetex, DOWN, BUFF_HALF)
        utex = (MathTex(r"u \in V \, \text{Banach}", tex_to_color_map={r"u": COLOR_SOLUTION},
                        substrings_to_isolate=[r"u"], font_size=MEDIUM_FS, )
                .next_to(Ptex, DOWN, BUFF_HALF))
        ytex = (MathTex(r"\y:=\{y_1, \dots, y_d\} \in \R^d",
                        substrings_to_isolate=[r"\y", r"y_1", r"y_d"],
                        tex_to_color_map={r"\y": COLOR_PARAMS, r"y_1": COLOR_PARAMS, r"y_d": COLOR_PARAMS},
                        font_size=MEDIUM_FS, )
                .next_to(utex, DOWN, BUFF_HALF))
        Group(pdetex, utex, ytex, Ptex).move_to(airfoil_img.get_center())

        # tex_parametric = ppde[0][0:10].copy().next_to(pdetex[0][-4], UP)
        # tex_PDE = ppde[0][12:15].copy().next_to(pdetex[0][0], DOWN)

        params_tex = Tex("parameters", color=COLOR_PARAMS).next_to(get_sub_objects(pdetex, num_chars=[4]), UP)
        self.next_slide()
        self.play(
            FadeOut(airfoil_img),
        )
        self.play(
            FadeIn(pdetex, target_position=ppde.get_center(), scale=0.25),
            Write(params_tex),
            self.update_slide_number(),
        )

        self.next_slide()
        self.play(
            Write(Ptex)
        )

        self.next_slide()
        self.play(
            Write(utex)
        )

        self.next_slide()
        self.play(
            Write(ytex)
        )
        return VDict({"pdetex": pdetex, "utex": utex, "ytex": ytex})
