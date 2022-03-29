project('docopt', 'cpp', version : '0.6.2',
        default_options : ['cpp_std=c++11'])


docopt_sources = ['docopt.cpp']
docopt_headers = [ 'docopt.h',
                   'docopt_private.h',
                   'docopt_util.h',
                   'docopt_value.h']

stdlib_includes = []
if host_machine.system() == 'android'
  stdlib_includes += include_directories(
    [join_paths(meson.get_cross_property('stdlib_rootdir'), 'include'),
     join_paths(meson.get_cross_property('stdlib_rootdir'), 'libs/armeabi-v7a/include'),
     '/Users/germandiago/android/crystax-ndk-10.3.2/platforms/android-19/arch-arm/usr/include'])
endif

docopt_inc = include_directories('..')
docopt_lib = static_library('docopt', sources : [docopt_sources, docopt_headers],
                           include_directories : [docopt_inc, stdlib_includes])

docopt_dep = declare_dependency(link_with : docopt_lib,
                                include_directories : docopt_inc)
