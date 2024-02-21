def colored(text, color_code):
    """
    Wrap the text with the ANSI escape codes for the given color.
    """
    return f"\033[{color_code}m{text}\033[0m"

def add_command(commands, text, color_code, is_command=False):
    """
    Adds a command or comment to the commands list with the appropriate color formatting.
    """
    if is_command:
        commands.append(colored(text, color_code))
    else:
        commands.append(colored("-----------------------------------------------------", "1;37"))
        commands.append(colored(text, color_code))

def generate_git_commands(new_branch_name, commit_message, repo_url):
    """
    Generate a list of git commands to sync with the remote repository,
    create a new branch, and commit changes, with improved modularity and color coding.
    """
    repository_name = repo_url.split('/')[-1].replace('.git', '')

    # Color codes: green for comments, magenta for commands
    green = "0;32"
    magenta = "0;35"

    commands = []
    add_command(commands, "# Test connection and clone the repository", green) # clones all files, history, and branches
    add_command(commands, f"git remote -v", magenta, is_command=True)
    add_command(commands, f"git clone {repo_url}", magenta, is_command=True)
    add_command(commands, f"# Reminder: Change to the cloned directory", green)
    add_command(commands, f"cd your-cloned-directory", magenta, is_command=True)
    add_command(commands, "# Fetch the latest changes from all branches", green)
    add_command(commands, "git fetch --all", magenta, is_command=True)
    add_command(commands, "# Switch to the master branch", green)
    add_command(commands, "git checkout master", magenta, is_command=True)
    add_command(commands, "# Pull the latest changes from the master branch", green)
    add_command(commands, "git pull origin master", magenta, is_command=True)
    add_command(commands, "# Create and switch to the new branch", green)
    add_command(commands, f"git checkout -b {new_branch_name}", magenta, is_command=True)
    add_command(commands, "# Check the current branch", green)
    add_command(commands, "git status", magenta, is_command=True)
    add_command(commands, "# Reminder: Make your code changes now", green)
    add_command(commands, "# Add changes to staging", green)
    add_command(commands, "git add .", magenta, is_command=True)
    add_command(commands, "# Commit the changes", green)
    add_command(commands, f"git commit -m \"{commit_message}\"", magenta, is_command=True)
    add_command(commands, "# Push the new branch to the remote repository", green)
    add_command(commands, f"git push -u origin {new_branch_name}", magenta, is_command=True)
    add_command(commands, "# Reminder: If it's a new branch - not in the repository yet,\n# need to use -u (shorthand for --set-upstream), then just use git push or git pull", green)


    return '\n'.join(commands)

new_branch_name = input("Enter the name of the new branch: ")
commit_message = input("Enter the commit message: ")
repo_url = input("Enter the repository URL (if SSL connection, starts with git): ")

git_instructions = generate_git_commands(new_branch_name, commit_message, repo_url)
print(git_instructions)

# The script should be run in a local Python environment where stdin is available.

# test connection:
# with ssh -T git@github.com or curl -u username https://api.github.com/user for basic HTTPS connectivity
# git remote -v
# git config user.name
# git config user.email

# git clone VS git pull
# git clone {repo_url}:
# initializes a .git directory inside and clones the remote repository to your local machine, including all files, history, and branches.
# git pull {repo_url}:
# Fetches changes from the remote branch and merges them into your local branch. It's essentially a combination of git fetch followed by git merge.
# setting upstream tracking with -u, you can just use git push or git pull while on new-branch

# The .git directory contains all the necessary repository metadata and object database.
# The .git directory is what makes a directory a Git repository.
# Changes to the .git directory can corrupt the repository.

#### IF YOU HAVE INCORRECTLY NAMED THE BRANCH ####
# Steps if you have named a branch incorrectly AND pushed this to the remote repository:

# Check on which branch you are:
#     git branch -a

# Switch to the local branch you want to rename
#     git checkout <old_name>

# Rename the local branch
#     git branch -m <new_name>

# Push the <new_name> local branch and reset the upstream branch
#     git push origin -u <new_name>

# Delete the <old_name> remote branch
#     git push origin --delete <old_name>

#### Fetch the Latest List of Branches from Remote ####
#   git fetch --prune
# List all branches again
#   git branch -a
# Delete local branch
#   git branch -d feature/branch
# Delete local branch unmerged changes with unmerged changes
#   git branch -D feature/branch

#### DELETE REMOTE & LOCAL BRANCH ####
# Delete remote
#       git push origin --delete hotfix/branch
# Change branch
#       git checkout master
# Delete local
#       git branch -D hotfix/branch


### DISCARD ALL LOCAL CHANGES AND COMMITS !!
# and completely overwrite your local repo
# with the state of the remote repository:


# Fetch the latest history from remote
#   git fetch origin

# Reset your current branch to the latest state from remote
#   git reset --hard origin/master

# Clean up any untracked files or directories in your local repository
#   git clean -fd