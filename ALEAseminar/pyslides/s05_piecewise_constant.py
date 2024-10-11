from collections import namedtuple

from ALEAseminar.config import *
from ALEAseminar.pyslides.s04_recontrucrion_from_cell_averages import ConvergencePLotLayout
from ALEAseminar.support_data import path_subcell
from lib.utils import MySlide, get_sub_objects

ModelData = namedtuple("ModelData", ["name", "x_values", "y_values", "y_values_fit", "rate", "color"])
PIECEWISE_COLOR = YELLOW  # #FFFF00
LVIRA_COLOR = RED  # #FC6255
AEROS_2_COLOR = BLUE  # #58C4DD
QUADRATIC_COLOR = GREEN  # #83C167
QUARTIC_COLOR = PURPLE  # #CAA3E8

CIRCLE_COLOR = YELLOW
VERTEX_COLOR = BLUE

name2filename_name_dict = {"Piecewise constant": "piecewise_constant", "LVIRA": "linear_obera_w",
                           "OBERA": "quadratic_obera_non_adaptive", "AEROS2": "quadratic_aero",
                           "AEROS4": "quartic_aero"}


def create_convergence_plot_objects(name, layout):
    img = ImageMobject(f"{path_subcell}/Convergence_HighOrderModels_10_20_{name2filename_name_dict[name]}").scale(0.75)
    xlab = MathTex(r"1/h").next_to(img, DOWN, buff=0.1)
    ylab = MathTex(r"\|u-\tilde u \|_{L^1}").next_to(img, LEFT)
    get_sub_objects(ylab, [1]).set_color(COLOR_SOLUTION)
    get_sub_objects(ylab, [3, 4]).set_color(COLOR_APPROXIMATION)
    return Group(img, xlab, ylab).move_to(layout.center_x_grid).set_y(layout.m_tex.get_y(), direction=UP)


# TODO: Put true values
pc_x_values = np.unique(np.logspace(1, 2, num=10, dtype=int))
pc_y_values = pc_x_values ** (-1 / 2)
pc_y_values_fit = pc_x_values ** (-1 / 2)
PIECEWISE_DATA = ModelData(name="Piecewise constant", x_values=pc_x_values, y_values=pc_y_values,
                           y_values_fit=pc_y_values_fit, rate=1, color=PIECEWISE_COLOR)

lvira_x_values = pc_x_values
lvira_y_values = lvira_x_values ** (-2.0 / 2)
lvira_y_values_fit = lvira_x_values ** (-2 / 2)
LVIRA_DATA = ModelData(name="LVIRA", x_values=lvira_x_values, y_values=lvira_y_values, y_values_fit=lvira_y_values_fit,
                       rate=2, color=LVIRA_COLOR)

obera_x_values = pc_x_values
obera_y_values = obera_x_values ** (-3.0 / 2)
obera_y_values_fit = obera_x_values ** (-3.0 / 2)
OBERA_DATA = ModelData(name="OBERA", x_values=obera_x_values, y_values=obera_y_values, y_values_fit=obera_y_values_fit,
                       rate=3, color=QUADRATIC_COLOR)

aeros_2_x_values = pc_x_values
aeros_2_values = 1.5 * aeros_2_x_values ** (-3.0 / 2)
aeros_2_values_fit = 1.5 * aeros_2_x_values ** (-3.0 / 2)
AEROS_2_DATA = ModelData(name="AEROS2", x_values=aeros_2_x_values, y_values=aeros_2_values,
                         y_values_fit=aeros_2_values_fit,
                         rate=3, color=AEROS_2_COLOR)

aeros_4_x_values = pc_x_values
aeros_4_values = aeros_4_x_values ** (-5.0 / 2)
aeros_4_values_fit = aeros_4_x_values ** (-5.0 / 2)
AEROS_4_DATA = ModelData(name="AEROS4", x_values=aeros_4_x_values, y_values=aeros_4_values,
                         y_values_fit=aeros_4_values_fit,
                         rate=5, color=QUARTIC_COLOR)


def create_grid4convergence_plot(x_values, y_values):
    grid = Axes(
        x_range=[np.floor(np.log10(np.min(x_values))), np.ceil(np.log10(np.max(x_values))), 0.25],
        y_range=[np.floor(np.log10(np.min(y_values))), np.ceil(np.log10(np.max(y_values))), 1],
        # x_length=,
        tips=False,
        axis_config={
            "include_numbers": True,
            # "font_size": 24
        },
        y_axis_config={"scaling": LogBase(custom_labels=True)},
        x_axis_config={"scaling": LogBase(custom_labels=True)},
    )
    y_label = grid.get_y_axis_label(r"\|u-\tilde{u}\|_{L^1}", edge=RIGHT, direction=LEFT, buff=1).next_to(grid, LEFT)
    x_label = grid.get_x_axis_label(r"1/h", edge=UP, direction=DOWN, buff=1).next_to(grid, DOWN)
    return grid, x_label, y_label


def plot_convergence(grid, x_values, y_values, y_values_rate, color):
    graph = grid.plot_line_graph(
        x_values=x_values, y_values=y_values_rate,
        line_color=color,
        add_vertex_dots=False,
        stroke_width=2
    )
    points = grid.plot_line_graph(
        x_values=x_values, y_values=y_values,
        vertex_dot_style=dict(stroke_width=1, fill_color=color),
        stroke_width=0
    )
    return graph, points


# def create_convergence_plot_objects(models: List[ModelData], layout):
#     all_x_values = list(itertools.chain(*[x_values for _, x_values, _, _, _, _ in models]))
#     all_y_values = list(itertools.chain(*[y_values for _, _, y_values, _, _, _ in models]))
#
#     grid, x_label, y_label = create_grid4convergence_plot(
#         x_values=all_x_values, y_values=all_y_values
#     )
#     graphs = dict()
#     points = dict()
#     order = dict()
#     for model_name, x_values, y_values, y_values_fit, rate, color in models:
#         graphs[model_name], points[model_name] = plot_convergence(grid, x_values, y_values=y_values,
#                                                                   y_values_rate=y_values_fit, color=color)
#
#     vg = VGroup(grid, x_label, y_label, *list(graphs.values()), *list(points.values())).scale(0.5)
#
#     rate_dict = {
#         1: r'\sim h',
#         2: r'\sim h^2',
#         3: r'\sim h^3',
#         4: r'\sim h^4',
#         5: r'\sim h^5',
#     }
#     for model_name, _, _, _, rate, color in models:
#         order[model_name] = (MathTex(rate_dict[rate],
#                                      color=color, font_size=EQ_FONT_SIZE)
#                              .next_to(points[model_name], RIGHT, aligned_edge=DOWN))
#     plot_group = Group(*list(order.values()), vg).move_to(layout.m_tex, aligned_edge=UP)
#     shift_to(plot_group, position=layout.center_x_grid,
#              coordinate="x")
#     return grid, x_label, y_label, points, graphs, order, plot_group


class PiecewiseConstantSlides(MySlide):

    def construct(self, objects_from_previous_slides):
        title = Title(r"Interface reconstruction: linear approach", font_size=STITLE_FS)
        layout = ConvergencePLotLayout(title)
        singular = objects_from_previous_slides["singular"]

        # -------------- -------------- -------------- #
        #   Piecewise constant approximation
        self.next_slide()
        # grid, x_label, y_label, points, graphs, order, plot_group = create_convergence_plot_objects(
        #     models=[PIECEWISE_DATA], layout=layout)
        plot_group_pwc = create_convergence_plot_objects("Piecewise constant", layout=layout)

        exp_citation = Text("[A. Cohen, M. Dolbeault, O. Mula, A. Somacal, 2023]",
                            font_size=CITATION_FONT_SIZE,
                            color=PIECEWISE_COLOR).set_x(plot_group_pwc.get_x()).set_y(-H + BUFF_HALF)

        self.play(
            self.update_main_title(title),
            self.update_slide_number(),
            FadeOut(singular),
            FadeIn(plot_group_pwc),
            Write(exp_citation)
            # FadeIn(grid, x_label, y_label),
            # Create(points["Piecewise constant"]),
        )

        # self.next_slide()
        # self.play(
        #     Create(graphs["Piecewise constant"]),
        # )
        # self.play(Write(order["Piecewise constant"]), Write(exp_citation))

        return {"exp_citation": exp_citation, "plot_group": plot_group_pwc}
