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