import os

def getVid(name):
    return """
<p>""" + name + """</p>
<img src="yura/""" + name + """" alt="cant display"/>
"""

print("<body>")

for i in os.listdir():
    print(getVid(i))

print("</body")
