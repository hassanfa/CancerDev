#!/usr/bin/env python3
"""
Submit this clustering script for sbatch to snakemake with:
    snakemake --forceall --snakefile Snakefile \
      --cluster-config config_cluster.json \
      -j 9999 \
      --cluster 'python3 runSbatch.py --config config_cluster.json {dependencies}' \
      --immediate-submit --notemp
"""
## Wrapper for sbatch to submit job dependencies

import sys
import re
import os
import json
import argparse
from snakemake.utils import read_job_properties

parser = argparse.ArgumentParser(description='Process script and dependecies.')
parser.add_argument("dependencies", nargs="*", help="{{dependencies}} string given by snakemake\n")
parser.add_argument("snakescript", help="Snakemake generated shell script with commands to execute snakemake rule\n")
parser.add_argument("--cluster_config", help="Config file to read sbatch settings from.")
parser.add_argument("--sample_config", help="Config file to read sbatch settings from.")
args = parser.parse_args()

## snakemake will generate a jobscript containing all the (shell) commands from your Snakefile. 
## https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html?highlight=markdown%20header%20job%20properties#job-properties
sample_config = json.load(open(args.sample_config))
jobscript = args.snakescript
job_properties = read_job_properties(jobscript)

# access property defined in the cluster configuration file (Snakemake >=3.6.0), cluster.json
time = job_properties["cluster"]["time"]
cpu = job_properties["cluster"]["n"]
account_slurm = job_properties["cluster"]["account"]

logpath = os.path.join(sample_config["analysis"]["analysis_dir"], sample_config["analysis"]["sample_id"], sample_config["analysis"]["log"])
scriptpath = os.path.join(sample_config["analysis"]["analysis_dir"], sample_config["analysis"]["sample_id"], sample_config["analysis"]["script"])
resultpath = os.path.join(sample_config["analysis"]["analysis_dir"], sample_config["analysis"]["sample_id"], sample_config["analysis"]["result"])

os.system('mkdir -p ' + logpath)
os.system('mkdir -p ' + scriptpath)
os.system('mkdir -p ' + resultpath)

os.system('cp ' + jobscript + ' ' + scriptpath)
scriptname=jobscript.split("/")
scriptname=scriptname[-1]
jobscript = os.path.join(scriptpath, scriptname)

output_log = logpath + scriptname + ".out"
error_log = logpath + scriptname + ".err"
cmdline = 'sbatch -A {account} -n {n} -t {time} --qos=low -o {output_log} -e {error_log}'.format(n=cpu, time=time, output_log=output_log, error_log=error_log, account=account_slurm)

cmdline += " "

# figure out job dependencies, the last argument is the jobscript which is baked in snakemake
dependencies = args.dependencies
if dependencies:
    cmdline += '--dependency=' + ','.join(["afterok:%s" % d for d in dependencies])

# the actual job
cmdline += " " + jobscript + " | cut -d' ' -f 4"

#logpath='/home/hassan.foroughi/repo/CancerDev/src/workflows/logs/'
#os.system('ln -sf ' + output_log + ' ' + logpath) 
#os.system('ln -sf ' + error_log + ' ' + logpath) 

#f = open('helloworld.txt','a')
#f.write("cancer." + job_properties["rule"] + "." +  str(job_properties["jobid"]) + "\t" + job_properties["cluster"]["name"] + "\n")
#f.close()

# call the command
os.system(cmdline)
