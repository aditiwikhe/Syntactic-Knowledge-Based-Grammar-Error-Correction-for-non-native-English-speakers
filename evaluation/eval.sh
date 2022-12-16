folder_name='tuesday_results/output_POS_B_WHOLE'
#lang='ru'

#python reranker.py $folder_name/test.nbest.tok $lang $folder_name/reranked.tok
#errant_m2 -gold $folder_name/fce.es.out.m2 -out $folder_name/new.m2
#errant_parallel -orig $folder_name/fce.test.ru.src -cor $folder_name/reranked.tok -out $folder_name/reranked.m2
errant_parallel -orig $folder_name/fce.test.lang.src -cor $folder_name/test.best.tok -out $folder_name/best.m2
#errant_compare -hyp $folder_name/reranked.m2 -ref $folder_name/russian.new.m2 > $folder_name/reranked.result
errant_compare -hyp $folder_name/best.m2 -ref $folder_name/fce.test.m2 > $folder_name/normal.result