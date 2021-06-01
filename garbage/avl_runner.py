## NOT WORKING

from openmdao.components.external_code_comp import ExternalCodeComp

INPUT_SESSION_FILE_NAME = "../resources/avl_session.txt"
STDERR_FILE_NAME = "test.err"
STDOUT_FILE_NAME = "test.log"

AVL_PATH = "../resources/avl335"

cl = 0.4
mach = 0.4

wing = ExternalCodeComp()

wing.options["command"] = AVL_PATH

wing.stdin = INPUT_SESSION_FILE_NAME
wing.stdout = STDOUT_FILE_NAME
wing.stderr = STDERR_FILE_NAME

try:
    wing.compute("", "")
except:
    print("AVL analysis iteration failed.")
