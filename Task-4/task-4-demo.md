![image](https://user-images.githubusercontent.com/79650473/137677694-ce7d973d-d464-4e2e-ac05-3fa6b0657de0.png)
In the above screenshot I’ve demonstrated the auto-pull changes in a local repository from remote repository.
Here I’ve taken “studentsweb” as a github repository for demo.
So, In the first step, I’ve used “cd studentsweb” command to get into its working directory.
And we are in “gcs_iitmandi” ie predetermined branch in which we have to pull changes.
Now by running “git status” we can see that, this branch in local repository is “110” commits behind from the remote branch.
Now to pull these changes into local I ran a python script named “git_init.py” which is present inside the local repository directory.
By running the script in git status we can see that now the branch is “up-to-date” and changes have been pulled.
So, this was the demo of my python script.
