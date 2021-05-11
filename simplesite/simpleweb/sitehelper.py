import os

def getVid(name):
    return """
<video width="320" height="240" controls>
  <source src="%s" type="video/mp4">
Your browser does not support the video tag.
</video>"""%name

print("<body>")

for i in os.listdir():
    print(getVid(i))

print("</body")
