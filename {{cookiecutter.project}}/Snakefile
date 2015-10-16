__author__ = "Inodb, Alneberg"
__license__ = "MIT"


configfile: "config.json"

import os
import glob
from subprocess import check_output

# Dynamically generate the missing items in the config dicionary here
# i.e. load config["bowtie2_rules"]["units"] with a dictionary of 
# the fastq files, pair is an unit. Collect the units originating to the
# same sample in the config["bowtie2_rules"]["samples"].

# Check that no git repo is dirty
submodules = ["snakemake-workflows", "toolbox"]
for submodule in submodules:
    submodule_status = check_output(["git", "status", "--porcelain", submodule])
    if not submodule_status == b"":
        print(submodule_status)
        raise Exception("Submodule {} is dirty. Commit changes before proceeding.".format(submodule))



# Add all samples that should be annotated with prokka extended
for contigs_f in glob.glob("samples/*/Contigs.fa"):
    sample = contigs_f.split('/')[-2]
    config["prokka_extended_rules"]["contigs"][sample] = contigs_f

SM_WORKFLOW_LOC="snakemake-workflows/"
include: SM_WORKFLOW_LOC + "bio/ngs/rules/annotation/prokka.rules"
