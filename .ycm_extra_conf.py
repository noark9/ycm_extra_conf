import os
import ycm_core

# path which you do not want include in your project search path
PROJECT_PATH_IGNORE = [ '.git', 'Pods', '.vscode', '.xcodeproj', 'fastlane', 'Images.xcassets', 'fir_build', '.xcassets', '.xcworkspace', 'shenzhenrenTests', 'shenzhenrenUITests', '.lproj', '.idea' ]

BASE_FLAGS = [
        '-resource-dir',
        '/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/../lib/clang/8.0.0',
        '-x objective-c',
        '-arch armv7',
        '-fmessage-length=0',
        '-fmodules',
        '-gmodules',
        '-fmodules-cache-path=/Users/apple/Library/Developer/Xcode/DerivedData/ModuleCache',
        '-fdiagnostics-show-note-include-stack',
        '-fmacro-backtrace-limit=0',
        '-D__arm__=1',
        '-D__IPHONE_OS_VERSION_MIN_REQUIRED=80000',
        '-std=gnu99',
        '-fobjc-arc',
        '-Wnon-modular-include-in-framework-module',
        '-Werror=non-modular-include-in-framework-module',
        '-Wno-trigraphs',
        '-fpascal-strings',
        '-Os',
        '-fno-common',
        '-Wno-missing-field-initializers',
        '-Wno-missing-prototypes',
        '-Werror=return-type',
        '-Wunreachable-code',
        '-Wno-implicit-atomic-properties',
        '-Werror=deprecated-objc-isa-usage',
        '-Werror=objc-root-class',
        '-Wno-arc-repeated-use-of-weak',
        '-Wduplicate-method-match',
        '-Wno-missing-braces',
        '-Wparentheses',
        '-Wswitch',
        '-Wunused-function',
        '-Wno-unused-label',
        '-Wno-unused-parameter',
        '-Wunused-variable',
        '-Wunused-value',
        '-Wempty-body',
        '-Wconditional-uninitialized',
        '-Wno-unknown-pragmas',
        '-Wno-shadow',
        '-Wno-four-char-constants',
        '-Wno-conversion',
        '-Wconstant-conversion',
        '-Wint-conversion',
        '-Wbool-conversion',
        '-Wenum-conversion',
        '-Wshorten-64-to-32',
        '-Wpointer-sign',
        '-Wno-newline-eof',
        '-Wno-selector',
        '-Wno-strict-selector-match',
        '-Wundeclared-selector',
        '-Wno-deprecated-implementations',
        '-DOBJC_OLD_DISPATCH_PROTOTYPES=0',
        '-isysroot',
        '/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator.sdk',
        '-fstrict-aliasing',
        '-Wprotocol',
        '-Wdeprecated-declarations',
        '-miphoneos-version-min=8.0',
        '-g',
        '-Wno-sign-conversion',
        '-Wno-infinite-recursion',
        '-fembed-bitcode-marker',
        ]

BASE_INCLUDE_FLAGS = [
        '-I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform',
        '-I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator.sdk/usr/include',
        '-I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator.sdk/System/Library/Frameworks',
        '-I/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator.sdk/System/Library/Frameworks/SpriteKit.framework/Headers',
        '-I/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/../lib/clang/8.0.0/include',
        ]

OTHER_FLAGS = [
        '-MMD',
        '-MT',
        '-MF',
]

PROJECT_PATH = os.getcwd()

SOURCE_EXTENSIONS = [ '.cpp', '.cxx', '.cc', '.c', '.m', '.mm' ]

HEADER_EXTENSIONS = [ '.hpp', '.hxx', '.hh', '.h' ]

def FindPodPath():
    list_path = os.walk(PROJECT_PATH)
    for path, dir, file in list_path:
        if path.endswith('Pods'):
            return path
    return None

def FindPchPath():
    list_path = os.walk(PROJECT_PATH)
    for path, dirs, files in list_path:
        for file in files:
            if not CheckPathIgnore(path):
                continue
            if file.endswith('.pch'):
                return os.path.join(path, file);
    return None

def FindAllPod():
    items = []
    pod_path = FindPodPath()
    if (pod_path):
        list_pods = os.walk(pod_path)
        for path, dirs, files in list_pods:
            path = path.replace(' ', '\\ ')
            isystem = '-isystem ' + path
            include = '-I' + path
            items.append(isystem)
            items.append(include)
    return items

def CheckPathIgnore(path):
    for ignore in PROJECT_PATH_IGNORE:
        if path.find(ignore) > 0:
            return False
    return True

def FindAllPath():
    list_all_path = os.walk(PROJECT_PATH)
    items = []
    for path, dir, file in list_all_path:
        if not CheckPathIgnore(path):
            continue
        path = path.replace(' ', '\\ ')
        header = '-H' + path
        include = '-I' + path
        items.append(header)
        items.append(include)
    return items

def FlagsForFile( filename, **kwargs ):
    flags = BASE_FLAGS
    pch_path = FindPchPath()
    if pch_path:
        flags.append('-include')
        flags.append(pch_path)
    flags += BASE_INCLUDE_FLAGS
    flags += FindAllPod()
    flags += FindAllPath()
    flags += OTHER_FLAGS
    return { 'flags': flags, 'do_cache': True }

