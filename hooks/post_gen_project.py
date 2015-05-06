#!/usr/bin/env python
"""Fetch the scripts needed for the snakefile"""

import argparse
import os

COMMIT = "{{cookiecutter.toolbox_commit}}"
GITHUB_PROJECT_REMOTE = "{{cookiecutter.github_project_remote}}"

WORKFLOW_REPO = "{{cookiecutter.snakemake_workflows_repo}}"
WORKFLOW_COMMIT = "{{cookiecutter.workflow_commit}}"

TOOLBOX_GITHUB_REPO = "{{cookiecutter.toolbox_github_repo}}"
TOOLBOX_COMMIT = "{{cookiecutter.toolbox_commit}}" 


def main(args):
    os.system('git init')
    os.system('git remote add origin {0}'.format(GITHUB_PROJECT_REMOTE))
    # Add toolbox as submodule
    os.system('git submodule add https://github.com/{} toolbox'.format(TOOLBOX_GITHUB_REPO))
    os.chdir("toolbox")
    os.system('git checkout {0} && echo {0}'.format(TOOLBOX_COMMIT))
    os.chdir("..")
    
    # The checkout might have left the toolbox dirty
    os.system("git add toolbox")
    os.system('git commit -m "Added toolbox submodule"') 


    # Add snakemake-workflows as submodule
    os.system('git submodule add https://github.com/{} snakemake-workflows'.format(WORKFLOW_REPO))
    os.chdir("snakemake-workflows")
    os.system('git checkout {0}'.format(WORKFLOW_COMMIT))
    os.chdir("..")
    
    # The checkout might have left the toolbox dirty
    os.system("git add snakemake-workflows")
    os.system('git commit -m "Added snakemake-workflows submodule"') 


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    args = parser.parse_args()
    main(args)
