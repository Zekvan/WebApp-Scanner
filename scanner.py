from fpdf import FPDF
from urllib.parse import urlparse
import os
import sys
from scanner import crawler
from scanner import attacker
from scanner import reporter
import time




def scanner(target,username):

	#target = "http://php.testsparker.com/hello.php?name=Visitor"
	#username = "testuser1"
	url = urlparse(target)
	url = url.netloc
	test = int(time.time())
	reportPath = url +"-"+ str(test)
	os.makedirs("./reports/"+username+"/"+reportPath)
	crawler.crawler(username,target,reportPath)


target = sys.argv[1]
username = sys.argv[2]
scanner(target,username)