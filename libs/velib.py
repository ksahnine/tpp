#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

__author__  = "Kadda SAHNINE"
__contact__ = "ksahnine@gmail.com"
__license__ = 'GPL v3'

import xml.etree.ElementTree as ET
import urllib
import urllib2
import sys
import getopt
import geopy
import geopy.distance

class Velib():

    def dispo(self, adresse = '', rayon = None):
        """
        Retourne une liste des stations dans le rayon de la position passee en parametre
        Le rayon est exprime en metres
        """
        if not adresse:
            raise ValueError("L'adresse ne doit pas etre vide")
        if not rayon:
            rayon = 270

        stations = dict()
        result = {}
        t = ET.parse(urllib2.urlopen("http://www.velib.paris/service/carto"))
        r = t.getroot()
    
        for c in r.findall(".//marker[@open='1']"):
            loc = geopy.Point( float(c.attrib['lat']), float(c.attrib['lng']))
            stations[loc] = {'name': c.attrib['name'], 'id': c.attrib['number']}
    
        pos = self.coordLatLng(adresse)
        stationsProches = [pt for pt in stations.keys() if geopy.distance.distance(pos, pt).m < rayon]
        for s in stationsProches:
            result[stations[s]['name'].split(' - ')[1]] = self.nbVelosDispos(stations[s]['id'])

        return result
    
    def coordLatLng(self, adresse):
        """
        Retourne les coordonnees geographiques (lat, lng) de l'adresse passee en parametre
        """
        param = urllib.urlencode({'address': adresse})
        t = ET.parse(urllib2.urlopen("https://maps.googleapis.com/maps/api/geocode/xml?address=%s" % param))
        r = t.getroot()
        status = r[0].text
        if status != 'OK':
            raise ValueError("Impossible de localiser l'adresse. Error code: %s" % status)
        lat = r.findall(".//location/lat")[0].text
        lng = r.findall(".//location/lng")[0].text
        return geopy.Point(float(lat), float(lng))
    
    def nbVelosDispos(self, stationId):
        """
        Retourne le nombre de velibs disponibles dans la station dont l'id est passe en parametre
        """
        t = ET.parse(urllib2.urlopen("http://www.velib.paris/service/stationdetails/paris/%s" % stationId))
        r = t.getroot()
        return int(r[0].text)
