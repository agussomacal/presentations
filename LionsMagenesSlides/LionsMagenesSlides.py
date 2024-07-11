from pyslides.s01_title import TitleSlide
from pyslides.s02_inverse_problems_examples import InvPrbExamplesSlides
from pyslides.s03_near_optimality import NearOptimalitySlides
from pyslides.s04_recontrucrion_from_cell_averages import InterfaceReconstructionSlides
from pyslides.s05_piecewise_constant import PiecewiseConstantSlides
from pyslides.s06_lvira import LVIRASlides
from pyslides.s07_obera import OBERASlides
from pyslides.s08_aeros import AEROSSlides
from pyslides.s09_aeros_convergence import AEROSConvergenceSlides
from pyslides.s10_corners import CornerSlides
from pyslides.s11_corners_reconstruction import CornerReconstructionSlides
from pyslides.s12_perspectives import PerspectivesSlides

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
    PerspectivesSlides,
]

# filter slides to test or run all then comment
# slides = slides[:12]


class LionsMagenesSlides(*slides):

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
