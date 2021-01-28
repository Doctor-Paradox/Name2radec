#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 18:34:36 2020

@author: gurpreet
"""
import sys
from astroquery.simbad import Simbad
from astropy import units as u
from astropy.coordinates import SkyCoord
# name=sys.argv[1]
name=' '.join(sys.argv[1:])
# name="capella"
if (name == '-h' or name == '-i'):
    print("----------------------------------------------------------------------------------------------------------------------------------")
    print("This code takes name as input and find its R.A. and Dec. from Simbad using astroquery...")
    print("Converts coordinates : hexadecimal to degrees")
    print("E.g.                         name2radec capella")
    print("----------------------------------------------------------------------------------------------------------------------------------")
else:
    result_table = Simbad.query_object(str(name)) 
    ra=result_table["RA"]
    dec=result_table["DEC"]
    c =SkyCoord(str(ra.data[0])+' '+str(dec.data[0]), unit=(u.hourangle, u.deg))
    print(result_table["MAIN_ID","RA","DEC"])
    print(c)
 #   c_icrs=SkyCoord(ra=c.ra*u.degree, dec=c.dec*u.degree, frame='icrs')
 #   c_fk5 = c_icrs.transform_to('fk5')
 #   print(c_fk5)
