TEXT='/netscratch/abusuttil/Guo_copy'
DICT='/netscratch/abusuttil/Guo_copy/src-trg'
DATA_DIR='/netscratch/abusuttil/Guo_copy/dest_dir'

python preprocess.py --task bert_xymasked_wp_seq2seq \
  --source-lang src --target-lang trg \
  --srcdict $DATA_DIR/dict.src.txt \
  --tgtdict $DATA_DIR/dict.trg.txt \
  --trainpref $DICT/train --validpref $DICT/valid --testpref $DICT/test \
  --destdir $DATA_DIR --workers 20