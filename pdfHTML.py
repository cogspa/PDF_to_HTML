import PyPDF2
from bs4 import BeautifulSoup

pdf_file = open('TBA0150.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

text = ''
for page in range(pdf_reader.numPages):
    text += pdf_reader.pages[page].extract_text()

html_template = """
<!DOCTYPE html>
<html>
<head>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<style>
		body {
			margin: 0;
			padding: 0;
			display: grid;
			grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
			grid-gap: 20px;
		}

		.item {
			background-color: #f2f2f2;
			padding: 20px;
			text-align: center;
			font-size: 30px;
		}
	</style>
</head>
<body>
	{}
</body>
</html>
"""

soup = BeautifulSoup(text, features="html.parser")
items = soup.find_all()

item_html = ""
for item in items:
    item_html += str(item)

html = html_template.format(item_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
