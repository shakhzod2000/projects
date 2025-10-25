import PyPDF2

# 'rb' = read in binary
with open('Resume.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    print(len(reader.pages))
    page = reader.pages[0]
    page.rotate(90)
    writer = PyPDF2.PdfWriter()
    writer.add_page(page) # add page at end of PDF
    writer.insert_page(page, index=0) # insert at specific page index
    writer.insert_blank_page()
    with open('rotated.pdf', 'wb') as output:
        writer.write(output)
