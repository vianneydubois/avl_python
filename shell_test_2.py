import os.path
import subprocess as sp

AVL_FOLDER_PATH = '.'
AVL_EXE_NAME = 'avl335'
avl_path = os.path.join(AVL_FOLDER_PATH, AVL_EXE_NAME)


def avl_command(cmd):
    return sp.run(cmd, check=True, shell=True)


result = avl_command([avl_path])

#result = avl_command(['LOAD', '/Users/vianneydubois/Desktop/AVL_VLM/test_gen.avl'])
