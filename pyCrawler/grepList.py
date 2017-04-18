# -*- coding: utf-8 -*-
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from itertools import groupby


clist = [u'RIVA TNT', u'Microsoft', u'Compaq', u'Dell', u'Hewlett-Packard', u'IBM', u'Micron', u'Packard BellNEC', u'Intel', u'RIVA', u'Intel Corporation', u'TNT', u'ELSA', u'Leadtek', u'STB', u'Packard Bell NEC', u'BestBuyand CompUSA', u'Diamond', u'Taiwan', u'TSMC', u'Amkor Technology Inc.', u'Siliconware PrecisionIndustries Company Ltd.', u'ChipPAC', u'ASUSTeK', u'Hewlett Packard', u'PC Magazine', u'CNET', u'VLSI', u'Cadence Design Systems , Inc.', u'IKOS Systems , Inc.', u'Synopsys', u'ATI Technologies Inc.', u'Matrox Electronics Systems Ltd.', u'Matrox', u'Trident Microsystems , Inc.', u'3Dlabs Inc. , Ltd.', u'Silicon Graphics , Inc.', u'Evans', u'Sutherland Computer Corporation', u'Intergraph Corporation', u'Intergraph', u'3Dfx Interactive , Inc.', u'VideoLogic Group', u'Videologic', u'Weexpect Intel', u'SGI', u'ATI', u'Chromatic Research Inc.', u'Rendition , Inc.', u'3Dfx', u'United States', u'Santa Clara', u'California', u'North Carolina', u'United Stated District Court', u'United States District', u'Jen-Hsun Huang', u'Mark K. Allen', u'Jeffrey D. Fisher', u'Christine B. Hoberg', u'Chris A. Malachowsky', u'Curtis R. Priem', u'Board of Directorssince', u'Huang', u'LSI', u'Advanced Micro Devices', u'Oregon State University', u'Stanford University', u'Allen', u'C-Cube Microsystems', u'Worldwide Manufacturing Operations for Cypress SemiconductorCorp.', u'Purdue University', u'Fisher', u'WeitekCorporation', u'Santa Clara University', u'Hoberg', u'atQuantum Corporation', u'Sun Microsystems , Inc.', u'Malachowskywas', u'Hewlett-Packard Company', u'Sun Microsystems', u'Malachowskyholds', u'University of Florida', u'Priem', u'GenRad , Inc.', u'Vermont Microsystems , Inc.', u'RensselaerPolytechnic Institute']


targetFile = './Demo/Part2.txt'

with open(targetFile, 'r') as myfile:
	text = myfile.read().replace('\n', '')

sent_tokenize_list = sent_tokenize(text)
print "# Sentence Count", len(sent_tokenize_list)

for company in clist:
	result = filter(lambda x: company in x, sent_tokenize_list)
	if len(result) != 0:
		print "# ", company
		print result