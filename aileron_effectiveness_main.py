import os
import aileron_effectiveness as ae
import numpy as np

INPUT_TEMPLATE_FOLDER = "resources"
INPUT_TEMPLATE_FILE_NAME = "geom_wing.avl"

INPUT_GENERATED_FOLDER = "generated_files"
INPUT_GENERATED_FILE_NAME = "generated_wing.avl"

AVL_FOLDER = os.path.expanduser('resources')
AVL_EXE_NAME = 'avl335'

AVL_SESSION_FOLDER = 'resources'
AVL_SESSION_FILE = 'avl_session.txt'

AVL_STABILITY_FOLDER = '/Users/vianneydubois/PycharmProjects/avl_python/generated_files'
AVL_STABILITY_FILE_NAME = 'gen_wing_st.txt'


input_template_path = os.path.join(INPUT_TEMPLATE_FOLDER, INPUT_TEMPLATE_FILE_NAME)
input_generated_path = os.path.join(INPUT_GENERATED_FOLDER, INPUT_GENERATED_FILE_NAME)
avl_path = os.path.join(AVL_FOLDER, AVL_EXE_NAME)
avl_session_path = os.path.join(AVL_SESSION_FOLDER, AVL_SESSION_FILE)
avl_stability_path = os.path.join(AVL_STABILITY_FOLDER, AVL_STABILITY_FILE_NAME)

aileron_x_c_range = [0.70, 0.75, 0.80]

aileron_effect_list = ae.compute_aileron(avl_path,
                                         avl_session_path,
                                         input_template_path,
                                         input_generated_path,
                                         avl_stability_path,
                                         aileron_x_c_range)

print("\n ##### RESULTS #####")
print(aileron_x_c_range)
print(np.array(aileron_effect_list)*180/np.pi)