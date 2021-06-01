import os.path
import subprocess as sp

# AVL_FOLDER_PATH = '~/Desktop/AVL_VLM'
AVL_FOLDER_PATH = '.'
AVL_EXE_NAME = 'avl335'
avl_path = os.path.join(AVL_FOLDER_PATH, AVL_EXE_NAME)

avl_ps = sp.Popen([avl_path], stdin=sp.PIPE, stdout=None, stderr=None)


def avl_command(cmd):
    cmd += '\n'
    cmd = cmd.encode('ascii')
    avl_ps.stdin.write(cmd)


avl_command('LOAD /Users/vianneydubois/Desktop/AVL_VLM/test_gen.avl')