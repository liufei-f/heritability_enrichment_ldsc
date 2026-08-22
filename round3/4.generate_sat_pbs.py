

pbstemplete = '''#PBS -q normal
#PBS -l select=1:ncpus=2:mem=200G
#PBS -l walltime=120:00:00
#PBS -P 11003054
#PBS -N CELLTYPE_sat_h2
#PBS -o /home/users/nus/e1124850/scratch/qsub_dir/CELLTYPE_sat_h2.o
#PBS -e /home/users/nus/e1124850/scratch/qsub_dir/CELLTYPE_sat_h2.e

source /home/users/nus/e1124850/anaconda3/etc/profile.d/conda.sh
conda activate snakemake

WORKDIR=/home/users/nus/e1124850/scratch/snakework/sat_CELLTYPE
mkdir -p $WORKDIR
ln -sfn /home/users/nus/e1124850/CELLECT/scripts $WORKDIR/scripts
cd $WORKDIR
PYTHONNOUSERSITE=1 snakemake \
  --use-conda \
  --conda-frontend conda \
  --conda-prefix /home/users/nus/e1124850/.snakemake/conda \
  -j 1 \
  -s /home/users/nus/e1124850/CELLECT/cellect-ldsc.snakefile \
  --configfile /home/users/nus/e1124850/scratch/github/heritability_enrichment_ldsc/round3/satconfig/config_sat_CELLTYPE.yaml
'''


for celltype in ['Adipocyte','AEC','Areg','CD4pos_T','CD56dim_CD16pos_NK','CD8pos_T','cDC2','CEC','Classical_monocyte','Committed_preadipocyte','Early_preadipocyte','LAM','Pericyte','PVM','SMC','Treg','VEC']:
    with open(f'/Users/theeeight/github/heritability_enrichment_ldsc/round3/satpbs/config_sat_{celltype}.pbs','w') as f:
        f.write(pbstemplete.replace('CELLTYPE',celltype))
        f.close()