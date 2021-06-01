import os
import subprocess as sp
from openmdao.utils.file_wrap import InputFileGenerator, FileParser


def generate_geometry(input_template_path: str, input_generated_path: str):
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


def run_avl_solver(avl_path: str, avl_session_path: str):
    # Creating a string containing all the commands
    command_string = ""
    with open(avl_session_path, 'r') as avl_session:
        lines = avl_session.readlines()
        for line in lines:
            command_string += line
        # saving the output file path
        output_stab_path = lines[6][:-1]  # removing the '\n' character
    command_string = command_string.encode('ascii')

    # if the output file already exists, it will make the execution crash since AVL will ask if the
    # file must be overwritten or not, and it will desynchronize the program
    if os.path.exists(output_stab_path):
        os.remove(output_stab_path)

    avl_ps = sp.Popen([avl_path], stdin=sp.PIPE, stdout=None, stderr=None)
    avl_ps.communicate(input=command_string)  # sending the commands to AVL


def read_output(avl_session_path: str) -> list:
    # reading the output file path from the avl_session file
    with open(avl_session_path, 'r') as avl_session:
        output_stab_path = avl_session.readlines()[6][:-1]  # removing the '\n' character

    parser = FileParser()
    parser.set_file(output_stab_path)
    derivative_list = []

    parser.mark_anchor('Cld1')
    derivative_list.append(parser.transfer_var(0, 6))

    return derivative_list