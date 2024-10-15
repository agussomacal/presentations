import pathlib
import sys

from manim import *  # or: from manimlib import *

presentation_dir = pathlib.Path(__file__).parent.parent.absolute()
sys.path.insert(0, str(presentation_dir))
from lib.utils import add_latex_file2preample

# ---------------------- Paths ---------------------- #
lib_dir = presentation_dir.joinpath("lib")
source_dir = pathlib.Path(__file__).parent.absolute()
pyslides_dir = source_dir.joinpath("pyslides")
material_dir = source_dir.joinpath("Material")
images_dir = material_dir.joinpath("images")
media_media = source_dir.joinpath("media")
main_tex = media_media.joinpath("Tex")

# this is needed to compile Tex equations outside construct method
main_tex.mkdir(parents=True, exist_ok=True)

# ---------------------- Canvas properties ---------------------- #
pixels_width, pixels_height = config["frame_size"]  # (1920, 1080)
points_height = config["frame_height"]  # 8
points_width = config["frame_width"]  # 14+2/9
pixels_per_width_point = pixels_width / points_width  # 135
# print(pixels_per_width_point)
W = points_width / 2
H = points_height / 2
TwoColumns_dx = W / 2
ThreeColumns_dx = 2 * W / 3

BUFF_ONE = 1
BUFF_HALF = BUFF_ONE / 2
BUFF_QUARTER = BUFF_HALF / 2

# ---------------------- Font Sizes ---------------------- #
# sizes are considered for Tex default font
# 100 the abcdefghijklmnopqrstuvwxyz enters exactly 1 time in the screen
# 50 the abcdefghijklmnopqrstuvwxyz enters exactly 2 times in the screen
# 25 the abcdefghijklmnopqrstuvwxyz enters exactly 4 times in the screen
TITLE_FS = 100
STITLE_FS = 50  # 75
BIG_FS = 41.67
MEDIUM_FS = 33.33
SMALL_FS = 25

CITATION_FONT_SIZE = SMALL_FS / 2
EQ_FONT_SIZE = SMALL_FS

# ---------------------- Latex template ---------------------- #
LatexTemplate = add_latex_file2preample(TexTemplate(documentclass="\documentclass[preview]{standalone}"),
                                        source_dir=source_dir)
MathTex.set_default(tex_template=LatexTemplate, font_size=EQ_FONT_SIZE)
Tex.set_default(tex_template=LatexTemplate, font_size=EQ_FONT_SIZE)
SingleStringMathTex.set_default(tex_template=LatexTemplate, font_size=EQ_FONT_SIZE)
# myBaseTemplate.add_to_preamble(r"\usepackage{amsmath}")
# myBaseTemplate.add_to_preamble(r"\DeclareMathOperator*{\argmin}{arg\,min}")
# myBaseTemplate.add_to_preamble(r"\newcommand{\uu}{u}")


# myBaseTemplate.add_to_preamble(r"\usepackage{ragged2e}")
# custom_tex_template = TexTemplate(
#     documentclass=r"\documentclass[preview, varwidth=285px]{standalone}"
# )
# custom_tex_template.add_to_preamble(r"\usepackage[charter]{mathdesign}")

# ---------------------- Collor palettes ---------------------- #
# Pastel palette
# https://paletton.com/#uid=c022R0I3x0kllllaFw0g0qFqFg0w0aF
red = ManimColor("#AA3E39")
green = ManimColor("#2C8437")
blue = ManimColor("#29506D")
yellow = ManimColor("#AA7939")

# Autumn-like palette
# https://coolors.co/palettes/trending
dark = ManimColor("#003049")
autumn_red = ManimColor("#D62828")
autumn_orange = ManimColor("#F77F00")
autumn_yellow = ManimColor("#FCBF49")
autumn_white = ManimColor("#EAE2B7")

special_green = ManimColor("#2a9134")
special_blue = ManimColor("#3a7ca5")

white = WHITE
black = BLACK
gray = ManimColor("#14213D")

config["background_color"] = dark

SLIDE_NUM_COLOR = autumn_white

PDE_COLOR = GREEN
FM_COLOR = PDE_COLOR
INV_COLOR = ORANGE

COLOR_PARAMS = BLUE
COLOR_SOLUTION = PDE_COLOR
COLOR_MEASUREMENTS = INV_COLOR

COLOR_APPROXIMATION = YELLOW

COLOR_LINEAR = RED
# NON_LINEAR_COLOR = TEAL
NON_LINEAR_COLOR = RED

EXP_DECAY_COLOR = YELLOW
FRACTIONAL_DECAY_COLOR = RED

COLOR_SHADOW = GRAY
