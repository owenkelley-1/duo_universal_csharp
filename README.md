# Purpose

The purpose of this repository is to generate a .DLL of the Duo Universal C# client, suitable for use in Windows products.

See https://wiki.duosec.org/pages/viewpage.action?pageId=33826201 for details of how this is intended to work.

# Cloning

This repository has duo_universal_csharp as a git submodule.  Use `git clone --recurse-submodules ...` to clone it.

If you didn't, you can use
`git submodule init`
then
`git submodule update`
to fetch the submodule.

# TODO
Create a CI workflow that:
1) Builds Duo Universal C# (needs dotnet, or maybe msbuild)
2) Merges duo universal with its dependencies (in ThirdParty)
3) ? Sign it ?
4) Export the combined DLL as an artifact
