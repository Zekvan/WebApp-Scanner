from fpdf import FPDF
import datetime


# domain = "http://php.testsparker.com/artist.php"
# method = "GET"
# parameter = "id"
# payload = "'><sVg/oNload=proMpt(1)>"
# vuln = "SQLi"
# counter=1

class PDF(FPDF):
    def header(self):
        # Logo
        self.image('./assets/logo.png', 5, 0, 52)
        # font
        self.set_font('helvetica', 'B', 30)
        # Title
        self.cell(205, 8, 'Detailed Scan Report', ln=1, align='R')
        # font
        self.set_font('helvetica', 'B', 10)
        # Time of creating report
        x = str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        self.cell(205, 8, x , ln=1, align='R')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Set position of the footer
        self.set_y(-15)
        # set font
        self.set_font('helvetica', 'I', 8)
        # Page number
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')




# Create a PDF object
pdf = PDF('P', 'mm', 'Letter')

# get total page numbers
pdf.alias_nb_pages()

# Set auto page break
pdf.set_auto_page_break(auto = True, margin = 15)

#Add Page
pdf.add_page()
epw = pdf.w - 2*pdf.l_margin

def ReportIt(domain,method,parameter,payload,vuln,counter):
 

    if vuln == "rXSS":
        pdf.set_text_color(255, 255, 255)
        pdf.set_font('helvetica', 'BIU', 16)
        # background color
        pdf.set_fill_color(255, 153, 0)
        # Vulnerability name
        pdf.cell(0, 10, str(counter)+'. Cross-site Scripting(XSS)', ln=1,fill=1)

        # specify font of
        pdf.set_text_color(0, 0, 0)
        pdf.set_font('helvetica', 'B', 12)
        # donaim name of vuln
        pdf.cell(25, 5, "Domain")
        pdf.set_font('helvetica', '', 12)
        pdf.cell(0, 5, ":     "+domain, ln=1)

        # specify font
        pdf.set_font('helvetica', 'B', 12)
        # method name of vuln
        pdf.cell(25, 5, "Method")
        pdf.set_font('helvetica', '', 12)
        pdf.cell(0, 5, ":     "+method, ln=1)

        # specify font
        pdf.set_font('helvetica', 'B', 12)
        # parameter name of vuln
        pdf.cell(25, 5, "Parameter")
        pdf.set_font('helvetica', '', 12)
        pdf.cell(0, 5, ":     "+parameter, ln=1)

        # specify font
        pdf.set_font('helvetica', 'B', 12)
        # payload name of vuln
        pdf.cell(25, 5, "Payload")
        pdf.set_font('helvetica', '', 12)
        pdf.cell(0, 5, ":     "+payload, ln=1)

        # specify font
        pdf.set_font('helvetica', 'BU', 12)
        # payload name of vuln
        pdf.cell(30, 10, "Definition : ", ln =1)

        # specify font
        pdf.set_font('helvetica', '', 12)
        # payload name of vuln
        pdf.multi_cell(0, 5, 'Cross-Site Scripting (XSS) attacks are a type of injection, in which malicious scripts are injected into otherwise benign and trusted websites. XSS attacks occur when an attacker uses a web application to send malicious code, generally in the form of a browser side script, to a different end user. Flaws that allow these attacks to succeed are quite widespread and occur anywhere a web application uses input from a user within the output it generates without validating or encoding it.')

        pdf.set_font('helvetica', 'BU', 12)
        # payload name of vuln
        pdf.cell(30, 10, "Impact : ", ln =1)
        # specify font
        pdf.set_font('helvetica', '', 12)
        # payload name of vuln
        pdf.multi_cell(0, 5, "Cross-site scripting (XSS) vulnerabilities continue to remain a major threat to web applications as attackers exploiting XSS attacks can gain control of the user's account and steal personal information such as passwords, bank account numbers, credit card info, personally identifiable information (PII), social security numbers, and more.")

        pdf.set_font('helvetica', 'BU', 12)
        # payload name of vuln
        pdf.cell(30, 10, "Prevention : ", ln =1)
        # specify font
        pdf.set_font('helvetica', '', 12)
        # payload name of vuln
        pdf.multi_cell(0, 5, 'Output encoding is the primary defense against cross-site scripting vulnerabilities. It is the process of converting untrusted data into a secure form where the input is visible to the user without executing the code in the browser.')

    elif vuln == "SQLi":
        pdf.set_text_color(255, 255, 255)
        pdf.set_font('helvetica', 'BIU', 16)
        # background color
        pdf.set_fill_color(255, 0, 0)
        # Vulnerability name
        pdf.cell(0, 10, str(counter)+'. SQL Injection(SQLi)', ln=1,fill=1)

        # specify font of
        pdf.set_text_color(0, 0, 0)
        pdf.set_font('helvetica', 'B', 12)
        # donaim name of vuln
        pdf.cell(25, 5, "Domain")
        pdf.set_font('helvetica', '', 12)
        pdf.cell(0, 5, ":     "+domain, ln=1)
        # specify font
        pdf.set_font('helvetica', 'B', 12)
        # method name of vuln
        pdf.cell(25, 5, "Method")
        pdf.set_font('helvetica', '', 12)
        pdf.cell(0, 5, ":     "+method, ln=1)
        # specify font
        pdf.set_font('helvetica', 'B', 12)
        # parameter name of vuln
        pdf.cell(25, 5, "Parameter")
        pdf.set_font('helvetica', '', 12)
        pdf.cell(0, 5, ":     "+parameter, ln=1)
        # specify font
        pdf.set_font('helvetica', 'B', 12)
        # payload name of vuln
        pdf.cell(25, 5, "Payload")
        pdf.set_font('helvetica', '', 12)
        pdf.cell(0, 5, ":     "+payload, ln=1)
        # specify font
        pdf.set_font('helvetica', 'BU', 12)
        # payload name of vuln
        pdf.cell(30, 10, "Definition : ", ln =1)
        # specify font
        pdf.set_font('helvetica', '', 12)
        # payload name of vuln
        pdf.multi_cell(0, 5, 'SQL injection, also known as SQLI, is a common attack vector that uses malicious SQL code for backend database manipulation to access information that was not intended to be displayed. This information may include any number of items, including sensitive company data, user lists or private customer details.')

        pdf.set_font('helvetica', 'BU', 12)
        # payload name of vuln
        pdf.cell(30, 10, "Impact : ", ln =1)
        # specify font
        pdf.set_font('helvetica', '', 12)
        # payload name of vuln
        pdf.multi_cell(0, 5, "Depending on the backend database, the database connection settings, and the operating system, an attacker can mount one or more of the following attacks successfully:\n- Reading, updating and deleting arbitrary data or tables from the database\n- Executing commands on the underlying operating system")

        pdf.set_font('helvetica', 'BU', 12)
        # payload name of vuln
        pdf.cell(30, 10, "Prevention : ", ln =1)
        # specify font
        pdf.set_font('helvetica', '', 12)
        # payload name of vuln
        pdf.multi_cell(0, 5, 'A robust method for mitigating the threat of SQL injection-based vulnerabilities is to use parameterized queries (prepared statements). Almost all modern languages provide built-in libraries for this. Wherever possible, do not create dynamic SQL queries or SQL queries with string concatenation.')

    elif vuln == "PHPCodeEx":
        pdf.set_text_color(255, 255, 255)
        pdf.set_font('helvetica', 'BIU', 16)
        # background color
        pdf.set_fill_color(255, 0, 0)
        # Vulnerability name
        pdf.cell(0, 10, str(counter)+'. Code Execution(PHP)', ln=1,fill=1)

        # specify font of
        pdf.set_text_color(0, 0, 0)
        pdf.set_font('helvetica', 'B', 12)
        # donaim name of vuln
        pdf.cell(25, 5, "Domain")
        pdf.set_font('helvetica', '', 12)
        pdf.cell(0, 5, ":     "+domain, ln=1)
        # specify font
        pdf.set_font('helvetica', 'B', 12)
        # method name of vuln
        pdf.cell(25, 5, "Method")
        pdf.set_font('helvetica', '', 12)
        pdf.cell(0, 5, ":     "+method, ln=1)
        # specify font
        pdf.set_font('helvetica', 'B', 12)
        # parameter name of vuln
        pdf.cell(25, 5, "Parameter")
        pdf.set_font('helvetica', '', 12)
        pdf.cell(0, 5, ":     "+parameter, ln=1)
        # specify font
        pdf.set_font('helvetica', 'B', 12)
        # payload name of vuln
        pdf.cell(25, 5, "Payload")
        pdf.set_font('helvetica', '', 12)
        pdf.cell(0, 5, ":     "+payload, ln=1)
        # specify font
        pdf.set_font('helvetica', 'BU', 12)
        # payload name of vuln
        pdf.cell(30, 10, "Definition : ", ln =1)
        # specify font
        pdf.set_font('helvetica', '', 12)
        # payload name of vuln
        pdf.multi_cell(0, 5, "Remote Code Evaluation is a vulnerability that can be exploited if user input is injected into a File or a String and executed (evaluated) by the programming language's parser. Usually this behavior is not intended by the developer of the web application. A Remote Code Evaluation can lead to a full compromise of the vulnerable web application and also web server. It is important to note that almost every programming language has code evaluation functions.")

        pdf.set_font('helvetica', 'BU', 12)
        # payload name of vuln
        pdf.cell(30, 10, "Impact : ", ln =1)
        # specify font
        pdf.set_font('helvetica', '', 12)
        # payload name of vuln
        pdf.multi_cell(0, 5, "An attacker can execute arbitrary PHP code on the system. The attacker may also be able to execute arbitrary system commands.")

        pdf.set_font('helvetica', 'BU', 12)
        # payload name of vuln
        pdf.cell(30, 10, "Prevention : ", ln =1)
        # specify font
        pdf.set_font('helvetica', '', 12)
        # payload name of vuln
        pdf.multi_cell(0, 5, 'Do not accept input from end users which will be directly interpreted as source code. If this is a business requirement, validate all input to the application by removing any data that could be directly interpreted as PHP source code.')

    elif vuln == "CommandInj":
        pdf.set_text_color(255, 255, 255)
        pdf.set_font('helvetica', 'BIU', 16)
        # background color
        pdf.set_fill_color(255, 0, 0)
        # Vulnerability name
        pdf.cell(0, 10, str(counter)+'. Command Injection', ln=1,fill=1)

        # specify font of
        pdf.set_text_color(0, 0, 0)
        pdf.set_font('helvetica', 'B', 12)
        # donaim name of vuln
        pdf.cell(25, 5, "Domain")
        pdf.set_font('helvetica', '', 12)
        pdf.cell(0, 5, ":     "+domain, ln=1)
        # specify font
        pdf.set_font('helvetica', 'B', 12)
        # method name of vuln
        pdf.cell(25, 5, "Method")
        pdf.set_font('helvetica', '', 12)
        pdf.cell(0, 5, ":     "+method, ln=1)
        # specify font
        pdf.set_font('helvetica', 'B', 12)
        # parameter name of vuln
        pdf.cell(25, 5, "Parameter")
        pdf.set_font('helvetica', '', 12)
        pdf.cell(0, 5, ":     "+parameter, ln=1)
        # specify font
        pdf.set_font('helvetica', 'B', 12)
        # payload name of vuln
        pdf.cell(25, 5, "Payload")
        pdf.set_font('helvetica', '', 12)
        pdf.cell(0, 5, ":     "+payload, ln=1)
        # specify font
        pdf.set_font('helvetica', 'BU', 12)
        # payload name of vuln
        pdf.cell(30, 10, "Definition : ", ln =1)
        # specify font
        pdf.set_font('helvetica', '', 12)
        # payload name of vuln
        pdf.multi_cell(0, 5, 'OS command injection (also known as shell injection) is a web security vulnerability that allows an attacker to execute arbitrary operating system (OS) commands on the server that is running an application, and typically fully compromise the application and all its data.')

        pdf.set_font('helvetica', 'BU', 12)
        # payload name of vuln
        pdf.cell(30, 10, "Impact : ", ln =1)
        # specify font
        pdf.set_font('helvetica', '', 12)
        # payload name of vuln
        pdf.multi_cell(0, 5, "Once attackers have gained control of a server, they can use the underlying application to exploit any and all capabilities built into the software. The resulting damage is determined by the user authorizations and security protections an organization has in place. What's more, attackers may retain access to systems even after an organization has detected and fixed the underlying vulnerability.")

        pdf.set_font('helvetica', 'BU', 12)
        # payload name of vuln
        pdf.cell(30, 10, "Prevention : ", ln =1)
        # specify font
        pdf.set_font('helvetica', '', 12)
        # payload name of vuln
        pdf.multi_cell(0, 5, 'In order to prevent an attacker from exploiting a vulnerable web application and inserting special characters into the operating system command, you should try to generally avoid system calls where possible. In all cases, avoid user input of any kind unless it is absolutely necessary. And if it is necessary, make sure there is proper input validation in place - input validation is always a must to ensure your web application code is not vulnerable to other high-impact vulnerabilities, ')

    return pdf

# def test(domain,method,parameter,payload,vuln):

#     counter=1
#     ReportIt(domain,method,parameter,payload,vuln,counter)
#     counter=2
#     ReportIt(domain,method,parameter,payload,vuln,counter)
#     return pdf.output('pdf_2.pdf')

# test(domain,method,parameter,payload,vuln)