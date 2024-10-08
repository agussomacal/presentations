import pathlib
import subprocess
import sys

from config import source_dir, pyslides_dir, presentation_dir

sys.path.insert(0, str(presentation_dir))
sys.path.insert(0, str(source_dir))
sys.path.insert(0, str(pyslides_dir))

name_of_presentation = pathlib.Path(__file__).parent.name
print("Name of presentation: ", name_of_presentation)
subprocess.run(f"manim {name_of_presentation}.py {name_of_presentation}".split(" "))
subprocess.run(f"manim-slides convert {name_of_presentation} {name_of_presentation}.html --open".split(" "))
subprocess.run(f"manim-slides convert {name_of_presentation} {name_of_presentation}.pdf".split(" "))

# manim ALEASeminarSlides.py ALEASeminarSlides
# manim-slides convert ALEASeminarSlides ALEASeminarSlides.html
# manim-slides convert ALEASeminarSlides ALEASeminarSlides.pdf
