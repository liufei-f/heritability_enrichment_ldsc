import pandas as pd
import os 
from glob import glob

from importlib import metadata
import pyranges as pr

## gene-coord-file
def __prepare_genecode(gencode):
    genecode_df = pr.read_gtf(gencode, as_df=True)
    genecode_df.drop(labels=genecode_df[genecode_df['Feature'] != 'gene'].index, inplace=True)
    genecode_df.reset_index(drop=True, inplace=True)
    genecode_df.drop(columns=[col for col in genecode_df if
                                col not in ['Chromosome', 'Start', 'End', 'Strand', 'gene_id', 'gene_name']],
                        inplace=True)
    genecode_df.rename({'Chromosome': 'chr', 'Start': 'start', 'End': 'end', 'Strand': 'strand'},
                        axis='columns', inplace=True)
    # gene_id_df = genecode_df['pheno_id'].str.split('.', n=1, expand=True)
    # genecode_df.loc[:, 'pheno_id'] = gene_id_df[0]

    genecode_df.loc[:, 'position'] = pd.NA
    genecode_df['position'].mask(genecode_df['strand'] == '+', genecode_df['start'], inplace=True)
    genecode_df['position'].mask(genecode_df['position'].isna(), genecode_df['end'], inplace=True)
    # genecode_df.drop(columns=['start', 'end'], inplace=True)
    genecode_df['chr'] = genecode_df['chr'].apply(lambda x: x.strip('chr'))
    return genecode_df


gtf = '/data/projects/11003054/e1101943/project/00.reference/hg38/cellranger_reference/refdata-gex-GRCh38-2020-A/genes/genes.gtf'
vcf = '/home/project/11003054/e1353486/project/adipose/fullgenotype/Ancestry_specific/00.merge_genotype/adipose_after_imputation_296_merged_genome_rename_rsID_nochr_neur.vcf.gz'

gene_coord_file_fullcolumn = __prepare_genecode(gtf)
gene_coord_file = gene_coord_file_fullcolumn[['gene_name','chr','start','end']]
gene_coord_file.columns = ['GENE', 'CHR', 'START', 'END']
gene_coord_file_path = '/home/users/nus/e1124850/heritability_enrichment_ldsc/gene_coord_file.txt'
gene_coord_file.to_csv(gene_coord_file_path, sep='\t', index=False)


## gene-set-file

eqtl_file = '/data/projects/11003054/e1101943/project/01.adipose_sqtl/data/09.eQTL/03.Saige_QTL/02.output/03.formal_calling/ancestry_specific_version/All_eQTL_SAT_and_VAT_with_beta.tsv'
eqtl_df = pd.read_csv(eqtl_file, sep='\t')
sat_eqtl_df = eqtl_df[eqtl_df['depot'] == 'SAT']
vat_eqtl_df = eqtl_df[eqtl_df['depot'] == 'VAT']


for celltype in sat_eqtl_df['celltype'].unique():
    celltype_df = sat_eqtl_df[sat_eqtl_df['celltype'] == celltype]
    celltype_df['gene'].drop_duplicates().to_csv(f'/home/users/nus/e1124850/heritability_enrichment_ldsc/tong_sat_{celltype}_gene_set_file.txt', index=False, header=False)


for celltype in vat_eqtl_df['celltype'].unique():
    celltype_df = vat_eqtl_df[vat_eqtl_df['celltype'] == celltype]
    celltype_df['gene'].drop_duplicates().to_csv(f'/home/users/nus/e1124850/heritability_enrichment_ldsc/tong_vat_{celltype}_gene_set_file.txt', index=False, header=False)


# sat_eqtl_sig_gene_path = '/home/users/nus/e1124850/heritability_enrichment_ldsc/tong_sat_gene_set_file.txt'

# vat_eqtl_sig_gene_path = '/home/users/nus/e1124850/heritability_enrichment_ldsc/tong_vat_gene_set_file.txt'

# sat_eqtl_df['gene'].drop_duplicates().to_csv(sat_eqtl_sig_gene_path, index=False, header=False)

# vat_eqtl_df['gene'].drop_duplicates().to_csv(vat_eqtl_sig_gene_path, index=False, header=False)


## plink --make-bed --freq 

# for chrid in range(1, 23):
#     vcf = f'/home/project/11003054/e1353486/project/adipose/fullgenotype/Ancestry_specific/02.vcf_by_chr_edited_rsid/adipose_after_imputation_296_merged_genome_rename_rsID_nochr_neur_chr{chrid}.vcf.gz'
#     os.system(f'plink --vcf {vcf} --make-bed --freq --out /home/users/nus/e1124850/scratch/adipose_after_imputation_296_merged_genome_rename_rsID_nochr_neur.{chrid}')


# python /home/users/nus/e1124850/ldsc-python3/make_annot.py --gene-set-file /home/users/nus/e1124850/heritability_enrichment_ldsc/tong_vat_gene_set_file.txt  --gene-coord-file /home/users/nus/e1124850/heritability_enrichment_ldsc/gene_coord_file.txt --windowsize 100000 --bimfile /home/users/nus/e1124850/scratch/adipose_after_imputation_296_merged_genome_rename_rsID_nochr_neur.{chrid}.bim --annot-file /home/users/nus/e1124850/heritability_enrichment_ldsc/tong_vat_eqtlsig.{chrid}.annot.gz





baseldfiles = glob('/home/users/nus/e1124850/e1124850/co_lab/tongyihan/1000G_Phase3_EAS_baselineLD_v2.2_ldscores/baselineLD.*.l2.ldscore.gz')

total_SNP_df = pd.DataFrame()
for ldfile in baseldfiles:
    ld_df = pd.read_csv(ldfile, sep='\t', usecols=['SNP'])
    total_SNP_df = pd.concat([total_SNP_df, ld_df['SNP']], axis=0)


total_SNP_df.to_csv('/home/users/nus/e1124850/e1124850/co_lab/tongyihan/baselineLD_v2.2.snps.txt',header=False, index=False)


# for chrid in range(1, 23):
#     cmd = f"""plink \
#     --bfile /home/users/nus/e1124850/e1124850/co_lab/tongyihan/1000G_Phase3_EAS_plinkfiles/1000G.EAS.QC.{chrid} \
#     --extract /home/users/nus/e1124850/e1124850/co_lab/tongyihan/baselineLD_v2.2.snps.txt \
#     --make-bed \
#     --out /home/users/nus/e1124850/e1124850/co_lab/tongyihan/1000G_Phase3_EAS_plinkfiles_filtered/1000G.EAS.QC.filtered.{chrid}"""
#     os.system(cmd)




##################
# sat_celltypes = ['Adipocyte', 'CEC', 'VEC', 'Committed_preadipocyte', 'SMC', 'AEC',
#        'LAM', 'PVM', 'Classical_monocyte', 'Early_preadipocyte', 'CD4+_T',
#        'Areg', 'CD8+_T', 'Pericyte', 'cDC2', 'CD56dim_CD16+_NK', 'Treg']

sat_celltypes = sat_eqtl_df['celltype'].unique()
for celltype in sat_celltypes:
    sat_eqtl_sig_gene_path = f'/home/users/nus/e1124850/heritability_enrichment_ldsc/tong_sat_{celltype}_gene_set_file.txt'
    for chrid in range(1, 23):
        cmd = (
            f'python /home/users/nus/e1124850/ldsc/make_annot.py '
            f'--gene-set-file {sat_eqtl_sig_gene_path} '
            f'--gene-coord-file {gene_coord_file_path} '
            f'--windowsize 100000 '
        f'--bimfile /home/users/nus/e1124850/e1124850/co_lab/tongyihan/1000G_Phase3_EAS_plinkfiles/1000G.EAS.QC.{chrid}.bim '
        f'--annot-file /home/users/nus/e1124850/e1124850/co_lab/tongyihan/gene_annot_file/tong_sat_{celltype}_eqtlsig_gene_annot_file.{chrid}.annot.gz'
    )
        os.system(cmd)

# python /home/users/nus/e1124850/ldsc-python3/make_annot.py --gene-set-file /home/users/nus/e1124850/heritability_enrichment_ldsc/tong_sat_gene_set_file.txt  --gene-coord-file /home/users/nus/e1124850/heritability_enrichment_ldsc/gene_coord_file.txt --windowsize 100000 --bimfile /home/users/nus/e1124850/scratch/adipose_after_imputation_296_merged_genome_rename_rsID_nochr_neur.{chrid}.bim --annot-file /home/users/nus/e1124850/heritability_enrichment_ldsc/tong_sat_eqtlsig.{chrid}.annot.gz


vat_celltypes = ['Adipocyte', 'Committed_preadipocyte', 'Mesothelial', 'CEC',
       'CD8+_T', 'SMC', 'TIM4+_ATM', 'LEC', 'PVM', 'Classical_monocyte',
       'TIM4+_CD11c+_ATM', 'Early_preadipocyte', 'CD4+_T', 'AEC',
       'IGFBP2+_cell', 'Pericyte', 'VEC', 'LAM', 'Areg', 'cDC2',
       'CD56dim_CD16+_NK']
vat_celltypes = vat_eqtl_df['celltype'].unique()
for celltype in vat_celltypes:
    vat_eqtl_sig_gene_path = f'/home/users/nus/e1124850/heritability_enrichment_ldsc/tong_vat_{celltype}_gene_set_file.txt'
    for chrid in range(1, 23):
        cmd = (
            f'python /home/users/nus/e1124850/ldsc/make_annot.py '
            f'--gene-set-file {vat_eqtl_sig_gene_path} '
            f'--gene-coord-file {gene_coord_file_path} '
            f'--windowsize 100000 '
            f'--bimfile /home/users/nus/e1124850/e1124850/co_lab/tongyihan/1000G_Phase3_EAS_plinkfiles/1000G.EAS.QC.{chrid}.bim '
            f'--annot-file /home/users/nus/e1124850/e1124850/co_lab/tongyihan/gene_annot_file/tong_vat_{celltype}_eqtlsig_gene_annot_file.{chrid}.annot.gz'
        )
        os.system(cmd)


annotfiles = glob('/home/users/nus/e1124850/e1124850/co_lab/tongyihan/gene_annot_file/*.annot.gz')

for annotfile in annotfiles:
    df = pd.read_csv(annotfile, sep='\t')
    df['base'] = 1
    df = df[['base', 'ANNOT']]
    df.to_csv(annotfile, sep='\t', index=False, compression='gzip')




# for j in $(seq 1 22); do
#     zcat /home/users/nus/e1124850/e1124850/co_lab/tongyihan/gene_annot_file/tong_sat_eqtlsig_gene_annot_file.${j}.annot.gz \
#         | awk 'BEGIN{OFS="\t"} NR==1{for(i=1;i<=NF;i++) if($i!="base") cols[i]=1} {out=""; for(i=1;i<=NF;i++) if(cols[i]) printf "%s%s", (out==""?"":"\t"), $i; printf "\n"}' \
#         | gzip > /home/users/nus/e1124850/e1124850/co_lab/tongyihan/gene_annot_file/tong_sat_fixed.${j}.annot.gz
#     echo "Chr ${j} done"
# done





# for j in $(seq 1 22); do
#     zcat /home/users/nus/e1124850/e1124850/co_lab/tongyihan/gene_annot_file/tong_vat_eqtlsig_gene_annot_file.${j}.annot.gz \
#         | awk 'BEGIN{OFS="\t"} NR==1{for(i=1;i<=NF;i++) if($i!="base") cols[i]=1} {out=""; for(i=1;i<=NF;i++) if(cols[i]) printf "%s%s", (out==""?"":"\t"), $i; printf "\n"}' \
#         | gzip > /home/users/nus/e1124850/e1124850/co_lab/tongyihan/gene_annot_file/tong_vat_fixed.${j}.annot.gz
#     echo "Chr ${j} done"
# done