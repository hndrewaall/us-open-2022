#! python3

import csv
from io import StringIO
from pprint import pprint
from sys import base_prefix

from lxml import etree, objectify


def main():
    # parser = etree.XMLParser(dtd_validation=True)
    # tree = etree.parse("opengotha.xml")
    # with open("opengotha.dtd") as dtd_file:
    #     dtd = etree.DTD(StringIO(dtd_file.read()))
    #     print(dtd.validate(tree))

    # with open("usopen2022.xml", "rb") as tournament_file:
    #     root = objectify.fromstring(tournament_file.read())
    #     print(objectify.dump(root))

    with etree.xmlfile("players.xml") as xf:
        with xf.element("Tournament") as tournament:
            with xf.element("Players") as players:
                with open("test.csv") as player_csv:
                    reader = csv.DictReader(player_csv)
                    for row in reader:
                        player = etree.Element("Player", attrib=row)
                        xf.write(player)


if __name__ == "__main__":
    main()
