from collections import namedtuple

from ALEAseminar.config import *
from ALEAseminar.pyslides.s03_near_optimality import best_fit_estimator, near_optimality_property, \
    text_continuity, text_inverse_stability, condition_inverse, text_near_optimality_property, condition_lipschitz, \
    best_fit_estimator_ell1, near_optimality_property_L1
from ALEAseminar.pyslides.s04_recontrucrion_from_cell_averages import ConvergencePLotLayout, \
    latex4average_measurements, get_original_data_and_ground_truth, get_reconstructions
from ALEAseminar.pyslides.s05_piecewise_constant import LVIRA_COLOR, LVIRA_DATA, \
    create_convergence_plot_objects
from ALEAseminar.pyslides.s08_aeros import get_scale_from_desired_width, GRID_COLOR, CELL_T_COLOR, \
    grid_averages
from lib.utils import MySlide, get_shift_from_xy_coordinate, get_sub_objects, create_grid, cmap_value2manimcolor, \
    create_grid_of_colored_rectangles


def grid_curve_and_averages(position, function, grid_shape=(7, 5), cmap="coolwarm", width=2, x0=0, y0=0,
                            curve_color=WHITE, num_points4shading_areas=1000, add_updater=True, value_up=0):
    scale = get_scale_from_desired_width(width=width, grid_shape=grid_shape)
    mo_grid = create_grid(shape=grid_shape, stroke_width=1, color=GRID_COLOR)

    mo_cell_T = Rectangle(height=1, width=1, stroke_width=0, color=CELL_T_COLOR, fill_opacity=0.35)
    mo_cell_T.move_to(mo_grid).shift(0.5 * LEFT * (1 - grid_shape[1] % 2)).shift(0.5 * DOWN * (1 - grid_shape[0] % 2))
    txt_cell_T = Tex(r"T", font_size=MEDIUM_FS).move_to(mo_cell_T)

    x_range = [x0 - grid_shape[1] / 2, x0 + grid_shape[1] / 2]
    y_range = [y0 - grid_shape[0] / 2, y0 + grid_shape[0] / 2]
    x_points = np.linspace(x_range[0], x_range[1], num_points4shading_areas)

    def get_valid_points():
        y_points = function(x_points)
        valid_idx = (y_points >= y_range[0]) & (y_points <= y_range[1])
        valid_x_points = x_points[valid_idx]
        valid_y_points = y_points[valid_idx]
        return namedtuple("pointxy", "x y")(valid_x_points, valid_y_points)

    # assumes the curve doesn't cross two times UP and DOWN
    mo_curve = FunctionGraph(
        function,
        x_range=[np.min(get_valid_points().x), np.max(get_valid_points().x)],
        stroke_width=4 * scale,
        color=curve_color,
        fill_opacity=0
    )

    mo_lower_part = Polygon(
        *np.array(
            [(x, y, 0) for x, y in zip(get_valid_points().x, get_valid_points().y)] +
            ([(x_range[1], min((y_range[1], function(x_range[1]))), 0),
              (x_range[1], y_range[0], 0)]
             if function(x_range[1]) > y_range[0] else []) +
            ([(x_range[0], y_range[0], 0),
              (x_range[0], min((y_range[0], function(x_range[0]))), 0)]
             if function(x_range[0]) > y_range[0] else [])
        ),
        color=cmap_value2manimcolor(float(1 - value_up), cmap="coolwarm"),
        fill_opacity=0.2,
        stroke_opacity=0
    )
    mo_upper_part = Polygon(
        *np.array(
            [(x, y, 0) for x, y in zip(get_valid_points().x, get_valid_points().y)] +
            ([(x_range[1], max((y_range[1], function(x_range[1]))), 0),
              (x_range[1], y_range[1], 0)]
             if function(x_range[1]) < y_range[1] else []) +
            ([(x_range[0], y_range[1], 0),
              (x_range[0], max((y_range[0], function(x_range[0]))), 0)]
             if function(x_range[0]) < y_range[1] else [])
        ),
        color=cmap_value2manimcolor(float(value_up), cmap="coolwarm"),
        fill_opacity=0.2,
        stroke_opacity=0
    )
    avg_values = grid_averages(grid_shape, function, N=100)
    avg_values = avg_values if value_up == 0 else (1 - avg_values)
    mo_avg_colors, mo_values = create_grid_of_colored_rectangles(avg_values, cmap=cmap, fill_opacity=0.5,
                                                                 stroke_width=0)

    Group(mo_avg_colors, mo_values).next_to(mo_grid, RIGHT, buff=BUFF_ONE)
    mo_grid_avg = create_grid(shape=grid_shape, stroke_width=1, color=GRID_COLOR).move_to(mo_avg_colors)
    mo_cell_T_avg = mo_cell_T.copy().move_to(mo_avg_colors)

    group = Group(mo_grid, mo_curve, mo_lower_part, mo_upper_part, mo_cell_T, txt_cell_T, mo_grid_avg, mo_avg_colors,
                  mo_values, mo_cell_T_avg).scale(scale)
    d_shift = position - group.get_edge_center(UP)
    group.shift(d_shift)

    if add_updater:
        mo_curve.add_updater(
            lambda m: m.become(
                FunctionGraph(
                    function,
                    x_range=[np.min(get_valid_points().x), np.max(get_valid_points().x)],
                    stroke_width=4 * scale,
                    color=curve_color,
                    fill_opacity=0
                ).scale(scale).set_x(mo_grid.get_x(RIGHT if function(x_range[1]) >= function(x_range[0]) else LEFT),
                                     direction=(UR if function(x_range[1]) >= function(x_range[0]) else UL))
                .set_y(mo_grid.get_y(), direction=(UR if function(x_range[1]) >= function(x_range[0]) else UL))
                .shift(
                    ((function(x_range[1]) if function(x_range[1]) >= function(x_range[0]) else function(
                        x_range[0])) + y0) * scale * UP)
            )
        )
        mo_lower_part.add_updater(
            lambda m: m.become(
                Polygon(
                    *np.array(
                        [(x, y, 0) for x, y in zip(get_valid_points().x, get_valid_points().y)] +
                        ([(x_range[1], min((y_range[1], function(x_range[1]))), 0),
                          (x_range[1], y_range[0], 0)]
                         if function(x_range[1]) > y_range[0] else []) +
                        ([(x_range[0], y_range[0], 0),
                          (x_range[0], min((y_range[0], function(x_range[0]))), 0)]
                         if function(x_range[0]) > y_range[0] else [])
                    ),
                    color=cmap_value2manimcolor(1.0, cmap="coolwarm"),
                    fill_opacity=0.2,
                    stroke_opacity=0
                ).scale(scale).set_x(0, direction=DOWN).set_y(0, direction=DOWN).move_to(mo_grid.get_edge_center(DOWN),
                                                                                         aligned_edge=DOWN)
            )
        )
        mo_upper_part.add_updater(
            lambda m: m.become(
                Polygon(
                    *np.array(
                        [(x, y, 0) for x, y in zip(get_valid_points().x, get_valid_points().y)] +
                        ([(x_range[1], max((y_range[1], function(x_range[1]))), 0),
                          (x_range[1], y_range[1], 0)]
                         if function(x_range[1]) < y_range[1] else []) +
                        ([(x_range[0], y_range[1], 0),
                          (x_range[0], max((y_range[0], function(x_range[0]))), 0)]
                         if function(x_range[0]) < y_range[1] else [])
                    ),
                    color=cmap_value2manimcolor(0.0, cmap="coolwarm"),
                    fill_opacity=0.2,
                    stroke_opacity=0
                ).scale(scale).set_x(0, direction=UP).set_y(0, direction=UP).move_to(mo_grid.get_edge_center(UP),
                                                                                     aligned_edge=UP)
            )
        )

        mo_avg_colors.add_updater(
            lambda m: m.become(
                create_grid_of_colored_rectangles(grid_averages(grid_shape, function, N=100),
                                                  cmap=cmap, fill_opacity=0.5, stroke_width=0)[0]
                .scale(scale).move_to(mo_grid_avg)
            )
        )
        mo_values.add_updater(
            lambda m: m.become(
                create_grid_of_colored_rectangles(grid_averages(grid_shape, function, N=100),
                                                  cmap=cmap, fill_opacity=0.5, stroke_width=0)[1]
                .scale(scale).move_to(mo_grid_avg)
            )
        )
    return VDict({"grid": mo_grid, "curve": mo_curve, "upper_part": mo_upper_part, "lower_part": mo_lower_part,
                  "cell_T": mo_cell_T, "tex_cell_T": txt_cell_T, "grid_avg": mo_grid_avg, "avg_colors": mo_avg_colors,
                  "avg_values": mo_values, "cell_T_avg": mo_cell_T_avg}), scale


def drop_cell_T(gca):
    return VDict(
        {"grid": gca["grid"], "curve": gca["curve"], "upper_part": gca["upper_part"], "lower_part": gca["lower_part"],
         "grid_avg": gca["grid_avg"], "avg_colors": gca["avg_colors"], "avg_values": gca["avg_values"]})


class LVIRASlides(MySlide):

    def construct(self, objects_from_previous_slides):
        title = Title(r"Non-linear approximation", font_size=STITLE_FS)
        layout = ConvergencePLotLayout(title)
        # exp_citation = objects_from_previous_slides["exp_citation"]
        # plot_group = objects_from_previous_slides["plot_group"]

        # ============== ============== ============== #
        # -------------- -------------- -------------- #
        #   Non-linear family

        vn_space = MathTex(
            r"V_n := \{ v_\mu: \mu \in \R^n\}",
            font_size=EQ_FONT_SIZE).next_to(title, DOWN, buff=BUFF_QUARTER)
        # vn_space = shift_to(vn_space, position=layout.center_x_grid, coordinate="x")
        v2_space = MathTex(
            r"V_2 := \{ \chi_{\vec{r}\cdot (x-\overline{x})\geq c} : \vec{r} \in \mathbb{S}^1, c \in \mathbb{R}\}",
            font_size=EQ_FONT_SIZE).move_to(vn_space)
        best_fit = best_fit_estimator.copy().next_to(vn_space, DOWN, buff=BUFF_QUARTER)

        m = ValueTracker(0.55)
        b = ValueTracker(-0.5)
        linear_function = lambda x: b.get_value() + m.get_value() * x
        # group_vn_element = Group(*grid_curve_and_averages(
        #     best_fit.get_edge_center(DOWN) + BUFF_HALF * DOWN, linear_function, grid_shape=(3, 3), cmap="coolwarm",
        #     width=2, x0=0, y0=0, curve_color=WHITE, num_points4shading_areas=1000, add_updater=True))

        group_vn_element = drop_cell_T(
            grid_curve_and_averages(best_fit.get_edge_center(DOWN) + BUFF_HALF * DOWN + 3 * LEFT, linear_function,
                                    grid_shape=(3, 3), cmap="coolwarm", width=2)[0])
        tex_v = MathTex("v\in V_2").next_to(group_vn_element, LEFT, buff=BUFF_HALF)
        tex_ell = MathTex("\ell(v) \in \R^m").next_to(group_vn_element, RIGHT, buff=BUFF_HALF)
        get_sub_objects(tex_ell, [2]).set_color(COLOR_APPROXIMATION)
        get_sub_objects(tex_v, [0]).set_color(COLOR_APPROXIMATION)

        # function = lambda x: 0.1 + 0.75 * x + 0.25 * (x - 1) ** 2
        function = lambda x: 0.1 * x ** 2 + 0.25 * x + 0.1
        group_curve_element = drop_cell_T(
            grid_curve_and_averages(group_vn_element.get_edge_center(DOWN) + BUFF_HALF * DOWN, function,
                                    grid_shape=(3, 3), cmap="coolwarm", width=2)[0])

        m2 = 0
        b2 = 0.
        linear_function2 = lambda x: b2 + m2 * x
        group_vn_element2 = drop_cell_T(
            grid_curve_and_averages(best_fit.get_edge_center(DOWN) + BUFF_HALF * DOWN + 3 * LEFT, linear_function2,
                                    grid_shape=(3, 3), cmap="coolwarm", width=2, value_up=1,
                                    add_updater=False)[0]).move_to(
            group_curve_element)

        tex_u = Tex(r"Unknown\\$u$").next_to(group_curve_element, LEFT, buff=BUFF_HALF)
        tex_z = Tex(r"$z\in \R^m$\\ Observed\\ averages").next_to(group_curve_element, RIGHT, buff=BUFF_HALF)
        get_sub_objects(tex_z, [0]).set_color(COLOR_MEASUREMENTS)
        get_sub_objects(tex_u, [-1]).set_color(COLOR_SOLUTION)

        group_vn_element.add({"tex_v": tex_v, "tex_ell": tex_ell})
        group_curve_element.add({"tex_u": tex_u, "tex_z": tex_z})

        # E.G. Puckett, A volume-of-fluid interface tracking algorithm with applications to computing shock wave refraction,
        #  in: H. Dwyer (Ed.), Proceedings of the Fourth International Symposium on Computational Fluid Dynamics, Davis, CA, 1991, pp. 933–938.
        cite_lvira = Tex(r"LVIRA [E.G. Puckett, 1991]", font_size=CITATION_FONT_SIZE).next_to(best_fit)
        txt_nop = text_near_optimality_property.copy().next_to(title, DOWN, buff=BUFF_HALF)
        txt_nop.shift(get_shift_from_xy_coordinate(txt_nop, layout.center_x_grid_two_columns_b, "x"))
        nop = near_optimality_property.copy().next_to(txt_nop, DOWN, BUFF_HALF)
        txt_continuity = text_continuity.copy().next_to(nop, DOWN, buff=BUFF_HALF)
        lip_cond = condition_lipschitz.copy().next_to(txt_continuity, DOWN, buff=BUFF_HALF)
        txt_invstab = text_inverse_stability.copy().next_to(lip_cond, DOWN, buff=BUFF_HALF)
        inv_cond = condition_inverse.copy().next_to(txt_invstab, DOWN, buff=BUFF_HALF)
        group_properties = Group(txt_nop, nop, txt_continuity, lip_cond, inv_cond, txt_invstab)

        group_vnspace = Group(group_vn_element, group_curve_element)
        # gvncopy = group_vnspace.copy()
        group_properties.next_to(group_vnspace, RIGHT, buff=BUFF_HALF).set_y(best_fit.get_y(direction=DOWN),
                                                                             direction=UP)

        # -------------- -------------- -------------- #
        #   Slides
        self.next_slide()
        self.play(
            self.fade_out_old_elements(exept=latex4average_measurements),
            self.update_main_title(title),
            self.update_slide_number(),
            FadeIn(vn_space)
        )

        title = Title(r"Non-linear approximation: linear interface", font_size=STITLE_FS)
        self.next_slide()
        self.play(
            self.update_main_title(title),
            ReplacementTransform(vn_space, v2_space)
        )

        # -------------- -------------- -------------- #
        #   linear interface examples
        self.next_slide()
        self.play(
            FadeIn(group_vn_element)
        )

        self.next_slide()
        self.play(
            b.animate.set_value(0),
            run_time=2,
        )
        self.play(
            m.animate.set_value(-0.25),
            run_time=2,
        )

        self.next_slide()
        self.play(
            FadeIn(group_curve_element, tex_u, tex_z)
        )

        # -------------- -------------- -------------- #
        #   best fit estimator
        self.next_slide()
        title = Title(r"Best fit estimator: LVIRA", font_size=STITLE_FS)
        self.play(
            self.update_main_title(title),
            Write(best_fit),
            Write(cite_lvira)
        )

        self.next_slide()
        # 0.1 + 0.75 * x + 0.25 * (x - 1) ** 2
        # 0.1+0.25
        # 0.75 - 0.5
        self.play(
            b.animate.set_value(0.1),
            m.animate.set_value(0.25),
            run_time=3,
        )

        approx_curve = group_vn_element["curve"].copy()
        [approx_curve.remove_updater(up) for up in approx_curve.get_updaters()]
        self.add(approx_curve)
        self.play(
            approx_curve.animate.set_color(COLOR_APPROXIMATION).shift(
                group_curve_element["grid"].get_center() - group_vn_element["grid"].get_center()),
            run_time=3,
        )
        self.play(
            approx_curve.animate.scale(1 / 3)
        )

        # -------------- -------------- -------------- #
        #   non linear framework
        self.next_slide()
        self.play(
            # group_vn_element.animate.set_x(gvncopy.get_x()),
            # group_curve_element.animate.set_x(gvncopy.get_x()),
            # group_vnspace.animate.move_to(gvncopy.get_center()),
            # FadeOut(group_vnspace),
            # FadeIn(gvncopy),
            FadeOut(cite_lvira)
        )

        self.play(
            Write(txt_nop),
            Write(nop)
        )

        self.next_slide()
        self.play(
            Write(txt_continuity),
            Write(lip_cond)
        )

        self.next_slide()
        self.play(
            Write(txt_invstab),
            Write(inv_cond)
        )

        self.next_slide()
        new_condition_lipschitz = MathTex(r"\|\ell(u)-\ell(v) \|_{\ell^1} \leq h^{-2} \|u-v\|_{L^1}, \;\; u,v \in V",
                                          substrings_to_isolate=["u", "v", r"\ell"],
                                          tex_to_color_map={"u": COLOR_SOLUTION, "v": COLOR_SOLUTION,
                                                            # r"\ell": COLOR_MEASUREMENTS
                                                            },
                                          font_size=EQ_FONT_SIZE)
        get_sub_objects(new_condition_lipschitz, [1, 6]).set_color(COLOR_MEASUREMENTS)
        new_condition_lipschitz.move_to(lip_cond)

        old_lip_constant = get_sub_objects(lip_cond, [13, 14])  # lip_cond[8][3]
        self.play(
            Indicate(old_lip_constant, scale_factor=2)
        )
        self.play(
            ReplacementTransform(lip_cond, new_condition_lipschitz)
        )

        # -------------- -------------- -------------- #
        #   new condition inverse
        self.next_slide()
        self.remove(group_curve_element)
        self.remove(approx_curve)
        self.play(
            FadeIn(group_vn_element2)
        )

        self.next_slide()
        self.play(
            b.animate.set_value(0.0),
            m.animate.set_value(0.0),
        )
        new_condition_inverse = MathTex(
            r"\|u-v\|_{L^1} \leq \frac{3}{2}h^2 \|\ell(u)-\ell(v) \|_{\ell^1}, \;\; u,v \in V_n",
            substrings_to_isolate=["v", r"\ell", "u"],
            tex_to_color_map={"v": COLOR_APPROXIMATION, "u": COLOR_APPROXIMATION,
                              # r"\ell": COLOR_MEASUREMENTS
                              },
            font_size=EQ_FONT_SIZE)
        get_sub_objects(new_condition_inverse, [14, 19]).set_color(COLOR_MEASUREMENTS)
        new_condition_inverse.move_to(inv_cond)

        old_mu_constant = get_sub_objects(inv_cond, [7, 8])  # inv_cond[4][2]
        self.play(
            Indicate(old_mu_constant, scale_factor=2)
        )
        cite_matthieu = (Text("[A. Cohen, M. Dolbeault, O. Mula, A. Somacal, 2024]",
                              font_size=CITATION_FONT_SIZE, color=LVIRA_DATA.color)
                         .next_to(new_condition_inverse, DOWN, buff=BUFF_HALF / 2))
        self.play(
            ReplacementTransform(inv_cond, new_condition_inverse),
            Write(cite_matthieu)
        )

        self.next_slide()
        self.play(
            Indicate(best_fit[-1][-1], scale_factor=2)
        )
        bfel2 = best_fit_estimator_ell1.copy().move_to(best_fit, aligned_edge=LEFT)
        self.play(
            ReplacementTransform(best_fit, bfel2)
        )

        self.next_slide()
        nopL1 = near_optimality_property_L1.copy().move_to(nop)
        # TODO: add indicate on V
        # L1 = list(find_substring_indexes(nopL1, substring=r"L^1", return_indices=False))
        # self.play(
        #     *list(map(partial(Indicate, scale_factor=2), L1)),
        # )
        self.play(
            ReplacementTransform(nop, nopL1)
        )

        self.next_slide()
        # i, j = next(find_substring_indexes(nopL1, substring="C", return_indices=True))
        # Cconst = nopL1[i][j]
        near_optimality_property_10 = MathTex(r"\|\uu-\tilde{u} \|_{L^1} \leq 10 \|\uu-P_{V_n} \uu\|_{L^1}",
                                              substrings_to_isolate=["z", r"\tilde{u}"],
                                              tex_to_color_map={"z": COLOR_MEASUREMENTS,
                                                                r"\tilde{u}": COLOR_APPROXIMATION},
                                              font_size=EQ_FONT_SIZE)
        near_optimality_property_10.move_to(nopL1)
        # self.play(Indicate(Cconst))
        self.play(
            FadeOut(txt_continuity, new_condition_inverse, new_condition_lipschitz, txt_invstab,
                    target_position=nopL1.get_center(), scale=0.1),
            cite_matthieu.animate.next_to(near_optimality_property_10, DOWN, buff=BUFF_HALF / 2),
            ReplacementTransform(nopL1, near_optimality_property_10)
        )

        # -------------- -------------- -------------- #
        #   Global convergence
        self.next_slide()
        global_convergence = Tex("Global convergence", font_size=EQ_FONT_SIZE, color=LVIRA_COLOR).move_to(txt_nop)
        corollary = Tex(r"Corollary: If $\Omega$ is a $\mathcal{C}^s$ domain with $s\geq 2$, the LVIRA "
                        r"method converges in $L^1$ norm at rate $h^2$",
                        font_size=EQ_FONT_SIZE,
                        tex_template=TexTemplate(
                            documentclass=fr"\documentclass[preview, varwidth={pixels_per_width_point}px]" + "{standalone}"
                        )).next_to(global_convergence, DOWN, BUFF_HALF)
        self.play(
            self.update_slide_number(),
            ReplacementTransform(near_optimality_property_10, corollary),
            ReplacementTransform(txt_nop, global_convergence),
            cite_matthieu.animate.next_to(corollary, DOWN, buff=BUFF_HALF / 2),
        )

        # -------------- -------------- -------------- #
        #    convergence
        # grid, x_label, y_label, points, graphs, order, plot_group = create_convergence_plot_objects(
        #     models=[PIECEWISE_DATA, LVIRA_DATA], layout=layout)
        plot_group = create_convergence_plot_objects("LVIRA", layout=layout)

        layout = ConvergencePLotLayout(title, shift=UP)
        ground_truth, original_avg_10, original_avg_20 = get_original_data_and_ground_truth(layout)
        lvira_reconstruction_avg_10, lvira_reconstruction_avg_20 = get_reconstructions(layout, "linear_obera_w")

        self.next_slide()
        self.play(
            self.fade_out_old_elements([cite_matthieu]),
            cite_matthieu.animate.set_x(plot_group.get_x()).set_y(-H + BUFF_HALF),
            # FadeOut(global_convergence, group_vnspace),
            FadeIn(ground_truth, original_avg_10, original_avg_20),
            FadeIn(plot_group)
            # FadeIn(grid, x_label, y_label),
            # Create(points["Piecewise constant"]),
            # Create(graphs["Piecewise constant"]),
            # ReplacementTransform(corollary, order["LVIRA"]),
            # Write(order["Piecewise constant"]),
        )
        self.play(
            # Create(points["LVIRA"]),
            # Create(graphs["LVIRA"]),
            FadeIn(lvira_reconstruction_avg_10, lvira_reconstruction_avg_20)
        )

        return dict()
