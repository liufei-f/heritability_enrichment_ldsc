import os
import subprocess
import sys

traits = [
    "Acute_Pancreatitis_ldsc",
    "BMI_ldsc",
    "Body_Weight_ldsc",
    "Chronic_Pancreatitis_ldsc",
    "Coronary_Artery_Disease_ldsc",
    "Diabetic_Nephropathy_ldsc",
    "Glucocorticoids_ldsc",
    "Glucose_ldsc",
    "HbA1c_ldsc",
    "HDL_ldsc",
    "Height_ldsc",
    "LDL_ldsc",
    "Pancreatic_Cancer_ldsc",
    "Total_Cholesterol_ldsc",
    "Triglycerides_ldsc",
    "Waist_Circumference_ldsc",
    "2hGlu_ldsc",
    "Adiponectin_ldsc",
    "Fasting_Glucose_ldsc",
    "Fasting_Insulin_ldsc",
    "T2DSakaue_ldsc",
    "T2DSpracklen_ldsc",
]

sat_celltypes = [
    "Adipocyte",
    "Committed_preadipocyte",
    "CEC",
    "VEC",
    "AEC",
    "PVM",
    "SMC",
    "Early_preadipocyte",
    "LAM",
    "Areg",
    "Pericyte",
]

ldsc = "/home/users/nus/e1124850/scratch/github/ldsc/ldsc.py"

sumstats_dir = "/home/users/nus/e1124850/scratch"
annotation_dir = (
    "/home/users/nus/e1124850/e1124850/"
    "co_lab/tianchi/gene_annot_file"
)
baseline_prefix = (
    "/home/users/nus/e1124850/e1124850/co_lab/tongyihan/"
    "1000G_Phase3_EAS_baselineLD_v2.2_ldscores/baselineLD."
)
frequency_prefix = (
    "/home/users/nus/e1124850/e1124850/co_lab/tongyihan/"
    "round1/1000G_Phase3_frq/1000G.EUR.QC."
)
weights_prefix = (
    "/home/users/nus/e1124850/e1124850/co_lab/tongyihan/"
    "round1/1000G_Phase3_EAS_weights_hm3_no_MHC/"
    "weights.EAS.hm3_noMHC."
)
output_dir = "/home/users/nus/e1124850/scratch/sqtl_h2"

os.makedirs(output_dir, exist_ok=True)

for trait in traits:
    for celltype in sat_celltypes:
        annotation_prefix = (
            f"{annotation_dir}/"
            f"tianchi_sat_{celltype}_sqtlsig_gene_annot_file."
        )
        output_prefix = (
            f"{output_dir}/tianchi_sat_{trait}_{celltype}"
        )

        cmd = [
            sys.executable,
            ldsc,
            "--h2",
            f"{sumstats_dir}/CELLECT_{trait}.sumstats.gz",
            "--ref-ld-chr",
            f"{annotation_prefix},{baseline_prefix}",
            "--overlap-annot",
            "--frqfile-chr",
            frequency_prefix,
            "--w-ld-chr",
            weights_prefix,
            "--out",
            output_prefix,
            "--print-coefficients",
        ]

        print(f"Running SAT: trait={trait}, celltype={celltype}")
        subprocess.run(cmd, check=True)