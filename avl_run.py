## Runs AVL
### WORKING
import os.path
import subprocess as sp

AVL_SESSION_FOLDER = 'resources'
AVL_SESSION_FILE = 'avl_session.txt'
avl_session_path = os.path.join(AVL_SESSION_FOLDER, AVL_SESSION_FILE)

AVL_FOLDER = os.path.expanduser('resources')
AVL_EXE_NAME = 'avl335'
avl_path = os.path.join(AVL_FOLDER, AVL_EXE_NAME)

# Creating a sting containing all the commands
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
