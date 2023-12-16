import re

text = """
data: {am one}
data: {am two}
data: {am three}
"""

all = re.split(':',text,1)

print(all)