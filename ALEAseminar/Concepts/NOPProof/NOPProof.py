import pathlib
from collections import OrderedDict

from ALEAseminar.config import *

from lib.utils import MySlide, get_sub_objects

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


# ------ create objects ------ #
class ConceptNOPProof:
    def __init__(self):
        # ------ init objects ------ #
        font_size = EQ_FONT_SIZE
        self.nop_proof_mobjs = OrderedDict()
        self.nop_proof_mobjs["approx_norm"] = MathTex(r"\|u - \tu\|_V", font_size=font_size)
        self.nop_proof_mobjs["triangular_inequality_in_V"] = MathTex(r"\|u - \tu\|_V \leq \|u - v\|_V + \|v - \tu\|_V",
                                                                     font_size=font_size)
        self.nop_proof_mobjs["inverse_stability"] = MathTex(
            r"\|u - \tu\|_V \leq \|u - v\| + \mu_Z\|\ell(v) - \ell(\tu)\|_Z", font_size=font_size)
        self.nop_proof_mobjs["triangular_inequality_in_Z"] = MathTex(
            r"\|\ell(v) - \ell(\tu)\|_Z \leq \|z - \ell(v)\|_Z + \|z - \ell(\tu)\|_Z", font_size=font_size)
        self.nop_proof_mobjs["best_fit_estimator_property"] = MathTex(
            r"\|\ell(v) - \ell(\tu)\|_Z \leq 2\|z - \ell(v)\|_Z", font_size=font_size)
        self.nop_proof_mobjs["definition_of_z"] = MathTex(
            r"\|z - \ell(v)\|_Z \leq \|\ell(u) - \ell(v)\|_Z + \|\eta\|_Z", font_size=font_size)
        self.nop_proof_mobjs["lipschitz"] = MathTex(r"\|z - \ell(v)\|_Z \leq \alpha_Z\|u-v\|_V + \beta_z\|\eta\|_p",
                                                    font_size=font_size)
        self.nop_proof_mobjs["nop"] = MathTex(
            r"\|u - \tu\|_V \leq (1+2\alpha_Z\mu_Z)\|u-v\|_V + 2\beta_z\mu_Z\|\eta\|_p", font_size=font_size)

        # ------ style objects ------ #

        # ------ relative positioning ------ #
        vertical_buffer = BUFF_QUARTER
        self.nop_proof_mobjs["triangular_inequality_in_V"].next_to(self.nop_proof_mobjs["approx_norm"], DOWN,
                                                                   aligned_edge=LEFT, buff=vertical_buffer)
        self.nop_proof_mobjs["inverse_stability"].move_to(self.nop_proof_mobjs["triangular_inequality_in_V"],
                                                          aligned_edge=LEFT)
        z_norm = get_sub_objects(self.nop_proof_mobjs["inverse_stability"], num_chars=list(range(-12, 0)))
        self.nop_proof_mobjs["triangular_inequality_in_Z"].next_to(z_norm, DOWN, aligned_edge=LEFT,
                                                                   buff=vertical_buffer)
        self.nop_proof_mobjs["best_fit_estimator_property"].move_to(self.nop_proof_mobjs["triangular_inequality_in_Z"],
                                                                    aligned_edge=LEFT)
        zv_diff = get_sub_objects(self.nop_proof_mobjs["best_fit_estimator_property"], num_chars=list(range(-9, 0)))
        self.nop_proof_mobjs["definition_of_z"].next_to(zv_diff, DOWN, aligned_edge=LEFT, buff=vertical_buffer)
        self.nop_proof_mobjs["lipschitz"].move_to(self.nop_proof_mobjs["definition_of_z"], aligned_edge=LEFT)
        self.nop_proof_mobjs["nop"].move_to(self.nop_proof_mobjs["approx_norm"], aligned_edge=LEFT)

    def get_action_001_start_nop_proof(self):
        return Write(self.nop_proof_mobjs["approx_norm"]),

    def get_action_002_triangular_inequality_in_V(self):
        return Write(self.nop_proof_mobjs["triangular_inequality_in_V"]),

    def get_action_003_inverse_stability(self):
        return (Write(self.nop_proof_mobjs["inverse_stability"]),
                Unwrite(self.nop_proof_mobjs["triangular_inequality_in_V"], reverse=False),)

    def get_action_004_triangular_inequality_in_Z(self):
        return Write(self.nop_proof_mobjs["triangular_inequality_in_Z"]),

    def get_action_005_best_fit_estimator_property(self):
        return (Unwrite(self.nop_proof_mobjs["triangular_inequality_in_Z"], reverse=False),
                Write(self.nop_proof_mobjs["best_fit_estimator_property"]),)

    def get_action_006_definition_of_z(self):
        return Write(self.nop_proof_mobjs["definition_of_z"]),

    def get_action_007_lipschitz(self):
        return (Unwrite(self.nop_proof_mobjs["definition_of_z"], reverse=False),
                Write(self.nop_proof_mobjs["lipschitz"]),)

    def get_action_008_nop(self):
        return Unwrite(self.nop_proof_mobjs["approx_norm"], reverse=False), Write(self.nop_proof_mobjs["nop"]),


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

    print("Name of presentation: ", name_of_presentation)
    print("---------- Compiling manim slides ----------")
    subprocess.run(f"manim {quality} {name_of_presentation}.py {name_of_presentation}".split(" "))
    print("---------- Creating html ----------")
    subprocess.run(f"manim-slides convert {name_of_presentation} {name_of_presentation}.html --open".split(" "))
    print("---------- Creating PDF ----------")
    subprocess.run(f"manim-slides convert {name_of_presentation} {name_of_presentation}.pdf".split(" "))
