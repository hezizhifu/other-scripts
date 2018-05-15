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
	text=' '
	#读取文本文件
	with open(path.join(fs,'平凡的世界.txt')) as txs:
		for line in txs.readlines():
			line=line.strip('\n')
			jib=jieba.cut(line)
			jieba.analyse.set_stop_words('stopwords.txt')
			text+=' '.join(jib)
			text+=' '
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
	word_cloud=wc.generate(text)#根据文本生成词云
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
