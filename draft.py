import os

AVL_SESSION_FOLDER = '.'
AVL_SESSION_FILE = 'resources/avl_session.txt'
avl_session_path = os.path.join(AVL_SESSION_FOLDER, AVL_SESSION_FILE)

command_string = ""

with open(avl_session_path, 'r') as avl_session:
    lines = avl_session.readlines()
    for line in lines:
        command_string += line

    output_st = lines[6][:-1]  # removing the '\n' character

print(output_st)
print(os.path.exists(output_st))
