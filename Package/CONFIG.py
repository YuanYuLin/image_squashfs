import ops
import iopc

pkg_path = ""
output_dir = ""
output_rootfs_dir = ""
squashfs_name = "rootfs.squashfs"

def set_global(args):
    global pkg_path
    global output_dir 
    global output_rootfs_dir
    pkg_path = args["pkg_path"]
    output_dir = args["output_path"]
    output_rootfs_dir = iopc.getTargetRootfs()

def MAIN_ENV(args):
    set_global(args)
    return False

def MAIN_EXTRACT(args):
    set_global(args)

    ops.pkg_mkdir(output_rootfs_dir, "bin")
    ops.pkg_mkdir(output_rootfs_dir, "dev")
    ops.mknod_char(ops.path_join(output_rootfs_dir, "dev"), "console", "5", "1")
    ops.mknod_char(ops.path_join(output_rootfs_dir, "dev"), "null", "1", "3")

    ops.pkg_mkdir(output_rootfs_dir, "etc")
    ops.pkg_mkdir(ops.path_join(output_rootfs_dir, "etc"), "network")
    ops.pkg_mkdir(ops.path_join(output_rootfs_dir, "etc/network"), "if-pre-up.d")
    ops.pkg_mkdir(ops.path_join(output_rootfs_dir, "etc/network"), "if-up.d")
    ops.pkg_mkdir(ops.path_join(output_rootfs_dir, "etc/network"), "if-down.d")
    ops.pkg_mkdir(ops.path_join(output_rootfs_dir, "etc/network"), "if-post-down.d")
    ops.ln(ops.path_join(output_rootfs_dir, "etc"), "/tmp/resolv.conf", "resolv.conf")
    ops.pkg_mkdir(output_rootfs_dir, "lib")
    ops.pkg_mkdir(output_rootfs_dir, "mnt")
    ops.pkg_mkdir(output_rootfs_dir, "root")
    ops.pkg_mkdir(output_rootfs_dir, "sbin")
    ops.pkg_mkdir(output_rootfs_dir, "proc")
    ops.pkg_mkdir(output_rootfs_dir, "sys")
    ops.pkg_mkdir(output_rootfs_dir, "var")
    ops.pkg_mkdir(output_rootfs_dir, "tmp")
    ops.pkg_mkdir(output_rootfs_dir, "cgroup")
    ops.pkg_mkdir(output_rootfs_dir, "hdd")
    ops.ln(output_rootfs_dir, "lib", "lib64")

    return True

def MAIN_PATCH(args, patch_group_name):
    set_global(args)
    for patch in iopc.get_patch_list(pkg_path, patch_group_name):
        if iopc.apply_patch(output_dir, patch):
            continue
        else:
            sys.exit(1)

    return True

def MAIN_CONFIGURE(args):
    set_global(args)

    return False

def MAIN_BUILD(args):
    set_global(args)

    iopc.make_squashfs(iopc.getTargetRootfs(), output_dir)
    return False

def MAIN_INSTALL(args):
    set_global(args)

    ops.copyto(ops.path_join(output_dir, squashfs_name), iopc.getOutputRootDir())
    return False

def MAIN_CLEAN_BUILD(args):
    set_global(args)

    return False

def MAIN(args):
    set_global(args)
    print "image squashfs"

