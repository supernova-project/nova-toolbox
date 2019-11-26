import git

def clone(path, repo):
    git.Git(path).clone(repo)