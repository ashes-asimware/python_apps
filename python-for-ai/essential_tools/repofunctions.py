def git_init():
    return "git init"


def git_clone(repository_url):
    return f"git clone {repository_url}"


def git_pull(remote, branch):
    return f"git pull {remote} {branch}"


def git_push(remote, branch):
    return f"git push {remote} {branch}"


def git_branch(branch_name):
    return f"git branch {branch_name}"


def git_checkout(branch_name):
    return f"git checkout {branch_name}"


def git_merge(branch_name):
    return f"git merge {branch_name}"


def git_rebase(branch_name):
    return f"git rebase {branch_name}"


def git_status():
    return "git status"


def git_log():
    return "git log"


def git_diff():
    return "git diff"
