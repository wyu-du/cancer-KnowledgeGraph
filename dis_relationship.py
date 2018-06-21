# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 15:42:59 2018

@author: Administrator
"""

import os
import codecs
import jieba
jieba.load_userdict('data_path/user_dict.txt')
import pandas as pd
from collections import defaultdict

TEXT_PATH = 'data_path/original_data/women/'  # 文本路径
DICT_PATH = 'data_path/disease.txt'  # 疾病字典路径
SAVE_NODE_PATH = 'node_women.csv'
SAVE_EDGE_PATH = 'edge_women.csv'


class RelationshipView(object):
    def __init__(self, text_path, dict_path):
        self._text_path=text_path
        self._dict_path=dict_path
        
        self._disease_counter=defaultdict(int)
        self._disease_per_doc=[]
        self._relationships={}
        
    def generate(self):
        self.count_disease()
        self.calc_relationship()
        self.save_node_and_edge()
        
    def get_clean_docs(self):
        files=os.listdir(self._text_path)
        docs=[]
        for file in files:
            df=pd.read_csv(TEXT_PATH+file)
            doc1=list(df['WYSText'])
            doc2=list(df['WYGText'])
            docs.extend(doc1)
            docs.extend(doc2)
        return docs
    
    def count_disease(self):
        docs=self.get_clean_docs()
        print('Start process node')
        disease_list=pd.read_csv(self._dict_path)
        disease_list=list(disease_list['dis'])
        for doc in docs:
            poss=jieba.cut(doc, cut_all=False)
            self._disease_per_doc.append([])
            for w in poss:
                if w not in disease_list:
                    continue
                self._disease_per_doc[-1].append(w)
                if self._disease_counter.get(w) is None:
                    self._relationships[w]={}
                self._disease_counter[w] += 1
        return self._disease_counter
    
    def calc_relationship(self):
        print('Start to process edge')
        for doc in self._disease_per_doc:
            for dis1 in doc:
                for dis2 in doc:
                    if dis1==dis2:
                        continue
                    if self._relationships[dis1].get(dis2) is None:
                        self._relationships[dis1][dis2]=1
                    else:
                        self._relationships[dis1][dis2]+=1
        return self._relationships
    
    def save_node_and_edge(self):
        with codecs.open(SAVE_NODE_PATH, 'w', 'utf-8') as f:
            f.write('Id,Label,Weigit\r\n')
            for name, times in self._disease_counter.items():
                f.write(name+','+name+','+str(times)+'\r\n')
                
        with codecs.open(SAVE_EDGE_PATH, 'w', 'utf-8') as f:
            f.write('Source,Target,Weight\r\n')
            for name, edges in self._relationships.items():
                for v, w in edges.items():
                    if w>3:
                        f.write(name+','+v+','+str(w)+'\r\n')
        print('Save file successful!')
        
if __name__=='__main__':
    v=RelationshipView(TEXT_PATH, DICT_PATH)
    v.generate()