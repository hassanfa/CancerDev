# ClinSeq

## Autoseq Installtion November 9 2017

Project link <https://github.com/ClinSeq/autoseq>

### Installation in Mac OS X:

Autoseq is prepared for ClinSeq's Anchorage cluster or their VM (see below). Here I tried to install it on Mac OS X. VEP and vt in the requirments were not available for conda Mac OS X, so they had to be installed separately.

vt <https://genome.sph.umich.edu/wiki/Vt> was installed using brew:

```
brew install homebrew/science/vt
```

Requirments for VEP <https://www.ensembl.org/info/docs/tools/vep/script/vep_download.html> and the missing Bio::DB:HTS was installed using cpan:

```
brew install homebrew/science/htslib
sudo cpan Bio::DB:HTS
```

After installing VEP, vt and htslib, a conda environment was created using [conda_list.txt](../dev/thirdParty/ClinSeq/conda_list.txt). With the exception that VEP and vt were removed, and following packages were updated to a more recent version available from Biobuilds conda channel.

```
sed -i 's/scalpel=0\.5\.1/scalpel=0\.5\.3/g' conda_list.txt
sed -i 's/pindel=0\.2\.5a7/pindel=0\.2\.5b8/g' conda_list.txt
sed -i 's/samblaster=0\.1\.21/samblaster=0\.1\.24g' conda_list.txt
conda create --name ClinSeq --file conda_list.txt
```

### Installing using vagrant and VMS

Resources:

1. [Hashicorp VirtualBox](https://www.vagrantup.com/docs/virtualbox/)
2. [Virtual box](https://www.virtualbox.org/) 3.

```bash
cd ~/vms/testing_setup
git clone https://github.com/ClinSeq/fairbanks

cd ~/vms/testing_setup/fairbanks
vagrant up
```

A time consuming step is to download databases of SNPs, regions of interest, etc.

```bash
vagrant ssh
cd
git clone https://github.com/clinseq/alascca-dotfiles.git /nfs/ALASCCA/alascca-dotfiles
cd /nfs/ALASCCA/alascca-dotfiles
```

- Updated the conda_list.txt for pindel=0.2.5b9 and htslib=1.6

Prepare reference (this usually takes a long time)

```bash
#enter ALASCCA production environment
. /nfs/ALASCCA/alascca-dotfiles/.bash_profile
```

#### Install prerequisites

```bash
#install prerequisites
#TEXlive will fail (explained below)
bash install-prereqs.sh
```

#### TexLive isntallation

```bash
## TexLive 2015
cd /tmp
wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
tar -zxvf install-tl-unx.tar.gz
cd install-tl-*
./install-tl -profile /nfs/ALASCCA/alascca-dotfiles/texlive.profile
rm -rf /tmp/install-tl-*
```

Added rm -rf /tmp/install-tl-* to remove the confilicting created directories. Installation requires permission to make directories (see error below):

```
Automated TeX Live installation using profile: /nfs/ALASCCA/alascca-dotfiles/texlive.profile
mkdir: cannot create directory ‘/scratch/tmp/tmp/cg3075-13758’: No such file or directory
mkdir: cannot create directory ‘/scratch/tmp/tmp/cg-3075’: No such file or directory
config.guess: cannot create a temporary directory in /scratch/tmp/tmp
./install-tl: could not run ./tlpkg/installer/config.guess, cannot proceed, sorry at tlpkg/TeXLive/TLUtils.pm line 236.
```

Sudo should solve this issue:

```bash
sudo ./install-tl -profile /nfs/ALASCCA/alascca-dotfiles/texlive.profile
```

It seems some of the collections are not available anymore, and couple of profile keys are not used. See log below

```
Automated TeX Live installation using profile: /nfs/ALASCCA/alascca-dotfiles/texlive.profile
Loading http://ftp.acc.umu.se/mirror/CTAN/systems/texlive/tlnet/tlpkg/texlive.tlpdb
Installing TeX Live 2017 from: http://ftp.acc.umu.se/mirror/CTAN/systems/texlive/tlnet (verified)
Platform: x86_64-linux => 'GNU/Linux on x86_64'
Distribution: net  (downloading)
Using URL: http://ftp.acc.umu.se/mirror/CTAN/systems/texlive/tlnet
Directory for temporary files: /tmp/88Dr4KWBCn
Profile key `in_place' is now ignored, please remove it.
Profile key `option_menu_integration' is now ignored, please remove it.
The profile references a non-existing collection: collection-mathextra
Exiting.
```

All the collections need to validated or somehow an alternative resource added to the list. So I just removed all the collection from TexLive profile, and created a new \"collection-free\" profile:

```bash
grep -v collection /nfs/ALASCCA/alascca-dotfiles/texlive.profile > /nfs/ALASCCA/alascca-dotfiles/texlive.profile.nocollection
sudo ./install-tl -profile /nfs/ALASCCA/alascca-dotfiles/texlive.profile.nocollection
```

Installation went through, so the issue was 1\. sudo 2\. some packages and collections are deprecated. I downloaded the older version of TeXLive from ftp://tug.org/historic/systems/texlive/2015/tlnet-final and removed old installation. Suggestion to update install-prereqs.sh for TexLive 2015.

```bash
cd /tmp
wget ftp://tug.org/historic/systems/texlive/2015/tlnet-final/install-tl-unx.tar.gz
tar -zxvf install-tl-unx.tar.gz
cd install-tl-*
sudo ./install-tl -profile /nfs/ALASCCA/alascca-dotfiles/texlive.profile \
    -repository ftp://tug.org/historic/systems/texlive/2015/tlnet-final/
rm -rf /tmp/install-tl-*
```

#### Install genome resources

```bash
$ generate-ref --genome-resources /nfs/ALASCCA/genome-resources --outdir /nfs/ALASCCA/autoseq-genome
INFO 2017-11-08 07:51:33,627 setup_logging - Started log with loglevel INFO
INFO 2017-11-08 07:51:33,628 main - Writing to /nfs/ALASCCA/autoseq-genome
  [------------------------------------]    1%  curl-split-leftalnWARNING 2017-11-08 10:18:12,402 run - Task curl-split-leftaln failed with exit code 1
WARNING 2017-11-08 10:18:12,402 run - Contents of /nfs/ALASCCA/autoseq-genome/variants/ExAC.r0.3.1.sites.vep.vcf.gz.out:
WARNING 2017-11-08 10:18:12,404 run -   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0normalize v0.5

options:     input VCF file                                  -
         [o] output VCF file                                 -
         [w] sorting window size                             10000
         [n] no fail on reference inconsistency for non SNPs true
         [q] quiet                                           false
         [d] debug                                           false
         [r] reference FASTA file                            /nfs/ALASCCA/autoseq-genome/genome/human_g1k_v37_decoy.fasta

decompose v0.5

options:     input VCF file        -
         [s] smart decomposition   true (experimental)
         [o] output VCF file       -

  0 4139M    0     0    0     0      0      0 --:--:--  0:00:02 --:--:--     0[W::vcf_parse] FILTER 'AC_Adj0_Filter' is not defined in the header
[W::vcf_parse] FILTER 'AC_Adj0_Filter' is not defined in the header
 95 4139M   95 3941M    0     0   458k      0  2:34:00  2:26:38  0:07:22     0
curl: (56) Recv failure: Connection reset by peer

gzip: stdin: unexpected end of file

stats: no. variants                 : 8899629
       no. biallelic variants       : 8189290
       no. multiallelic variants    : 710339

       no. additional biallelics    : 793793
       total no. of biallelics      : 9693422

Time elapsed: 6m 26s


stats: biallelic
          no. left trimmed                      : 0
          no. right trimmed                     : 151929
          no. left and right trimmed            : 0
          no. right trimmed and left aligned    : 0
          no. left aligned                      : 9

       total no. biallelic normalized           : 151938

       multiallelic
          no. left trimmed                      : 0
          no. right trimmed                     : 0
          no. left and right trimmed            : 0
          no. right trimmed and left aligned    : 0
          no. left aligned                      : 0

       total no. multiallelic normalized        : 0

       total no. variants normalized            : 151938
       total no. variants observed              : 9693422
       total no. reference observed             : 0

Time elapsed: 7m 38s



INFO 2017-11-08 10:18:12,457 run - Pipeline failed with exit code 1.
```

Note: The process was interrupted couple of times due to "Connection reset by peer". It seems Mac OS X going to sleep suspends VM, which in turn suspends curl. Download doesn't resume, as the "-C" option is not specified in <https://github.com/ClinSeq/autoseq/blob/master/autoseq/tools/unix.py> Curl function:

```python
#Original function
class Curl(Job):
    def __init__(self):
        Job.__init__(self)
        self.remote = None
        self.output = None
        self.jobname = "curl"

# -C is no specified, and thus download starts from scratch every time generate-ref is called
    def command(self):
        return "curl " + \
               required(" ", self.remote) + \
               required(" > ", self.output)
```

Keeping VM without suspending, generate-ref failed with the following status:

```bash
$ generate-ref --genome-resources /nfs/ALASCCA/genome-resources --outdir /nfs/ALASCCA/autoseq-genome
INFO 2017-11-08 11:59:30,736 setup_logging - Started log with loglevel INFO
INFO 2017-11-08 11:59:30,736 main - Writing to /nfs/ALASCCA/autoseq-genome
  [#-----------------------------------]    4%  2d 17:14:32  curl-split-leftalnWARNING 2017-11-08 14:43:20,484 run - Task curl-split-leftaln failed with exit code 1
WARNING 2017-11-08 14:43:20,485 run - Contents of /nfs/ALASCCA/autoseq-genome/variants/clinvar_20160203.vcf.gz.out:
WARNING 2017-11-08 14:43:20,485 run - normalize v0.5

options:     input VCF file                                  -
         [o] output VCF file                                 -
         [w] sorting window size                             10000
         [n] no fail on reference inconsistency for non SNPs true
         [q] quiet                                           false
         [d] debug                                           false
         [r] reference FASTA file                            /nfs/ALASCCA/autoseq-genome/genome/human_g1k_v37_decoy.fasta

decompose v0.5

options:     input VCF file        -
         [s] smart decomposition   true (experimental)
         [o] output VCF file       -

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:--  0:00:01 --:--:--     0
curl: (9) Server denied you to change to the given directory

gzip: stdin: unexpected end of file
[bcf_ordered_reader.cpp:49 BCFOrderedReader] Not a VCF/BCF file: -
[bcf_ordered_reader.cpp:49 BCFOrderedReader] Not a VCF/BCF file: -


INFO 2017-11-08 14:43:20,486 run - Pipeline failed with exit code 1.
```

**Reason:** The link to Clinvar in [generate_ref_files_pipeline.py](https://github.com/ClinSeq/autoseq/blob/master/autoseq/pipeline/generate_ref_files_pipeline.py) is broken. All files from archive folder are now in two separate folders on Clinvar's FTP server. The new path is: ftp://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh37/archive_1.0/2016/clinvar_20160203.vcf.gz

**FIXME:**

1. Check if file exists.
2. Generate md5 function.
3. Add md5 from source (if it exists) and match with local md5 (i.e. don't download).
4. Capture `$PIPESTATUS` to check curl status and log it properly. Cause the only status that there is a dot file .XXXX.fail or .XXXX.done, and XXXX.out files. Curl exit codes/status: <https://ec.haxx.se/usingcurl-returns.html> and <https://curl.haxx.se/libcurl/c/libcurl-errors.html>

dbSNP b147 is also missing from the hard-coded link. A directory listing of dbSNP was prepared using:

```bash
lftp ftp://ftp.ncbi.nlm.nih.gov/snp/ -e "du -a;exit" > server-listing.txt
```

Thre was no file matching dbSNP147 file in the generate_ref_files_pipeline.py. So I updated it to the closest version, b149, ftp://ftp.ncbi.nlm.nih.gov/snp/organisms/human_9606_b149_GRCh37p13/VCF/All_20161121.vcf.gz . Old VCF path was: ftp://ftp.ncbi.nih.gov/snp/organisms/human_9606_b147_GRCh37p13/VCF/archive/All_20160408.vcf.gz

Another solution is to use b149, and filter out all the 149 and create a new VCF file.

```bash
$ ftp://ftp.ncbi.nlm.nih.gov/snp/organisms/human_9606_b149_GRCh37p13/VCF/All_20161121.vcf.gz
$ tabix -p vcf All_20161121.vcf.gz
$ bcftools query -f '%INFO/dbSNPBuildID\n' All_20161121.vcf.gz | sort | uniq -c > All_20161121.buildStat
$ bcftools stats All_20161121.vcf.gz > All_20161121.bcfStats

$ head All_20161121.bcfStats
# This file was produced by bcftools stats (1.4.1+htslib-1.4.1) and can be plotted using plot-vcfstats.
# The command line was:    bcftools stats  All_20161121.vcf.gz
#
# Definition of sets:
# ID    [2]id    [3]tab-separated file names
ID    0    All_20161121.vcf.gz
# SN, Summary numbers:
# SN    [2]id    [3]key    [4]value
SN    0    number of samples:    0
SN    0    number of records:    153824740

$ # cumulative sum of SNPs in each dbSNP
$ cat All_20161121.buildStat | tr -s ' ' | sed 's/^[ ]//g' | sort -k2,2n | awk '{s+=$1; print $2,s}' | tail
135 47421253
136 47461283
137 50302140
138 59799184
141 59799849
142 110967762
144 148476322
146 149454090
147 153080365
149 153824740

$ # SNPs in each dbSNP version
$ sort -k2,2nr All_20161121.buildStat | column -t | head
744375    149
3626275   147
977768    146
37508560  144
51167913  142
665       141
9497044   138
2840857   137
40030     136
12721218  135
```

SNPs can be filtered using `bcftools view`:

```bash
#The following was run on Mac OS X, and the result is not hardlinked in the autoseq pipeline yet.
#The solution is to filter from newer version of dbSNP, filterout nonmatching dbSNP version,
#and swap the hard link: file:///Users/hassanforoughi/Desktop/playground/server-listing.txt .
#A more elegant solution would be to incorporate this analysis into the generate_ref_files_pipeline.py
brew install bcftools
bcftools view -e dbSNPBuildID=149 --threads 2 All_20161121.vcf.gz > All_20161121.no_b149.vcf.gz
```

**TODO:** Add dbSNP variant selection as explained above, and add it to the pipeline.

Finally, after fixing installation, and granting permission to create directory on the following directory: `/scratch/tmp/`, `generate-ref` was successfully run and finished.

```
$ generate-ref --genome-resources /nfs/ALASCCA/genome-resources --outdir /nfs/
ALASCCA/autoseq-genome
INFO 2017-11-10 09:07:32,720 setup_logging - Started log with loglevel INFO
INFO 2017-11-10 09:07:32,720 main - Writing to /nfs/ALASCCA/autoseq-genome
  [####################################]  100%  Done!
INFO 2017-11-10 10:44:21,660 run - Pipeline finished successfully.
```

### Setting up permission:

Permissions for write permission in ```/scratch/tmp/``` needs to be checked, although it is supposedly set in [Vagrantfile](https://github.com/ClinSeq/fairbanks/blob/master/Vagrantfile):

```bash
sudo mkdir -p /scratch/tmp/
sudo chmod a+w /scratch/tmp
```

but still there were some issues with the during the installation when it comes to creating directories in ```/scratch/tmp/```


