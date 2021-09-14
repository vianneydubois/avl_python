import numpy as np
import control_effectiveness as ce
import os

INPUT_TEMPLATE_FOLDER = "resources"
INPUT_TEMPLATE_FILE_NAME = "geom.avl"

INPUT_GENERATED_FOLDER = "generated_files"
INPUT_GENERATED_FILE_NAME = "generated_full_geometry.avl"

AVL_FOLDER = os.path.expanduser('resources')
AVL_EXE_NAME = 'avl335'

AVL_SESSION_FOLDER = 'resources'
AVL_SESSION_FILE = 'avl_session.txt'

AVL_STABILITY_FOLDER = '/Users/vianneydubois/PycharmProjects/avl_python/generated_files'
AVL_STABILITY_FILE_NAME = 'full_st.txt'

input_template_path = os.path.join(INPUT_TEMPLATE_FOLDER, INPUT_TEMPLATE_FILE_NAME)
input_generated_path = os.path.join(INPUT_GENERATED_FOLDER, INPUT_GENERATED_FILE_NAME)
avl_path = os.path.join(AVL_FOLDER, AVL_EXE_NAME)
avl_session_path = os.path.join(AVL_SESSION_FOLDER, AVL_SESSION_FILE)
avl_stability_path = os.path.join(AVL_STABILITY_FOLDER, AVL_STABILITY_FILE_NAME)

# hinge chordwise position ranges
aileron_range = [.7, .75, .8]
elevator_range = [.7, .8]
rudder_range = [.5, .55, .6]

res = ce.compute_range(avl_path,
                      avl_session_path,
                 input_template_path,
                 input_generated_path,
                 avl_stability_path,
                 aileron_range,
                 elevator_range,
                 rudder_range)

print("\n\n#####  Control derivatives  ##### [rad^-1]")
print("##  Lines 1 & 2 : ailerons, 3 & 4 : elevator, 5 & 6 : rudder ##\n")
print(res)