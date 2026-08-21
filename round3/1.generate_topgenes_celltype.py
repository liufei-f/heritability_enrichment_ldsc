import pandas as pd
import os

## SAT

sat_cellex = '/data/projects/11003054/e1101943/project/01.adipose_sqtl/data/33.CELLEX/cellex_Annotation_level2.SAT_filtered.ensembl.esmu.csv.gz'
filtered_top_genes_percent = 0.1
outdir = '/home/users/nus/e1124850/e1124850/co_lab/tongyihan/round3'

sat_cellex_df = pd.read_csv(sat_cellex)


for celltype in sat_cellex_df.columns[1:]:
    sub_df = sat_cellex_df[['gene',celltype]]
    celltype = celltype.replace('+','pos')
    sub_df.columns = ['gene',celltype]
    sub_df = sub_df.sort_values(celltype,ascending=False).iloc[:int(len(sub_df)*filtered_top_genes_percent),:]
    sub_df.to_csv(os.path.join(outdir,f'SAT_top_{int(filtered_top_genes_percent*100)}percent_{celltype}.csv.gz'),index=False,compression='gzip')



## VAT

vat_cellex = '/data/projects/11003054/e1101943/project/01.adipose_sqtl/data/33.CELLEX/cellex_Annotation_level2.VAT_filtered.ensembl.esmu.csv.gz'
filtered_top_genes_percent = 0.1
outdir = '/home/users/nus/e1124850/e1124850/co_lab/tongyihan/round3'

vat_cellex_df = pd.read_csv(vat_cellex)


for celltype in vat_cellex_df.columns[1:]:
    sub_df = vat_cellex_df[['gene',celltype]]
    celltype = celltype.replace('+','pos')
    sub_df.columns = ['gene',celltype]
    sub_df = sub_df.sort_values(celltype,ascending=False).iloc[:int(len(sub_df)*filtered_top_genes_percent),:]
    sub_df.to_csv(os.path.join(outdir,f'VAT_top_{int(filtered_top_genes_percent*100)}percent_{celltype}.csv.gz'),index=False,compression='gzip')

