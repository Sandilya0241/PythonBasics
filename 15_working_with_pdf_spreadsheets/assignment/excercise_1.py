import csv
import PyPDF2
import re

def read_csv_and_download_file():
    '''
    This will read find_the_link.csv file and read the http link and download the pdf file
    '''
    url = ""
    with open("find_the_link.csv",encoding='utf-8') as csv_fp:
        cr = csv.reader(csv_fp,delimiter=",")
        csv_content = list(cr)
        for row_index,line in enumerate(csv_content):
            url += line[row_index]
    print(url)


def read_pdf_find_phone_num():
    pattern = r'(\d{3}.\d{3}.\d{4})'
    with open("Find_the_Phone_Number.pdf","rb") as pr:
        pdf_reader = PyPDF2.PdfReader(pr)
        for page_index in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_index]
            result = re.search(pattern, page.extract_text())
            if result != None:
                print(result.group()) 


if __name__ == "__main__":
    '''
    This is the main method
    '''
    # read_csv_and_download_file()
    read_pdf_find_phone_num()