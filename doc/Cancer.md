# Cancer pipeline

### Resources and knowledgebase

1. Mutation Identification Pipeline (MIP):
	* http://mip-api.readthedocs.io/en/latest/index.html
	* https://github.com/Clinical-Genomics/MIP 
2. ClinSeq autoseq:
	* https://github.com/ClinSeq/autoseq 
3. MSK-Impact pipeline: https://www.mskcc.org/msk-impact
4. TCGA: https://cancergenome.nih.gov/
5. COSMIC: http://cancer.sanger.ac.uk/cosmic
6. CAW: https://github.com/SciLifeLab/CAW
7. Probablistic2020: https://github.com/KarchinLab/probabilistic2020 and it's sister, 2020plus: https://github.com/KarchinLab/2020plus
8. dbSNP
9. ClinVar
10. ExAC
11. GTEx
12. OMIM
13. Drug resistance database
14. Mutational pattern
15. 

---

### Papers

1. **MSK-IMPACT papers:**
	* Cheng, D. T., Mitchell, T. N., Zehir, A., Shah, R. H., Benayed, R., Syed, A., … Berger, M. F. (2015). Memorial sloan kettering-integrated mutation profiling of actionable cancer targets (MSK-IMPACT): A hybridization capture-based next-generation sequencing clinical assay for solid tumor molecular oncology. Journal of Molecular Diagnostics, 17(3), 251–264. https://doi.org/10.1016/j.jmoldx.2014.12.006
	* Cheng, D. T., Prasad, M., Chekaluk, Y., Benayed, R., Sadowska, J., Zehir, A., … Zhang, L. (2017). Comprehensive detection of germline variants by MSK-IMPACT, a clinical diagnostic platform for solid tumor molecular oncology and concurrent cancer predisposition testing. BMC Medical Genomics, 10(1), 33. https://doi.org/10.1186/s12920-017-0271-4
2. **Application of MSK-IMPACT:** Zehir, A., Benayed, R., Shah, R. H., Syed, A., Middha, S., Kim, H. R., … Berger, M. F. (2017). Mutational landscape of metastatic cancer revealed from prospective clinical sequencing of 10,000 patients. Nature Medicine, 23(6), 703–713. https://doi.org/10.1038/nm.4333
3. **VarDict:** Lai, Z., Markovets, A., Ahdesmaki, M., Chapman, B., Hofmann, O., Mcewen, R., … Dry, J. R. (2016). VarDict: A novel and versatile variant caller for next-generation sequencing in cancer research. Nucleic Acids Research, 44(11), 1–11. https://doi.org/10.1093/nar/gkw227
4. **Review on bioinformatic pipelins:** Leipzig, J. (2017). A review of bioinformatic pipeline frameworks. Briefings in Bioinformatics, 18(3), 530–536. https://doi.org/10.1093/bib/bbw020
5. **Mutational signature reviews:**
	* Helleday, T., Eshtad, S., & Nik-Zainal, S. (2014). Mechanisms underlying mutational signatures in human cancers. Nature Reviews Genetics, 15(9), 585–598. https://doi.org/10.1038/nrg3729
	* Alexandrov, L. B., & Stratton, M. R. (2014). Mutational signatures: The patterns of somatic mutations hidden in cancer genomes. Current Opinion in Genetics and Development, 24(1), 52–60. https://doi.org/10.1016/j.gde.2013.11.01
6. 

---

### Tools:

1. Teaser: NGS readmapping benchmarking.
	* http://teaser.cibiv.univie.ac.at/
	* https://github.com/Cibiv/Teaser
2. FastQC: Quality control tool. https://www.bioinformatics.babraham.ac.uk/projects/fastqc/
3. Cutadapt: Adapter removal tool. https://cutadapt.readthedocs.io/en/stable/
4. Trim Galore!: FastQC and Cutadapt wrapper. https://www.bioinformatics.babraham.ac.uk/projects/trim_galore/
5. Picardtools: BAM/SAM/VCF/CRAM manipulator. http://broadinstitute.github.io/picard/
	* MarkDuplicate: Mark duplicate reads and potentially remove them
	* LiftoverVcf: liftover VCF between builds
	* 
6. GATK: A variant discovery tool: https://software.broadinstitute.org/gatk/
	* BaseRecalibrator: Detect systematic error in base quality score
	* Somatic Indel Realigner: Local Realignment around Indels
	* ContEst: Estimate cross sample contamination
7. Samtools
8. Sambamba
9. bcftools
10. vcftools
11. Delly
12. plink
13. freebayes
14. ASCAT: Allele-Specific Copy Number Analysis of Tumors https://github.com/Crick-CancerGenomics/ascat
15. MutationalPatterns: https://github.com/UMCUGenetics/MutationalPatterns
16. desconstructSigs: https://github.com/raerose01/deconstructSigs
17. treeOmics: https://github.com/johannesreiter/treeomics
18. controlFreeC: http://boevalab.com/FREEC/
19. MuTect2: Call somatic SNPs and indels via local re-assembly of haplotypes https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_gatk_tools_walkers_cancer_m2_MuTect2.php
20. Annovar: annotation of detected genetic variation http://annovar.openbioinformatics.org/en/latest/
21. Strelka: Small variant caller https://github.com/Illumina/strelka
22. Manta: Structural variant caller https://github.com/Illumina/manta
23. PurBayes: estimate tumor purity and clonality
