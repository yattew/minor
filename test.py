from pprint import pprint
import PyPDF2
import re
from typing import List
path = "./pdfs/Array.pdf"


def pdf_to_text(PDF):
    text = ""
    for page_i in range(PDF.numPages):
        page = PDF.getPage(page_i)
        text += page.extract_text()
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


def levels_from_pdf(PDF):
    text = pdf_to_text(PDF).lower()
    # print(text)
    levels_i = [text.find("beginner"),
                text.find("intermediate"),
                text.find("advanced")]
    levels_str = [text[levels_i[0]:levels_i[1]],
                  text[levels_i[1]:levels_i[2]],
                  text[levels_i[2]:]]
    levels = []
    for level_str in levels_str:
        lines: List[str] = level_str.splitlines()
        print(lines)
        data = []
        i = 0
        while i < len(lines):
            line = lines[i]
            if line[0].isnumeric() and line[1] == ".":
                text = lines[i+1]
                data[-1][1].append(text)
            elif line[-1] == ":":
                data.append([line, []])
            else:
                pass  # unrecognised
            i += 1
        levels.append(data)
    return levels


PDFFile = open(path, 'rb')

PDF = PyPDF2.PdfFileReader(PDFFile)
links = get_links(PDF)
level_data = levels_from_pdf(PDF)
pprint(level_data)
