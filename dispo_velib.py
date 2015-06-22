#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__  = "Kadda SAHNINE"
__contact__ = "ksahnine@gmail.com"
__license__ = 'GPL v3'

import getopt
import json
import sys
from libs.velib import Velib

def usage():
    """
    Display usage
    """
    sys.stderr.write( "Usage: dispo_velib.py -a <adresse>             | --adresse=<adresse>\n"+
          "                     [-r <rayon_recherche_metres> | --rayon=<rayon_recherche_metres>]\n")

def main(argv):
    # Checks the optional parameters
    adresse=None
    rayon=None

    try:
        opts, args = getopt.getopt(argv, "ha:r:",
                ["help","adresse=","rayon="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        if o in ("-a", "--adresse" ):
            adresse = a
        if o in ("-r", "--rayon" ):
            rayon = int(a)

    if not adresse:
        # adresse obligatoire
        usage()
        sys.exit(0)

    velib = Velib()
    print json.dumps(velib.dispo(adresse, rayon), sort_keys=True, indent=4)

if __name__ == "__main__":
    main(sys.argv[1:])
