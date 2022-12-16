# Syntactic-Knowledge-Based-Grammar-Error-Correction

This repository contains the codebase for our CS 546 Final Project.

The repo contains 4 steps

##Preprocess
The Preprocess folder contains scripts for applying the error supression logic.
   Steps to run the preprocessing:
   
1. Generate the error distribution for languages
`python lang_id.py`
This script runs through the error tag file (fce.test.lang.m2) and generates a count of errors for each language.

2. Run the error suppression logic 
The script is present in `NEW_CS546_error_suppression_pt.ipynb`; which can be run on Colab.
   
##BERT finetuning
This folder contains a notebook to run visualization with Fine-Tuned BERT 

##Training
The Training folder contains scripts for running training with the output generated from the preprocess step.
This folder contains a python notebook: `POS_BERT_FUSE_GEC_11.ipynb`.
When running, two changes have to be made:
1. Replace the train.src & train.trg files in  with the files generated from the preprocess step.
2. Replace the train.sh in bert-gec/scripts with the train.sh files present in the training folder in this repository.
The notebook also contains a script to run inference on the test set.

##Evaluation
The Evaluation folder contains `eval.sh` to run the m2 scorer and generate precision, recall and F-scores.
It also contains script for our reranker logic.
Note: Install errant before running this script.