"""
A simple demo of git in memory.

This demo is a simplified version of git. It only supports 1 file & the following operations:
    - commit .................................................. def commit(file_new)
    - create a new branch ..................................... def new_branch(branch_name)
    - fork a branch from another branch ....................... def fork_branch(source, target)
    - switch the current branch ............................... def switch_branch(branch_name)

"""

import difflib


def _hash(string):
    """Generate hash for a string."""
    return hash(string)


def compare(string1, string2):
    """Compare two strings and return the diff info."""
    diff = difflib.unified_diff(string1.splitlines(), string2.splitlines())
    return '\n'.join(diff)


def commit(file_new):
    """Commit a file and return the hash of the commit."""
    global file_old

    # gather commit info
    commit_diff = compare(file_old, file_new)
    commit_hash = _hash(commit_diff)

    # generate a new commit
    commits[commit_hash] = commit_diff

    # update commit to branch
    branches[curr_branch].append(commit_hash)

    # update `file_old`
    file_old = file_new

    return commit_hash


def new_branch(branch_name):
    """Create a new branch."""
    branches[branch_name] = []


def fork_branch(source, target):
    """Fork a branch from another branch."""
    # get the commits of the source branch
    commits_source = branches[source]
    # create a new branch
    branches[target] = commits_source.copy()


def switch_branch(branch_name):
    """Switch the current branch."""
    global curr_branch
    curr_branch = branch_name


if __name__ == '__main__':
    # init git worktree
    commits = {}    # {commit_hash: commit_diff} ........................ stored all the commits indexed by their `hash`
    branches = {    # {branch_name: branch_list} ........................ stored all the branches indexed by their `name`
        "master": [],   # Each branch is a list of commits.
    }
    file_old = ""  # the content of the last commit
    curr_branch = "master"  # the current branch
    # init end.

    # [TASK 1] create a new branch
    if not print("\n\n===== TASK 1 ====="):
        files = [
            "Line1\nLine2\nLine3\n",
            "Line1\nLine2\nLine43\nLine new\nLine n1\n",
            "Line1\nLine2"
        ]

        commit(files[0])
        print(branches)
        commit(files[1])
        print(branches)
        commit(files[2])
        print(branches)

        # get the hash of the latest commit
        latest_commit_hash = branches["master"][-1]
        # print the info (only diff info, in this demo) of the latest commit
        print(commits[latest_commit_hash])

    # [TASK 2] create another branch
    if not print("\n\n===== TASK 2 ====="):
        new_branch("dev")
        fork_branch("master", "dev")
        switch_branch("dev")
        print(branches[curr_branch])
        # add a new commit to the `dev` branch
        commit("Line1\nLine2\nLine3\nLine4\n")
        print(branches[curr_branch])
