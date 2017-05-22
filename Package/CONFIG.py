import ops
import iopc

def MAIN_ENV(args):
    pkg_path = args["pkg_path"]
    output_dir = args["output_path"]
    return False

def MAIN_EXTRACT(args):
    output_dir = args["output_path"]
    return False

def MAIN_CONFIGURE(args):
    return False

def MAIN_BUILD(args):
    output_dir = args["output_path"]
    iopc.make_squashfs(iopc.getTargetRootfs(), output_dir)
    return False

def MAIN_INSTALL(args):
    output_dir = args["output_path"]
    return False

def MAIN_CLEAN_BUILD(args):
    output_dir = args["output_path"]
    return False

def MAIN(args):
    print "image squashfs"

