TEXT='/netscratch/abusuttil/Guo_copy/src-trg'
DATA_DIR='/netscratch/abusuttil/Guo_copy/dest_dir'

python train.py $DATA_DIR \
  --task bert_xymasked_wp_seq2seq -s src -t trg \
  -a transformer_nat_ymask_bert_two_adapter_gec_bert_base \
  --optimizer adam --adam-betas '(0.9, 0.999)' --clip-norm 0.5 \
  --lr-scheduler cosine --warmup-updates 20000 --warmup-init-lr '1e-05' \
  --lr '1e-05' --min-lr '1e-07' --max-lr 0.0003 \
  --criterion label_smoothed_length_cross_entropy --label-smoothing 0.1 \
  --weight-decay 0.01 --max-tokens 3000 --update-freq 1 --max-update 300000 \
  --left-pad-source False --adapter-dimension 128 \
  --use-adapter-bert --bert-model-name 'mbertu' --decoder-bert-model-name  'mbertu' \
  --batch-size 32 \
  --dropout 0.2 \
  --attention-dropout 0.2
  





