#!/usr/bin/env python
"""Fetch the scripts needed for the snakefile"""

import argparse
import os

TOOLBOX_REPO = "{{cookiecutter.toolbox_repo}}"
COMMIT = "{{cookiecutter.toolbox_commit}}"
GITHUB_PROJECT_REMOTE = "{{cookiecutter.github_project_remote}}"
TOOLBOX_GITHUB_REPO = "{{cookiecutter.toolbox_github_repo}}"
TOOLBOX_COMMIT = "{{cookiecutter.toolbox_commit}}" 

def main(args):
    os.system('git init')
    os.system('git remote add origin {0}'.format(GITHUB_PROJECT_REMOTE))
    os.system('git submodule add https://github.com/{} toolbox'.format(TOOLBOX_GITHUB_REPO))
    os.chdir("toolbox")
    os.system('git checkout {0} && echo {0}'.format(TOOLBOX_COMMIT))
    os.chdir("..")
    # The checkout might have left the toolbox dirty
    os.system("git add toolbox")
    os.system('git commit -m "Added toolbox submodule"') 


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    args = parser.parse_args()
    main(args)
