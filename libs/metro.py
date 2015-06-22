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

from bs4 import BeautifulSoup
import urllib2

class Metro():

    def lignes(self):
        lignes = []
        soup = BeautifulSoup(urllib2.urlopen('http://www.ratp.fr/meteo/').read())
        for row in soup.find('div', id='inside').find_all('div', class_='lignes')[1].find_all('div', class_='encadre_ligne'):
            idLigne=row['id'].split('_')[2]
            icon='http://www.ratp.fr' + row.img['src']
            infos=row.find('span', class_='perturb_message').text
            lignes.append( { idLigne: { 'icon': icon, 'infos': infos } } )
        return lignes

    def stations(self):
        stations = []
        soup = BeautifulSoup(urllib2.urlopen('http://www.ratp.fr/horaires/fr/ratp/metro').read())
        for row in soup.find('div', id='horMetroStations').find_all('option')[1:]:
            stations.append( { row['value']: row.text } )
        return stations

    def getPassages(self, station, ligne, sens):
        passages = []
        soup = BeautifulSoup(urllib2.urlopen('http://www.ratp.fr/horaires/fr/ratp/metro/prochains_passages/PP/%s/%s/%s' % (station, ligne, sens)).read())
        direction = soup.find_all('span', class_="direction")[0].text
        for row in soup.find('div', id='prochains_passages').find("fieldset").find("table").find_all('tr')[2:4]:
             passages.append(row("td")[1].text)
        return { direction: passages }

    def prochainsPassages(self, station = '', ligne = ''):
        """
        Retourne la liste des 2 prochains passage du metro, dans les 2 sens
        """
        if not station:
            raise ValueError("Le nom de la station ne doit pas etre vide")
        if not ligne:
            raise ValueError("Le numero de la ligne ne doit pas etre vide")
        result = {}
        result.update( self.getPassages(station, ligne, 'A') ) # Aller
        result.update( self.getPassages(station, ligne, 'R') ) # Retour
        return result
    
