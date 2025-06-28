# Process Notes

I think the whole exhibition is driven by the map as a navigation source.

Then each panel is a IIIF Manifest (i.e., an individual exhibition in Delft / ME terms).


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
```

### Now create a Manifest for the map

(in the manifest editor)

## Links in the map

Many of the red entries on the RHS of the map will feature on the "exhibition" panels; these should link into the panels where possible.

This is done with linking annotations.

