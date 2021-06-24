import requests
from urllib3 import response
from requests.exceptions import Timeout
import time
from . import reporter 
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(4)




counter = 0

def attacker(username,Path):

    reading_file=open("./reports/"+username+"/"+Path+"/seeds.csv","r")
    reading_eachline = reading_file.read().split("\n")
    for line in reading_eachline[1:-1]:

        line00= line.split(",",3)
        print("-------------------------------------")
        print(line00)
        print(line00[1]+line00[2]+line00[3])

        url_from_seeds = line00[1]
        method_from_seeds = line00[2]
        parameters_from_seeds = line00[3]


        XSSengine(url_from_seeds,method_from_seeds,parameters_from_seeds) 
        SQLiengine(url_from_seeds,method_from_seeds,parameters_from_seeds)
        PHPCodeExEngine(url_from_seeds,method_from_seeds,parameters_from_seeds)
        CommandiEngine(url_from_seeds,method_from_seeds,parameters_from_seeds)

    return reporter.pdf.output("./reports/"+username+"/"+Path+"/Detailed-Scan-Report.pdf")


def XSSengine(domain,method,parameters):
	
    XSSpayloads = open("./scanner/payloads/xss.txt", "r").read().split("\n")
    parameters = parameters.split(",")
    global counter
    vuln = "rXSS"
    print("-------------------------------------")

    for payload in XSSpayloads:
        #print "2"
        print(payload)
        print(domain)
        print(method)
        data = {}
        for j in range(len(parameters)):
            #print "3"
            print (parameters[j])
            data[parameters[j]] = payload
            if method == "GET":
                r = requests.get(domain, data)
                if str(payload) in r.text:
                    # report.write("Cross-Site Scripting\n")
                    # report.write("------------------------------\n")
                    # report.write("Domain: "+domain+"\n")
                    # report.write("Parameter: "+parameters[j]+"\n")
                    # report.write("Payload: "+payload+"\n")
                    # report.write("******************************\r\n")
                    print("############# I Found it ###############")
                    print(r)
                    print(domain)
                    counter +=1
                    reporter.ReportIt(domain,method,parameters[j],payload,vuln,counter)
            elif method == "POST":
                r = requests.post(domain, data)
                if payload in r.text:
                    # report.write("Cross-Site Scripting\n")
                    # report.write("------------------------------\n")
                    # report.write("Domain: "+domain+"\n")
                    # report.write("Parameter: "+parameters[j]+"\n")
                    # report.write("Payload: "+payload+"\n")
                    # report.write("******************************\r\n")
                    print("############# I Found it ###############")
                    print(r)
                    print(domain)
                    counter +=1
                    reporter.ReportIt(domain,method,parameters[j],payload,vuln,counter)
    return reporter.pdf


def SQLiengine(domain,method,parameters):
    SQLipayloads = open("./scanner/payloads/sqli.txt", "r").read().split("\n")
    global counter
    vuln = "SQLi"
    parameters = parameters.split(",")
	
    print("-------------------------------------")
    for payload in SQLipayloads:
        print(parameters)
        
        print(parameters)
        print(payload)
        print(domain)
        print(method)
        data = {}
        for j in range(len(parameters)):

            data[parameters[j]] = payload

            if method == "GET":
                try:
                    r = requests.get(domain, data,timeout=5)
                except Timeout:
                    # report.write("SQL Injection\n")
                    # report.write("------------------------------\n")
                    # report.write("Domain: "+domain+"\n")
                    # report.write("Parameter: "+parameters[j]+"\n")
                    # report.write("Payload: "+payload+"\n")
                    # report.write("******************************\r\n")
                    print("############# I Found it ###############")
                    print(r)
                    print(domain)
                    counter +=1
                    reporter.ReportIt(domain,method,parameters[j],payload,vuln,counter)
                    return reporter.pdf
            elif method == "POST":
                try:
                    r = requests.post(domain, data,timeout=5)
                    print(data)
                except Timeout:
                    # report.write("SQL Injection\n")
                    # report.write("------------------------------\n")
                    # report.write("Domain: "+domain+"\n")
                    # report.write("Parameter: "+parameters[j]+"\n")
                    # report.write("Payload: "+payload+"\n")
                    # report.write("******************************\r\n")
                    print("############# I Found it ###############")
                    print(r)
                    print(domain)
                    counter +=1
                    reporter.ReportIt(domain,method,parameters[j],payload,vuln,counter)
                    return reporter.pdf

def PHPCodeExEngine(domain,method,parameters):
    CodePayloads = open("./scanner/payloads/CodeE.txt", "r").read().split("\n")
    global counter
    vuln = "PHPCodeEx"
    parameters = parameters.split(",")
    print("-------------------------------------")
    for payload in CodePayloads:
        print(parameters)
        print(payload)
        print(domain)
        print(method)
        data = {}
        for j in range(len(parameters)):

            data[parameters[j]] = payload
            if method == "GET":
                r = requests.get(domain, data)
                print(r.request)
                if "98734" in r.text:
                    # report.write("Code Evaluation\n")
                    # report.write("------------------------------\n")
                    # report.write("Domain: "+domain+"\n")
                    # report.write("Parameter: "+parameters[j]+"\n")
                    # report.write("Payload: "+payload+"\n")
                    # report.write("******************************\r\n")
                    print("############# I Found it ###############")
                    print(r)
                    print(domain)
                    counter +=1
                    reporter.ReportIt(domain,method,parameters[j],payload,vuln,counter)
            elif method == "POST":
                r = requests.post(domain, data)
                if "98734" in r.text:
                    # report.write("Code Evaluation\n")
                    # report.write("------------------------------\n")
                    # report.write("Domain: "+domain+"\n")
                    # report.write("Parameter: "+parameters[j]+"\n")
                    # report.write("Payload: "+payload+"\n")
                    # report.write("******************************\r\n")
                    print("############# I Found it ###############")
                    print(r)
                    print(domain)
                    counter +=1
                    reporter.ReportIt(domain,method,parameters[j],payload,vuln,counter)
    return reporter.pdf

def CommandiEngine(domain,method,parameters):
    CommandPayloads = open("./scanner/payloads/CommandI.txt", "r").read().split("\n")
    global counter
    vuln = "CommandInj"
    parameters = parameters.split(",")
    print("-------------------------------------")
    for payload in CommandPayloads:

        print(payload)
        data = {}
        for j in range(len(parameters)):

            data[parameters[j]] = payload
            print(data)
            if method == "GET":
                r = requests.get(domain, data)
                if "98733" in r.text:
                    # report.write("Command Injection\n")
                    # report.write("------------------------------\n")
                    # report.write("Domain: "+domain+"\n")
                    # report.write("Parameter: "+parameters[j]+"\n")
                    # report.write("Payload: "+payload+"\n")
                    # report.write("******************************\r\n")
                    print("############# I Found it ###############")
                    print(r)
                    print(domain)
                    counter +=1
                    reporter.ReportIt(domain,method,parameters[j],payload,vuln,counter)
            elif method == "POST":
                r = requests.post(domain, data)
                if "98733" in r.text:
                    # report.write("Command Injection\n")
                    # report.write("------------------------------\n")
                    # report.write("Domain: "+domain+"\n")
                    # report.write("Parameter: "+parameters[j]+"\n")
                    # report.write("Payload: "+payload+"\n")
                    # report.write("******************************\r\n")
                    print("############# I Found it ###############")
                    print(r)
                    print(domain)
                    counter +=1
                    reporter.ReportIt(domain,method,parameters[j],payload,vuln,counter)
    return reporter.pdf


