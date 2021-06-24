# WebApp-Scanner

The Web Application Vulnerabilety Scanner is for a Dynamic Application Security Testting which is in Black-Box testing. It has 3 main feature: Crawling, Attacking and Reporting.

### Crawling

In this phase, it collects all pages which are under main domian and saves spider1.txt. After collecting different pages, It looks for parameters which are in form tags and saves them into seeds.csv

### Attacking 

In this phase, it uses 4 different attack engine for Cross-Site Scripting(XSS), SQL injection, Code Injection for PHP, Command Injection for both Operation systems which are Unix and Windows.

For XSS,
it sends payloads one by one with a request from xss.txt(this file includes xss payloads). And it looks for payload in response.  

For SQLi,
it use Time-based SQLi for detection. it sends payloads one by one with a request from sqli.txt(this file includes sqli payloads).And it expects to wait 5 second to receive response.

For Code injection and Command Injection,
it send math problems one by one with different format and it looks for result of the math problem in response.

### Reporting 

it provides a pdf file which includes that vulnerabilites was found. For each vulnerabilite , it provides domain+page,method of request,parameter, payload as well as definition of vulnerabilite , impact and Prevention.


after installing requried modul, run this script in terminal;

`python scanner.py http://php.testsparker.com/hello.php?name=Visitor usertest`

First argument ,http://php.testsparker.com/hello.php?name=Visitor is a website which includes several web application vulnerabile and provided by Netsparker.
Second argument is defition of username. After scanning, your report will be in a file which is with username. Also you can scan several time with same username. the tool will order your scan reports by time.

