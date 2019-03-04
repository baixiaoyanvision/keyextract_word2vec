  #1/usr/bin/python                                                                                                                                                                      
  # -*- coding: utf-8 -*-
  # encoding: utf-8
  
  import os
  import sys
  import re
  import codecs,sys
  
  
  f = open("data_seg.txt", 'r')
  stopkey = [w.strip() for w in codecs.open('stopWrod.txt', 'r').readlines()]
  w = open('data_result.txt','w')
  
  
  
  seg = f.readline()
  while seg:
      l = []
      s1 = re.split(' ', seg)
      for i in s1:
          if i not in l and i not in stopkey:
              l.append(i)
              #allword.append(i)
      for j in l:
          w.write(j)
          w.write('   ')
      seg = f.readline()
 
 f.close()
 w.close()
