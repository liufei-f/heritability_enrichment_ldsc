








```bash


#PBS -q normal
#PBS -l select=1:ncpus=2:mem=300G
#PBS -l walltime=24:00:00
#PBS -P 11003054
#PBS -N ldscore_tong_sat
#PBS -o /home/users/nus/e1124850/scratch/qsub_dir/ldscore_tong_sat.o
#PBS -e /home/users/nus/e1124850/scratch/qsub_dir/ldscore_tong_sat.e

# for j in $(seq 1 22); do
#     echo $j
#     python /home/users/nus/e1124850/ldsc/ldsc.py \
#         --l2 \
#         --bfile /home/users/nus/e1124850/e1124850/co_lab/tongyihan/1000G_Phase3_EAS_plinkfiles/1000G.EAS.QC.${j} \
#         --ld-wind-cm 1 \
#         --annot /home/users/nus/e1124850/e1124850/co_lab/tongyihan/gene_annot_file/tong_sat_fixed.${j}.annot.gz \
#         --thin-annot \
#         --out /home/users/nus/e1124850/e1124850/co_lab/tongyihan/gene_annot_file/tong_sat_fixed.${j} \
#         --print-snps /home/users/nus/e1124850/e1124850/co_lab/tongyihan/baselineLD_v2.2.snps.txt & \
# done



source /home/project/11003054/e1124850/MM/software/anaconda3/etc/profile.d/conda.sh
conda deactivate
conda deactivate
conda activate ldsc39


sat_celltypes=("Adipocyte" "CEC" "VEC" "Committed_preadipocyte" "SMC" "AEC" \
"LAM" "PVM" "Classical_monocyte" "Early_preadipocyte" "CD4+_T" \
"Areg" "CD8+_T" "Pericyte" "cDC2" "CD56dim_CD16+_NK" "Treg")

for cell in "${sat_celltypes[@]}"; do
    echo "Processing cell type: ${cell}"

    for j in $(seq 1 22); do
        echo "  Chromosome ${j}"

        python /home/users/nus/e1124850/ldsc/ldsc.py \
            --l2 \
            --bfile /home/users/nus/e1124850/e1124850/co_lab/tongyihan/1000G_Phase3_EAS_plinkfiles/1000G.EAS.QC.${j} \
            --ld-wind-cm 1 \
            --annot /home/users/nus/e1124850/e1124850/co_lab/tongyihan/gene_annot_file/tong_sat_${cell}_eqtlsig_gene_annot_file.${j}.annot.gz \
            --thin-annot \
            --out /home/users/nus/e1124850/e1124850/co_lab/tongyihan/gene_annot_file/tong_sat_${cell}_eqtlsig_gene_annot_file.${j} \
            --print-snps /home/users/nus/e1124850/e1124850/co_lab/tongyihan/baselineLD_v2.2.snps.txt &
    done
done
wait


```
qsub ldscore_tong_sat.pbs


```bash

#PBS -q normal
#PBS -l select=1:ncpus=2:mem=300G
#PBS -l walltime=24:00:00
#PBS -P 11003054
#PBS -N ldscore_tong_vat
#PBS -o /home/users/nus/e1124850/scratch/qsub_dir/ldscore_tong_vat.o
#PBS -e /home/users/nus/e1124850/scratch/qsub_dir/ldscore_tong_vat.e



source /home/project/11003054/e1124850/MM/software/anaconda3/etc/profile.d/conda.sh
conda deactivate
conda deactivate
conda activate ldsc39



# for j in $(seq 1 22); do
#     echo $j
#     python /home/users/nus/e1124850/ldsc/ldsc.py \
#         --l2 \
#         --bfile /home/users/nus/e1124850/e1124850/co_lab/tongyihan/1000G_Phase3_EAS_plinkfiles/1000G.EAS.QC.${j} \
#         --ld-wind-cm 1 \
#         --annot /home/users/nus/e1124850/e1124850/co_lab/tongyihan/gene_annot_file/tong_vat_fixed.${j}.annot.gz \
#         --thin-annot \
#         --out /home/users/nus/e1124850/e1124850/co_lab/tongyihan/gene_annot_file/tong_vat_fixed.${j} \
#         --print-snps /home/users/nus/e1124850/e1124850/co_lab/tongyihan/baselineLD_v2.2.snps.txt & \
# done

source /home/project/11003054/e1124850/MM/software/anaconda3/etc/profile.d/conda.sh
conda deactivate
conda deactivate
conda activate ldsc39

vat_celltypes=('Adipocyte' 'Committed_preadipocyte' 'Mesothelial' 'CEC' \
'CD8+_T' 'SMC' 'TIM4+_ATM' 'LEC' 'PVM' 'Classical_monocyte' \
'TIM4+_CD11c+_ATM' 'Early_preadipocyte' 'CD4+_T' 'AEC' \
'IGFBP2+_cell' 'Pericyte' 'VEC' 'LAM' 'Areg' 'cDC2' \
'CD56dim_CD16+_NK')

for cell in "${vat_celltypes[@]}"; do
    echo "Processing cell type: ${cell}"

    for j in $(seq 1 22); do
        echo "  Chromosome ${j}"

        python /home/users/nus/e1124850/ldsc/ldsc.py \
            --l2 \
            --bfile /home/users/nus/e1124850/e1124850/co_lab/tongyihan/1000G_Phase3_EAS_plinkfiles/1000G.EAS.QC.${j} \
            --ld-wind-cm 1 \
            --annot /home/users/nus/e1124850/e1124850/co_lab/tongyihan/gene_annot_file/tong_vat_${cell}_eqtlsig_gene_annot_file.${j}.annot.gz \
            --thin-annot \
            --out /home/users/nus/e1124850/e1124850/co_lab/tongyihan/gene_annot_file/tong_vat_${cell}_eqtlsig_gene_annot_file.${j} \
            --print-snps /home/users/nus/e1124850/e1124850/co_lab/tongyihan/baselineLD_v2.2.snps.txt &
    done
done

wait


```
qsub ldscore_tong_vat.pbs






