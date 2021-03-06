from __future__ import print_function
import xml.etree.ElementTree as ET

"""
XML - looping through nodes
"""
input_string = """
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>"""

stuff = ET.fromstring(input_string)
lst = stuff.findall("users/user")
print("User count:", len(lst))

for item in lst:
    print()
    print("Name", item.find("name").text)
    print("Id", item.find("id").text)
    print("Attribute", item.get("x"))
