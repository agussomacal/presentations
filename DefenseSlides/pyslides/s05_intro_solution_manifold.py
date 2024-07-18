from functools import partial

from DefenseSlides.config import *
from DefenseSlides.pyslides.s04_intro_two_problems import num_snapshots, get_Yshape_object, Yshape, get_diff_eq_images, \
    DOMAIN_STROKE_WIDTH, DOMAIN_FILL_OPACITY
from lib.utils import MySlide


def linear_approx(t, p=np.array([0, 0]), v=np.array([0, 1])):
    return np.append(p + t * v / np.linalg.norm(v), [0])


def solution_manifold(t, r=1.0):
    xc = 0.3
    theta = t * 2 * np.pi

    x = np.cos(theta) * r * 2
    y = np.sin(theta) * r - (x - xc) ** 2 / 3 + (x - xc) / 6

    return np.array((x, y, 0))


# def is_in_solution_manifold(x, y, r=1.0):
#     xc = 0.3
#     theta = np.arccos(x/2/r)
#     np.arcsin((y + (x - xc) ** 2 / 3 - (x - xc) / 6)/r)


def non_linear_approx(t, r=1.2):
    return np.mean([solution_manifold(t, r), solution_manifold(-t, r)], axis=0)


def get_solution_manifold_oject(color=RED, opacity=0.5, stroke=0.5):
    pf = ParametricFunction(solution_manifold, t_range=np.array([-PI, PI]), fill_opacity=opacity).set_color(
        color).set_stroke(width=stroke)
    return pf


buff_images = 1.5


class SolutionManifoldSlides(MySlide):

    def construct(self, objects_from_previous_slides):
        title = Title(r"Solution Manifold", font_size=STITLE_FS)
        if len(objects_from_previous_slides) > 0:
            self.next_slide()
            self.remove_old_elements()
            fmeq = objects_from_previous_slides["forward_map"]
            Y = objects_from_previous_slides["Y"]
            self.add(fmeq, Y)
            fmeq_dummy = fmeq.copy().next_to(title, DOWN)
            self.play(
                # self.fade_out_old_elements(exept=[fmeq, Y]),
                fmeq.animate.next_to(title, DOWN),
                Y.animate.next_to(fmeq_dummy, DOWN, buff=buff_images).shift(2 * LEFT),
                self.update_slide_number(),
                self.update_main_title(title),
            )
        else:
            fmeq = MathTex(r"y \in Y \mapsto u \in V", substrings_to_isolate=["y", "u"],
                           tex_to_color_map={"y": COLOR_PARAMS, "u": COLOR_SOLUTION},
                           font_size=MEDIUM_FS)
            Y = get_Yshape_object(fill_color=COLOR_PARAMS, fill_opacity=DOMAIN_FILL_OPACITY)
            fmeq.next_to(title, DOWN)
            Y = Y.next_to(fmeq, DOWN, buff=buff_images).shift(2 * LEFT)
            self.next_slide()
            self.play(
                self.fade_out_old_elements(),
                FadeIn(fmeq),
                FadeIn(Y),
                # FadeIn(approx),
                self.update_slide_number(),
                self.update_main_title(title)
            )
        self.wait(0.01)
        ytextobj = fmeq[0][0]
        maptotextobj = fmeq[1][2:]
        utextobj = fmeq[2][0]

        # -------------- -------------- -------------- #
        # sampling parameters
        num_points = 1000
        np.random.seed(42)
        T = np.random.uniform(0, 1, size=num_points)
        R = np.random.uniform(0, 1, size=num_points)

        ydots = [Dot(r * Yshape(2 * np.pi * t), radius=0.2 * DEFAULT_DOT_RADIUS,
                     stroke_width=0.5, fill_color=COLOR_PARAMS, color=WHITE) for r, t in zip(R, T)]
        udots = [Dot(solution_manifold(t, r), radius=0.2 * DEFAULT_DOT_RADIUS,
                     stroke_width=0.5, fill_color=COLOR_SOLUTION, color=WHITE) for r, t in zip(R, T)]
        udots2center = [Dot(solution_manifold(t, 1), radius=0.2 * DEFAULT_DOT_RADIUS, stroke_width=0.5) for t in T]
        ydots2center = [Dot(Yshape(2 * np.pi * t), radius=0.2 * DEFAULT_DOT_RADIUS, stroke_width=0.5, ) for t in T]

        manifold = (ParametricFunction(solution_manifold, t_range=np.array([0, 1]), fill_opacity=DOMAIN_FILL_OPACITY)
        .set_color(COLOR_SOLUTION).set_stroke(width=DOMAIN_STROKE_WIDTH).next_to(Y, ORIGIN, buff=0).shift(
            2 * Y.get_x() * LEFT))
        Group(*ydots, *ydots2center).move_to(Y)
        Group(*udots, *udots2center).move_to(manifold)

        num_solutions = min((10, num_snapshots))
        I = np.random.choice(num_snapshots, num_solutions, replace=False)
        se_scale = 0.25
        solutions = [get_diff_eq_images(name="solutions", i=i).scale(se_scale).move_to(udot)
                     for i, udot in zip(I, udots)]

        cM = MathTex("\cM", color=COLOR_SOLUTION).move_to(manifold, aligned_edge=RIGHT).shift(0.25 * LEFT)
        fmeqcM = MathTex(r"y \in Y \mapsto \uu \in \cM \subset V", substrings_to_isolate=["y", r"\uu"],
                         tex_to_color_map={"y": COLOR_PARAMS, r"\uu": COLOR_SOLUTION},
                         font_size=MEDIUM_FS).move_to(fmeq)

        overload = 1.2
        m_nl = (ParametricFunction(partial(non_linear_approx, r=overload), t_range=np.array([0, 1]))
                .set_color(NON_LINEAR_COLOR).set_stroke(width=DOMAIN_STROKE_WIDTH).move_to(manifold)).shift(DOWN)
        # v = np.array([2, 1])
        # m_lin = ParametricFunction(function=partial(linear_approx, p=np.array([0, 0]), v=v),
        #                            t_range=[0, manifold.width * overload], color=LINEAR_COLOR).move_to(m_nl).shift(UP)
        m_lin = Line(np.array([0, 0, 0]), (manifold.width * overload) / 2 * np.array([2, 1, 0]),
                     color=COLOR_LINEAR).move_to(m_nl).shift(UP)
        Vn_nl = MathTex("V_n", color=NON_LINEAR_COLOR).next_to(m_nl, UP)
        Vn = MathTex("V_n", color=COLOR_LINEAR).next_to(m_lin, UR)
        # -------------- -------------- -------------- #
        # SLIDES
        self.next_slide()
        self.play(
            *[FadeIn(ydot, target_position=ytextobj.get_center()) for ydot in ydots[:num_solutions]],
        )

        self.next_slide()
        self.play(
            *[FadeIn(s, target_position=utextobj) for s in solutions]
        )

        self.next_slide()
        self.play(
            *[FadeOut(s, target_position=s) for s in solutions],
            *[FadeIn(udot) for udot in udots[:num_solutions]]
        )

        self.next_slide()
        self.play(
            *[FadeIn(ydot, target_position=ytextobj.get_center()) for ydot in ydots[num_solutions:]],
        )

        self.next_slide()
        self.play(
            *[FadeIn(udot, target_position=utextobj.get_center()) for udot in udots[num_solutions:]]
        )

        self.next_slide()
        self.play(
            FadeIn(manifold)
        )

        self.next_slide()
        self.play(
            *list(map(FadeOut, ydots)),
            *list(map(FadeOut, udots)),
            Write(cM),
            ReplacementTransform(fmeq, fmeqcM)
        )

        # -------------- -------------- -------------- #
        # non-linear approximation
        self.next_slide()
        title = Title(r"Reduce order models", font_size=STITLE_FS)

        rom = Tex("")
        self.play(
            self.update_main_title(title),
            Write(rom),
            Create(m_nl),
            Create(Vn_nl)
        )

        # -------------- -------------- -------------- #
        # linear approximation
        self.next_slide()
        title = Title(r"Linear reduce order models", font_size=STITLE_FS)
        self.play(
            self.update_main_title(title),
            ReplacementTransform(m_nl, m_lin),
            ReplacementTransform(Vn_nl, Vn)
        )

        return {"map_group": VDict(
            {"map_eq": fmeqcM, "Y space": Y, "solution manifold": manifold, "linear space": m_lin, "tex Vn space": Vn,
             "tex cM": cM})}


if __name__ == '__main__':
    import numpy as np
    import matplotlib.pyplot as plt

    h = 1e-5
    dt = 0.4
    t = np.linspace(0, dt)
    # theta = np.abs(t)
    theta = t
    fy = lambda theta: np.sin(2 * np.pi * theta) * (1 + theta)
    fx = lambda theta: np.cos(2 * np.pi * theta) * (1 + theta) * 2
    # dy = (fy(theta+h)-fy(theta))/h
    # dx = (fx(theta+h)-fx(theta))/h
    # orth = np.array([-dy, dx])
    # orth = orth/np.sqrt(np.sum(orth**2))
    # y = fy(theta) + np.sign(t)*orth[1]
    # x = fx(theta) + np.sign(t)*orth[0]
    # y = fy(theta)+5*(t-dt)*t*(t+dt)
    y = fy(theta)
    x = fx(theta)

    N = 1000
    rt = np.random.uniform(0, dt, size=N)

    fs = lambda t: (0.4 - (t - 0.1) ** 2)

    sy = fy(rt) + np.random.normal(loc=0, scale=fs(rt))
    sx = fx(rt) + np.random.normal(loc=0, scale=0.1, size=N)

    # theta =
    # r = np.array([[np.cos(2*np.pi*theta), 0], [0, 1]])

    plt.plot(x, y)
    plt.scatter(sx, sy, marker=".", s=5, c="gray")
    plt.axis("equal")
    plt.show()
