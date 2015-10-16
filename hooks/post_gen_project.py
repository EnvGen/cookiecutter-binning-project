#!/usr/bin/env python
"""Fetch the scripts needed for the snakefile"""

import argparse
import os
import logging

PROJECT_NAME = "{{cookiecutter.project}}"

COMMIT = "{{cookiecutter.toolbox_commit}}"
GITHUB_PROJECT_REMOTE = "{{cookiecutter.github_project_remote}}"

WORKFLOW_REPO = "{{cookiecutter.snakemake_workflows_repo}}"
WORKFLOW_COMMIT = "{{cookiecutter.workflow_commit}}"

TOOLBOX_GITHUB_REPO = "{{cookiecutter.toolbox_github_repo}}"
TOOLBOX_COMMIT = "{{cookiecutter.toolbox_commit}}" 

LOGFILE_LOCATION = os.path.expanduser("{{cookiecutter.logfile_location}}")

def main(args):
    # Create logfile with link to main.log within repo
    LOGFILE_LOCATION = LOGFILE_LOCATION.format(year=datetime.now().year,
            month=datetime.now().month,
            project_name=PROJECT_NAME)

    if os.path.isfile(LOGFILE_LOCATION):
        raise Exception("Logfile already exists, please delete it and start over")

    open(LOGFILE_LOCATION, 'w').close()
    os.symlink(LOGFILE_LOCATION, 'main.log')

    logging.basicConfig(format='%(asctime)s %(message)s', filename='main.log', level=logging.INFO) 
    os.system('git init')

    GITHUB_PROJECT_REMOTE=GITHUB_PROJECT_REMOTE.format(year=datetime.now().year,
            month=datetime.now().month,
            project_name=PROJECT_NAME)

    os.system('git remote add origin {0}'.format(GITHUB_PROJECT_REMOTE))
    logging.info("Initalized git repo with remote {0}".format(GITHUB_PROJECT_REMOTE))

    # Add toolbox as submodule
    os.system('git submodule add https://github.com/{} toolbox'.format(TOOLBOX_GITHUB_REPO))
    os.chdir("toolbox")
    os.system('git checkout {0} && echo {0}'.format(TOOLBOX_COMMIT))
    os.chdir("..")

    # The checkout might have left the toolbox dirty
    os.system("git add toolbox")
    os.system('git commit -m "Added toolbox submodule"') 
    logging.info("Added toolbox repo {0} at {1} as submodule.".format(TOOLBOX_GITHUB_REPO, TOOLBOX_COMMIT))

    # Add snakemake-workflows as submodule
    os.system('git submodule add https://github.com/{} snakemake-workflows'.format(WORKFLOW_REPO))
    os.chdir("snakemake-workflows")
    os.system('git checkout {0}'.format(WORKFLOW_COMMIT))
    os.chdir("..")
    
    # The checkout might have left the snakemake-workflows dirty
    os.system("git add snakemake-workflows")
    os.system('git commit -m "Added snakemake-workflows submodule"') 

    logging.info("Added snakemake-workflows repo {0} at {1} as submodule.".format(WORKFLOW_REPO, WORKFLOW_COMMIT))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    args = parser.parse_args()
    
    main(args)
