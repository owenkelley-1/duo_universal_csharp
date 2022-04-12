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

# Pulling in Duo Universal C# changes
Follow the instructions at https://git-scm.com/book/en/v2/Git-Tools-Submodules for "Pulling in upstream changes":
`cd duo_universal_csharp'
`git fetch`
`git merge origin/main`

Then commit the changes:
`cd ..`
`git add duo_universal_csharp`
`git commit -m "Pulling in upstream changes"`
`git push origin main`

# Getting the built DLL
Go to the `duo_universal_csharp_packager` project in GitLab https://ci.duosec.org/mirrors/duo_universal_csharp_packager/-/pipelines.

If you just pushed a diff (such as merging in upstream changes to duo_universal_csharp) there is probably a pipeline that is running or just finished.  Otherwise, you can manually run the pipeline on the main branch.

Open the target pipeline and click on the last step (sign_merged_dll), then download the artifacts of that job.  This will have the merged, signed DLL of the Duo Universal C# client assembly.
