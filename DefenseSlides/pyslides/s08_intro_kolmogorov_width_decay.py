from DefenseSlides.config import *
from lib.utils import MySlide, get_sub_objects

EQ_FONT_SIZE = SMALL_FS


def kolmo_decay_plot(n_max):
    x_values = np.arange(1, n_max + 1)
    y_exp_values = np.exp(-1.2 * x_values)
    y_frac_values = x_values ** (-0.5)
    grid = Axes(
        x_range=[0, n_max, 1],
        y_range=[-7, 1, 2],
        tips=False,
        axis_config={
            "include_numbers": True,
            "font_size": MEDIUM_FS
        },
        y_axis_config={"scaling": LogBase(custom_labels=True)},
        # x_axis_config={"scaling": LinearBase() if t == 0 else LogBase(custom_labels=True)},
    )
    expdecay_graph = grid.plot_line_graph(
        x_values=x_values, y_values=y_exp_values,
        line_color=EXP_DECAY_COLOR,  # vertex_dot_style=dict(stroke_width=3, fill_color=SOLUTION_COLOR),
        add_vertex_dots=False,
        stroke_width=2
    )
    expdecay_points = grid.plot_line_graph(
        x_values=x_values, y_values=y_exp_values * np.sort(np.random.normal(0.5, 0.1, size=n_max)[::-1]),
        vertex_dot_style=dict(stroke_width=1, fill_color=EXP_DECAY_COLOR),
        stroke_width=0
    )
    stepfuncdecay_graph = grid.plot_line_graph(
        x_values=x_values, y_values=y_frac_values,
        line_color=FRACTIONAL_DECAY_COLOR,  # vertex_dot_style=dict(stroke_width=3, fill_color=SOLUTION_COLOR),
        add_vertex_dots=False,
        stroke_width=2
    )
    stepfuncdecay_points = grid.plot_line_graph(
        x_values=x_values, y_values=y_frac_values * np.sort(np.random.normal(1.5, 0.2, size=n_max)[::-1]),
        vertex_dot_style=dict(stroke_width=1, fill_color=FRACTIONAL_DECAY_COLOR),
        stroke_width=0
    )
    y_label = grid.get_y_axis_label(r"d_n(\mathcal{M})_V", edge=RIGHT, direction=LEFT, buff=1).next_to(grid, LEFT)
    y_label = MathTex(r"d_n(\mathcal{M})_V", font_size=BIG_FS).move_to(y_label, aligned_edge=RIGHT)
    x_label = grid.get_x_axis_label(r"n=\text{dim}(V_n)", edge=UP, direction=DOWN, buff=1).next_to(grid, DOWN)
    x_label = MathTex(r"n=\text{dim}(V_n)", font_size=BIG_FS).move_to(x_label, aligned_edge=UP)
    return expdecay_graph, expdecay_points, grid, stepfuncdecay_graph, stepfuncdecay_points, x_label, y_label


class KolmoDecaySlides(MySlide):

    def construct(self, objects_from_previous_slides):
        title = Title(r"Kolmogorov width decay", font_size=STITLE_FS)
        if "kolmowidth" in objects_from_previous_slides:
            kolmowidth = objects_from_previous_slides["kolmowidth"]
        else:
            kolmowidth = MathTex(
                # r"&\textt{dist}(\mathcal{M}, V_n)_V = \sup_{u\in\mathcal{M}}\inf_{v\in V_n}\|u-v\|_V \\"
                r"d_n(\mathcal{M})_V = \inf_{V_n}\text{dist}(\mathcal{M}, V_n)_V",
                # r"d_n(\mathcal{M})_V=\inf_{V_n}\sup_{u\in\mathcal{M}}\inf_{v\in V_n}\|u-v\|_V",
                substrings_to_isolate=["u", "v", r"\mathcal{M}"], font_size=EQ_FONT_SIZE,
                tex_to_color_map={"u": COLOR_SOLUTION, "v": COLOR_APPROXIMATION, r"\mathcal{M}": PDE_COLOR})
            # self.remove_old_elements()
            self.add(kolmowidth)

        # -------------- -------------- -------------- #
        # SLIDE: Kolmogorov width decay
        # -------------- -------------- -------------- #

        # --------- decay rates graph --------- #
        # Create exponential decay for diffusion equation
        scale = 0.45
        n_max = 10
        expdecay_graph, expdecay_points, grid, stepfuncdecay_graph, stepfuncdecay_points, x_label, y_label = kolmo_decay_plot(
            n_max)
        expgroup = VGroup(grid, expdecay_graph, expdecay_points, stepfuncdecay_graph, stepfuncdecay_points, y_label,
                          x_label)
        expgroup.scale(scale).next_to(title, DOWN, buff=BUFF_HALF + BUFF_ONE + kolmowidth.height).shift(3 * LEFT)

        # --------- decay rates --------- #
        expeq = (MathTex(r'd_n(\mathcal{M})_V \leq Ce^{-cn^{1/d}}', color=EXP_DECAY_COLOR, font_size=EQ_FONT_SIZE)
                 .next_to(expdecay_points, RIGHT, aligned_edge=DOWN))
        fraceq = (
            MathTex(r'd_n(\mathcal{M})_V \geq Cn^{-\frac{1}{2}}', color=FRACTIONAL_DECAY_COLOR, font_size=EQ_FONT_SIZE)
            .next_to(stepfuncdecay_points, RIGHT, aligned_edge=UP))

        # --------- citations --------- #
        exp_citation = Text("[A. Cohen, R. DeVore. Acta Numerica, 2015]", font_size=CITATION_FONT_SIZE,
                            color=EXP_DECAY_COLOR)
        frac_citation = Text("[M. Ohlberger, S. Rave. Proceedings of the Conference Algoritmy, 2016]\n"
                             "[C. Greif, K. Urban, Applied Mathematics Letters, 2019]",
                             font_size=CITATION_FONT_SIZE,
                             color=FRACTIONAL_DECAY_COLOR).next_to(exp_citation, RIGHT, aligned_edge=UP)
        citation = VGroup(exp_citation, frac_citation).next_to(grid, DOWN)
        citation.set_x(0)
        citation.set_y(BUFF_HALF - H, direction=DOWN)

        # --------- associated equations --------- #
        x_position = (W + min((fraceq.get_x(direction=RIGHT), expeq.get_x(direction=RIGHT)))) / 2
        text_transport = Text("Hyperbolic PDE", font_size=EQ_FONT_SIZE, color=FRACTIONAL_DECAY_COLOR)
        transport = (MathTex(
            # r"\frac{\partial u}{\partial t}-v \cdot \nabla u=0",
            r"\frac{\partial u}{\partial t}-v \frac{\partial u}{\partial x} =0",
            font_size=EQ_FONT_SIZE,
        ).next_to(text_transport, DOWN))
        get_sub_objects(transport, [1, 8]).set_color(COLOR_SOLUTION)
        get_sub_objects(transport, [6]).set_color(COLOR_PARAMS)

        a = 0.2
        b = 0.25
        l = 0.4
        x_range = (0, 1)
        scale = 3
        f = lambda x: b * (
                sigmoid(1000 * (x - a)) -
                sigmoid(1000 * (x - l * x_range[-1] - a)) +
                sigmoid(1000 * (x_range[-1] + x - a)) -
                sigmoid(1000 * (x_range[-1] + x - l * x_range[-1] - a))
        )
        ci = FunctionGraph(f, x_range=x_range, color=WHITE).next_to(transport, DOWN, BUFF_HALF).scale(
            scale)
        VGroup(text_transport, transport, ci).next_to(fraceq, RIGHT, aligned_edge=DOWN).set_x(x_position).shift(
            0.5 * DOWN)

        text_diffusion = Text("Elliptic PDE", font_size=EQ_FONT_SIZE, color=EXP_DECAY_COLOR)
        diffusion = (MathTex(r"-\text{div} (\diffcoef \nabla u)=f",
                             font_size=EQ_FONT_SIZE,
                             tex_to_color_map={r"\diffcoef": COLOR_PARAMS})
                     .next_to(text_diffusion, DOWN))
        get_sub_objects(diffusion, [-4]).set_color(COLOR_SOLUTION)
        kappa = MathTex(r"\diffcoef (x,y)=\overline{a}(x) + \sum_{j=1}^d \yj \psi_j(x)",
                        font_size=EQ_FONT_SIZE,
                        tex_to_color_map={r"\diffcoef": COLOR_PARAMS, "\yj": COLOR_PARAMS}).next_to(diffusion, DOWN,
                                                                                                    BUFF_QUARTER)
        get_sub_objects(kappa, [4]).set_color(COLOR_PARAMS)
        Group(text_diffusion, diffusion, kappa).next_to(expeq, RIGHT, aligned_edge=UP).set_x(x_position)

        # -------------- -------------- -------------- #
        #   Decay rates
        self.next_slide()
        self.play(
            self.fade_out_old_elements(exept=[kolmowidth]),
            self.update_slide_number(),
            self.update_main_title(title)
        )
        self.play(
            kolmowidth.animate.next_to(title, DOWN, buff=BUFF_ONE).set_font_size(MEDIUM_FS),
        )
        self.play(FadeIn(grid, y_label, x_label))

        # -------------- -------------- -------------- #
        #   dots
        self.next_slide()
        self.play(Create(expdecay_points), Write(diffusion), Write(text_diffusion), Write(kappa), run_time=2)

        # -------------- -------------- -------------- #
        #   tendency
        self.next_slide()
        self.play(Create(expdecay_graph))
        self.play(Write(expeq), Write(exp_citation))

        # -------------- -------------- -------------- #
        #   dots
        self.next_slide()
        self.play(Create(stepfuncdecay_points), Write(transport), Write(text_transport), Create(ci), run_time=2)

        # -------------- -------------- -------------- #
        #   tendency
        self.next_slide()
        self.play(Create(stepfuncdecay_graph))
        self.play(Write(fraceq), Write(frac_citation))

        return dict()
