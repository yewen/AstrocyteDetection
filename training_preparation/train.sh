#!/bin/bash
#SBATCH -J m ### job name
#SBATCH -o m.o%j ### output and error file name (%j expands to jobID)
#SBATCH --mail-user=yewenh55@gmail.com
#SBATCH --mem-per-cpu=8500 ### How much memory in megabytes per cpu that you are using, Max is approximately 8800.

#SBATCH --mail-type=all #### email me when the job starts (changes its status on the queue
#### and gets the need resources resources),
#### or when the job fails or when it finishes

#SBATCH -p volta -t 96:00:00 -N 1 -n 24 --gres=gpu:1  ### time allocated to your job, num cpus, and num gpus to be used
### Tell SLURM which account (advisor) to charge this job to
#SBATCH -A labate

hostname
#nvidia-smi
module add pytorch/1.6.0-python-3.7 ### activate the python environment you need.
#### In my case i need pytorch (latest version)

python train.py --img 1024 --batch 32 --epochs 300 --data bcc1.yaml --adam --weights yolov5s.pt --cfg models/yolov5s.yaml --name ASTROCYTES1



