project('docopt', 'cpp', version : '0.6.2',
        default_options : ['cpp_std=c++11'])


docopt_sources = ['docopt.cpp']
docopt_headers = [ 'docopt.h',
                   'docopt_private.h',
                   'docopt_util.h',
                   'docopt_value.h']
		
docopt_inc = include_directories('..')
docopt_lib = static_library('docopt', sources : [docopt_sources, docopt_headers],
                           include_directories : docopt_inc)

docopt_dep = declare_dependency(link_with : docopt_lib,
                                include_directories : docopt_inc)
