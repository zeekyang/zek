# File: homework5.py

# 3.1

# 1. Git vs. GitHub
# Git is a software used for version control and tracking changes in code.
# GitHub is an online hosting service for Git repositories, allowing for collaboration.

# 2. Terminal vs. Command Line
# Terminal is an app that provides a text-based interface to interact with the system.
# Command Line is the environment inside the terminal where users type and execute commands.

# 3. Local vs. Remote Repository
# Local Repository exists on your own computer.
# Remote Repository is hosted online on a server.

# 4. Version Control
# Version Control records changes to files over time, allowing us to revert to earlier versions and track history.

# 5. Staging Area
# Staging Area is where you can prepare or review changes before committing.

# 6. git add
# Adds changes in files to the staging area.

# 7. git commit
# Records the changes in the staging area into the local repository.

# 8. git push
# Uploads local repository commits to a remote repository.

# 9. git status
# Displays the current state of the working directory and staging area.

# 10. git pull
# Fetches and merges changes from a remote repository into your local branch, updates local version with latest code.

# 11. pwd
# Prints the current working directory.

# 12. ls
# Lists the files and directories in the current directory.

# 13. cd
# Changes the current directory.

# 14. nano
# Opens the Nano text editor in the terminal.

# 15. touch
# Creates a new file or updates the timestamp of an existing file.

# 16. mv
# Moves or renames files.

# 17. rm
# Removes files permanently.

# 18. cat
# Displays the contents of a file in the terminal.

# 3.2
# 1. pwd

# 2. ls

# 3. cd brianna-repo
#    git pull

# 4. mv homework.py ../judy_decal/homework/

# 5. cd ../judy_decal/homework

# 6. cat homework.py

# 7. git add .
#    git commit -m "Completed homework"
#    git push

# 8. This means that her local repo is not as updaed as the remote repo, perhaps because someone else made changes to it.
#    She should do:
# git pull origin main
# git add .
# git commit -m "Resolved merge conflicts after pulling latest changes"
# git push origin main

# 9. cd ~/Recents

#4
#4.1
def checkDataType(value):
    return type(value).__name__

#4.2
def evenOrOdd(num):
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

#5
def sumWithLoop(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

#6.1
def duplicateList(lst):
    new_list = []
    for item in lst:
        new_list.append(item)
        new_list.append(item)
    return new_list

#6.2
# missing a colon after the function definition
def square(num):
    return num * num

#7.2
print(sumWithLoop([65,66,67,68,69]))







