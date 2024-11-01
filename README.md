# Git group 
I created this assignment to familiarize students with the basics of git workflow. Students can either work alone or in groups. *This repository is intended to be forked. That fork should be used as the main repository throughout the assignments so that this original repository remains unchanged.*

### Skills covered by these assignments
- Forking and cloning repositories
- Branching and merging
- Making pull requests
- Reviewing and merging PR's
- Resolving merge conflicts
- Rebasing and finalizing updates

## Assignment setup
1. Fork the repository to your own Github account.
2. Clone the forked repository to your pc with `git clone <forked_repository_url>`

## Assignment 1: Fix and debug
1. Each group should create a new branch from `main` named `fix-debug` for debugging work
2. Debug `file_1.py`
3. Commit the changes (Choose an appropriate commit message)
4. Push the `fix-debug` branch to the forked repository
5. Create a pull request

## Assignment 2: Add a feature
1. Create a new branch named `feature-senior-dog`
2. Enhance the `Dog` class in `file_2.py` as described in the docstring
3. Commit the changes
4. Push the branch and make a pull request

## Assignment 3: Code review
1. Switch to another students fork. Review the pull requests created by another student by adding comments or suggesting improvements.
2. Approve and merge the PR.

## Assignment 4: Resolve conflicts
1. Let's simulate a conflict! In the main repository, we will add some functionality to `file_1.py` and committing this to the main branch.
2. Now sync your forked repository with the main repository. (Hint: add the main repository as upstream remote, then try to merge the changes into your local main branch).
3. Resolve the conflict
4. Push the resolved main branch back to the forked repository

## Assignment 5: Final cleanup
1. Create a new branch `final-cleanup` and rebase it onto the latest `main` branch to ensure it has all updates from the previous assignments
2. Add a comment or docstring.
3. Commit and push `final-cleanup` to your fork and open a final PR.
