from xml.dom import minidom

dom = minidom.parse('info.xml')

gen = dom.documentElement

provinces = gen.getElementsByTagName('province')
citys     = gen.getElementsByTagName('city')
p1 = provinces[0].firstChild.data
p2 = citys[1].firstChild.data
print(p1)
print(p2)