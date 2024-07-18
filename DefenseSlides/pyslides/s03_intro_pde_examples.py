from DefenseSlides.config import *
from DefenseSlides.pyslides.s04_intro_two_problems import get_param_matrix, get_diff_eq_images
from lib.utils import MySlide, get_sub_objects


class PDEExamplesSlides(MySlide):

    def construct(self, objects_from_previous_slides):
        # VDict({"pdetex": pdetex, "utex": utex, "ytex": ytex})
        if "pdetex" not in objects_from_previous_slides:
            pdetex = MathTex(r"\mathcal{P}(u, y)=0",
                             tex_to_color_map={"y": COLOR_PARAMS, "\mathcal{P}": PDE_COLOR, "u": COLOR_SOLUTION})
            ytex = (MathTex(r"\y:=\{y_1, \dots, y_d\} \in \R^d",
                            substrings_to_isolate=[r"\y", r"y_1", r"y_d"],
                            tex_to_color_map={r"\y": COLOR_PARAMS, r"y_1": COLOR_PARAMS, r"y_d": COLOR_PARAMS},
                            font_size=MEDIUM_FS, ))
            utex = (MathTex(r"u \in V", tex_to_color_map={r"u": COLOR_SOLUTION},
                            substrings_to_isolate=[r"u"], font_size=MEDIUM_FS, )
                    .next_to(ytex, DOWN, BUFF_HALF))
            objects_from_previous_slides = VDict({"pdetex": pdetex, "utex": utex, "ytex": ytex})

        # -------------- -------------- -------------- #
        # SLIDE 4: PDE Examples
        # -------------- -------------- -------------- #
        EQ_FONT_SIZE = MEDIUM_FS

        # -------------- -------------- -------------- #
        # PDE Transport
        title = Title("Example PDEs", font_size=STITLE_FS)
        text_transport = (Text("Transport PDE", font_size=EQ_FONT_SIZE,
                               t2c={"PDE": PDE_COLOR}).next_to(title, DOWN, buff=BUFF_HALF)
                          .shift(TwoColumns_dx * LEFT))
        transport = (MathTex(r"\frac{\partial u}{\partial t}-v \cdot \nabla u=0",
                             font_size=EQ_FONT_SIZE,
                             ).next_to(text_transport, DOWN))
        transport[0][1].set_color(COLOR_SOLUTION)
        transport[0][9].set_color(COLOR_SOLUTION)
        # transport[0][7].set_color(COLOR_PARAMS)
        tparam = transport[0][6].set_color(COLOR_PARAMS)

        self.next_slide()
        self.play(
            self.update_slide_number(),
            self.update_main_title(title),
            self.fade_out_old_elements([objects_from_previous_slides["pdetex"], objects_from_previous_slides["ytex"],
                                        objects_from_previous_slides["utex"]])
        )
        self.play(
            FadeIn(text_transport),
            objects_from_previous_slides["ytex"].animate.set_font_size(SMALL_FS)
            .next_to(title, DOWN, buff=BUFF_HALF * 2),
            objects_from_previous_slides["utex"].animate.set_font_size(SMALL_FS)
            .next_to(title, DOWN, buff=BUFF_HALF),
        )
        self.play(
            ReplacementTransform(objects_from_previous_slides["pdetex"], transport),
        )

        # init_cond = MathTex(r"u_0=g(y)=\sum_{j=1}^d y_j sin(k_j x)",
        #                     font_size=EQ_FONT_SIZE,
        #                     tex_to_color_map={"u_0": PARAMS_COLOR, "y_j": PARAMS_COLOR}).next_to(transport, DOWN)
        v_parameterized = MathTex(r"\vv=\vv(y)=\overline{v} + \sum_{j=1}^d y_j \psi_j",
                                  font_size=EQ_FONT_SIZE,
                                  tex_to_color_map={"u_0": COLOR_PARAMS, "y_j": COLOR_PARAMS,
                                                    r"\vv": COLOR_PARAMS}).next_to(transport, DOWN)
        get_sub_objects(v_parameterized, [4]).set_color(COLOR_PARAMS)

        self.next_slide()
        self.play(
            Indicate(tparam),
            FadeIn(v_parameterized, target_position=tparam, scale=0.5)
        )

        pos = v_parameterized.get_edge_center(DOWN) + DOWN
        positions = [pos + 2.25 * LEFT, pos + DOWN, pos + 2.25 * RIGHT]
        u0 = [
            Ellipse(width=3 * 0.25 / 2, height=1 * 0.25 / 2, fill_opacity=0.5, color=COLOR_PARAMS, stroke_width=1)
            .rotate(35).shift(UR * 0.4),
            Circle(radius=2 * 0.25 / 2, fill_opacity=0.5, color=COLOR_PARAMS, stroke_width=1).shift(UL * 0.4),
            Circle(radius=3 * 0.25 / 2, fill_opacity=0.5, color=COLOR_PARAMS, stroke_width=1).shift(UL * 0.25 / 2)
        ]
        functions = [
            # lambda pos: 1.5 * (0.25 * pos[1] * UP + 0.1 * np.abs(pos[0]) * RIGHT),
            # lambda pos: 1.5 * (0.25 * pos[1] * UP + 0.1 * np.abs(pos[0]) * RIGHT),
            # lambda pos: 1.5 * (0.25 * pos[1] * UP + 0.1 * np.abs(pos[0]) * RIGHT),
            lambda pos: np.array([pos[1], -pos[0], 0]),
            lambda pos: np.array([pos[1], pos[0], 0]),
            lambda pos: np.array([pos[0], pos[1], 0]) / 2,
        ]

        def transport_evolve(u0, function, position):
            x, y, z = position
            vector_field = ArrowVectorField(
                lambda pos: function(pos - np.array(position)),
                x_range=[x - 0.75, x + 0.75, 0.1],
                y_range=[y - 0.75, y + 0.75, 0.1],
                length_func=lambda norm: 0.2 * sigmoid(norm),
                # length_func=lambda norm: 2 * 0.45 * sigmoid(norm - np.sqrt(2) / 2),
                # length_func=lambda norm: norm / 2,
                # length_func=lambda norm: 0.45 * sigmoid(norm - 8 * np.sqrt(2 ** 2 * (0.25 ** 2 + 0.1 ** 2) / 2)),
                color=COLOR_PARAMS
            )

            u0.shift(position)
            ut = u0.copy().set_color(GRAY)
            # Group(vector_field, u0, ut).scale(0.25 / 2).next_to(v_parameterized, DOWN).shift(shift)
            vector_field.nudge(ut, 0.01, 120, pointwise=True)
            ut.add_updater(vector_field.get_nudge_updater(speed=0.35, pointwise=True))
            return vector_field, ut

        vf, ut = zip(*[transport_evolve(u0, func, position) for u0, func, position in
                       zip(u0, functions, positions)])

        self.next_slide()
        self.play(
            Indicate(tparam),
            *[FadeIn(u, target_position=tparam, scale=0.5) for u in u0],
            *[FadeIn(v, target_position=tparam, scale=0.5) for v in vf],
        )

        self.next_slide()
        self.add(*ut)
        self.wait(2)

        # -------------- -------------- -------------- #
        # PDE Diffusion
        text_diffusion = (Text("Diffusion PDE", font_size=EQ_FONT_SIZE, t2c={"PDE": PDE_COLOR})
                          .next_to(title, DOWN, buff=BUFF_HALF)
                          .shift(TwoColumns_dx * RIGHT))
        diffusion = MathTex(r"-\text{div} (\diffcoef \nabla u)=f",
                            font_size=EQ_FONT_SIZE,
                            tex_to_color_map={r"\diffcoef": COLOR_PARAMS}).move_to(
            np.array([text_diffusion.get_x(), transport.get_y(), 0]))
        diffusion[-1][1].set_color(COLOR_SOLUTION)

        self.next_slide()
        [u.remove_updater(up) for u in ut for up in u.get_updaters()]
        self.play(
            FadeIn(text_diffusion),
            FadeIn(diffusion),
        )
        self.next_slide()
        kappa = MathTex(r"\diffcoef (x,y)=\overline{a}(x) + \sum_{j=1}^d \yj \psi_j(x)",
                        font_size=EQ_FONT_SIZE,
                        tex_to_color_map={r"\diffcoef": COLOR_PARAMS, "\yj": COLOR_PARAMS}).move_to(
            np.array([text_diffusion.get_x(), v_parameterized.get_y(), 0]))
        get_sub_objects(kappa, [4]).set_color(COLOR_PARAMS)
        self.play(
            Indicate(diffusion[-2]),
            FadeIn(kappa, target_position=diffusion[-2], scale=0.25)
        )
        self.next_slide()
        piecewiseconstat = MathTex(r"\diffcoef (x,y)=\overline{a}(x) + \sum_{j=1}^d \yj \chi_{\Omega_j}(x)",
                                   font_size=EQ_FONT_SIZE,
                                   tex_to_color_map={r"\diffcoef (x,y)": COLOR_PARAMS, "\yj": COLOR_PARAMS}).shift(
            kappa.get_center())
        omega = (MathTex(r"\Omega = \Omega_1 \cup \dots \cup \Omega_d",
                         font_size=EQ_FONT_SIZE,
                         tex_to_color_map={r"\diffcoef (x,y)": COLOR_PARAMS, "\yj": COLOR_PARAMS})
                 .next_to(piecewiseconstat, DOWN, BUFF_QUARTER))
        self.play(Indicate(kappa[-1]))
        self.play(ReplacementTransform(kappa, piecewiseconstat), FadeIn(omega))
        u = diffusion[-1][1]
        yj = piecewiseconstat[-2]

        def get_diffusion_param_solutions(i, shift):
            param_matrix = (get_param_matrix(i).scale(0.37)
                            .next_to(omega, DOWN, buff=0.2).shift(shift))
            solution = get_diff_eq_images(name="solutions", i=i).scale(0.6).next_to(param_matrix, DOWN, buff=0.2)
            return (FadeIn(param_matrix, target_position=yj, scale=0.5),
                    FadeIn(solution, target_position=u, scale=0.5))

        p, s = zip(*[get_diffusion_param_solutions(i, shift) for i, shift in
                     zip([2, 4, 6], [1.75 * LEFT, 0.25 * DOWN, 1.75 * RIGHT])])

        self.next_slide()
        piecewiseconstat_4 = (MathTex(r"\diffcoef (x,y)=\overline{a}(x) + \sum_{j=1}^4 \yj \chi_{\Omega_j}(x)",
                                      font_size=EQ_FONT_SIZE,
                                      tex_to_color_map={r"\diffcoef (x,y)": COLOR_PARAMS, "\yj": COLOR_PARAMS})
                              .move_to(piecewiseconstat))
        omega_4 = (MathTex(r"\Omega = \Omega_1 \cup  \Omega_2 \cup  \Omega_3 \cup \Omega_4",
                           font_size=EQ_FONT_SIZE,
                           tex_to_color_map={r"\diffcoef (x,y)": COLOR_PARAMS, "\yj": COLOR_PARAMS})
                   .move_to(omega))
        self.play(
            ReplacementTransform(piecewiseconstat, piecewiseconstat_4),
            ReplacementTransform(omega, omega_4),
            Indicate(yj),
            *p
        )

        self.next_slide()
        self.play(
            Indicate(u),
            *s
        )

# t = ValueTracker(0)
# x_range = (0, 2.5)
# scale = 0.5
#
# def transport_equations(f, relative_position, shift, v_direction=(1, 1)):
#     ci = (FunctionGraph(f, color=COLOR_PARAMS, x_range=x_range)
#           .next_to(v_parameterized, relative_position).scale(scale).shift(shift))
#     v = Arrow(start=v_direction[0] * LEFT, end=v_direction[1] * RIGHT, color=COLOR_PARAMS,
#               buff=0.8 * np.abs(np.mean(v_direction))).next_to(ci, UP)
#     vtext = MathTex(r"\vec{v}", color=COLOR_PARAMS).next_to(v, UP, buff=0.1).scale(scale)
#     first_animations = (
#         Indicate(v_parameterized[0]),
#         FadeIn(ci, target_position=v_parameterized[0], scale=0.5),
#     )
#     second_animations = (
#         Indicate(tparam),
#         FadeIn(v, target_position=tparam, scale=0.5),
#         FadeIn(vtext, target_position=tparam, scale=0.5),
#     )
#
#     graph = FunctionGraph(f, color=autumn_white, x_range=x_range).scale(scale).move_to(ci)
#     graph.add_updater(
#         lambda func: func.become(
#             FunctionGraph(f, color=autumn_white, x_range=x_range).scale(scale).move_to(ci)))
#     return first_animations, second_animations, graph
#
# f = lambda x: np.sin(2 * np.pi / x_range[-1] * (x - t.get_value()))
#
# f2 = lambda x: (
#         np.sin(2 * np.pi / x_range[-1] * (x + 2 * t.get_value())) +
#         0.9 * np.cos(2 * np.pi / x_range[-1] * (x + 2 * t.get_value())) +
#         0.5 * np.sin(2 * 2 * np.pi / x_range[-1] * (x + 2 * t.get_value())) +
#         0.2 * np.cos(2 * 2 * np.pi / x_range[-1] * (x + 2 * t.get_value()))
# )
#
# f3 = lambda x: 2 * (
#         sigmoid(100 * (x - t.get_value())) -
#         sigmoid(100 * (x - 0.4 * x_range[-1] - t.get_value())) +
#         sigmoid(100 * (x_range[-1] + x - t.get_value())) -
#         sigmoid(100 * (x_range[-1] + x - 0.4 * x_range[-1] - t.get_value()))
# ) - 1
#
# first_animations1, second_animations1, graph1 = transport_equations(f, relative_position=DOWN, shift=2 * LEFT)
# first_animations2, second_animations2, graph2 = transport_equations(f2, relative_position=1.5 * DOWN, shift=0,
#                                                                     v_direction=(-1.5, -1.5))
# first_animations3, second_animations3, graph3 = transport_equations(f3, relative_position=DOWN, shift=2 * RIGHT)
#
# self.play(*first_animations1, *first_animations2, *first_animations3)
# self.play(FadeIn(graph1, graph2, graph3), *second_animations1, *second_animations2, *second_animations3)
# self.next_slide(loop=True)
# self.play(t.animate.set_value(x_range[-1]), run_time=4)
