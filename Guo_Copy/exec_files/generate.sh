TEXT='/netscratch/abusuttil/Guo_copy/src-trg'
DATA_DIR='/netscratch/abusuttil/Guo_copy/dest_dir'

CUDA_LAUNCH_BLOCKING=1 python generate.py $DATA_DIR \
  --task bert_xymasked_wp_seq2seq --bert-model-name 'mbertu' \
  --path /netscratch/abusuttil/Guo_copy/checkpoints/checkpoint_best.pt --decode_use_adapter \
  --mask_pred_iter 10 --left-pad-source False \
  --batch-size 16 --beam 4 --lenpen 1.1 --remove-bpe wordpiece