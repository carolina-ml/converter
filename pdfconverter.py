# pip install pdf2docx

from pdf2docx import Converter
pdf_file = 'prova_oab.pdf'
docx_file = 'prova_oab.docx'
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()
