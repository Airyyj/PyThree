from xml.dom import minidom

#打开xml
#parse()解析，打开xml文件
dom = minidom.parse('info.xml')

#得到文档元素对象
root = dom.documentElement

print(root.nodeName)
print(root.nodeValue)
print(root.nodeType)
print(root.ELEMENT_NODE)

#获取标签
#getElementsByTagName()可以获得指定标签名的一组标签。
browser = root.getElementsByTagName('browser')
print(browser[0].tagName)

login = root.getElementsByTagName('login')
print(login[0].tagName)
print(login[1].tagName)

province = root.getElementsByTagName('province')
print(province[0].tagName)

#获取标签的属性值
#getAttribute()方法用于获取元素的属性值 和webdriver 的 get_attribute()方法相似
username = login[0].getAttribute("username")
print(username)
password = login[0].getAttribute("password")
print(password)

#获取标签对之间的数据
#获取第一个province标签对的值
#firstChild 属性返回被选节点的第一个子节点。data 表示获取该节点的数据，与webdriver 中的text方法相似。
province1 = province[0].firstChild.data
print(province1)
