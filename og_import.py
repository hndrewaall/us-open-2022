#! python3

import csv
from io import StringIO
from pprint import pprint
from sys import base_prefix

from lxml import etree, objectify


def csv_xml():
    with etree.xmlfile("players.xml") as xf:
        with xf.element("Tournament") as tournament:
            with xf.element("Players") as players:
                with open("test.csv") as player_csv:
                    reader = csv.DictReader(player_csv)
                    for row in reader:
                        player = etree.Element("Player", attrib=row)
                        xf.write(player)


def xml_csv():
    tree = etree.parse("usopen2022.xml")
    with open("players.csv", "w") as player_csv:
        writer = csv.DictWriter(player_csv, ["firstName", "name", "rank", "agaId"])
        for player in tree.find("Players"):
            row = {
                "firstName": player.attrib["firstName"],
                "name": player.attrib["name"],
                "rank": player.attrib["rank"],
                "agaId": player.attrib["agaId"],
            }
            writer.writerow(row)


def main():
    # parser = etree.XMLParser(dtd_validation=True)
    # tree = etree.parse("opengotha.xml")
    # with open("opengotha.dtd") as dtd_file:
    #     dtd = etree.DTD(StringIO(dtd_file.read()))
    #     print(dtd.validate(tree))

    # with open("usopen2022.xml", "rb") as tournament_file:
    #     root = objectify.fromstring(tournament_file.read())
    #     print(objectify.dump(root)):
    xml_csv()


if __name__ == "__main__":
    main()
