# Purpose

The purpose of this repository is to generate a .DLL of the Duo Universal C# client, suitable for use in Windows products.

See [ADR](https://cisco-sbg.atlassian.net/wiki/spaces/dev/pages/657047974/ADFS+Universal+-+Duo+Universal+C+Dependency) for details of how this is intended to work.

# Cloning

This repository has duo_universal_csharp as a git submodule.  Use `git clone --recurse-submodules ...` to clone it.

If you didn't, you can use
`git submodule init`
then
`git submodule update`
to fetch the submodule.

# Pulling in Duo Universal C# changes
Follow the instructions at https://git-scm.com/book/en/v2/Git-Tools-Submodules for "Pulling in upstream changes":
`cd duo_universal_csharp`

`git fetch`

`git merge origin/main`

Then commit the changes:

`cd ..`

`git add duo_universal_csharp`

`git commit -m "Pulling in upstream changes"`

`git push origin main`

# Getting the built DLL
Go to the 'Actions' tab within the ZT-duo_universal_csharp_packager repository.

Select the 'build' workflow on the left then use the 'Run workflow' drop-down on the right to select a branch and start the workflow.

Select the workflow that was just started and download the 'build_deps' artifact. This will have the merged, signed DLL of the Duo Universal C# client assembly. There are two versions available: signedNet471/DuoUniversalDeps.dll which is only for use with Epic Hyperdrive, and signNetStandard/DuoUniversalDeps.dll for use with everything else.

# Other resources
[adfs - figure out duo universal dll dependency](https://phab.duosec.org/T145074) - Has notes on dependencies etc.


