## 1.搜索主题与愿景

“笔墨纸宴”是围绕古书画文物构建的搜索引擎。现下市面上的搜索引擎并不完备，存在信息收入不全、产品分散文化联系松弛、不支持自然语言查询，及无法聚焦搜索结果等问题，用户友好型搜索方案。我们的项目前期从中国五大博物馆收集了近1600件书画作品的信息，构建书画类专门的搜索引擎，旨在为用户提供更好地搜索体验，满足用户的文化需求。用户通过搜索引擎可以查询到书画的年代、作者尺寸等基本信息。除此之外，通过高亮、分面、自然语言查询等增强型搜索功能，用户可以查看到年代、作者、书画内容等字画相关知识的拓展阅读。如用户搜索阎立本《步辇图》可查看到步辇图的创作背景。

## 2.元数据设计方案

###### 参考资料与标准

- CDWA Lite: Specification 1.1；

- Using Dublin Core - Dublin Core Qualifiers；

- Dublin Core Metadata Element Set, Version 1.1: Reference Description；

- CBDB: 中国古代人物数据库。

## 3.数据采集

###### 数据来源

- 故宫博物院、上海博物馆、中国国家博物馆、湖北省博物馆。

###### 技术思路

- 使用Scrapy框架；

- 使用Selenium模拟用户操作浏览器；

- 数据采集软件（八爪鱼）；

- 手工爬取；

###### 网页解析

- Xpath、Css和循环。

## 4.数据清洗与整理

- Pandas：去除空行、去除标题/图片字段为空的行、将尺寸统一字段格式等；

- Excel：手动清洗：将错位的字段内容人工放回所匹配处，对冗余字段进行清洗。

## 5.索引构建

###### Document

- 增加字段”Category“，将法书和绘画合入一张表；

- 将”coverageDynastry（朝代）“、”displayMaterials（材质）“中关于同一朝代的不同表述进行统一；

- 为减少数据冗余，检查作者的重复性，并将作者和作者简介分离成另一张表，去重后，再次进行索引的构建。

###### Schema

- 配置分词包；

- 配置用户词典；

- 规定field name。

## 6.搜索交互界面原型设计与搜索体验评价

###### 基础搜索

- 框搜索：searchitem

- 高级搜素：利用fq构造筛选，先用searchitem:*找出所有数据，然后再进行筛选。url构造：

```
http://47.101.171.247:8983/solr/test_01/select?fq=category:*&fq=coverageDynasty:*&fq=creatorAuthor:*&fq=description:*&fq=displayMaterials:*&fq=sourceLocation:*&fq=subject:*&fq=title:*&q=searchitem:*
```

- 二次筛选

二次筛选主要进一步添加了搜索结果页的进一步搜索，筛选条件为类别。

- 自然语言查询示例

![](C:\Users\73536\AppData\Roaming\marktext\images\2024-02-28-23-27-22-image.png)

###### 增强型搜索

- 高亮：将用户搜索的内容在搜索结果中进行高亮显示，突出重点。

- 分面：将用户搜索的结果按照“分类”进行数量统计，为用户呈现当前搜索结果的大致情况。

- dismax解析器：对多个字段进行维度的综合打分排序时，需要用dismax和edismax来解决。

###### 搜索体验

因为小程序拥有轻量级的特性，所以当数据量大时传输的时间比一般网页版搜索引擎要长，容易给用户造成不好的搜索体验，且结果页面只能呈现6条左右的数据，用户需要不停地滑动页面。

## 搜索功能设计与Solr界面展示

![微信图片_20240228233219](https://github.com/archykool/SearchEngine_AncientChineseCalligraphy-Painting/assets/34702275/05662fb1-8319-4f8e-bf51-9ad6433fde0d)
