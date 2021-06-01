import os
import aileron_effectiveness as ae

INPUT_TEMPLATE_FOLDER = "resources"
INPUT_TEMPLATE_FILE_NAME = "geom_wing.avl"

INPUT_GENERATED_FOLDER = "generated_files"
INPUT_GENERATED_FILE_NAME = "generated_wing.avl"

AVL_FOLDER = os.path.expanduser('resources')
AVL_EXE_NAME = 'avl335'

AVL_SESSION_FOLDER = 'resources'
AVL_SESSION_FILE = 'avl_session.txt'


input_template_path = os.path.join(INPUT_TEMPLATE_FOLDER, INPUT_TEMPLATE_FILE_NAME)
input_generated_path = os.path.join(INPUT_GENERATED_FOLDER, INPUT_GENERATED_FILE_NAME)
avl_path = os.path.join(AVL_FOLDER, AVL_EXE_NAME)
avl_session_path = os.path.join(AVL_SESSION_FOLDER, AVL_SESSION_FILE)


ae.generate_geometry(input_template_path, input_generated_path)

ae.run_avl_solver(avl_path, avl_session_path)

derivative_list = ae.read_output(avl_session_path)

print(f"\nCld1 = {derivative_list[0]*180/3.14:.3f}")