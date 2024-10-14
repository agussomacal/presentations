import pathlib

from ALEAseminar.pyslides.s01_title import TitleSlide
from ALEAseminar.pyslides.s02_inverse_problems_examples import InvPrbExamplesSlides
from ALEAseminar.pyslides.s03a_near_optimality import NearOptimalitySlides
from ALEAseminar.pyslides.s04_recontrucrion_from_cell_averages import InterfaceReconstructionSlides
from ALEAseminar.pyslides.s05_piecewise_constant import PiecewiseConstantSlides
from ALEAseminar.pyslides.s06_lvira import LVIRASlides
from ALEAseminar.pyslides.s07_obera import OBERASlides
from ALEAseminar.pyslides.s08_aeros import AEROSSlides
from ALEAseminar.pyslides.s09_aeros_convergence import AEROSConvergenceSlides
from ALEAseminar.pyslides.s10_corners import CornerSlides
from ALEAseminar.pyslides.s11_corners_reconstruction import CornerReconstructionSlides
from ALEAseminar.pyslides.s12_perspectives import PerspectivesSlides

# define the set of slides you want
slides = [
    TitleSlide,
    # InvPrbExamplesSlides,
    NearOptimalitySlides,
    # InterfaceReconstructionSlides,
    # PiecewiseConstantSlides,
    # LVIRASlides,
    # OBERASlides,
    # AEROSSlides,
    # AEROSConvergenceSlides,
    # CornerSlides,
    # CornerReconstructionSlides,
    # PerspectivesSlides,
]

# filter slides to test or run all then comment
# slides = slides[:12]


class ALEASeminarSlides(*slides):

    def setup(self):
        # setup each scene
        for s in slides:
            s.setup(self)

    def construct(self):
        # play each scene
        s = slides[0]
        objects_from_previous_slides = s.construct(self)
        for s in slides[1:]:
            objects_from_previous_slides = s.construct(self, objects_from_previous_slides)


if __name__ == '__main__':
    LOW_QUALITY = True
    quality = "-ql" if LOW_QUALITY else ""
    import subprocess

    # overrides latex configuration from config
    path2file = pathlib.Path(__file__).parent
    name_of_presentation = __file__.split(".")[0].split("/")[-1]


    print("Name of presentation: ", name_of_presentation)
    print("---------- Compiling manim slides ----------")
    subprocess.run(f"manim {quality} {name_of_presentation}.py {name_of_presentation}".split(" "))
    print("---------- Creating html ----------")
    subprocess.run(f"manim-slides convert {name_of_presentation} {name_of_presentation}.html --open".split(" "))
    print("---------- Creating PDF ----------")
    subprocess.run(f"manim-slides convert {name_of_presentation} {name_of_presentation}.pdf".split(" "))
