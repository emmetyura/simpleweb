import os

def getVid(name):
    return """
<p>""" + name + """</p>
<video width="720" height="720" controls>
  <source src="emmet/""" + name + """" type="video/mp4">
Your browser does not support the video tag.
</video>"""

print("<body>")

for i in os.listdir():
    print(getVid(i))

print("</body")
