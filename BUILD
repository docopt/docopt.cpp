# -*- python -*-

# This makes
#
#  #include "docopt.cpp/docopt.h"
#
# do the right thing, which is also as near as I can tell the
# recommended Bazel style (ie. prefixing the header with the
# library name.)
cc_library(
    name = "docopt",
    hdrs = ["docopt.h"],
    srcs = [
        "docopt.h",
        "docopt_value.h",
        "docopt_util.h",
        "docopt_private.h",
        "docopt.cpp"
    ],
    include_prefix = "docopt.cpp",
    visibility = ["//visibility:public"],
)
