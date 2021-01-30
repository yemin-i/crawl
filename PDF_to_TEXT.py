#!/usr/bin/env python
# coding: utf-8

# # PDF to TEXT

# In[2]:


from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# PDFResourceManager : pdf 내의 폰트, 이미지 저장하기 위함
# PDFPageInterpreter : 페이지 내용 번역
from pdfminer.pdfpage import PDFPage  # PDF페이지 관련 처리
from pdfminer.converter import TextConverter # 텍스트 전환 관련 처리
from pdfminer.layout import LAParams  # 페이지 내의 객체 트리 구조 관련 처리
from io import StringIO  # 문자열 데이터를 처리하기 위해 임시 파일 형식으로 만드는 기능(메모리 절약을 위해 하나의 주소에 계속 값을 저장)

def pdf_to_text(inputfile, outputfile):
    # pdf to text 전처리 과정 : PDF 내 각 페이지의 폰트, 이미지 등을 파일로 만든 후, text를 변환 및 번역
    infile = open(inputfile, 'rb')
    resmgr = PDFResourceManager()  
    resdata = StringIO()     
    txt_converter = TextConverter(resmgr, resdata, laparams = LAParams())
    interpreter = PDFPageInterpreter(resmgr, txt_converter)
    
    # pdf의 각 페이지를 txt 작업하기
    for page in PDFPage.get_pages(infile):
        interpreter.process_page(page)
        
    txt = resdata.getvalue() # resdata의 저장된 값을 txt 변수에 저장
    
    # output 파일을 txt 파일로 저장하기
    with open(outputfile, 'w', encoding = 'utf-8') as f:
        f.write(txt)
        
inputfile = 'C:/Users/user/Desktop/포트폴리오_이재성.pdf'
outputfile = 'C:/Users/user/Desktop/포트폴리오_이재성.txt'
pdf_to_text(inputfile, outputfile)


# In[ ]:




