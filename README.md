# Cancer-KnowledgeGraph Demo

## 数据获取
1. 疾病信息：来自中国公众健康网的常见疾病信息。
2. 医生信息：来自中国公众健康网的医生信息。

## 数据存储
1. 疾病索引表：常见肿瘤科疾病索引列表。
2. 疾病信息表：根据疾病索引检索出的疾病信息列表。
3. 医院索引表：单独的医院名称索引列表。
4. 医生信息表：根据疾病索引检索出的相关医生信息列表。
5. 疾病相关关系表：给定病历数据库中常见疾病间的共现频率统计表。

## 数据关系
1. 疾病简称/俗称<-[检索]->疾病学名
2. 医生名-[治疗]->疾病学名
3. 医生名<-[从属]->医院名
4. 疾病简称/俗称<-[共现]->疾病简称/俗称

## 数据可视化
用Neo4j生成可视化数据关系图如下：
<img src='https://github.com/ddddwy/cancer-KnowledgeGraph/blob/master/graphs/disease_graph.png'/>
<img src='https://github.com/ddddwy/cancer-KnowledgeGraph/blob/master/graphs/hospital_graph.png'/>