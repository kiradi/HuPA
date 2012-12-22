import elementtree.ElementTree as ET
tree = ET.parse('test.xml')

root = tree.getroot()

for element in root.getchildren():
	print element.tag
	for child in element.getchildren():
		print child.tag,child.text
		if child.tag == "DateCreated":
			for ch in child.getchildren():
				print ch.tag,ch.text


