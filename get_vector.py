 #!/usr/bin/env python                                                                                                                                                                  
 # -*- coding: utf-8 -*-
 # encoding: utf-8
 
 #逐行读取文件数据进行jieba分词
 
 import jieba
 import jieba.analyse
 import jieba.posseg as pseg  #引入词性标注接口
 import codecs,sys
 
 
 f = codecs.open('data.txt' , 'r', encoding = 'utf8')
 target = codecs.open('data_seg.txt', 'w', encoding = 'utf8')
 stopkey = [w.strip() for w in codecs.open('stopWrod.txt', 'r').readlines()]
 print("open files")
 #count = 0
 lineNum = 1
 line = f.readline()
 while line:
     print("---processiong", lineNum, "article---")
     seg_list = jieba.cut(line, cut_all = False)
     line_seg = ''
     for word in seg_list:
         if word not in stopkey:
            line_seg += word
            line_seg += ' '
     #line_seg = ' '.join(seg_list)
     target.writelines(line_seg)
     lineNum += 1
     line = f.readline()
 
 print("well done")
 f.close()
 target.close()
