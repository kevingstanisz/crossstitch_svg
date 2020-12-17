import xml.etree.ElementTree
import math

# Open original file
tree = xml.etree.ElementTree.parse('test1.svg')
root = tree.getroot()

for child in root.findall('{http://www.w3.org/2000/svg}g[@id="Grid"]/'):
	gridSize = float(child.attrib.get('width'))
	print(gridSize)
	break;



class Diag(object):
    x1 = 0
    x2 = 0
    y1 = 0
    x2 = 0

    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2


class TrianglePoints(object):
    point1_1 = 0
    point1_2 = 0
    point2_1 = 0
    point2_2 = 0
    point3_1 = 0
    point3_2 = 0

    def __init__(self, shortDiag, longDiag):
    	point1_1 = 0
        


longDiagArr = []
shortDiagArr = []

shortdiags = 0

for child in root.findall('{http://www.w3.org/2000/svg}g[@id="Custom_lines"]/'):
	x1 = float(child.attrib.get('x1'))
	x2 = float(child.attrib.get('x2'))
	y1 = float(child.attrib.get('y1'))
	y2 = float(child.attrib.get('y2'))

	pythag = math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))

	if pythag > gridSize:
		longDiag = Diag(x1, x2, y1, y2)
		longDiagArr.append(longDiag)
	elif pythag < gridSize:
		shortdiags += 1
		shortDiag = Diag(x1, x2, y1, y2)
		shortDiagArr.append(shortDiag)




halfStitchArr = []

matchesfound = 0

for shortDiag in shortDiagArr:
    for longDiag in longDiagArr:
    	if ((shortDiag.x1 > longDiag.x1 or shortDiag.x1 > longDiag.x2 or shortDiag.x2 > longDiag.x1 or shortDiag.x2 > longDiag.x2) 
    	and (shortDiag.y1 > longDiag.y1 or shortDiag.y1 > longDiag.y2 or shortDiag.y2 > longDiag.y1 or shortDiag.y2 > longDiag.y2) 
    	and (shortDiag.x1 < longDiag.x1 or shortDiag.x1 < longDiag.x2 or shortDiag.x2 < longDiag.x1 or shortDiag.x2 < longDiag.x2) 
    	and (shortDiag.y1 < longDiag.y1 or shortDiag.y1 < longDiag.y2 or shortDiag.y2 < longDiag.y1 or shortDiag.y2 < longDiag.y2)):
    		matchesfound += 1
    		halfStitch = TrianglePoints(shortDiag, longDiag)



print(shortdiags)
print(matchesfound)




# # Append new tag: <a x='1' y='abc'>body text</a>
# new_tag = xml.etree.ElementTree.SubElement(et.getroot(), 'a')
# new_tag.text = 'body text'
# new_tag.attrib['x'] = '1' # must be str; cannot be an int
# new_tag.attrib['y'] = 'abc'

# # Write back to file
# #et.write('file.xml')
# et.write('file_new.xml')