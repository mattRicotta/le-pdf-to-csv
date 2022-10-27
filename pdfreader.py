from PyPDF2 import PdfReader
import re
import os

path = '.\\le-files\\'

# Get file(s) from directory
provider = 'predictive'
le_files = []
for file in os.scandir(path):
    if provider in file.name.lower():
       le_files.append(file.path)

# Read first file in list
reader = PdfReader(le_files[0])
page = reader.pages[0]
text = page.extract_text()
lines = text.splitlines()

for i, line in enumerate(lines):
    if line[-1] == ':':
        tag = re.sub(r'\W+', '', line[:-1].upper())
        print('<'+tag+'>'+lines[i+1]+'</'+tag+'>')

# Test 
'''
expected = 'Activity:'
actual = lines[23]
print(expected == actual)
'''

# Write to text file
'''
text_file = open('result.txt', 'w')
text_file.write(text)
text_file.close()
'''