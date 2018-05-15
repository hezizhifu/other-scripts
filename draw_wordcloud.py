#!/usr/bin/env python
#-*-coding:utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import jieba 
import jieba.analyse
import codecs
import os
from os import path
def draw_word():

	fs=path.dirname(__file__)
	text=[]
	out=' '
	stopwords=[u'这里',u'那里',u'你们',u'我们',u'已经',u'一个',u'他们',u'起来',u'这个',u'这些'
	u'自己',u'出来',u'东西',u'不知',u'没有',u'现在',u'就是',u'不是',u'地方'		
	]
	#读取文本文件
	with open(path.join(fs,'平凡的世界.txt')) as txs:
		for line in txs.readlines():
			line=line.strip('\n')
			jib=jieba.cut(line)
			for word in jib:
				if word not in stopwords:
					if word !='\n':
						out+=word
						out+=' '
	mask_img=plt.imread(path.join(fs,'mask.jpg'))
	wc=WordCloud(background_color='gray',
	     mask=mask_img,
	     max_words=150,
	     stopwords=STOPWORDS,
	     font_path=path.join(fs,'msyh.ttf'),
	     max_font_size=400,
	     random_state=30

		  )		
	#生成词云
	word_cloud=wc.generate(out)#根据文本生成词云
	#word_cloud=wc.generate_from_frequencies(text)#根据频率生成词云
	#保存为图片
	word_cloud.to_file('ciyun.jpg')
	#展示生成的词云
	#plt.figure()
	plt.imshow(word_cloud, interpolation="bilinear")
	plt.axis("off")
	plt.show()

if __name__=='__main__':
	draw_word()
