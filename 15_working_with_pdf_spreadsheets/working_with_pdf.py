import PyPDF2

def read_pdf_file():
    with open("Working_Business_Proposal.pdf","rb") as pdf_reader:
        pr = PyPDF2.PdfReader(pdf_reader)
        # print(len(pr.pages))
        page1 = pr.pages[0]
        page1_text = page1.extract_text()
        print(page1_text)


def write_pdf_file():
    with open("Working_Business_Proposal.pdf","rb") as p_reader:
        pdf_reader = PyPDF2.PdfReader(p_reader)
        first_page = pdf_reader.pages[0]
        print(type(first_page))
        pdf_writer = PyPDF2.PdfWriter()
        pdf_writer.add_page(first_page)
        with open("New_document.pdf","wb") as pdf_output:
            pdf_writer.write(pdf_output)


def read_pdf_file2():
    pdf_content = []
    with open("Working_Business_Proposal.pdf","rb") as pdf_reader:
        pr = PyPDF2.PdfReader(pdf_reader)
        for page_num in range(len(pr.pages)):
            page = pr.pages[page_num]
            pdf_content.append(page.extract_text())
    print(f'Page 1 contents is \n {pdf_content[0]}')
    print(f'Page 2 contents is \n {pdf_content[1]}')


if __name__ == "__main__":
    # read_pdf_file()
    # write_pdf_file()
    read_pdf_file2()