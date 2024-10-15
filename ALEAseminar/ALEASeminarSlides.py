import pathlib
import time

from ALEAseminar.pyslides.s01_title import TitleSlide
from ALEAseminar.pyslides.s02_inverse_problems_examples import InvPrbExamplesSlides
from ALEAseminar.pyslides.s03_near_optimality import NearOptimalitySlides
from ALEAseminar.pyslides.s04_recontrucrion_from_cell_averages import InterfaceReconstructionSlides
from ALEAseminar.pyslides.s05_piecewise_constant import PiecewiseConstantSlides
from ALEAseminar.pyslides.s06_lvira import LVIRASlides
from ALEAseminar.pyslides.s07_obera import OBERASlides
from ALEAseminar.pyslides.s08_aeros import AEROSSlides
from ALEAseminar.pyslides.s09_aeros_convergence import AEROSConvergenceSlides
from ALEAseminar.pyslides.s10_corners import CornerSlides
from ALEAseminar.pyslides.s11_corners_reconstruction import CornerReconstructionSlides
from ALEAseminar.pyslides.s12_finite_volumes import FiniteVolumesSlides
from ALEAseminar.pyslides.s13_perspectives import PerspectivesSlides
from ALEAseminar.pyslides.s14_end import EndSlides

# define the set of slides you want
slides = [
    TitleSlide,
    InvPrbExamplesSlides,
    NearOptimalitySlides,
    InterfaceReconstructionSlides,
    PiecewiseConstantSlides,
    LVIRASlides,
    OBERASlides,
    AEROSSlides,
    AEROSConvergenceSlides,
    CornerSlides,
    CornerReconstructionSlides,
    FiniteVolumesSlides,
    PerspectivesSlides,
    EndSlides
]


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
    LOW_QUALITY = False
    import subprocess

    # overrides latex configuration from config
    path2file = pathlib.Path(__file__).parent
    name_of_presentation = __file__.split(".")[0].split("/")[-1]

    t0 = time.time()
    print(f"Starting compiling slides: {(time.time() - t0) / 60:.2f}min")
    print("Name of presentation: ", name_of_presentation)
    print("---------- Compiling manim slides ----------")
    subprocess.run(f"manim {'-ql ' if LOW_QUALITY else ''}{name_of_presentation}.py {name_of_presentation}".split(" "))
    print("---------- Creating html ----------")
    subprocess.run(f"manim-slides convert {name_of_presentation} {name_of_presentation}.html --open".split(" "))
    print("---------- Creating PDF ----------")
    subprocess.run(f"manim-slides convert {name_of_presentation} {name_of_presentation}.pdf".split(" "))
    print(f"Finished compiling slides after {(time.time() - t0) / 60:.2f}min")
