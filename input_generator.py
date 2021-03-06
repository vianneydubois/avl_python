# Generates a geometry input file for AVL
from openmdao.utils.file_wrap import InputFileGenerator
import os.path

INPUT_TEMPLATE_FOLDER = "resources"
INPUT_TEMPLATE_FILE_NAME = "geom_wing.avl"
INPUT_GENERATED_FOLDER = "generated_files"
INPUT_GENERATED_FILE_NAME = "generated_wing.avl"

mach = 0.4
sref = 28
bref = 14
cref = 2

# section 0
xle0 = 0
yle0 = 0
c0 = 2
# section 1
xle1 = 0
yle1 = 4
c1 = 2
c_a1 = 0.75  # chordwise position of aileron hinge
# section 2
xle2 = 0
yle2 = 7
c2 = 2
c_a2 = 0.75  # chordwise position of aileron hinge

input_template_path = os.path.join(INPUT_TEMPLATE_FOLDER, INPUT_TEMPLATE_FILE_NAME)
input_generated_path = os.path.join(INPUT_GENERATED_FOLDER, INPUT_GENERATED_FILE_NAME)

parser = InputFileGenerator()
parser.set_template_file(input_template_path)
parser.set_generated_file(input_generated_path)

parser.mark_anchor("#Mach")
parser.transfer_var(float(mach), 1, 1)
parser.reset_anchor()

parser.mark_anchor("#Sref")
parser.transfer_var(float(sref), 1, 1)
parser.transfer_var(float(cref), 1, 2)
parser.transfer_var(float(bref), 1, 3)
parser.reset_anchor()

# wing
# section 0
parser.mark_anchor("#Xle")
parser.transfer_var(float(c0), 1, 4)

# section 1
parser.mark_anchor("#Xle")
parser.transfer_var(float(yle1), 1, 2)
parser.transfer_var(float(c1), 1, 4)
parser.mark_anchor("CONTROL")
parser.transfer_var(float(c_a1), 1, 3)

# section 2
parser.mark_anchor("#Xle")
parser.transfer_var(float(yle2), 1, 2)
parser.transfer_var(float(c2), 1, 4)
parser.mark_anchor("CONTROL")
parser.transfer_var(float(c_a2), 1, 3)

parser.generate()
