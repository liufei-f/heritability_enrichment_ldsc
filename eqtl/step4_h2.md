

```python
import os

traits=[
    # 'Acute_Pancreatitis_ldsc',
    'BMI_ldsc',
    'Body_Weight_ldsc',
    'Chronic_Pancreatitis_ldsc',
    'Coronary_Artery_Disease_ldsc',
    'Diabetic_Nephropathy_ldsc',
    'Glucocorticoids_ldsc',
    'Glucose_ldsc',
    'HbA1c_ldsc',
    'HDL_ldsc',
    'Height_ldsc',
    'LDL_ldsc',
    'Pancreatic_Cancer_ldsc',
    'Total_Cholesterol_ldsc',
    'Triglycerides_ldsc',
    'Waist_Circumference_ldsc',
    "2hGlu_ldsc",
    "Adiponectin_ldsc",
    "Fasting_Glucose_ldsc",
    "Fasting_Insulin_ldsc",
    "T2DSakaue_ldsc",
    "T2DSpracklen_ldsc"]

sat_celltypes = ['Adipocyte', 'CEC', 'VEC', 'Committed_preadipocyte', 'SMC', 'AEC',
       'LAM', 'PVM', 'Classical_monocyte', 'Early_preadipocyte', 'CD4+_T',
       'Areg', 'CD8+_T', 'Pericyte', 'cDC2', 'CD56dim_CD16+_NK', 'Treg']


traits=['Diabetic_Nephropathy_ldsc']
for trait in traits:
    for celltype in sat_celltypes:
        cmd = (f"python /home/users/nus/e1124850/ldsc/ldsc.py "
              f"--h2 /home/users/nus/e1124850/scratch/{trait}.sumstats.gz "
              f"--ref-ld-chr /home/users/nus/e1124850/e1124850/co_lab/tongyihan/gene_annot_file/tong_sat_{celltype}_eqtlsig_gene_annot_file.,/home/users/nus/e1124850/e1124850/co_lab/tongyihan/1000G_Phase3_EAS_baselineLD_v2.2_ldscores/baselineLD. "
              f"--overlap-annot "
              f"--frqfile-chr /home/users/nus/e1124850/e1124850/co_lab/tongyihan/1000G_Phase3_frq/1000G.EUR.QC. "
              f"--w-ld-chr /home/users/nus/e1124850/e1124850/co_lab/tongyihan/1000G_Phase3_EAS_weights_hm3_no_MHC/weights.EAS.hm3_noMHC. "
              f"--out /home/users/nus/e1124850/e1124850/co_lab/tongyihan/satldscenrichment/tong_sat_{trait}_{celltype} "
              f"--print-coefficients")
        os.system(cmd)


```



```python

import os

traits=[
    # 'Acute_Pancreatitis_ldsc',
    'BMI_ldsc',
    'Body_Weight_ldsc',
    'Chronic_Pancreatitis_ldsc',
    'Coronary_Artery_Disease_ldsc',
    'Diabetic_Nephropathy_ldsc',
    'Glucocorticoids_ldsc',
    'Glucose_ldsc',
    'HbA1c_ldsc',
    'HDL_ldsc',
    'Height_ldsc',
    'LDL_ldsc',
    'Pancreatic_Cancer_ldsc',
    'Total_Cholesterol_ldsc',
    'Triglycerides_ldsc',
    'Waist_Circumference_ldsc',
    "2hGlu_ldsc",
    "Adiponectin_ldsc",
    "Fasting_Glucose_ldsc",
    "Fasting_Insulin_ldsc",
    "T2DSakaue_ldsc",
    "T2DSpracklen_ldsc"]

traits=['Diabetic_Nephropathy_ldsc']
vat_celltypes = ['Adipocyte', 'Committed_preadipocyte', 'Mesothelial', 'CEC',
       'CD8+_T', 'SMC', 'TIM4+_ATM', 'LEC', 'PVM', 'Classical_monocyte',
       'TIM4+_CD11c+_ATM', 'Early_preadipocyte', 'CD4+_T', 'AEC',
       'IGFBP2+_cell', 'Pericyte', 'VEC', 'LAM', 'Areg', 'cDC2',
       'CD56dim_CD16+_NK']

for trait in traits:
    for celltype in vat_celltypes:
        cmd = (f"python /home/users/nus/e1124850/ldsc/ldsc.py "
              f"--h2 /home/users/nus/e1124850/scratch/{trait}.sumstats.gz "
              f"--ref-ld-chr /home/users/nus/e1124850/e1124850/co_lab/tongyihan/gene_annot_file/tong_vat_{celltype}_eqtlsig_gene_annot_file.,/home/users/nus/e1124850/e1124850/co_lab/tongyihan/1000G_Phase3_EAS_baselineLD_v2.2_ldscores/baselineLD. "
              f"--overlap-annot "
              f"--frqfile-chr /home/users/nus/e1124850/e1124850/co_lab/tongyihan/1000G_Phase3_frq/1000G.EUR.QC. "
              f"--w-ld-chr /home/users/nus/e1124850/e1124850/co_lab/tongyihan/1000G_Phase3_EAS_weights_hm3_no_MHC/weights.EAS.hm3_noMHC. "
              f"--out /home/users/nus/e1124850/e1124850/co_lab/tongyihan/vatldscenrichment/tong_vat_{trait}_{celltype} "
              f"--print-coefficients")
        os.system(cmd)
```