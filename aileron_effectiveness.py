import os
import subprocess as sp
import numpy as np
from openmdao.utils.file_wrap import InputFileGenerator, FileParser


def generate_geometry(input_template_path: str, input_generated_path: str, aileron_x_c: float):
    mach = 0.78
    sref = 122.4
    bref = 34.1
    cref = 4.2
    sweep_0 = 0.472709635153824

    ## WING
    # section 0
    xle0 = 0
    yle0 = 0
    c0 = 5.968267075021899
    # section 2
    yle2 = bref/2
    xle2 = yle2 * np.tan(sweep_0)
    c2 = 1.6599009162290415
    c_a2 = aileron_x_c  # chordwise position of aileron hinge
    # section 1
    yle1 = 0.8*bref/2
    xle1 = yle1 * np.tan(sweep_0)
    c1 = c0 + 0.8 * (c2 - c0)
    c_a1 = aileron_x_c  # chordwise position of aileron hinge

    ## HORIZONTAL TAIL
    x_translate_ht = 19.341
    z_translate_ht = 2
    # section 0
    ht_xle0 = 0
    ht_yle0 = 0
    ht_c0 = 4.19446
    c_e0 = 0.75  # chordwise position of elevator hinge
    # section 1
    ht_xle1 = 3.8419
    ht_yle1 = 5.84509
    ht_c1 = 1.25834
    c_e1 = 0.75  # chordwise position of elevator hinge

    ## VERTICAL TAIL
    x_translate_vt = 17.137
    z_translate_vt = 2.749
    # section 0
    vt_xle0 = 0
    vt_zle0 = 0
    vt_c0 = 5.90875
    c_r0 = 0.75  # chordwise position of rudder hinge
    # section 1
    vt_xle1 = 5.724
    vt_zle1 = 6.70056
    vt_c1 = 1.77262
    c_r1 = 0.75  # chordwise position of rudder hinge


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

    # WING
    # section 0
    parser.mark_anchor("#Xle")
    parser.transfer_var(float(c0), 1, 4)
    # section 1
    parser.mark_anchor("#Xle")
    parser.transfer_var(float(xle1), 1, 1)
    parser.transfer_var(float(yle1), 1, 2)
    parser.transfer_var(float(c1), 1, 4)
    parser.mark_anchor("CONTROL")
    parser.transfer_var(float(c_a1), 1, 3)
    # section 2
    parser.mark_anchor("#Xle")
    parser.transfer_var(float(xle2), 1, 1)
    parser.transfer_var(float(yle2), 1, 2)
    parser.transfer_var(float(c2), 1, 4)
    parser.mark_anchor("CONTROL")
    parser.transfer_var(float(c_a2), 1, 3)

    # HORIZONTAL TAIL
    parser.reset_anchor()
    parser.mark_anchor('Stab')
    parser.mark_anchor('TRANSLATE')
    parser.transfer_var(float(x_translate_ht), 1, 1)
    parser.transfer_var(float(z_translate_ht), 1, 3)
    # section 0
    parser.mark_anchor("#Xle")
    parser.transfer_var(float(ht_c0), 1, 4)
    parser.mark_anchor("CONTROL")
    parser.transfer_var(float(c_e0), 1, 3)
    # section 1
    parser.mark_anchor("#Xle")
    parser.transfer_var(float(ht_xle1), 1, 1)
    parser.transfer_var(float(ht_yle1), 1, 2)
    parser.transfer_var(float(ht_c1), 1, 4)
    parser.mark_anchor("CONTROL")
    parser.transfer_var(float(c_e1), 1, 3)

    # VERTICAL TAIL
    parser.reset_anchor()
    parser.mark_anchor('Fin')
    parser.mark_anchor('TRANSLATE')
    parser.transfer_var(float(x_translate_vt), 1, 1)
    parser.transfer_var(float(z_translate_vt), 1, 3)
    # section 0
    parser.mark_anchor("#Xle")
    parser.transfer_var(float(vt_c0), 1, 4)
    parser.mark_anchor("CONTROL")
    parser.transfer_var(float(c_r0), 1, 3)
    # section 1
    parser.mark_anchor("#Xle")
    parser.transfer_var(float(vt_xle1), 1, 1)
    parser.transfer_var(float(vt_zle1), 1, 3)
    parser.transfer_var(float(vt_c1), 1, 4)
    parser.mark_anchor("CONTROL")
    parser.transfer_var(float(c_r1), 1, 3)

    parser.generate()


def run_avl_solver(avl_path: str, avl_session_path: str, avl_stability_path: str):
    # Creating a string containing all the commands
    command_string = ""
    with open(avl_session_path, 'r') as avl_session:
        lines = avl_session.readlines()
        for line in lines:
            command_string += line

    command_string = command_string.encode('ascii')

    # if the output file already exists, it will make the execution crash since AVL will ask if the
    # file must be overwritten or not, and it will desynchronize the program
    if os.path.exists(avl_stability_path):
        os.remove(avl_stability_path)

    avl_ps = sp.Popen([avl_path], stdin=sp.PIPE, stdout=None, stderr=None)
    avl_ps.communicate(input=command_string)  # sending the commands to AVL


def read_output(avl_stability_path: str) -> list:
    # reading the output file path from the avl_session file
    #with open(avl_session_path, 'r') as avl_session:
     #   output_stab_path = avl_session.readlines()[6][:-1]  # removing the '\n' character

    parser = FileParser()
    parser.set_file(avl_stability_path)
    derivative_list = []

    parser.mark_anchor('Cld1')
    derivative_list.append(parser.transfer_var(0, 6))

    return derivative_list


def compute_aileron(avl_path: str,
                    avl_session_path: str,
                    input_template_path: str,
                    input_generated_path: str,
                    avl_stability_path: str,
                    aileron_x_c_range: list) -> list:

    aileron_effectiveness_list = []
    for aileron_x_c in aileron_x_c_range:
        generate_geometry(input_template_path, input_generated_path, aileron_x_c)
        run_avl_solver(avl_path, avl_session_path, avl_stability_path)
        aileron_effectiveness_list.append(read_output(avl_stability_path)[0])

    return aileron_effectiveness_list