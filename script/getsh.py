#python run_gc_adj.py -b ../data/bam/PA209U0237-C5C9H20XNF1-H001K799Y00D.5X.sort.dedup.bam --bed ../data/tss.sort.bed  --genome2bit /dssg/home/zhangjp/database/hg19/genome/hs37d5.fa.2bit --threads 30
import sys
import os
with open (sys.argv[1]) as f:
    for i in f:
        line=i.strip()
        print("python /dssg/home/zhangjp/soft/AECT/AECT-master/script/run_gc_adj.py -b "+line+"  --bed "+sys.argv[2]+" --genome2bit /dssg/home/zhangjp/database/hg19/genome/hs37d5.fa.2bit --threads 15")
