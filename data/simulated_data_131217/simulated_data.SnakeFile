# vim: syntax=python tabstop=4 expandtab
# coding: utf-8

__author__ = "Hassan Foroughi Asl"

rule all:
  input:
    expand("ref_data/samples/normal.{suffix}",suffix=["bwa.read2.fastq", "bwa.read1.fastq"]),
    expand("ref_data/samples/tumor.{suffix}",suffix=["bwa.read2.fastq", "bwa.read1.fastq"]),
  
rule prepare_genome:
  input:
    fa="../../../db/GRCh38/GRCh38.primary_assembly.genome.fa"
  output:
    "ref_data/db/genome.fa"
  shell:
    "samtools faidx {input.fa} chr22:15000000-15050000 |  sed 's/>chr22:15000000-15050000/>chr22/g' > {output}; "

rule simulate_reads:
  input:
    fa="ref_data/db/genome.fa"
  output:
    expand("ref_data/samples/normal.{suffix}",suffix=["bwa.read2.fastq", "bwa.read1.fastq"]),
    expand("ref_data/samples/tumor.{suffix}",suffix=["bwa.read2.fastq", "bwa.read1.fastq"]),
  params:
    Coverage="500",
    MutationRate="0.01",
    readLength="100"
  shell:
    "dwgsim -N 20000 -e 0.02 -E 0.02 -d 500 "
    "-s 50 -C {params.Coverage} -1 {params.readLength} -2 {params.readLength} "
    "-r 0 -F 0 -R 0 -X 0.3 "
    "-I 1 -y 0 -n 0 -c 0 -S 0 -z 123456 "
    "{input} normal; mv normal* ref_data/samples/; "
    "dwgsim -N 20000 -e 0.02 -E 0.02 -d 500 "
    "-s 50 -C {params.Coverage} -1 {params.readLength} -2 {params.readLength} "
    "-r {params.MutationRate} -F 0.5 -R 0.1 -X 0.3 "
    "-I 1 -y 0 -n 0 -c 0 -S 0 -z 123456 "
    "{input} tumor; mv tumor* ref_data/samples/; "

