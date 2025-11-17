from pyslides.s01_intro_title import TitleSlide
from pyslides.s02_intro_motivation import MotivationSlides
from pyslides.s03_intro_pde_examples import PDEExamplesSlides
from pyslides.s04_intro_two_problems import TwoProblems
from pyslides.s05_intro_solution_manifold import SolutionManifoldSlides
from pyslides.s06_intro_linear_approach import LinearApproachSlides
from pyslides.s07_intro_main_questions import MainQuestionsSlides
from pyslides.s08_intro_kolmogorov_width_decay import KolmoDecaySlides
from pyslides.s09_intro_objectives_of_thesis import ThesisObjectivesSlides
from pyslides.s10_hcontr_uea import UEASlides
from pyslides.s11_hcontr_results import ResultsSlides
from pyslides.s12_hcontr_fminvpr import FmInvPSlides
from pyslides.s13_nonlininv_objectives_of_thesis import ThesisObjective2sSlides
from pyslides.s14_nonlininv_near_optimality import NearOptimalitySlides
from pyslides.s15_nonlininv_recontrucrion_from_cell_averages import InterfaceReconstructionSlides
from pyslides.s16_nonlininv_piecewise_constant import PiecewiseConstantSlides
from pyslides.s17_nonlininv_lvira import LVIRASlides
from pyslides.s18_cellavg_objectives_of_thesis import ThesisObjectives3Slides
from pyslides.s19_cellavg_obera import OBERASlides
from pyslides.s20_cellavg_aeros import AEROSSlides
from pyslides.s21_cellavg_aeros_convergence import AEROSConvergenceSlides
from pyslides.s22_cellavg_corners import CornerSlides
from pyslides.s23_cellavg_corners_reconstruction import CornerReconstructionSlides
from pyslides.s24_crb_objectives_of_thesis import ThesisObjective4sSlides
from pyslides.s26_end_perspectives import PerspectivesSlides
from pyslides.s25_crb_sensing_numbers import SensingSlides

# define the set of slides you want
slides = [
    TitleSlide,
    MotivationSlides,
    PDEExamplesSlides,
    TwoProblems,
    SolutionManifoldSlides,
    LinearApproachSlides,
    MainQuestionsSlides,
    KolmoDecaySlides,
    ThesisObjectivesSlides,
    UEASlides,
    ResultsSlides,
    FmInvPSlides,
    ThesisObjective2sSlides,
    NearOptimalitySlides,
    InterfaceReconstructionSlides,
    PiecewiseConstantSlides,
    LVIRASlides,
    ThesisObjectives3Slides,
    OBERASlides,
    AEROSSlides,
    AEROSConvergenceSlides,
    CornerSlides,
    CornerReconstructionSlides,
    ThesisObjective4sSlides,
    SensingSlides,
    PerspectivesSlides,
]


class DefenseSlides(*slides):

    def setup(self):
        # setup each scene
        for s in slides:
            s.setup(self)

    def construct(self):
        # play each scene
        s = slides[0]
        objects_from_previous_slides = s.construct(self)
        # canvas_data = s.get_canvas_data(self)
        for s in slides[1:]:
            # s.init_canvas(self, canvas_data)
            objects_from_previous_slides = s.construct(self, objects_from_previous_slides)
            # canvas_data = s.get_canvas_data(self)
