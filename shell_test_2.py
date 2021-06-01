import os.path
import subprocess as sp

load = 'LOAD'
input_geometry = '/Users/vianneydubois/Desktop/AVL_VLM/test_gen.avl'
oper = 'OPER'
alpha = 'A C 0.5'
execute = 'X'
stab = 'ST'
output_st = '/Users/vianneydubois/Desktop/AVL_VLM/test_out.txt'
back = ''
quit = 'QUIT'

command_list = [load,
                input_geometry,
                oper,
                alpha,
                execute,
                stab,
                output_st,
                back,
                quit]

command_string = '\n'.join(command_list)
command_string = command_string.encode('ascii')

# AVL_FOLDER_PATH = '~/Desktop/AVL_VLM'
AVL_FOLDER_PATH = '.'
AVL_EXE_NAME = 'avl335'
avl_path = os.path.join(AVL_FOLDER_PATH, AVL_EXE_NAME)

avl_ps = sp.Popen([avl_path], stdin=sp.PIPE, stdout=None, stderr=None)
avl_ps.communicate(input=command_string)


