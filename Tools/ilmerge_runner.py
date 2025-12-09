#!/usr/bin/env python3
import os
import argparse

descr = "Helps run ILMerge.exe. Intended to be run as a github submodule step."
parser = argparse.ArgumentParser(description=descr)
parser.add_argument("platform", choices=["netstandard2.0", "net47"])
args = parser.parse_args()

if args.platform == "netstandard2.0":
    base_dir = "nuget"
    include_check = "\\" + args.platform
    # Directories that have netstandard2.0 in the path and contain at least one dll.
    lib_dirs = []
    for root, dirs, files in os.walk(base_dir):
        if include_check in root and any([f.lower().endswith("dll") for f in files]):
            lib_dirs.append(root)

    # entries look like:
    # 'nuget\\packages\\microsoft.identitymodel.logging\\6.34.0\\lib\\netstandard2.0',
    # sort to provide repeatability
    lib_dirs.sort()
    dlls = """
        DuoUniversal.dll
        Microsoft.Bcl.AsyncInterfaces.dll
        Microsoft.CSharp.dll
        Microsoft.IdentityModel.JsonWebTokens.dll
        Microsoft.IdentityModel.Logging.dll
        Microsoft.IdentityModel.Tokens.dll
        System.Buffers.dll
        System.Memory.dll
        System.Net.Http.Json.dll
        System.Numerics.Vectors.dll
        System.Runtime.CompilerServices.Unsafe.dll
        System.Security.Cryptography.Cng.dll
        System.Text.Encodings.Web.dll
        System.Text.Json.dll
        System.Threading.Tasks.Extensions.dll
    """
    dlls_line = " ".join(dlls.replace("\n", " ").split())
    lib_line = ""
    for dir in lib_dirs:
        # The ILMerge.exe /lib arg contains a directory with dlls. It doesn't recurse into multiple dirs.
        lib_line += "/lib:\"..{}{}\" ".format(os.path.sep, dir)

    # The /out arg doesn't appear to like paths, so we chdir to the target dir.
    os.chdir("mergeNetstandard")
    # DLL Properties such as copyright, version, and original filename will all
    # come from the first DLL specified, so make sure DuoUniversal.dll is always the first one listed
    cmd = "..\\Tools\\ILMerge.exe /closed /out:DuoUniversalDeps.dll /keyFile:..\DuoUniversalDeps.snk {} {}".\
        format(lib_line, dlls_line)

elif args.platform == "net47":
    dlls = """
        DuoUniversal.dll
        Microsoft.Bcl.AsyncInterfaces.dll
        Microsoft.IdentityModel.JsonWebTokens.dll
        Microsoft.IdentityModel.Logging.dll
        Microsoft.IdentityModel.Tokens.dll
        System.Buffers.dll
        System.Memory.dll
        System.Net.Http.Json.dll
        System.Numerics.Vectors.dll
        System.Runtime.CompilerServices.Unsafe.dll
        System.Text.Encodings.Web.dll
        System.Text.Json.dll
        System.Threading.Tasks.Extensions.dll
        Microsoft.IdentityModel.Abstractions.dll
        System.ValueTuple.dll
    """

    dlls_line = " ".join(dlls.replace("\n", " ").split())
    lib_line = "/lib:\"..\\reference_assemblies\""
    target_platform_line = "/targetplatform:v4,\"..\\reference_assemblies\""

    os.chdir("mergeNet471")
    cmd = "..\\Tools\\ILMerge.exe /closed /out:DuoUniversalDeps471.dll /keyFile:..\DuoUniversalDeps.snk {} {} {}".\
        format(lib_line, target_platform_line, dlls_line)

# Max command length 8191. Current length around 2550 so we have headroom.
print("cmd (len:{}): {}".format(len(cmd), cmd))
print("About to run ILMerge.exe...")
ret = os.system(cmd)
print("Completed: ret: {}".format(ret))
if ret != 0:
    raise Exception("ILMerge.exe command failed. (Look above for error message)")

