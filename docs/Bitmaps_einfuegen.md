# Bitmaps einfügen


:::{note}
in der ISO 11783-6 werden für VT3/UT2 keine PNG Grafiken unterstützt. 
siehe auch [ISOBUS-Objekte-Versionen](ISOBUS-Objekte-Versionen.md)
:::

## PNG finden

<https://www.iso.org/obp/>

## PNG herunterladen


Rechtsklick auf das Symbol, und Speichern, idealerweise im Ordner: 

C:\git\ms\4diac_training1\Ventilsteuerung\ISO-DesignerProjects\Workspace\DefaultPool\img

andere Ordner sind möglich, aber der Ordnung halber sei dieser empfohlen. 


## PNG in BMP umwandlen

das Bitmap geeigent benennen, die Dateinamen von ISO sind oft wenig aussagekräftig. 
(keine Leerzeichen, keine Umlaute) siehe: <https://docs.ms-muc-docs.de/projects/visual-programming-languages-docs/de/latest/Allgemeines.html#namen>


### Paint

mit Microsoft Paint das in jedem Windows enthlaten ist geht das umwandeln PNG in BMP ganz leicht. 
will man jedoch viele Dateien wandeln, so ist der Aufwand nicht unerheblich. 


### ImageMagick®

<https://imagemagick.org/> kann das umwandeln erleichtern, es wandelt bei Bedarf 100te Bilder mit einem Mausklick. 

<https://imagemagick.org/script/download.php#windows> Download für Windows


unter: 
<https://github.com/Meisterschulen-am-Ostbahnhof-Munchen/4diac_training1/tree/main/Ventilsteuerung/ISO-DesignerProjects/Workspace_TECU/DefaultPool/img/script>

finden Sie ein Script, das, (vorausgesetzt Image Magick ist installiert) 
per Doppelklick folgende Prozesse ausführt: 


Original: 

![image](https://www.iso.org/obp/graphics/grs/343178e8-8b69-4dd7-83c6-cee7c66b28a4_200.png)

von `https://www.iso.org/obp/graphics/grs/343178e8-8b69-4dd7-83c6-cee7c66b28a4_200.png`


#### 1. Alle Dateien unter img_original werden um 2 Pixel ringsum zugeschnitten:

| vorher                                                                                                                                                                                                            |     | nachher                                                                                                                                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![image](https://raw.githubusercontent.com/Meisterschulen-am-Ostbahnhof-Munchen/4diac_training1/main/Ventilsteuerung/ISO-DesignerProjects/Workspace_TECU/DefaultPool/img/img_original/Tractor_wheel_slip_200.png) | --> | ![image](https://raw.githubusercontent.com/Meisterschulen-am-Ostbahnhof-Munchen/4diac_training1/main/Ventilsteuerung/ISO-DesignerProjects/Workspace_TECU/DefaultPool/img/img_cropped/Tractor_wheel_slip_200.png) |
| 200x200                                                                                                                                                                                                           |     | 196x196                                                                                                                                                                                                          |

dadurch werden die 2px großen Schnittmarken von <https://www.iso.org/obp/> entfernt. In der Regel will man die Aufgrund des Erscheinungsbildes nicht haben.

Danach liegen die Zugeschnittenen Bilder unter "img_cropped"


#### 2. Alle Dateien unter img_cropped werden auf 64x64 skaliert

| vorher                                                                                                                                                                                                            |     | nachher                                                                                                                                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![image](https://raw.githubusercontent.com/Meisterschulen-am-Ostbahnhof-Munchen/4diac_training1/main/Ventilsteuerung/ISO-DesignerProjects/Workspace_TECU/DefaultPool/img/img_cropped/Tractor_wheel_slip_200.png) | --> | ![image](https://raw.githubusercontent.com/Meisterschulen-am-Ostbahnhof-Munchen/4diac_training1/main/Ventilsteuerung/ISO-DesignerProjects/Workspace_TECU/DefaultPool/img/img_resized/Tractor_wheel_slip_200.png) |
| 196x196                                                                                                                                                                                                           |     | 94x64                                                                                                                                                                                                          |

Danach liegen die Zugeschnittenen Bilder unter "img_resized"




## BMP Skalieren

die Größe ist wichtig: 


| wo       | Größe       |   |   |   |
|----------|-------------|---|---|---|
| Softkey  | 72x72 pixel |   |   |   |
| Datamask | frei        |   |   |   |
| CCI A3   | 64x64 pixel |   |   |   |

Empfehlung: 
wenn das Symbol als Softkey und als CCI A3 Symbol verwendet werden soll, dann 64x64 Pixel machen. 

Man kann die Bilder vor dem Skalieren auch zuschneiden. 


## BMP Farbtiefe reduzieren

für ein schnelles laden die Farbtiefe so weit als möglich reduzieren. 

Windows Paint bietet folgende Farbtiefen an: 

![image](https://github.com/user-attachments/assets/e8f49c00-4a94-4d6f-b1e2-3ce32dc89c61)


| Format            | Farben                       | Bit | Hinweis                        |
|-------------------|------------------------------|-----|--------------------------------|
| Monochrom-Bitmap  | 2<sup>1</sup> = 2            | 1   |                                |
| 16-Farben-Bitmap  | 2<sup>4</sup> = 16           | 4   |                                |
| 256-Farben-Bitmap | 2<sup>8</sup> = 256          | 8   |                                |
| 24-Bit-Bitmap     | 2<sup>24</sup> = 16.777.216  | 24  | in ISO 11783-6 nicht vorhanden |



## BMP in ISO-Designer einfügen
