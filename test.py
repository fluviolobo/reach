import git 
import os

git_dir = os.getcwd()
print( git_dir )

g = git.cmd.Git(git_dir)
g.pull()



"""
References

1. https://stackoverflow.com/questions/15315573/how-can-i-call-git-pull-from-within-python
"""
