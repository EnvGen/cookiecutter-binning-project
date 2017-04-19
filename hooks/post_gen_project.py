#!/usr/bin/env python
"""Fetch the scripts needed for the snakefile"""

import argparse
import os
import logging
import glob

GITHUB_PROJECT_REMOTE = "{{cookiecutter.github_project_remote}}"

WORKFLOW_REPO = "{{cookiecutter.snakemake_workflows_repo}}"
SUBWORKFLOW_NAME = "{{cookiecutter.snakemake_subworkflow_name}}" 

TOOLBOX_GITHUB_REPO = "{{cookiecutter.toolbox_github_repo}}"

def main(args):
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO) 
    os.system('git init')
    os.system('git remote add origin {0}'.format(GITHUB_PROJECT_REMOTE))
    logging.info("Initalized git repo with remote {0}".format(GITHUB_PROJECT_REMOTE))

    # Add toolbox as submodule
    os.system('git submodule add https://github.com/{} toolbox'.format(TOOLBOX_GITHUB_REPO))
    logging.info("Added toolbox repo {0} as submodule.".format(TOOLBOX_GITHUB_REPO))

    # Add snakemake-workflows as submodule
    os.system('git submodule add https://github.com/{} snakemake-workflows'.format(WORKFLOW_REPO))
    subworkflow_files = os.path.join("snakemake-workflows", "workflows", SUBWORKFLOW_NAME)
    
    for workflow_file_path in glob.glob(subworkflow_files + "/*"):
        workflow_file_name = os.path.basename(workflow_file_path) 
        os.symlink(workflow_file_path, workflow_file_name)
    logging.info("Added snakemake-workflows repo {0} as submodule.".format(WORKFLOW_REPO))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    args = parser.parse_args()
    
    main(args)
