








```bash


#PBS -q normal
#PBS -l select=1:ncpus=2:mem=300G
#PBS -l walltime=24:00:00
#PBS -P 11003054
#PBS -N ldscore_tianchi_sat
#PBS -o /home/users/nus/e1124850/scratch/qsub_dir/ldscore_tianchi_sat.o
#PBS -e /home/users/nus/e1124850/scratch/qsub_dir/ldscore_tianchi_sat.e

source /home/project/11003054/e1124850/MM/software/anaconda3/etc/profile.d/conda.sh
conda deactivate
conda deactivate
conda activate ldsc39

sat_celltypes=('Adipocyte' 'Committed_preadipocyte' 'CEC' 'VEC' 'AEC' 'PVM' 'SMC' 'Early_preadipocyte' 'LAM' 'Areg' 'Pericyte')

for cell in "${sat_celltypes[@]}"; do
    echo "Processing cell type: ${cell}"

    for j in $(seq 1 22); do
        echo "  Chromosome ${j}"

        python /home/users/nus/e1124850/ldsc/ldsc.py \
            --l2 \
            --bfile /home/users/nus/e1124850/e1124850/co_lab/tongyihan/1000G_Phase3_EAS_plinkfiles/1000G.EAS.QC.${j} \
            --ld-wind-cm 1 \
            --annot /home/users/nus/e1124850/e1124850/co_lab/tianchi/gene_annot_file/tianchi_sat_${cell}_sqtlsig_gene_annot_file.${j}.annot.gz \
            --thin-annot \
            --out /home/users/nus/e1124850/e1124850/co_lab/tianchi/gene_annot_file/tianchi_sat_${cell}_sqtlsig_gene_annot_file.${j} \
            --print-snps /home/users/nus/e1124850/e1124850/co_lab/tongyihan/baselineLD_v2.2.snps.txt &
    done
done
wait

```
qsub ldscore_tianchi_sat.pbs


```bash

#PBS -q normal
#PBS -l select=1:ncpus=2:mem=300G
#PBS -l walltime=24:00:00
#PBS -P 11003054
#PBS -N ldscore_tianchi_vat
#PBS -o /home/users/nus/e1124850/scratch/qsub_dir/ldscore_tianchi_vat.o
#PBS -e /home/users/nus/e1124850/scratch/qsub_dir/ldscore_tianchi_vat.e


source /home/project/11003054/e1124850/MM/software/anaconda3/etc/profile.d/conda.sh
conda deactivate
conda deactivate
conda activate ldsc39

vat_celltypes=('Mesothelial' 'Adipocyte' 'Committed_preadipocyte' 'PVM' 'CEC' 'AEC' 'SMC' 'VEC' 'Early_preadipocyte' 'TIM4+_ATM' 'LEC' 'Pericyte' 'IGFBP2+_cell' 'CD8+_T')

for cell in "${vat_celltypes[@]}"; do
    echo "Processing cell type: ${cell}"

    for j in $(seq 1 22); do
        echo "  Chromosome ${j}"

        python /home/users/nus/e1124850/ldsc/ldsc.py \
            --l2 \
            --bfile /home/users/nus/e1124850/e1124850/co_lab/tongyihan/1000G_Phase3_EAS_plinkfiles/1000G.EAS.QC.${j} \
            --ld-wind-cm 1 \
            --annot /home/users/nus/e1124850/e1124850/co_lab/tianchi/gene_annot_file/tianchi_vat_${cell}_sqtlsig_gene_annot_file.${j}.annot.gz \
            --thin-annot \
            --out /home/users/nus/e1124850/e1124850/co_lab/tianchi/gene_annot_file/tianchi_vat_${cell}_sqtlsig_gene_annot_file.${j} \
            --print-snps /home/users/nus/e1124850/e1124850/co_lab/tongyihan/baselineLD_v2.2.snps.txt &
    done
done
wait


```
qsub ldscore_tianchi_vat.pbs






