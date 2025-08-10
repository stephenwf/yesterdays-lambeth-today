# Process Notes

I think the whole exhibition is driven by the map as a navigation source.

Then each panel is a IIIF Manifest (i.e., an individual exhibition in Delft / ME terms).

Digirati resources:

https://exhibitionviewer.org/docs/creating-exhibitions

https://digirati-workshops.pages.dev/exhibition-building/

https://heritage.tudelft.nl/en/exhibitions

https://leedsunilibrary.exhibitionviewer.org/marie-hartley





## The map

This produces level 0 static tiles.

### Convert PDF to PNG with GhostScript:

https://ghostscript.readthedocs.io/en/gs10.05.1/Use.html

```
gs -dSAFER -dBATCH -dNOPAUSE -sDEVICE=png16m -r400 -sOutputFile='map400.png' '.\84cm x 178.2cm 180g matte_Exhibition Layouts 220823_p1.pdf'
```

(400 dpi)

### Crop the png to remove text and extra whitespace

(Don't need images and panel text in the deep zoom map image itself)


### Create IIIF tiles from PNG using VIPS

```
vips dzsave map.png map --layout iiif

'C:\Program Files\vips\vips-dev-8.17\bin\vips.exe' dzsave '<file>' <name_part> --layout iiif
```

### Now create a Manifest for the map

(in the manifest editor)

## Links in the map

Many of the red entries on the RHS of the map will feature on the "exhibition" panels; these should link into the panels where possible.

This is done with linking annotations.

# Possible TODOs

Allmaps

overlay map / open streetmap tiles

What is the landing page? The map? Or the Intro text?


# Static IIIF

```
.\StaticIIIF.exe 'C:\Users\TomCrane\Dropbox\personal\Lambeth Archives\220825_Exhibition Lambeth Archives 2208\Exhibition Layouts 220823 Folder\Links\09414.jpg' 'C:\git\tomcrane\yesterdays-lambeth-today\iiif-img\09414'
```