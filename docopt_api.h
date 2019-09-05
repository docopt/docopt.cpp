//
//  docopt.h
//  docopt
//
//  Created by Dmitriy Vetutnev on 2019-09-05.
//  Copyright (c) 2019 Dmitriy Vetutnev. All rights reserved.
//

#ifndef docopt__api_h_
#define docopt__api_h_

#ifdef DOCOPT_HEADER_ONLY
    #define DOCOPT_INLINE inline
    #define DOCOPT_API
#else 
    #define DOCOPT_INLINE

    // With Microsoft Visual Studio, export certain symbols so they 
    // are available to users of docopt.dll (shared library). The DOCOPT_DLL
    // macro should be defined if building a DLL (with Visual Studio),
    // and by clients using the DLL. The CMakeLists.txt and the
    // docopt-config.cmake it generates handle this.
    #ifdef DOCOPT_DLL
        // Whoever is *building* the DLL should define DOCOPT_EXPORTS.
        // The CMakeLists.txt that comes with docopt does this.
        // Clients of docopt.dll should NOT define DOCOPT_EXPORTS.
        #ifdef DOCOPT_EXPORTS
            #define DOCOPT_API __declspec(dllexport)
        #else
            #define DOCOPT_API __declspec(dllimport)
        #endif
    #else
        #define DOCOPT_API
    #endif
#endif

#endif /* defined(docopt__api_h_) */