SAMPLES = ["tumor", "normal"]
ref_data_prefix = "../../data/snakemake_tutorial_data_131217/"

rule all:
  input:
      expand(ref_data_prefix + "ref_data/samples/{sample}.fastq", sample=SAMPLES),
      ref_data_prefix + "ref_data/db/genome.fa"
    

rule get_data:
    output:
        expand(ref_data_prefix + "ref_data/samples/{sample}.fastq", sample=SAMPLES),
        ref_data_prefix + "ref_data/db/genome.fa"
    shell:
        "rm -rf ref_data; "
        "wget https://bitbucket.org/snakemake/snakemake/downloads/snakemake-tutorial-data.tar.gz; "
        "tar -xf snakemake-tutorial-data.tar.gz; "
        "rm requirements.txt; rm snakemake-tutorial-data.tar.gz; "
        "mv data ref_data; rm ref_data/genome.fa.*; "
        "mkdir -p ref_data/db; mv ref_data/genome.fa ref_data/db/; "
        "mv ref_data/samples/A.fastq ref_data/samples/tumor.fastq; "
        "mv ref_data/samples/B.fastq ref_data/samples/normal.fastq; "
        "rm ref_data/samples/C.fastq; "
