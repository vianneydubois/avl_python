### NOT WORKING
import os.path
import subprocess as sp

# AVL_FOLDER_PATH = '~/Desktop/AVL_VLM'
AVL_FOLDER_PATH = '..'
AVL_EXE_NAME = 'avl335'
avl_path = os.path.join(AVL_FOLDER_PATH, AVL_EXE_NAME)

avl_ps = sp.Popen([avl_path], stdin=sp.PIPE, stdout=None, stderr=None)


def avl_command(cmd):
    cmd += '\n'
    cmd = cmd.encode('ascii')
    avl_ps.stdin.write(cmd)


avl_command('LOAD')
avl_command('/Users/vianneydubois/Desktop/AVL_VLM/test_gen.avl')
avl_command('OPER')
avl_command('A C 0.4')
avl_command('X')
avl_command('ST')
avl_command('/Users/vianneydubois/Desktop/AVL_VLM/test_out.txt')
avl_command('')
avl_command('QUIT')
avl_ps.stdin.flush()
