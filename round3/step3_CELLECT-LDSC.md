  - id: 2hGlu
    path: 
  - id: Acute_Pancreatitis
    path: 
  - id: Adiponectin
    path: /home/users/nus/e1124850/scratch/CELLECT_Adiponectin_ldsc.sumstats.gz
  - id: BMI
    path: 
  - id: Body_Weight
    path: 
  - id: Chronic_Pancreatitis
    path: 
  - id: Coronary_Artery_Disease
    path: 
  - id: Diabetic_Nephropathy
    path: 
  - id: Fasting_Glucose
    path: 
  - id: Fasting_Insulin
    path: 
  - id: Glucocorticoids
    path: 
  - id: Glucose
    path: 
  - id: HbA1c
    path: 
  - id: HDL
    path: 
  - id: Height
    path: 
  - id: LDL
    path: 
  - id: Pancreatic_Cancer
    path: 
  - id: Total_Cholesterol
    path: 
  - id: Triglycerides
    path: 
  - id: T2DSakaue
    path: 
  - id: T2DSpracklen
    path: 
  - id: Waist_Circumference
    path: 



```python
import pandas as pd
import os

rename_dict = {
    "CD4+_T": "CD4pos_T",
    "CD8+_T": "CD8pos_T",
    "CD56dim_CD16+_NK": "CD56dim_CD16pos_NK",
    "IGFBP2+_cell": "IGFBP2pos_cell",
    "TIM4+_ATM": "TIM4pos_ATM",
    "TIM4+_CD11c+_ATM": "TIM4pos_CD11cpos_ATM",
}

files = [
    "/data/projects/11003054/e1101943/project/01.adipose_sqtl/data/33.CELLEX/cellex_Annotation_level2.SAT_filtered.ensembl.esmu.csv.gz",
    "/data/projects/11003054/e1101943/project/01.adipose_sqtl/data/33.CELLEX/cellex_Annotation_level2.VAT_filtered.ensembl.esmu.csv.gz",
]

for file in files:
    df = pd.read_csv(file)
    df = df.rename(columns=rename_dict)

    outfilename = os.path.basename(file.replace(".csv.gz", ".cellect.csv.gz"))
    output = os.path.join('/home/users/nus/e1124850/scratch/', outfilename)
    df.to_csv(output, index=False, compression="gzip")

    print(output)

```


```bash
conda create \
  -n snakemake \
  -c conda-forge \
  -c bioconda \
  snakemake=5.27.4 \
  -y

```





```bash

#PBS -q normal
#PBS -l select=1:ncpus=2:mem=200G
#PBS -l walltime=120:00:00
#PBS -P 11003054
#PBS -N h2_sat
#PBS -o /home/users/nus/e1124850/scratch/qsub_dir/h2_sat.o
#PBS -e /home/users/nus/e1124850/scratch/qsub_dir/h2_sat.e

source /home/users/nus/e1124850/anaconda3/etc/profile.d/conda.sh
conda activate snakemake

cd
PYTHONNOUSERSITE=1 snakemake \
  --use-conda \
  --conda-frontend conda \
  -j 1 \
  -s /home/users/nus/e1124850/CELLECT/cellect-ldsc.snakefile \
  --configfile /home/users/nus/e1124850/heritability_enrichment_ldsc/round2/config_SAT.yml


```




```bash

#PBS -q normal
#PBS -l select=1:ncpus=2:mem=200G
#PBS -l walltime=120:00:00
#PBS -P 11003054
#PBS -N h2_sat
#PBS -o /home/users/nus/e1124850/scratch/qsub_dir/h2_sat.o
#PBS -e /home/users/nus/e1124850/scratch/qsub_dir/h2_sat.e

source /home/users/nus/e1124850/anaconda3/etc/profile.d/conda.sh
conda activate snakemake

cd
PYTHONNOUSERSITE=1 snakemake \
  --use-conda \
  --conda-frontend conda \
  -j 1 \
  -s /home/users/nus/e1124850/CELLECT/cellect-ldsc.snakefile \
  --configfile /home/users/nus/e1124850/heritability_enrichment_ldsc/round2/config_VAT.yml


```