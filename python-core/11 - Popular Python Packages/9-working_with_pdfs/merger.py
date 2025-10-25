import PyPDF2


merger = PyPDF2.PdfMerger()
file_names = ['Resume.pdf', 'rotated.pdf']
for file_name in file_names:
    merger.append(file_name)

merger.write('combined.pdf')
