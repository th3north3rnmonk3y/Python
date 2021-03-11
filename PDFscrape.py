import PyPDF2
import openpyxl

pdffileobj = open('test4.pdf','rb')

pdfReader = PyPDF2.PdfFileReader(pdffileobj)

print(pdfReader.numPages)

pages = (pdfReader.numPages)

for pageNum in range(0, pdfReader.numPages):
         pageObj = pdfReader.getPage(pageNum)
         export = (pageObj.extractText())
         f = open("sample.txt", "a")
         print(export, file=f)
         f.close()

print('Done')

