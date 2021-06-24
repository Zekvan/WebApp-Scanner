#!/usr/bin/python
# -*- coding: utf-8 -*-

# pip install beautifulsoup4
# apt-get install python-bs4

import urllib.request
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import sys
import time
from . import attacker 
import os 


def crawler(username,target,reportPath):
    urls1, urllist ,urllist2 = [], [], []
    roottarget = target[: (target.find(".com") + 4)]


    f1 = open("./reports/"+username+"/"+reportPath+"/seeds.csv", "w+")
    f = open("./reports/"+username+"/"+reportPath+"/spider1.txt", "w+")
    f.writelines(roottarget  + "\n")
    f1.writelines("{},{},{},{}\n".format("REFERER", "HOST", "METHOD", " PARAMETRELER "))


    newline = {}

    



    def actionsforFirstPage():

        source = urllib.request.urlopen(target).read()
        # print(source)
        soup = BeautifulSoup(source, "html.parser")
        # print(soup)
        for line in soup.find_all("a"):
            newline = line.get("href")
            if newline.find("#") !=  -1:
                newline = newline.split("#")[0]

            try:
                ## if newline started with "http" , newline append in urllist
                if newline[:4] == "http" and newline not in urllist:
                    urllist.append(newline)

                ## if newline started with "/" , newline append as roottarget+newline in urllist
                elif (newline[:1] == "/") and (roottarget + newline not in urllist):
                    urllist.append(roottarget + newline)

                elif (newline[:2] == "./" or newline[:3] == "../") and (roottarget + newline not in urllist):
                    urllist.append(roottarget + newline)

                ## if newline started with another character , nweline append in urllist

            except:
                pass

        linkingPages()
        findingForms()
        removeDuplicatedLines()

    def linkingPages():

        ## every link defined as i
        for i in urllist:


            ## if i start with roottarget. because we dont want other domain
            if i.startswith(roottarget):
                f.writelines(i  + "\n")

                try:
                    source = urllib.request.urlopen(i).read()
                    print(i)
                except:
                	pass
                    
                soup = BeautifulSoup(source, "html.parser")
                ##
                for line in soup.find_all('a'):

                    newline = line.get('href')
                    if newline.find("#") !=  -1:
                        newline = newline.split("#")[0]

                    try:
                        ## if newline started with "http" , newline append in urllist
                        if newline[:4] == "http" and newline not in urllist2:
                            #urllist.append(newline)
                            urllist2.append(newline)

     					## if newline started with "/" , newline append as roottarget+newline in urllist
                        elif newline.startswith("/")  and ((roottarget + newline) not in urllist2):
                            #urllist.append(roottarget + newline)
                            urllist2.append(roottarget + newline)

                        ## if newline started with another character , nweline append in urllist
                        elif newline[:4] != "http"  and  newline.startswith("/") == 0 and ((roottarget + '/' + newline) not in urllist2):
                            #urllist.append(roottarget + '/' + newline+ "\n")
                            urllist2.append(roottarget + '/' + newline)

                    except:
                        pass

        print("urllist2 : ")
        print(urllist2)
        print("urllist : ")
        print(urllist)


    def findingForms():

        for c in urllist2:

            if c.startswith(roottarget):

                if c.find("#") !=  -1:
                    c = c.split("#")[0]

                if c.find("=") != -1:
                    para = c[c.find("?") + 1 : c.find("=")]
                    f1.writelines("{},{},{},{}\n".format(c, c.split("?")[0], "GET", para))

                print(c)
                try:
                    url = urllib.request.urlopen(c).read()
                except:
                    print(c + "  there is not path on the website")
                    pass

                soup = BeautifulSoup(url, "html.parser")

                if soup.find_all("form"):

                    for form in soup.find_all("form"):
                        value = []

                        method = form.get("method")

                        if method.upper() == "POST":

                            act = form.get("action")
                            if act.startswith("/") == 0:
                                forwardpage = c.split("?")[0]+ str(act)
                            else:
                                forwardpage = roottarget +  str(act)


                            for inp in form.find_all("input"):
                                # print( inp)
                                if inp.get("type").lower() == "submit":

                                    pass
                                else:
                                    value.append(inp.get("name"))

                                if "?" in act:
                                    act = act.split("?")[0]

                            f1.writelines("{},{},{}".format(c, forwardpage, "POST"))
                            for b in value:
                                f1.writelines(",{}".format(b))

                        elif method.upper() == "GET":

                            act = form.get("action")
                            if act.startswith("/") == 0:
                                forwardpage = c.split("?")[0]+ str(act)
                            else:
                                forwardpage = roottarget +  str(act)

                            for inp in form.find_all("input"):
                                # print(inp)

                                if inp.get("type").lower() == "submit":
                                    pass
                                else:
                                    value.append(inp.get("name"))

                            f1.writelines("{},{},{}".format(c, forwardpage, "GET"))
                            
                            for b in value:
                                f1.writelines(",{}".format(b))

                        else:
                            print("\n Write non-defined a method\n")
                            print(form.get("method"))

                        f1.writelines("\n")

                else:
                    print(c + "  there is not form.....")

            # for i in urllist:
            #    f.writelines(i + "\n")
        f1.close()


    def removeDuplicatedLines():
        reading_file = open("./reports/"+username+"/"+reportPath+"/seeds.csv", "r")
        reading_eachline = reading_file.read().split("\n")
        res = []
        new_content = "{},{},{},{}".format("REFERER", "HOST", "METHOD", "PARAMETRELER")

        for line in reading_eachline[1:]:

            line00 = line.split(",")

            if line00[1:] not in res:
                res.append(line00[1:])
                new_content+= "\n"+line

        print(new_content)

        writing_file = open("./reports/"+username+"/"+reportPath+"/seeds.csv", "w")
        writing_file.write(new_content)
        writing_file.close()

    actionsforFirstPage()
    attacker.attacker(username,reportPath)


# if __name__ == "__main__":
#     target = "http://php.testsparker.com/hello.php?name=Visitor"
#     username = "testuser"
#     url = urlparse(target)
#     url = url.netloc
#     os.makedirs("./reports/"+username+"/"+url)
#     crawler(username,target,url)

#from attacker import attacker
#attacker()
