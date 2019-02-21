#!/usr/bin/python                                                                                                                                                                      
# -*- encoding: utf-8 -*-
# coding:utf-8

import numpy as np
import gensim
model = gensim.models.word2vec.Word2Vec.load('data.model')

def predict_proba(oword, iword):
    iword_vec = model[iword]
    oword = model.wv.vocab[oword]
    oword_l = model.syn1[oword.point].T
    dot = np.dot(iword_vec, oword_l)
    lprob = -sum(np.logaddexp(0, -dot) + oword.code*dot)
    return lprob

from collections import Counter
def keywords(s):
    s = [w for w in s if w in model]
    ws = {w:sum([predict_proba(u, w) for u in s]) for w in s}
    return Counter(ws).most_common()

import pandas as pd #引入它主要是为了更好的显示效果
import jieba

f = open('test_data.txt', 'r')
w = open('result.txt', 'w')
s = f.readline()
while s:
    result = pd.Series(keywords(jieba.cut(s)))
    for i in result:
        ci = i[0]
        print(ci)
        print("============")
        w.write(ci.encode('utf-8'))
        w.write('   ')
    w.write('\n')
    s = f.readline()

#s = u'今天我们来说说“迪丽热巴和奚梦瑶同台亮相，坐姿是亮点，网友：演员与超模的差距！”迪丽热巴是作为演员而出名的，奚梦瑶是作为超模而出名的，两位都是长腿大美女，还一起参加过《快乐大本营
》呢'
#result = pd.Series(keywords(jieba.cut(s)))
#print(result)
