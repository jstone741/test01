#_*_ coding: utf-8 _*_

import requests
import random
import multiprocessing
import sys
import time
import psutil
import os
import urllib.parse
import xml.etree.ElementTree as elemTree


#ipLST = []
#urlLST = []

#fhr = open('/home/blacktiger/tving_mp4_precache/python_smil/iplist.txt', 'r')
#for line in fhr.readlines():
#        line = line.strip()
#        if line == '':
#                continue
#        ipLST.append(line)
#fhr.close()

#fhr = open('/home/blacktiger/tving_mp4_precache/python_smil/filelist.txt', 'r')
#for line in fhr.readlines():
#        line = line.strip()
#        if line == '':
#                continue
#        urlLST.append(line)
#fhr.close()


tree = elemTree.parse('D:/github_Root_Folder/python/json/vhosts.xml')

root = tree.getroot()


print (tree)
print (root)
#print(root.tag)
#print(root.attrib)

print(root[0][2])

for child in root:
        print(child.tag, child.attrib)
test