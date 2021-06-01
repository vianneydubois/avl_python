import os
from openmdao.utils.file_wrap import FileParser

AVL_SESSION_FOLDER = 'resources'
AVL_SESSION_FILE = 'avl_session.txt'
avl_session_path = os.path.join(AVL_SESSION_FOLDER, AVL_SESSION_FILE)

# reading the output file path from the avl_session file
with open(avl_session_path, 'r') as avl_session:
    output_stab_path = avl_session.readlines()[6][:-1]  # removing the '\n' character
print(f"OUTPUT FILE PATH : {output_stab_path}")

parser = FileParser()
parser.set_file(output_stab_path)
derivative_list = []


parser.mark_anchor("Cld1")
derivative_list.append(parser.transfer_var(0, 6))

cld1 = derivative_list[0]*180/3.142

print(f"Cld1 = {cld1:.3f}")
