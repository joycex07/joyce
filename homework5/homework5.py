"""
Homework 1+2 Review
1. 
Git: A version control system used to track changes in code locally. 
GitHub: A cloud-based platform that hosts Hit repositories and enables collaboration.
2. 
Terminal: The application used to interact with the system.
Command Line: The text-based way of interacting with the system through typing commands.
3. 
Local Repository: The version of your project stored on your own computer.
Remote Repository: The version of your project stored on GitHub.
4. Version Control: A system that records changes to files over time so you can track history and revert if needed.
5. Staging Area: A place where changes are prepared before being commited to the repository. 
6. git add: add chagnes to the staging area
7. git commit: saves staged chagnes ot the local repository with message.
8. git push: uploads local commits to a remote repository.
9. git status: shows current state of working directory and staging area.
10. git pull: fetches and merges chagnes from remote repository to local repository.
11. pwd: prints current working directory path.
12. ls: lists files and directories in the current directory.
13. cd: changes the current directory.
14. nano: opens text editor in terminal.
15. touch: creates a new empty file
16. mv: moves or renames files and directories.
17. rm: deletes files or directories
18: cat: displaycs contents of a file in terminal

A Directory Tree
1. pwd
2. ls
3. cd ..
   cd brianna_repo
   git pull
4. mv ~/python_decal/brianna_repo/homework.py ~/python_decal/judy_decal/homework/
5. cd ~/python_decal/brianna_repo
6. cat homework.py
7. git add .
   git commit -m "Finished homework"
   git push
8. This means there are commts on GitHub that you don't have locally. 
   git pull origin main
   git push origin main
9. cd /Users/brianna/Recents
"""

## Homework 3 Review

def checkDataType(n):
   s = str(type(n))
   return s.split("'")[1]

def evenOrOdd(n):
   if n % 2 == 0:
      return "Even"
   return "Odd"

def sumWithLoop(numbers):
   total = 0
   for i in numbers:
      total += i
   return total

## Homework 4
def duplicateList(lst):
   newLst = []
   for i in lst:
      newLst.append(i)
      newLst.append(i)
   return newLst

def square(num):
   return num*num


lst = ['a', 'b', 'c']
print(duplicateList(lst))