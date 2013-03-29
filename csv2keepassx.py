#!/usr/bin/env python
# vim:ts=4:sw=4:ft=python:fileencoding=utf-8
"""Python Template.

This is a template for python.

"""


import sys
import traceback
import logging
import csv
from datetime import datetime
import time


__version__ = 'alpha'


def main():
    """The main function."""
    log = logging.getLogger('main()')
    #log.debug('Printing hello world to screen')
    #print "hello world!"
    csv_name = 'example.csv'
    xml_name = 'example.xml'
    with open(csv_name, 'rb') as csvfile:
        csv_rows = csv.reader(csvfile)
        date_fmt = "%Y-%m-%dT%H:%M:%S"
        with open(xml_name, 'w') as xmlfile:
            xmlfile.write("<!DOCTYPE KEEPASSX_DATABASE>\n")
            xmlfile.write("<database>\n")
            xmlfile.write("  <group>\n")
            xmlfile.write("    <title>imported</title>\n")
            xmlfile.write("    <icon>0</icon>\n")
            for row in csv_rows:
                log.debug(row)
                xmlfile.write("    <entry>\n")
                xmlfile.write("      <title>%s</title>\n" % (row[0]))
                xmlfile.write("      <username>%s</username>\n" % (row[1]))
                xmlfile.write("      <password>%s</password>\n" % (row[2]))
                xmlfile.write("      <url>%s</url>\n" % (row[3]))
                xmlfile.write("      <comment>%s</comment>\n" % (row[4]))
                xmlfile.write("      <icon>0</icon>\n")
                xmlfile.write("      <creation>%s</creation>\n" %
                    (datetime.now().strftime(date_fmt)))
                xmlfile.write("      <lastaccess>%s</lastaccess>\n" %
                    (datetime.now().strftime(date_fmt)))
                xmlfile.write("      <lastmod>%s</lastmod>\n" %
                    (datetime.now().strftime(date_fmt)))
                xmlfile.write("      <expire>Never</expire>\n")
                xmlfile.write("    </entry>\n")
            xmlfile.write("  </group>\n")
            xmlfile.write("</database>\n")


if __name__ == "__main__":
    # DEBUG, WARNING, ERROR, or CRITICAL
    logging.basicConfig(level=logging.WARNING)
    log = logging.getLogger('ifmain')
    try:
        main()
    except KeyboardInterrupt, e:
        # Ctrl-c
        log.error('Received keyboard interupt')
        raise e
    except SystemExit, e:
        # sys.exit()
        log.debug('Received sys.exit()')
        raise e
    except Exception, e:
        log.error("ERROR, UNEXPECTED EXCEPTION")
        log.error(str(e))
        log.error(traceback.format_exc())
        sys.exit(1)
    else:
        # Main function is done, exit cleanly
        sys.exit(0)


