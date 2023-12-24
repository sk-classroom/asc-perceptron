#/bin/bash
repoName=$1
git remote add template https://github.com/sk-classroom/$repoName
git fetch --all
git merge template/main --allow-unrelated-histories
