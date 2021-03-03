#!/usr/bin/env python3

import pyora
import xml.etree.ElementTree as xmlT
from PIL import Image, ImageDraw, ImageFont
import os.path

def placeholderCallback(p: str):
    print("ORIGINIZER:",p)

def originize( ifpng: str, ifxml: str, ofora: str, _progressCallback=placeholderCallback ):

    _progressCallback("Loading image...")
    inimage = Image.open( ifpng )

    _progressCallback("Initializing pyora project...")
    ora = pyora.Project.new( *inimage.size )
    ora.add_layer( inimage, os.path.basename(ifpng) )

    _progressCallback("Creating overlay...")
    overlay = Image.new('RGBA', inimage.size)
    overlayDraw = ImageDraw.Draw(overlay)

    _progressCallback("Loading XML...")
    xmld = xmlT.parse( ifxml ).getroot()

    _progressCallback("Drawing overlay...")
    for SubTexture in xmld:
        
        if SubTexture.tag != "SubTexture": continue
        sta = SubTexture.attrib
        
        if "name" in sta:
            overlayDraw.text(
                ( int(sta['x'])+8, int(sta['y'])+8 ),
                sta["name"],
                fill=(255,0,0,255)
            )
        
        w = int(sta['width']); h = int(sta['height'])
        x1 = int(sta['x']); y1 = int(sta['y'])
        x2 = x1+w; y2 = y1+h
        
        overlayDraw.rectangle(
            [( x1,y1 ), ( x2,y2 )],
            width=1,
            outline=(255,0,0,255)
        )
        
        if ("frameX" in sta) and ("frameY" in sta):
            
            ox = int(sta['frameX']); oy = int(sta['frameY'])
            
            overlayDraw.line(
                [(x2-(w/2), y2), (x2-(w/2)+ox, y2+oy)],
                width=1,
                fill=(255,0,0,255)
            )

    _progressCallback("Adding overlay...")
    ora.add_layer( overlay, "FNF Originizer Overlay" )

    _progressCallback("Saving .ora... (this may take about 30 sec.)")
    ora.save( ofora )
