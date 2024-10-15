from PhDDefense.pyslides.s15_nonlininv_recontrucrion_from_cell_averages import ConvergencePLotLayout
from config import *
from lib.utils import cmap_value2manimcolor, MySlide, create_grid_of_colored_rectangles, create_grid, \
    create_column_grid, create_column_rectangles

GRID_COLOR = GRAY
AEROS_COLOR = special_blue
CELL_T_COLOR = GREEN
ORIENTATION_COLOR = special_green
STENCIL_COLOR = RED
STENCIL_STROKE_WIDTH = 1.5


def cell_average(function, x_lim, y_lim, N=100):
    x = np.linspace(x_lim[0], x_lim[1], num=N)
    y = np.vectorize(function)(x) - y_lim[0]
    y[y >= 1] = 1
    y[y <= 0] = 0
    return np.mean(y)


def grid_averages(grid_shape, function, N=100):
    avg = np.zeros(grid_shape)
    for i in range(grid_shape[1]):
        for j in range(grid_shape[0]):
            avg[j, i] = cell_average(function, x_lim=[i - grid_shape[1] / 2, i + 1 - grid_shape[1] / 2],
                                     y_lim=[j - grid_shape[0] / 2, j + 1 - grid_shape[0] / 2], N=N)
    return avg[::-1, :]


def fit_quadratic_averages(x_range, column_averages):
    return np.linalg.solve(np.diff(np.vander(x_range, len(x_range)), axis=0)[:, :-1], column_averages)[::-1]


def get_scale_from_desired_width(width, grid_shape):
    return width / grid_shape[1]


def aeros_stencil_animation_objects(layout, function, grid_shape=(7, 5), stencil_size=(3, 3),
                                    stencil_2_size=(4, 3), cmap="coolwarm", width=2):
    scale = get_scale_from_desired_width(width=width, grid_shape=grid_shape)
    grid = create_grid(shape=grid_shape, stroke_width=1, color=GRID_COLOR)
    cell_T = Rectangle(height=1, width=1, stroke_width=0, color=CELL_T_COLOR, fill_opacity=0.35)
    cell_T.move_to(grid).shift(0.5 * LEFT * (1 - grid_shape[1] % 2)).shift(0.5 * DOWN * (1 - grid_shape[0] % 2))
    txt_cell_T = Tex(r"T", font_size=MEDIUM_FS).move_to(cell_T)
    stencil = create_grid(shape=stencil_size, stroke_width=STENCIL_STROKE_WIDTH, color=STENCIL_COLOR)
    stencil_DL_vertex = ((grid_shape[1] - stencil_size[1]) // 2, (grid_shape[0] - stencil_size[0]) // 2)
    stencil.move_to(grid, aligned_edge=DL).shift(stencil_DL_vertex[0] * RIGHT, stencil_DL_vertex[1] * UP)
    stencil_2 = create_grid(shape=stencil_2_size, stroke_width=STENCIL_STROKE_WIDTH, color=STENCIL_COLOR)
    stencil_2.move_to(stencil, aligned_edge=UL)
    x_range = [-grid_shape[1] / 2, grid_shape[1] / 2]
    y_range = [-grid_shape[0] / 2, grid_shape[0] / 2]
    curve = FunctionGraph(
        function,
        x_range=x_range,
        stroke_width=4 * scale,
        color=WHITE,
        fill_opacity=0
    )
    x_points = np.linspace(x_range[0], x_range[1], 1000)
    lower_part = Polygon(
        *np.array(
            [(x, function(x), 0) for x in x_points] +
            [(x_range[1], min((y_range[0], function(x_range[0]))), 0)] +
            ([(x_range[0], y_range[0], 0)] if function(x_range[0]) > y_range[0] else [])
        ),
        color=cmap_value2manimcolor(1.0, cmap="coolwarm"),
        fill_opacity=0.2,
        stroke_opacity=0
    )
    upper_part = Polygon(
        *np.array(
            [(x, function(x), 0) for x in x_points] +
            ([(x_range[1], y_range[1], 0)] if function(x_range[1]) < y_range[1] else []) +
            [(x_range[0], y_range[1], 0)]

        ),
        color=cmap_value2manimcolor(0.0, cmap="coolwarm"),
        fill_opacity=0.2,
        stroke_opacity=0
    )
    avg_values = grid_averages(grid_shape, function, N=100)
    mo_avg_colors, mo_values = create_grid_of_colored_rectangles(avg_values, cmap=cmap, fill_opacity=0.5,
                                                                 stroke_width=0)
    Group(mo_avg_colors, mo_values).next_to(grid, RIGHT, buff=BUFF_ONE)
    grid_avg = create_grid(shape=grid_shape, stroke_width=1, color=GRID_COLOR).move_to(mo_avg_colors)
    # [2, 3, 4] [1, 2, 3]
    row_ix = np.arange(-1 - (stencil.get_y(DL) - grid.get_y(DL)),
                       -1 - (stencil_size[0] + stencil.get_y(DL) - grid.get_y(DL)), -1,
                       dtype=int).tolist()
    col_ix = np.arange(stencil.get_x(DL) - grid.get_x(DL), stencil_size[1] + stencil.get_x(DL) - grid.get_x(DL),
                       dtype=int).tolist()
    stencil_avg_matrix = (avg_values[row_ix, :][:, col_ix])
    column_avg = stencil_avg_matrix.sum(axis=0)
    try:
        coeffs = fit_quadratic_averages(x_range=np.linspace(0, 3, num=4) - 1.5, column_averages=column_avg - 1.5)
        approx_function = lambda x: sum([c * x ** i for i, c in enumerate(coeffs)])
    except:
        approx_function = function
    curve_approx = FunctionGraph(
        approx_function,
        x_range=x_range,
        stroke_width=4 * scale,
        color=COLOR_APPROXIMATION,
        fill_opacity=0
    )
    approx_column_avg = (avg_values[row_ix, :][:, col_ix]).sum(axis=0)
    graph_group = Group(cell_T, grid, curve, curve_approx, lower_part, stencil, mo_avg_colors, grid_avg, mo_values,
                        lower_part, upper_part, txt_cell_T, stencil_2).scale(scale)
    graph_group.set_x(layout.m_measurements.get_x(LEFT), LEFT)
    cell_T_avg = cell_T.copy().move_to(mo_avg_colors)
    stencil_avg = stencil.copy().move_to(mo_avg_colors)
    stencil_2_avg = stencil_2.copy().move_to(stencil_avg, aligned_edge=UP)
    curve.add_updater(
        lambda m: m.become(FunctionGraph(
            function,
            x_range=x_range,
            stroke_width=4 * scale,
            color=WHITE,
            fill_opacity=0
        ).scale(scale).set_x(grid.get_x()).set_y(grid.get_y() - 1 * scale))
    )
    lower_part.add_updater(
        lambda m: m.become(
            Polygon(
                *np.array(
                    [(x, function(x), 0) for x in x_points] +
                    [(x_range[1], min((y_range[0], function(x_range[0]))), 0)] +
                    ([(x_range[0], y_range[0], 0)] if function(x_range[0]) > y_range[0] else [])
                ),
                color=cmap_value2manimcolor(1.0, cmap="coolwarm"),
                fill_opacity=0.2,
                stroke_opacity=0
            ).scale(scale).set_x(grid.get_x()).set_y(grid.get_y(DR), DR).shift(
                (y_range[0] - min((y_range[0], function(x_range[0])))) * scale * DOWN)
        )
    )
    upper_part.add_updater(
        lambda m: m.become(
            Polygon(
                *np.array(
                    [(x, function(x), 0) for x in x_points] +
                    ([(x_range[1], y_range[1], 0)] if function(x_range[1]) < y_range[1] else []) +
                    [(x_range[0], y_range[1], 0)]

                ),
                color=cmap_value2manimcolor(0.0, cmap="coolwarm"),
                fill_opacity=0.2,
                stroke_opacity=0
            ).scale(scale).set_x(grid.get_x()).set_y(grid.get_y(UL), UL)
        )
    )
    return (approx_column_avg, approx_function, mo_avg_colors, cell_T, cell_T_avg, column_avg, curve, curve_approx,
            graph_group, grid, grid_avg, lower_part, scale, stencil, stencil_avg, stencil_avg_matrix, stencil_2,
            stencil_2_avg, stencil_size, txt_cell_T, upper_part, mo_values)


class AEROSSlides(MySlide):

    def construct(self, objects_from_previous_slides):
        title = Title(r"Fast higher order methods", font_size=STITLE_FS)
        layout = ConvergencePLotLayout(title)

        # -------------- -------------- -------------- #
        #   AEROS
        self.next_slide()
        aeros = Tex(r"Algorithm for Edge Reconstruction using Oriented Stencils", font_size=STITLE_FS,
                    substrings_to_isolate=["A", "E", "R", "O", "S"],
                    tex_to_color_map={"A": AEROS_COLOR, "E": AEROS_COLOR, "R": AEROS_COLOR, "O": AEROS_COLOR,
                                      "S": AEROS_COLOR})
        self.play(
            self.fade_out_old_elements(),
            self.update_main_title(title),
            self.update_slide_number(),
            Write(aeros)
        )

        # -------------- -------------- -------------- #
        #   Function and approx
        title = Title(r"Higher order: AEROS", font_size=STITLE_FS)
        cte = ValueTracker(0.0)
        function = lambda x: cte.get_value() * x - 0.16 * x ** 2 + 0.073333 * x ** 3
        (approx_column_avg, approx_function, averages, cell_T, cell_T_avg, column_avg, curve, curve_approx,
         graph_group, grid, grid_avg, lower_part, scale, stencil, stencil_avg, stencil_avg_matrix, stencil_2,
         stencil_2_avg, stencil_size, txt_cell_T, upper_part, values) = aeros_stencil_animation_objects(
            layout, function, grid_shape=(7, 5), stencil_size=(3, 3), stencil_2_size=(4, 3), cmap="coolwarm",
            width=2)

        bullets_4 = BulletedList("Find orientation for cell $T=(i, j)$",
                                 "Define an appropriate stencil $S_T$",
                                 "Sum averages $a_{S_T}$ column-wise: $C_i = \sum_{l=j-1}^{j+1}\ell_{il}(u)$",
                                 "Fit a polynomial to the associated 1D-problem",
                                 font_size=EQ_FONT_SIZE)
        bullets_4.next_to(graph_group, RIGHT, buff=BUFF_ONE)
        equations = MathTex(r"C_i = (j-1)h + \int_{ih}^{(i+1)h}p(x)dx",
                            # tex_environment="equation*",
                            font_size=EQ_FONT_SIZE)
        equations.next_to(bullets_4, DOWN, buff=BUFF_HALF)
        bullets_3 = BulletedList("Find orientation for cell $T=(i, j)$",
                                 "Define an appropriate stencil $S_T$",
                                 "Sum averages $a_{S_T}$ column-wise: $C_i = \sum_{l=j-1}^{j+1}\ell_{il}(u)$",
                                 font_size=EQ_FONT_SIZE)
        bullets_3.move_to(bullets_4, aligned_edge=UL)
        bullets_2 = BulletedList("Find orientation for cell $T=(i, j)$",
                                 "Define an appropriate stencil $S_T$",
                                 font_size=EQ_FONT_SIZE)
        bullets_2.move_to(bullets_4, aligned_edge=UL)
        bullets_1 = BulletedList("Find orientation for cell $T=(i, j)$",
                                 font_size=EQ_FONT_SIZE)
        bullets_1.move_to(bullets_4, aligned_edge=UL)

        # ----- curve and grid ----- #
        self.next_slide(auto_next=True)
        self.play(
            self.update_main_title(title),
            FadeOut(aeros, target_position=title.get_center(), scale=0.1),
        )
        self.play(
            Create(grid),
            FadeIn(curve),
            FadeIn(lower_part),
            FadeIn(upper_part),
        )
        self.next_slide()

        # ----- averages and move ----- #
        self.next_slide()
        averages_copy = averages.copy().move_to(grid)
        self.play(
            Create(averages_copy),
        )
        self.play(
            ReplacementTransform(averages_copy, averages),
        )
        self.play(
            Create(values),
            Create(grid_avg),
        )

        self.next_slide()
        self.play(
            Create(cell_T),
            Create(txt_cell_T),
            Create(cell_T_avg),
        )

        self.next_slide()
        self.play(
            FadeIn(bullets_1),
        )

        # ----- Orientations ----- #
        self.next_slide()
        V_orient = DoubleArrow(DOWN, UP).move_to(cell_T)
        H_orient = DoubleArrow(LEFT, RIGHT).move_to(cell_T)
        txt_V = Tex(r"Vertical orientation", font_size=MEDIUM_FS).next_to(grid, UP, buff=BUFF_HALF)
        txt_H = Tex(r"Horizontal orientation", font_size=MEDIUM_FS).next_to(grid, UP, buff=BUFF_HALF)
        self.play(
            Write(txt_H),
            Indicate(H_orient),
        )

        self.next_slide()
        self.play(
            FadeOut(H_orient),
            ReplacementTransform(txt_H, txt_V),
            Indicate(V_orient),
        )

        self.next_slide()
        stencil_sobel = Rectangle(height=3 * scale, width=3 * scale, color=ORIENTATION_COLOR,
                                  fill_opacity=0.25).move_to(cell_T_avg)
        stencil_sobel = Group(stencil_sobel, stencil_avg.copy())
        txt_sobel = Tex("Orientation test based on\nSobel filter",
                        tex_to_color_map={"Sobel filter": ORIENTATION_COLOR}, font_size=EQ_FONT_SIZE)
        txt_sobel.next_to(bullets_1, DOWN, buff=BUFF_HALF).shift(RIGHT)
        txt_grad = MathTex(r"G_T=(H_T, V_T)", font_size=EQ_FONT_SIZE).next_to(txt_sobel, DOWN, buff=BUFF_HALF)

        kv_vals = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
        kh_vals = kv_vals.T
        txt_grad_repl1 = MathTex(fr"G_T=({np.sum(stencil_avg_matrix * kh_vals):.1f}, V_T)",
                                 font_size=EQ_FONT_SIZE).next_to(txt_sobel, DOWN, buff=BUFF_HALF).move_to(txt_grad,
                                                                                                          aligned_edge=LEFT)
        txt_grad_repl2 = MathTex(
            fr"G_T=({np.sum(stencil_avg_matrix * kh_vals):.1f}, {np.sum(stencil_avg_matrix * kv_vals):.1f})",
            font_size=EQ_FONT_SIZE).next_to(txt_sobel, DOWN, buff=BUFF_HALF).move_to(txt_grad, aligned_edge=LEFT)
        txt_grad_repl3 = MathTex(
            fr"{np.abs(np.sum(stencil_avg_matrix * kh_vals)):.1f}=|H_T|<|V_T|={np.abs(np.sum(stencil_avg_matrix * kv_vals)):.1f}",
            font_size=EQ_FONT_SIZE).next_to(txt_sobel, DOWN, buff=BUFF_HALF).move_to(txt_grad, aligned_edge=LEFT)
        txt_ht = txt_grad_repl1[0][-8:-4]
        txt_vt = txt_grad_repl2[0][-5:-1]

        matscale = 0.4
        SH = DecimalMatrix(stencil_avg_matrix,
                           element_to_mobject_config={"num_decimal_places": 1, "color": ORIENTATION_COLOR})
        txt_prod_H = MathTex(r"*").next_to(SH, RIGHT)
        KH = IntegerMatrix(kh_vals, ).next_to(txt_prod_H, RIGHT)
        gh = Group(SH, txt_prod_H, KH)

        SV = SH.copy().next_to(KH, RIGHT, buff=BUFF_ONE)
        txt_prod_V = MathTex(r"*").next_to(SV, RIGHT)
        KV = IntegerMatrix(kv_vals, ).next_to(txt_prod_V, RIGHT)
        gv = Group(SV, txt_prod_V, KV)
        Group(gh, gv).scale(matscale).next_to(txt_grad, DOWN, buff=BUFF_HALF)
        self.play(
            FadeOut(V_orient),
            Write(txt_sobel),
        )

        self.next_slide()
        self.play(
            Write(txt_grad),
        )

        self.next_slide()
        self.play(
            Indicate(stencil_sobel),
            FadeIn(SH, target_position=stencil_sobel.get_center()),
            FadeIn(SV, target_position=stencil_sobel.get_center())
        )

        self.next_slide()
        self.play(
            FadeIn(txt_prod_V, txt_prod_H),
            Create(KH),
            Create(KV)
        )

        self.next_slide()
        self.play(
            Indicate(gh),
            ReplacementTransform(txt_grad, txt_grad_repl1)
        )
        self.play(
            Indicate(txt_ht),
        )
        self.next_slide()
        self.play(
            Indicate(gv),
            ReplacementTransform(txt_grad_repl1, txt_grad_repl2)
        )
        self.play(
            Indicate(txt_vt),
        )

        self.next_slide()
        self.play(
            ReplacementTransform(txt_grad_repl2, txt_grad_repl3),
            Write(txt_V),
            Indicate(V_orient),
        )

        # --------------------------------------------- #
        # ----- Stencil ----- #
        self.next_slide()
        self.play(
            FadeOut(stencil_sobel, SH, SV, txt_prod_H, txt_prod_V, txt_sobel, txt_grad_repl3, V_orient, txt_V),
            KV.animate.scale(0.5).next_to(bullets_1, RIGHT, buff=BUFF_HALF),
            KH.animate.scale(0.5).next_to(bullets_1, RIGHT, buff=1.5 * BUFF_ONE),
            FadeOut(bullets_1),
            FadeIn(bullets_2),
            Create(stencil),
            Create(stencil_avg)
        )

        self.next_slide()
        self.play(
            cte.animate.set_value(0.9),
            FadeOut(stencil),
            FadeIn(stencil_2),
            FadeOut(stencil_avg),
            FadeIn(stencil_2_avg),
        )

        self.next_slide()
        self.play(
            stencil_2.animate.shift(UR * scale),
            stencil_2_avg.animate.shift(UR * scale),
        )

        self.next_slide()
        self.play(
            cte.animate.set_value(0.0),
            FadeIn(stencil),
            FadeOut(stencil_2),
            FadeIn(stencil_avg),
            FadeOut(stencil_2_avg),
        )

        # --------------------------------------------- #
        # ----- Column stencil ----- #
        self.next_slide()
        column_stencil = (create_column_grid(
            stencil_size, rows=False, color=STENCIL_COLOR, stroke_width=2 * STENCIL_STROKE_WIDTH, fill_opacity=0.25)
                          .scale(scale).move_to(grid))
        column_stencil_avg = (create_column_grid(
            stencil_size, rows=False, color=STENCIL_COLOR, stroke_width=2 * STENCIL_STROKE_WIDTH, fill_opacity=0.25)
                              .scale(scale))
        column_stencil_avg.move_to(cell_T_avg)
        column_stencil.move_to(cell_T)

        self.play(
            FadeOut(bullets_2),
            FadeIn(bullets_3),
            Indicate(stencil_avg),
            Indicate(stencil),
            FadeOut(stencil_avg),
            FadeIn(column_stencil_avg),
            FadeOut(stencil),
            FadeIn(column_stencil),
        )

        r, t = create_column_rectangles(column_avg, cmap=STENCIL_COLOR, stroke_width=1, fill_opacity=0.5)
        group_col_avg = Group(r, t).scale(scale)
        r_fixed = r.copy().move_to(column_stencil_avg, aligned_edge=DOWN)
        group_col_avg.next_to(grid_avg, DOWN, buff=BUFF_HALF)
        self.play(
            Indicate(column_stencil_avg),
            FadeIn(r, target_position=stencil_avg.get_center()),
            FadeIn(t, target_position=stencil_avg.get_center()),
            FadeIn(r_fixed),
        )

        self.next_slide()

        approx_r, approx_t = create_column_rectangles(approx_column_avg, cmap=COLOR_APPROXIMATION, stroke_width=1,
                                                      fill_opacity=0.5)
        group_col_avg_approx = Group(approx_r, approx_t).scale(scale)
        r_fixed_approx = approx_r.copy().move_to(column_stencil, aligned_edge=DOWN)
        group_col_avg_approx.next_to(grid, DOWN, buff=BUFF_HALF)
        self.play(
            FadeOut(bullets_3),
            FadeIn(bullets_4),
            FadeIn(equations),
            Create(curve_approx),
            Indicate(column_stencil),
            FadeIn(approx_r, target_position=stencil.get_center()),
            FadeIn(approx_t, target_position=stencil.get_center()),
            FadeIn(r_fixed_approx)
        )

        self.next_slide()

        curve_approx_on_T = FunctionGraph(
            approx_function,
            x_range=[-0.5, 0.5],
            stroke_width=4 * scale,
            color=COLOR_APPROXIMATION,
            fill_opacity=0
        ).scale(scale).move_to(curve_approx, aligned_edge=UP)
        self.play(
            FadeOut(column_stencil, column_stencil_avg, group_col_avg_approx, r_fixed_approx, group_col_avg, r_fixed)
        )
        self.play(
            ReplacementTransform(curve_approx, curve_approx_on_T)
        )

        # --------------------------------------------- #
        # ----- Theoretical results ----- #
        self.next_slide()
        title = Title(r"AEROS theoretical results", font_size=STITLE_FS)
        orientation_title = Tex(r"Orientation test result", font_size=EQ_FONT_SIZE, color=ORIENTATION_COLOR)
        orientation_result = Tex(r"The orientation given by the Sobel filter "
                                 r"ensures that if the mesh size $h$ is below a critical value $h^*$ then there is a "
                                 r"tall or wide enough stencil so that the interface croses the sides of it.",
                                 font_size=EQ_FONT_SIZE,
                                 tex_template=TexTemplate(
                                     documentclass=fr"\documentclass[preview, varwidth={1.5 * pixels_per_width_point}px]" + "{standalone}"
                                 )).next_to(orientation_title, DOWN, BUFF_HALF)

        aeros_theorem_title = (Tex(r"AEROS global convergence theorem", font_size=EQ_FONT_SIZE, color=AEROS_COLOR)
                               .next_to(orientation_result, DOWN, BUFF_ONE))
        aeros_theorem = Tex(r"If $\Omega$ is a $\mathcal{C}^s$ domain with $s\geq n$, the AEROS "
                            r"method based on polynomials of degree n has a global convergence rate in $L^1$ norm "
                            r"of $h^{n+1}$",
                            font_size=EQ_FONT_SIZE,
                            tex_template=TexTemplate(
                                documentclass=fr"\documentclass[preview, varwidth={1.5 * pixels_per_width_point}px]" + "{standalone}"
                            )).next_to(aeros_theorem_title, DOWN, BUFF_HALF)
        (Group(orientation_title, orientation_result, aeros_theorem_title, aeros_theorem)
         .next_to(bullets_4, LEFT, buff=BUFF_ONE)).set_y(CENTER_Y)

        box_orient = RoundedRectangle(color=ORIENTATION_COLOR).surround(Group(orientation_title, orientation_result))
        box_aeros = RoundedRectangle(color=AEROS_COLOR).surround(Group(aeros_theorem, aeros_theorem_title))

        self.play(
            self.update_main_title(title),
            self.update_slide_number(),
            FadeOut(curve_approx_on_T, curve, upper_part, lower_part, grid, grid_avg, txt_cell_T,
                    cell_T_avg, cell_T, averages, values),
        )
        self.play(
            Write(orientation_title),
            Write(aeros_theorem_title),
        )

        self.next_slide()
        self.play(
            Write(orientation_result),
            Create(box_orient)
        )

        self.next_slide()
        self.play(
            Write(aeros_theorem),
            Create(box_aeros)
        )

        return dict()
