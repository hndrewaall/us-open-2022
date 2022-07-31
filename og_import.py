#! python3

from lxml import etree


def main():
    parser = etree.XMLParser(dtd_validation=True)
    tree = etree.parse("opengotha.xml", parser)


if __name__ == "__main__":
    main()
