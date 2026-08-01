import repofunctions as rf

"""
Fill the dictionary with the name of git commands as keys and the lambda of the function that returns the command and needed parameters as string
"""
git_commands = {
    "clone": lambda repository_url: rf.git_clone(repository_url),
    "pull": lambda remote, branch: rf.git_pull(remote, branch),
    "push": lambda remote, branch: rf.git_push(remote, branch),
    "branch": lambda branch_name: rf.git_branch(branch_name),
    "checkout": lambda branch_name: rf.git_checkout(branch_name),
    "merge": lambda branch_name: rf.git_merge(branch_name),
    "rebase": lambda branch_name: rf.git_rebase(branch_name),
    "status": lambda: rf.git_status(),
    "log": lambda: rf.git_log(),
    "diff": lambda: rf.git_diff(),
}
