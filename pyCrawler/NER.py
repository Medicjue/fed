# -*- coding: utf-8 -*-
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from itertools import groupby

st = StanfordNERTagger(
		'/Users/Kojima/Downloads/stanford-ner-2016-10-31/classifiers/english.all.3class.distsim.crf.ser.gz',
		'/Users/Kojima/Downloads/stanford-ner-2016-10-31/stanford-ner.jar',
		encoding='utf-8'
	)

targetFile = './Demo/Part1.txt'

with open(targetFile, 'r') as myfile:
	text = myfile.read().replace('\n', '')

sent_tokenize_list = sent_tokenize(text)
print "# Sentence Count", len(sent_tokenize_list)

OrgList = []
for idx, sent in enumerate(sent_tokenize_list):
	if idx % 10 == 0:
		print idx

	tokenized_text = word_tokenize(sent)
	classified_text = st.tag(tokenized_text)

	for tag, chunk in groupby(classified_text, lambda x:x[1]):
		if tag != "O":
			item = " ".join(w for w, t in chunk)
			if item not in OrgList:
				OrgList.append(item)

print "# Organization Count", len(OrgList)
print OrgList