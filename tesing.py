print("hello doston")
PS C:\Users\Abrar Nadaf\Desktop\github> git status
On branch master
Changes to be committed:
        new file:   extention.py

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   tesing.py

[master 68f2889] added extention.py
 1 file changed, 9 insertions(+)
 create mode 100644 extention.py
PS C:\Users\Abrar Nadaf\Desktop\github> git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
PS C:\Users\Abrar Nadaf\Desktop\github> git push         
fatal: The current branch master has no upstream branch.

    git push --set-upstream origin master

To have this happen automatically for branches without a tracking
upstream, see 'push.autoSetupRemote' in 'git help config'.

PS C:\Users\Abrar Nadaf\Desktop\github> 
PS C:\Users\Abrar Nadaf\Desktop\github> git add .
[master 5764b94] added extention.py
 1 file changed, 1 insertion(+)
PS C:\Users\Abrar Nadaf\Desktop\github> git push
fatal: The current branch master has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin master

To have this happen automatically for branches without a tracking

PS C:\Users\Abrar Nadaf\Desktop\github> git push -u origin master
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 8 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (6/6), 748 bytes | 187.00 KiB/s, done.
Total 6 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/Abrar060795/github.git
PS C:\Users\Abrar Nadaf\Desktop\github> git status
On branch master

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   extention.py

no changes added to commit (use "git add" and/or "git commit -a")
PS C:\Users\Abrar Nadaf\Desktop\github> git add .
PS C:\Users\Abrar Nadaf\Desktop\github> git commit -m "updated extension.py"
PS C:\Users\Abrar Nadaf\Desktop\github> git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 326 bytes | 163.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/Abrar060795/github.git
   5764b94..3599e72  master -> master
PS C:\Users\Abrar Nadaf\Desktop\github> git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   extention.py

PS C:\Users\Abrar Nadaf\Desktop\github> git commit -m "updated extention.py"
[master db24560] updated extention.py
 1 file changed, 14 insertions(+), 1 deletion(-)
PS C:\Users\Abrar Nadaf\Desktop\github> git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 756 bytes | 378.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/Abrar060795/github.git
   3599e72..db24560  master -> master
PS C:\Users\Abrar Nadaf\Desktop\github> 