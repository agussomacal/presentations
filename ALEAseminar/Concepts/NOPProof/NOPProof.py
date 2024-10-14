from collections import OrderedDict

from ALEAseminar.config import *
from lib.utils import MySlide, get_sub_objects


# ------ create objects ------ #
class ConceptNOPProof:
    @property
    def group(self):
        return VDict(self.nop_proof_mobjs)

    def __init__(self):
        # ------ style objects ------ #
        font_size = EQ_FONT_SIZE
        style_dict = {
            "tex_to_color_map": {
                r"\uu": COLOR_SOLUTION,
                r"\tu": COLOR_APPROXIMATION,
                r"\vv": COLOR_APPROXIMATION,
                "z": COLOR_MEASUREMENTS
            },
            "substrings_to_isolate": [r"\uu", r"\tu", r"v"],
            "font_size": font_size
        }

        # ------ init objects ------ #
        self.nop_proof_mobjs = OrderedDict()
        self.nop_proof_mobjs["approx_norm"] = MathTex(r"\|\uu - \tu\|_V", **style_dict)
        self.nop_proof_mobjs["triangular_inequality_in_V"] = MathTex(
            r"\|\uu - \tu\|_V \leq \|\uu - \vv\|_V + \|\vv - \tu\|_V", **style_dict)
        self.nop_proof_mobjs["inverse_stability"] = MathTex(
            r"\|\uu - \tu\|_V \leq \|\uu - \vv\| + \mu_Z\|\ell(\vv) - \ell(\tu)\|_Z", **style_dict)
        # new line
        self.nop_proof_mobjs["triangular_inequality_in_Z"] = MathTex(
            r"\|\ell(\vv) - \ell(\tu)\|_Z \leq \|z - \ell(\vv)\|_Z + \|z - \ell(\tu)\|_Z", **style_dict)
        self.nop_proof_mobjs["best_fit_estimator_property"] = MathTex(
            r"\|\ell(\vv) - \ell(\tu)\|_Z \leq 2\|z - \ell(\vv)\|_Z", **style_dict)
        # new line
        self.nop_proof_mobjs["definition_of_z"] = MathTex(
            r"\|z - \ell(\vv)\|_Z \leq \|\ell(\uu) - \ell(\vv)\|_Z + \|\eta\|_Z", **style_dict)
        self.nop_proof_mobjs["lipschitz"] = MathTex(
            r"\|z - \ell(\vv)\|_Z \leq \alpha_Z\|\uu-\vv\|_V + \beta_z\|\eta\|_p", **style_dict)
        self.nop_proof_mobjs["nop"] = MathTex(
            r"\|\uu - \tu\|_V \leq (1+2\alpha_Z\mu_Z)\|\uu-\vv\|_V + 2\beta_z\mu_Z\|\eta\|_p", **style_dict)

        # ------ relative positioning ------ #
        vertical_buffer = BUFF_QUARTER
        self.nop_proof_mobjs["triangular_inequality_in_V"].move_to(self.nop_proof_mobjs["approx_norm"],
                                                                   aligned_edge=LEFT)
        self.nop_proof_mobjs["inverse_stability"].move_to(self.nop_proof_mobjs["triangular_inequality_in_V"],
                                                          aligned_edge=LEFT)
        # new line
        self.nop_proof_mobjs["triangular_inequality_in_Z"].next_to(self.nop_proof_mobjs["inverse_stability"], DOWN,
                                                                   buff=vertical_buffer)
        self.nop_proof_mobjs["best_fit_estimator_property"].move_to(self.nop_proof_mobjs["triangular_inequality_in_Z"],
                                                                    aligned_edge=LEFT)
        # new line
        zv_diff = get_sub_objects(self.nop_proof_mobjs["best_fit_estimator_property"], num_chars=list(range(-9, 0)))
        self.nop_proof_mobjs["definition_of_z"].next_to(zv_diff, DOWN, aligned_edge=LEFT, buff=vertical_buffer)
        self.nop_proof_mobjs["lipschitz"].move_to(self.nop_proof_mobjs["definition_of_z"], aligned_edge=LEFT)
        self.nop_proof_mobjs["nop"].move_to(self.nop_proof_mobjs["approx_norm"], aligned_edge=LEFT)

        # ------ auxiliary objects ------ #
        z_norm = get_sub_objects(self.nop_proof_mobjs["inverse_stability"], num_chars=list(range(-13, 0)))
        z_norm_new_line = get_sub_objects(self.nop_proof_mobjs["triangular_inequality_in_Z"], num_chars=list(range(13)))
        self.nop_proof_mobjs["first_braceline_up"] = Line(z_norm.get_corner(DL), z_norm.get_corner(DR),
                                                          color=YELLOW, stroke_width=1).shift(
            vertical_buffer / 4 * DOWN)
        self.nop_proof_mobjs["first_braceline_down"] = Line(z_norm_new_line.get_corner(UL),
                                                            z_norm_new_line.get_corner(UR), color=YELLOW,
                                                            stroke_width=1).shift(vertical_buffer / 4 * UP)

    def get_action_001_start_nop_proof(self):
        return Write(self.nop_proof_mobjs["approx_norm"]),

    def get_action_002_triangular_inequality_in_V(self):
        return (Unwrite(self.nop_proof_mobjs["approx_norm"], reverse=False),
                Write(self.nop_proof_mobjs["triangular_inequality_in_V"]),)

    def get_action_003_inverse_stability(self):
        return (Write(self.nop_proof_mobjs["inverse_stability"]),
                Unwrite(self.nop_proof_mobjs["triangular_inequality_in_V"], reverse=False),)

    def get_action_004_triangular_inequality_in_Z(self):
        return (Write(self.nop_proof_mobjs["triangular_inequality_in_Z"]),
                Create(self.nop_proof_mobjs["first_braceline_up"]),
                Create(self.nop_proof_mobjs["first_braceline_down"]))

    def get_action_005_best_fit_estimator_property(self):
        return (Unwrite(self.nop_proof_mobjs["triangular_inequality_in_Z"], reverse=False),
                Write(self.nop_proof_mobjs["best_fit_estimator_property"]),)

    def get_action_006_definition_of_z(self):
        return Write(self.nop_proof_mobjs["definition_of_z"]),

    def get_action_007_lipschitz(self):
        return (Unwrite(self.nop_proof_mobjs["definition_of_z"], reverse=False),
                Write(self.nop_proof_mobjs["lipschitz"]),)

    def get_action_008_nop(self):
        return (Unwrite(self.nop_proof_mobjs["inverse_stability"], reverse=False),
                Uncreate(self.nop_proof_mobjs["first_braceline_up"]),
                Uncreate(self.nop_proof_mobjs["first_braceline_down"]),
                Write(self.nop_proof_mobjs["nop"]),)


class NOPProof(MySlide):

    def construct(self, *args, **kwargs):
        nopproof = ConceptNOPProof()

        self.next_slide()
        self.play(
            *nopproof.get_action_001_start_nop_proof()
        )
        self.next_slide()
        self.play(
            *nopproof.get_action_002_triangular_inequality_in_V()
        )
        self.next_slide()
        self.play(
            *nopproof.get_action_003_inverse_stability()
        )
        self.next_slide()
        self.play(
            *nopproof.get_action_004_triangular_inequality_in_Z()
        )
        self.next_slide()
        self.play(
            *nopproof.get_action_005_best_fit_estimator_property()
        )
        self.next_slide()
        self.play(
            *nopproof.get_action_006_definition_of_z()
        )
        self.next_slide()
        self.play(
            *nopproof.get_action_007_lipschitz()
        )
        self.next_slide()
        self.play(
            *nopproof.get_action_008_nop()
        )


if __name__ == '__main__':
    LOW_QUALITY = True
    quality = "-ql" if LOW_QUALITY else ""
    import subprocess

    # overrides latex configuration from config
    path2file = pathlib.Path(__file__).parent
    name_of_presentation = __file__.split(".")[0].split("/")[-1]
    media_media = path2file.joinpath("media")
    main_tex = media_media.joinpath("Tex")
    # this is needed to compile Tex equations outside construct method
    main_tex.mkdir(parents=True, exist_ok=True)
    LatexTemplate = add_latex_file2preample(TexTemplate(documentclass="\documentclass[preview]{standalone}"),
                                            source_dir=source_dir)
    MathTex.set_default(tex_template=LatexTemplate, font_size=EQ_FONT_SIZE)
    Tex.set_default(tex_template=LatexTemplate, font_size=EQ_FONT_SIZE)
    SingleStringMathTex.set_default(tex_template=LatexTemplate, font_size=EQ_FONT_SIZE)

    print("Name of presentation: ", name_of_presentation)
    print("---------- Compiling manim slides ----------")
    subprocess.run(f"manim {quality} {name_of_presentation}.py {name_of_presentation}".split(" "))
    print("---------- Creating html ----------")
    subprocess.run(f"manim-slides convert {name_of_presentation} {name_of_presentation}.html --open".split(" "))
    print("---------- Creating PDF ----------")
    subprocess.run(f"manim-slides convert {name_of_presentation} {name_of_presentation}.pdf".split(" "))
