# Cancer-KnowledgeGraph Demo

## 数据获取
用Python的Selenium包编写简易爬虫，获取<a href='http://www.chealth.org.cn/' target='_blank'>中国公众健康网</a>上的如下信息：
1. 疾病信息：来自中国公众健康网的常见疾病信息。
2. 医生信息：来自中国公众健康网的医生信息。

## 数据存储
将爬取的数据分为如下表格，以csv文件的形式进行存储：
1. 疾病索引表：常见肿瘤科疾病索引列表。
2. 疾病信息表：根据疾病索引检索出的疾病信息列表。
3. 医院索引表：单独的医院名称索引列表。
4. 医生信息表：根据疾病索引检索出的相关医生信息列表。
5. 疾病相关关系表：给定病历数据库中常见疾病间的共现频率统计表。

## 数据关系
建立数据间的关联关系如下：
1. 疾病简称/俗称<-[检索]->疾病学名
2. 医生名-[治疗]->疾病学名
3. 医生名<-[从属]->医院名
4. 疾病简称/俗称<-[共现]->疾病简称/俗称

## 数据可视化
用Neo4j生成可视化数据关系图如下：<br>
1. 疾病关系图谱：<br>
<img src='https://github.com/ddddwy/cancer-KnowledgeGraph/blob/master/graphs/disease_graph.png'/>
2. 医院关系图谱：<br>
<img src='https://github.com/ddddwy/cancer-KnowledgeGraph/blob/master/graphs/hospital_graph.png'/>

## Inference
<a href='http://www.shuang0420.com/2017/09/05/%E9%A1%B9%E7%9B%AE%E5%AE%9E%E6%88%98-%E7%9F%A5%E8%AF%86%E5%9B%BE%E8%B0%B1%E5%88%9D%E6%8E%A2/' target='_blank'>项目实战--知识图谱初探</a>
