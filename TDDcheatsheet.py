# new branch
git checkout -b feature/crazy-experiment
# move back to main branch
git checkout main
# merge branch (while on master)
git merge feature/crazy-experiment
# delete branch
git branch -D feature/crazy-experiment