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







## ImageMagick®

<https://imagemagick.org/> kann das umwandeln erleichtern, es wandelt bei Bedarf 100te Bilder mit einem Mausklick. 

<https://imagemagick.org/script/download.php#windows> Download für Windows


unter: 
<https://github.com/Meisterschulen-am-Ostbahnhof-Munchen/4diac_training1/tree/main/Ventilsteuerung/ISO-DesignerProjects/Workspace_TECU/DefaultPool/img/script>

finden Sie ein Script, das, (vorausgesetzt Image Magick ist installiert) 
per Doppelklick folgende Prozesse ausführt: 


Original: 

![image](https://www.iso.org/obp/graphics/grs/343178e8-8b69-4dd7-83c6-cee7c66b28a4_200.png)

von `https://www.iso.org/obp/graphics/grs/343178e8-8b69-4dd7-83c6-cee7c66b28a4_200.png`


### 1. Alle Dateien unter img_original werden um 2 Pixel ringsum zugeschnitten:


zum Ordner: [img_original](https://github.com/Meisterschulen-am-Ostbahnhof-Munchen/4diac_training1/tree/main/Ventilsteuerung/ISO-DesignerProjects/Workspace_TECU/DefaultPool/img/img_original)


| vorher                                                                                                                                                                                                            |     | nachher                                                                                                                                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![image](https://raw.githubusercontent.com/Meisterschulen-am-Ostbahnhof-Munchen/4diac_training1/main/Ventilsteuerung/ISO-DesignerProjects/Workspace_TECU/DefaultPool/img/img_original/Tractor_wheel_slip_200.png) | --> | ![image](https://raw.githubusercontent.com/Meisterschulen-am-Ostbahnhof-Munchen/4diac_training1/main/Ventilsteuerung/ISO-DesignerProjects/Workspace_TECU/DefaultPool/img/img_cropped/Tractor_wheel_slip_200.png) |
| 200x200                                                                                                                                                                                                           |     | 196x196                                                                                                                                                                                                          |

dadurch werden die 2px großen Schnittmarken von <https://www.iso.org/obp/> entfernt. In der Regel will man die Aufgrund des Erscheinungsbildes nicht haben.

Danach liegen die Zugeschnittenen Bilder unter "img_cropped"


### 2. Alle Dateien unter img_cropped werden auf 64x64 skaliert

zum Ordner: [img_cropped](https://github.com/Meisterschulen-am-Ostbahnhof-Munchen/4diac_training1/tree/main/Ventilsteuerung/ISO-DesignerProjects/Workspace_TECU/DefaultPool/img/img_cropped)

| vorher                                                                                                                                                                                                            |     | nachher                                                                                                                                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![image](https://raw.githubusercontent.com/Meisterschulen-am-Ostbahnhof-Munchen/4diac_training1/main/Ventilsteuerung/ISO-DesignerProjects/Workspace_TECU/DefaultPool/img/img_cropped/Tractor_wheel_slip_200.png) | --> | ![image](https://raw.githubusercontent.com/Meisterschulen-am-Ostbahnhof-Munchen/4diac_training1/main/Ventilsteuerung/ISO-DesignerProjects/Workspace_TECU/DefaultPool/img/img_resized/Tractor_wheel_slip_200.png) |
| 196x196                                                                                                                                                                                                           |     | 64x64                                                                                                                                                                                                          |

Danach liegen die Zugeschnittenen Bilder unter "img_resized"


### 3. umwandlung auf 2 Farben (Monochrome)

zum Ordner: [img_resized](https://github.com/Meisterschulen-am-Ostbahnhof-Munchen/4diac_training1/tree/main/Ventilsteuerung/ISO-DesignerProjects/Workspace_TECU/DefaultPool/img/img_resized)

| vorher                                                                                                                                                                                                            |     | nachher                                                                                                                                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![image](https://raw.githubusercontent.com/Meisterschulen-am-Ostbahnhof-Munchen/4diac_training1/main/Ventilsteuerung/ISO-DesignerProjects/Workspace_TECU/DefaultPool/img/img_resized/Tractor_wheel_slip_200.png) | --> | ![image](https://raw.githubusercontent.com/Meisterschulen-am-Ostbahnhof-Munchen/4diac_training1/main/Ventilsteuerung/ISO-DesignerProjects/Workspace_TECU/DefaultPool/img/img_monochrome/Tractor_wheel_slip_200.png) |
| 64x64                                                                                                                                                                                                           |     | 64x64                                          

Danach liegen die Bilder unter "img_monochrome"


### 4. Konvertierung ins Format BMP


zum Ordner: [img_monochrome](https://github.com/Meisterschulen-am-Ostbahnhof-Munchen/4diac_training1/tree/main/Ventilsteuerung/ISO-DesignerProjects/Workspace_TECU/DefaultPool/img/img_monochrome)


| vorher                                                                                                                                                                                                            |     | nachher                                                                                                                                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![image](https://raw.githubusercontent.com/Meisterschulen-am-Ostbahnhof-Munchen/4diac_training1/main/Ventilsteuerung/ISO-DesignerProjects/Workspace_TECU/DefaultPool/img/img_monochrome/Tractor_wheel_slip_200.png) | --> | ![image](https://raw.githubusercontent.com/Meisterschulen-am-Ostbahnhof-Munchen/4diac_training1/main/Ventilsteuerung/ISO-DesignerProjects/Workspace_TECU/DefaultPool/img/img/Tractor_wheel_slip_200.bmp) |
| 64x64                                                                                                                                                                                                           |     | 64x64                                          

Danach liegen die Bilder unter "img"


zum Ordner: [img](https://github.com/Meisterschulen-am-Ostbahnhof-Munchen/4diac_training1/tree/main/Ventilsteuerung/ISO-DesignerProjects/Workspace_TECU/DefaultPool/img/img)




## Paint



mit Microsoft Paint das in jedem Windows enthlaten ist geht das umwandeln PNG in BMP ganz leicht. 
will man jedoch viele Dateien wandeln, so ist der Aufwand nicht unerheblich. 




### PNG in BMP umwandlen

das Bitmap geeigent benennen, die Dateinamen von ISO sind oft wenig aussagekräftig. 
(keine Leerzeichen, keine Umlaute) siehe: <https://docs.ms-muc-docs.de/projects/visual-programming-languages-docs/de/latest/Allgemeines.html#namen>




### BMP Skalieren

die Größe ist wichtig: 


| wo       | Größe       |   |   |   |
|----------|-------------|---|---|---|
| Softkey  | 72x72 pixel |   |   |   |
| Datamask | frei        |   |   |   |
| CCI A3   | 64x64 pixel |   |   |   |


Gedanken: 
80x80 --> als Button, macht Innenfläche 72x72

72x72 --> als Button, macht Innenfläche 64x64


:::{note}
Tipp: auch bei Buttons diese Größen anwenden, macht ein klares Erscheinungsbild. 

für Größere Buttons vielfache davon, z.B. 80x160, 160x160 usw. 
:::


Empfehlung: 
wenn das Symbol als Softkey und als CCI A3 Symbol verwendet werden soll, dann 64x64 Pixel machen. 

Man kann die Bilder vor dem Skalieren auch zuschneiden. 


### BMP Farbtiefe reduzieren

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

nun können die Bilder in ISO-Designer verwendet werden, 
im Falle von Monochrom kann Weiß als Transparenter Hintergrund gesetzt werden, 
im Falle einer anderen Farbtiefe wird oft Pink verwendet. 

