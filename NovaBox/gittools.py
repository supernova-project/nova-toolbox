import git

def clone(path, repo):
    git.Git(path).clone(repo, recursive=True)


def checkout(path, branch):
    git.Git(path).checkout(branch)