"""
    pdfminer is able to extract both text and images.
    But only text extraction with this library is demonstrated
"""

import re   #   used to find certain string patterns for manipulation of data
from pdfminer.high_level import extract_pages, extract_text

#   prints all the elements
# for page_layout in extract_pages("./res/test.pdf"):
#     for element in page_layout:
#         print(element)


text = extract_text("./res/test.pdf")
print(text)
with open("pdfminer-test_text.txt", "w") as wfs:
    wfs.write(text)

"""
    The below regular expression means:
        any letter either uppercase or lowercase followed
        by exactly one comma and followed by exactly one space 
"""
pattern = re.compile(r"[a-zA-Z]+,{1}\s{1}")
#   finds text that match the above pattern
matches = pattern.findall(text)
# print(matches)
#   the below prints out the text that match the patterns, excluding the comma hence the slice operator [::]
names = [n[:-2] for n in matches]