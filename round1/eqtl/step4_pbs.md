```bash
#PBS -q normal
#PBS -l select=1:ncpus=2:mem=300G
#PBS -l walltime=24:00:00
#PBS -P 11003054
#PBS -N step4_sat
#PBS -o /home/users/nus/e1124850/scratch/qsub_dir/step4_sat.o
#PBS -e /home/users/nus/e1124850/scratch/qsub_dir/step4_sat.e



source /home/project/11003054/e1124850/MM/software/anaconda3/etc/profile.d/conda.sh
conda deactivate
conda deactivate
conda activate ldsc39


python /home/users/nus/e1124850/scratch/qsub_dir/step4_sat.py



```




```bash
#PBS -q normal
#PBS -l select=1:ncpus=2:mem=300G
#PBS -l walltime=24:00:00
#PBS -P 11003054
#PBS -N step4_vat
#PBS -o /home/users/nus/e1124850/scratch/qsub_dir/step4_vat.o
#PBS -e /home/users/nus/e1124850/scratch/qsub_dir/step4_vat.e



source /home/project/11003054/e1124850/MM/software/anaconda3/etc/profile.d/conda.sh
conda deactivate
conda deactivate
conda activate ldsc39


python /home/users/nus/e1124850/scratch/qsub_dir/step4_vat.py



```