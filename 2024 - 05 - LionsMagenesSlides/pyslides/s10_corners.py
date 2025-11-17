from matplotlib import pyplot as plt

from config import *
from pyslides.s04_recontrucrion_from_cell_averages import path_subcell, ConvergencePLotLayout
from pyslides.s08_aeros import aeros_stencil_animation_objects, STENCIL_STROKE_WIDTH, \
    STENCIL_COLOR, get_scale_from_desired_width, GRID_COLOR, CELL_T_COLOR

from lib.utils import MySlide, create_grid, create_column_grid, create_column_rectangles

path_corners_images = Path(path_subcell, "Corners", "imageShapesVertexjpg")

AVROS_COLOR = autumn_yellow
TEM_COLOR = RED


def save_fig_without_white(filename):
    plt.gca().set_axis_off()
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.margins(0, 0)
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.savefig(filename, bbox_inches='tight', pad_inches=0, transparent=True)
    plt.close()


class VertexClassAnimation:
    def __init__(self, theta_1, theta_2, scale=0.5):
        self.scale = scale
        self.rotation_center = ORIGIN
        self.dot_center = Dot(self.rotation_center)
        self.theta_1_tracker = ValueTracker(theta_1)
        self.theta_2_tracker = ValueTracker(theta_2)
        self.line_ref = Line(self.rotation_center, 2 * RIGHT)
        self.line_1 = Line(self.rotation_center, 2 * RIGHT).rotate(
            self.theta_1_tracker.get_value() * DEGREES, about_point=self.rotation_center
        )
        self.line_2 = Line(self.rotation_center, 2 * RIGHT).rotate(
            self.theta_2_tracker.get_value() * DEGREES, about_point=self.rotation_center
        )
        self.theta_1 = Angle(self.line_ref, self.line_1, radius=0.5, other_angle=False)
        self.theta_2 = Angle(self.line_ref, self.line_2, radius=0.7, other_angle=True)

        self.txt_theta_1 = MathTex(r"\theta_1").move_to(
            Angle(
                self.line_ref, self.line_1, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
            ).point_from_proportion(0.5)
        )
        self.txt_theta_2 = MathTex(r"\theta_2").move_to(
            Angle(
                self.line_ref, self.line_2, radius=0.7 + 3 * SMALL_BUFF, other_angle=True
            ).point_from_proportion(0.5)
        )

        self.x0y0 = MathTex(r"(x_0, y_0)").move_to(self.dot_center).shift(DOWN)
        # (Group(self.line_1, self.line_2, self.dot_center, self.theta_1, self.theta_2, self.txt_theta_1,
        #        self.txt_theta_2, self.x0y0)
        #  .scale(self.scale).set_y(CENTER_Y).set_x(0))

    def add_updaters(self):
        self.line_1.add_updater(
            lambda x: x.become(self.line_ref.copy()).rotate(
                self.theta_1_tracker.get_value() * DEGREES, about_point=self.rotation_center
            )
        )
        self.line_2.add_updater(
            lambda x: x.become(self.line_ref.copy()).rotate(
                self.theta_2_tracker.get_value() * DEGREES, about_point=self.rotation_center
            )
        )

        self.theta_1.add_updater(
            lambda x: x.become(Angle(self.line_ref, self.line_1, radius=0.5, other_angle=False))
        )
        self.theta_2.add_updater(
            lambda x: x.become(Angle(self.line_ref, self.line_2, radius=0.7, other_angle=True))
        )

        self.txt_theta_1.add_updater(
            lambda x: x.move_to(
                Angle(
                    self.line_ref, self.line_1, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
                ).point_from_proportion(0.5)
            )
        )
        self.txt_theta_2.add_updater(
            lambda x: x.move_to(
                Angle(
                    self.line_ref, self.line_2, radius=0.7 + 3 * SMALL_BUFF, other_angle=True
                ).point_from_proportion(0.5)
            )
        )

    def get_initial_animation(self):
        return [
            Create(self.line_1),
            Create(self.line_2),
            Create(self.theta_1),
            Create(self.theta_2),
            Write(self.txt_theta_1),
            Write(self.txt_theta_2),
            Write(self.x0y0),
            Create(self.dot_center)
        ]

    def get_remove_animation(self):
        return [
            FadeOut(self.line_1),
            FadeOut(self.line_2),
            FadeOut(self.theta_1),
            FadeOut(self.theta_2),
            FadeOut(self.txt_theta_1),
            FadeOut(self.txt_theta_2),
            FadeOut(self.x0y0),
            FadeOut(self.dot_center)
        ]

    def animate_change_angles(self, theta_1, theta_2):
        return [
            self.theta_1_tracker.animate.set_value(theta_1),
            self.theta_2_tracker.animate.set_value(theta_2)
        ]


class CornerSlides(MySlide):

    def construct(self, objects_from_previous_slides):
        title = Title(r"Corners", font_size=STITLE_FS)
        layout = ConvergencePLotLayout(title)

        # -------------- -------------- -------------- #
        #   Corners
        example_corner_image1 = ImageMobject(Path(f"{path_corners_images}/HandVertex.jpg")).scale_to_fit_height(
            2).set_y(CENTER_Y)
        example_corner_image2 = (ImageMobject(Path(f"{path_corners_images}/Polygon.jpg"))
                                 .scale_to_fit_height(2).next_to(example_corner_image1, RIGHT, buff=BUFF_ONE))
        example_corner_image3 = (ImageMobject(Path(f"{path_corners_images}/ShapesVertex.jpg"))
                                 .scale_to_fit_height(2).next_to(example_corner_image1, LEFT, buff=BUFF_ONE))

        self.next_slide()
        self.play(
            self.fade_out_old_elements(),
            self.update_main_title(title),
            self.update_slide_number(),
            FadeIn(example_corner_image1, example_corner_image2, example_corner_image3),
        )

        self.next_slide()
        vn_space = MathTex(
            r"V_n := \{ v_{\mu}: \mu \in \R^n \}",
            font_size=EQ_FONT_SIZE).next_to(title, DOWN, buff=BUFF_HALF)
        vn_space_vertex = MathTex(
            r"V_4 := \{ v_{\mu}: \mu = (x_0, y_0, \theta_1, \theta_2) \}",
            font_size=EQ_FONT_SIZE).next_to(title, DOWN, buff=BUFF_HALF)
        vertex_animation = VertexClassAnimation(theta_1=160, theta_2=-25)

        self.play(
            FadeOut(example_corner_image1, example_corner_image2, example_corner_image3),
            Write(vn_space)
        )

        self.next_slide()
        self.play(
            ReplacementTransform(vn_space, vn_space_vertex)
        )
        self.play(
            *vertex_animation.get_initial_animation()
        )

        self.next_slide()
        vertex_animation.add_updaters()
        self.play(
            *vertex_animation.animate_change_angles(theta_1=200, theta_2=-50),
        )

        self.next_slide()
        txt_aeros_vertex = (Tex(r"AEROS Vertex", font_size=EQ_FONT_SIZE, color=AVROS_COLOR)
                            .next_to(vn_space_vertex, DOWN, buff=BUFF_HALF).shift(TwoColumns_dx * LEFT))
        txt_tem = (Tex(r"Tangent Extension Method (TEM)", font_size=EQ_FONT_SIZE, color=TEM_COLOR)
                   .next_to(vn_space_vertex, DOWN, buff=BUFF_HALF).shift(TwoColumns_dx * RIGHT))
        self.play(
            self.fade_out_old_elements(vn_space_vertex),
            # *vertex_animation.get_remove_animation(),
        )
        self.play(
            Write(txt_aeros_vertex),
            Write(txt_tem)
        )

        # -------------- -------------- -------------- #
        #   AVROS
        x0 = ValueTracker(-0.25)
        function = lambda x: (0.25 * (x - x0.get_value()) * (x < x0.get_value()) +
                              -0.5 * (x - x0.get_value()) * (x >= x0.get_value()))
        (approx_column_avg, approx_function, averages, cell_T, cell_T_avg, column_avg, curve, curve_approx,
         graph_group, grid, grid_avg, lower_part, scale, stencil, stencil_avg, stencil_avg_matrix, stencil_2,
         stencil_2_avg, stencil_size, txt_cell_T, upper_part, values) = aeros_stencil_animation_objects(
            layout, function, grid_shape=(7, 6), stencil_size=(4, 4), stencil_2_size=(3, 3), cmap="coolwarm",
            width=2)

        (Group(cell_T, curve, grid, lower_part, stencil, stencil_2, upper_part)
         .next_to(txt_aeros_vertex, DOWN, buff=BUFF_HALF))

        # AEROS column averages
        column_stencil = (create_column_grid(
            stencil_size, rows=False, color=STENCIL_COLOR, stroke_width=2 * STENCIL_STROKE_WIDTH, fill_opacity=0.25)
                          .scale(scale).move_to(stencil, aligned_edge=DL))
        r, t = create_column_rectangles(column_avg, cmap=STENCIL_COLOR, stroke_width=1, fill_opacity=0.5)
        group_col = Group(r, t).scale(scale)
        r_fixed = r.copy().move_to(column_stencil, aligned_edge=DL)
        group_col.next_to(r_fixed, RIGHT, buff=BUFF_ONE)

        self.next_slide(auto_next=True)
        self.play(
            Create(grid),
            FadeIn(curve),
            FadeIn(lower_part),
            FadeIn(upper_part),
            FadeIn(stencil_2),
            FadeIn(cell_T)
        )
        self.next_slide()

        self.next_slide()
        self.play(
            ReplacementTransform(stencil_2, stencil)
        )

        self.next_slide()
        self.play(
            FadeOut(stencil),
            FadeIn(column_stencil),
            FadeIn(group_col),
            FadeIn(r_fixed)
        )

        self.next_slide()
        self.play(
            FadeIn(stencil),
            FadeOut(column_stencil),
            FadeOut(group_col),
            FadeOut(r_fixed),
            x0.animate.set_value(0.3),
        )

        #   AVROS problem
        txt_avros_problems = BulletedList("More than $1$ posibility to test",
                                          r"Can not deal with orientation change").next_to(grid, DOWN, buff=BUFF_HALF)
        # vertex_animation = VertexClassAnimation(theta_1=180, theta_2=-90)
        citation = Text("[B. Després, H. Jourdren, Journal of Computational Physics, 2020]",
                        font_size=CITATION_FONT_SIZE, color=TEM_COLOR).next_to(txt_avros_problems, DOWN,
                                                                               buff=BUFF_HALF)
        self.next_slide()
        self.play(
            # *vertex_animation.get_initial_animation(),
            Write(txt_avros_problems),
        )

        self.next_slide()
        self.play(
            Write(citation)
        )

        # -------------- -------------- -------------- #
        #   TEM

        grid_shape = (7, 7)
        width = 2
        y0 = ValueTracker(0.2)
        function_right = lambda x: y0.get_value() + 0.1 * x
        function_left = lambda x: y0.get_value() + 1 * x
        function_tem = lambda x: function_right(x) * (x > 0) + function_left(x) * (x <= 0)
        scale = get_scale_from_desired_width(width=width, grid_shape=grid_shape)
        grid_tem = create_grid(shape=grid_shape, stroke_width=1, color=GRID_COLOR)
        vertex_cell = Rectangle(height=1, width=1, stroke_width=0, color=CELL_T_COLOR, fill_opacity=0.35).move_to(
            grid_tem).shift(0.5 * LEFT * (1 - grid_shape[1] % 2)).shift(0.5 * DOWN * (1 - grid_shape[0] % 2))
        cell_T_1 = vertex_cell.copy().shift(RIGHT)
        cell_T_2 = vertex_cell.copy().shift(DL)
        vertex_cell.set_color(STENCIL_COLOR)

        stencil_tem_1 = create_grid(shape=(3, 3), stroke_width=STENCIL_STROKE_WIDTH, color=STENCIL_COLOR).move_to(
            cell_T_1)
        stencil_tem_2 = create_grid(shape=(3, 3), stroke_width=STENCIL_STROKE_WIDTH, color=STENCIL_COLOR).move_to(
            cell_T_2)
        stencil_tem_1_shifted = stencil_tem_1.copy().shift(RIGHT)
        stencil_tem_2_shifted = stencil_tem_2.copy().shift(LEFT)
        cell_T_1_shifted = cell_T_1.copy().shift(RIGHT)
        cell_T_2_shifted = cell_T_2.copy().shift(LEFT)

        x_range = [-grid_shape[1] / 2, grid_shape[1] / 2]
        y_range = [-grid_shape[0] / 2, grid_shape[0] / 2]
        curve_tem = FunctionGraph(
            function_tem,
            x_range=x_range,
            stroke_width=4 * scale,
            color=WHITE,
            fill_opacity=0
        )

        curve_approx_on_T_1 = FunctionGraph(
            function_right,
            x_range=[0.5, 1.5],
            stroke_width=4 * scale,
            color=COLOR_APPROXIMATION,
            fill_opacity=0
        )
        curve_approx_on_T_2 = FunctionGraph(
            function_left,
            x_range=[-1.5, -0.5],
            stroke_width=4 * scale,
            color=COLOR_APPROXIMATION,
            fill_opacity=0
        )
        curve_approx_on_T_1_extend = FunctionGraph(
            function_right,
            x_range=[-0.5, 1.5],
            stroke_width=4 * scale,
            color=COLOR_APPROXIMATION,
            fill_opacity=0
        )
        curve_approx_on_T_2_extend = FunctionGraph(
            function_left,
            x_range=[-1.5, 0.5],
            stroke_width=4 * scale,
            color=COLOR_APPROXIMATION,
            fill_opacity=0
        )
        curve_approx_on_T_1_extend_to_point = FunctionGraph(
            function_right,
            x_range=[0, 1.5],
            stroke_width=4 * scale,
            color=COLOR_APPROXIMATION,
            fill_opacity=0
        )
        curve_approx_on_T_2_extend_to_point = FunctionGraph(
            function_left,
            x_range=[-1.5, 0],
            stroke_width=4 * scale,
            color=COLOR_APPROXIMATION,
            fill_opacity=0
        )

        curve_approx_1_final = FunctionGraph(
            function_right,
            x_range=[0, 0.5],
            stroke_width=6 * scale,
            color=COLOR_APPROXIMATION,
            fill_opacity=0
        )
        curve_approx_2_final = FunctionGraph(
            function_left,
            x_range=[-0.5, 0],
            stroke_width=6 * scale,
            color=COLOR_APPROXIMATION,
            fill_opacity=0
        )
        graph_group = Group(cell_T_1, cell_T_2, grid_tem, curve_tem, curve_approx_on_T_1, curve_approx_on_T_2,
                            curve_approx_on_T_1_extend, curve_approx_on_T_2_extend, curve_approx_on_T_2_extend_to_point,
                            curve_approx_on_T_1_extend_to_point, curve_approx_1_final, curve_approx_2_final,
                            vertex_cell, cell_T_1_shifted, cell_T_2_shifted, stencil_tem_1, stencil_tem_2,
                            stencil_tem_1_shifted, stencil_tem_2_shifted).scale(
            scale)
        graph_group.next_to(txt_tem, DOWN, buff=BUFF_ONE).set_y(grid.get_y())

        self.next_slide(auto_next=True)
        self.play(
            # *vertex_animation.get_remove_animation(),
            Create(curve_tem),
            Create(grid_tem),
            FadeIn(cell_T_1),
            FadeIn(cell_T_2),
        )
        self.next_slide()

        self.next_slide()
        self.play(
            Create(curve_approx_on_T_1),
            Create(curve_approx_on_T_2),
        )

        self.next_slide()
        self.play(
            ReplacementTransform(curve_approx_on_T_1, curve_approx_on_T_1_extend),
            ReplacementTransform(curve_approx_on_T_2, curve_approx_on_T_2_extend),
        )

        self.next_slide()
        center = Dot(np.array([grid_tem.get_x(), grid_tem.get_y() + y0.get_value() * scale, 0]),
                     radius=DEFAULT_DOT_RADIUS / 2, color=COLOR_APPROXIMATION)
        self.play(
            FadeIn(center),
            ReplacementTransform(curve_approx_on_T_1_extend, curve_approx_on_T_1_extend_to_point),
            ReplacementTransform(curve_approx_on_T_2_extend, curve_approx_on_T_2_extend_to_point),
        )

        self.next_slide()
        self.play(
            FadeIn(center),
            ReplacementTransform(curve_approx_on_T_1_extend_to_point, curve_approx_1_final),
            ReplacementTransform(curve_approx_on_T_2_extend_to_point, curve_approx_2_final),
        )

        self.next_slide()
        self.play(
            FadeIn(stencil_tem_1),
            FadeIn(stencil_tem_2)
        )
        self.next_slide()
        self.play(
            Indicate(vertex_cell)
        )

        self.next_slide()
        self.play(
            ReplacementTransform(stencil_tem_1, stencil_tem_1_shifted),
            ReplacementTransform(stencil_tem_2, stencil_tem_2_shifted),
            ReplacementTransform(cell_T_1, cell_T_1_shifted),
            ReplacementTransform(cell_T_2, cell_T_2_shifted),
        )

        self.next_slide()
        txt_tem_problems = (
            BulletedList(r"Exact only if both sides of vertex are straight lines", font_size=EQ_FONT_SIZE)
            .next_to(grid_tem, DOWN, buff=BUFF_HALF))
        self.play(
            Write(txt_tem_problems),
        )
