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



## BMP in ISO-Designer einfügen