import PyPDF2
import re
path = "./pdfs/Array.pdf"


def pdf_to_text(path: str):
    text = ""
    with open(path,"rb") as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        for page_i in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_i)
            text+=page.extract_text()
    return text

def get_links(PDF):
    pages = PDF.getNumPages()
    key = '/Annots'
    uri = '/URI'
    ank = '/A'
    links = []
    for page in range(pages):
        pageSliced = PDF.getPage(page)
        pageObject = pageSliced.getObject()
        curr_links = []
        if key in pageObject.keys():
            ann = pageObject[key]
            for a in ann:
                u = a.getObject()
                if uri in u[ank].keys():
                    curr_links.append(u[ank][uri])
        links.append(curr_links)
    return links
        
    
from pprint import pprint
PDFFile = open(path,'rb')

PDF = PyPDF2.PdfFileReader(PDFFile)
pprint(get_links(PDF))

