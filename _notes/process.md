
### Convert PDF to PNG with GhostScript:

https://ghostscript.readthedocs.io/en/gs10.05.1/Use.html

```
gs -dSAFER -dBATCH -dNOPAUSE -sDEVICE=png16m -r400 -sOutputFile='map400.png' '.\84cm x 178.2cm 180g matte_Exhibition Layouts 220823_p1.pdf'
```

(400 dpi)

### Crop the png to remove text and extra whitespace

(Not required as the text will be carried elsewhere)


### Create IIIF tiles from PNG using VIPS

```
vips dzsave map.png map --layout iiif
```


