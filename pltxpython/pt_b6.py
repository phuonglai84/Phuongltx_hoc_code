# from os import replace
# import docx2txt


# filename = "text.txt"
# file = open("d:\\Learning\\Python\\Phuongltx_hoc_code\\pltxpython/" + filename, 'r')
# content = file.read()
# content_new = content.replace(".","")
# print(content_new)

from docx import Document

document = Document('d:\\Learning\\Python\\Phuongltx_hoc_code\\pltxpython/small.docx')
allText = []
for para in document.paragraphs:
    para_text = para.text.lower()
    word = para_text.split()
    allText.extend(word)
    allText2 = sorted(allText)

# print(allText)
# print(sorted(allText))

d={}
for i in allText2:
    allText2.count(i)
    d[i] = allText2.count(i)
print(d)

for j in d.keys():
    print(j, "", d[j])