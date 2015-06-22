#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__  = "Kadda SAHNINE"
__contact__ = "ksahnine@gmail.com"
__license__ = 'GPL v3'

import getopt
import sys
import json
from libs.metro import Metro

def usage():
    """
    Display usage
    """
    sys.stderr.write( "Usage: passages_metro.py [-S           | --reseau-stations]\n"+
          "                         [-L           | --reseau-lignes]\n"+
          "                         -s <station>  | --station=<station>\n"+
          "                         -l <ligne>    | --ligne=<ligne>\n")

def main(argv):
    m = Metro()

    # Checks the optional parameters
    try:
        opts, args = getopt.getopt(argv, "hSLs:l:",
                     ["help","reseau-stations","reseau-lignes","station=","ligne="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        if o in ("-S", "--reseau-stations" ):
            print json.dumps(m.stations(), sort_keys=True, indent=4)
            sys.exit(0)
        if o in ("-L", "--reseau-lignes" ):
            print json.dumps(m.lignes(), sort_keys=True, indent=4)
            sys.exit(0)
        if o in ("-s", "--station" ):
            station = a
        if o in ("-l", "--ligne" ):
            ligne = a

    if len(argv) != 4:
        usage()
        sys.exit(0)

    print json.dumps(m.prochainsPassages(station, ligne), sort_keys=True, indent=4)

if __name__ == "__main__":
    main(sys.argv[1:])
