In this task we have to create a script that performs git-auto pull from a remote git repository. So, in my script file , I've used a python module "git".
I imported "Repo" object from 'git' module and I've also imported 'os'. So , now starting with the script after importing required modules. Firstly I obtained the current directory of the repository
by using "git_dir = os.getcwd()", which provides the output in the form of "C:/Users/user-name/repo_name" and then by using "Repo" function from 'git' module like "repo=Repo(git_dir)" which return the name of repository like 'repo=repo_name'
and then in the next step I've found the current active branch of the repository by using "branch = repo.active_branch" which will return output as "branch=active_branch_name". And further I have fetched the changes from remote reository by 
using "repo.remotes.origin.fetch()" which will download all the files in my local remote repository and will not make changes in my current local repository. And then I have obtained if there is any changes in the remote repository by using
"diff=str(Repo(git_dir).git.diff('origin/main')).splitlines()" which provides the commits which are ahead of local branch in remote branch. And then in the last step I've checked if there are any changes or commits in remote 
repository then I'll pull changes by using " Repo(git_dir).remote().pull(branch)" otherwise I'll not pull changes. 
This is how the whole script works.
