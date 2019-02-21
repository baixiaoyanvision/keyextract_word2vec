#!/usr/bin/env python                                                                                                                                                                  
# -*- coding: utf-8 -*-
#使用gensim word2vec训练脚本获取词向量


import warnings
warnings.filterwarnings(action = 'ignore', category = UserWarning, module = 'gensim')#忽略警告

import logging
import os.path
import sys
import multiprocessing

from gensim.corpora import WikiCorpus
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence


#program = os.path.basename(sys.argv[0])
#logger = logging.getLogger(program)

#logging.basicConfig(format = '%(asctime)s: %(levelname)s:' %('message)s'),level = logging.INFO)
#logger.info("running %s" % ' '.join(sys.argv))

fdir = '/data1/word2vec/'
inp = fdir + 'data_result.txt'
outp1 = fdir + 'data.model'
outp2 = fdir + 'data.vector'

#model = Word2Vec(LineSentence(inp), size = 400, window = 5, min_count = 5, workers = multiprocessing.cpu_count())
model = Word2Vec(LineSentence(inp), size = 256, window = 5, min_count = 5,sg=1, hs=1, iter=10, workers=25)
print(model)
model.save(outp1)
model.wv.save_word2vec_format(outp2, binary=False)
