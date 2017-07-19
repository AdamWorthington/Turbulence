
#!/usr/bin/env bash

make docs

git add --all
git commit -m "Building docs in master."

# Switch branches and clear directory
git checkout gh-pages
git pull origin gh-pages
rm -rf ./*
touch .nojekyll

# Get docs from master
git checkout master backend/docs/_build/html
mv ./backend/docs/_build/html/* .
rm -rf ./backend/docs
git add --all
git commit -m "Publishing revised docs."
git push origin gh-pages

# Go back to master
git checkout master