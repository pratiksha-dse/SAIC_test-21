from git import Repo
import os
#getting the path of current repository
git_dir =  os.getcwd()
#getting the name of repository using "Repo" function
try:
    repo=Repo(git_dir)
    #getting the active branch
    branch = repo.active_branch
    # fetching the changes from remote to local repository
    repo.remotes.origin.fetch()
    # Obtaining the changes in remote repository
    diff = str(Repo(git_dir).git.diff('origin/main')).splitlines()
    #if there are changes in remote then it will pull changes to local active brancg otherwise not.
    if len(diff) != 0:
        Repo(git_dir).remote().pull(branch)
except:
    print("Invalid repository or invalid access")