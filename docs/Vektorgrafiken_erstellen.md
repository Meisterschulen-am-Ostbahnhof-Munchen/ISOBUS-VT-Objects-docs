# Vektorgrafiken erstellen

```{index} single: Vektorgrafiken erstellen
```

## Coral Draw X5
Für den Fall, dass die Datei aus einer z.B. PDF Datei gewonnen werden soll, kann man sich mit Coral Draw X5 behelfen.
Die Größe kann auch über Anordnen-->Änderungen–>Größe geändert werden.
Achtung: Sehr ungenau und wird ein paar Versuche benötigen, um die gewünschte Größe zu bekommen.
Falls es eine andere Möglichkeit geben sollte, bitte hier ausbessern (Lächeln) 

## Solid Edge
* Falls etwas nicht klappt, hilft es einfach sich die Arbeit zu machen und jeden Strich noch ein Mal neu zu setzen,
* um die klaren Bezüge zwischen den Linien sicherzustellen. Zeitraubend, aber dann sollte es gehen. (Zwinkern) 
* Wenn man Symbole für die Displays zeichnet müssen diese die Maße 72x72 haben. Kurz ein Rechteck zeichnen und kontrollieren, dann ist man auf der sicheren Seite.
* Gesamtes Objekt markieren → Block → Alle Gruppen auflösen

![image2015-10-21 10_4_0](https://github.com/Meisterschulen-am-Ostbahnhof-Munchen/ISOBUS-VT-Objects-docs/assets/69573151/8c3efd93-6903-4d12-93b1-c1be96ed3976)

Fertig skalierte Vektordatei speichern

Danach Speichern unter →  Als übersetzt speichern (im .dxf Format)

Achtung ! Im Objekt darf es keine Rundungen geben. Alles muss in "Polygon über Mittelpunkt" sein. Im Idealfall neun Seitenteile.

Ein Weiterarbeiten mit Rundungen würde sonst in Libre CAD bzw. ISO Designer zu Problemen führen !

## Libre CAD

Gespeicherte .dfx Datei in Libre CAD öffnen
Alle Linien müssen verbunden werden:
gesamtes Objekt markieren → Zeichnen (Werkzeuge) → Polylinie → Polylinie aus vorhandenen Objekten erstellen
Achtung: Es kann sein, dass nur Bruchstücke von dem Objekt als Polygon verbunden werden und

es dann im ISO-Designer (nächster Schritt) zu Problemen kommt. Das Objekt wird nur an diesen Teilen sichtbar sein!!!

Es hilft dann, in Solid Edge das Objekt noch ein Mal Schritt für Schritt durch zu gehen.

Falls man beim Klick auf die Linie keine lila/pinke Linie hat, sondern eine gestrichelte "lila" Linie hat, hat man den Fehler vielleicht schon gefunden.

Dieses gestrichelte Linie mit z.B. dem Trimmwerkzeug aus Solid Edge entfernen und mit einer neuen Linie die Punkte verbinden.

![image2015-10-21 10_6_24](https://github.com/Meisterschulen-am-Ostbahnhof-Munchen/ISOBUS-VT-Objects-docs/assets/69573151/ca471324-0a91-4cec-92c1-65b72c1f22f5)

 Vorgang mit allen einzelnen Objekten wiederholen
 Speichern
Schließen

## ISO-Designer

* Die Unterstützung von DXFs für den Import von Vektorgrafiken wurde von Jetter entfernt. 
* ISO-Designer 5.3.1 ist die letzte die noch DXF importieren kann. 

File → New → Workspace: Name der .dfx Datei)
File → New → Project :
neuste Plattform wählen (2010)
höchste Auflösung (480x480)
Display name und Project name mit Name der .dfx Datei benennen

Linie oder irgendwas in WorkingSet.jvi zeichnen

Rechtsklick in DataMask.jvi → DXF importieren → Haken bei create container around drawing

WICHTIG: im Working Set bleibt bis zum Schluss der Stricht/Linie drin.

Das Symbol wird auch in DataMask eingefügt. Zwei verschiedene Registerkarten !!!
Sonst kommt es am Ende zu einer Fehlermeldung und es funktioniert nicht !!! 

![image2015-10-21 10_10_43](https://github.com/Meisterschulen-am-Ostbahnhof-Munchen/ISOBUS-VT-Objects-docs/assets/69573151/dcdfbdc6-2b03-4250-802a-85bacef2d1ac)

Speichern

Close Workspace (wegen BUG)

Wieder öffnen über Recent Workspaces

Füllattribute ausfüllen

Build → Build All

Build → Deploy

Über "Deployment" sollte man jetzt "0 Error(s)" lesen können.

Falls das nicht so ist, den Strich unter WorkingSet überprüfen. (siehe oben)

## Alternative mit Autodesk Fusion 360 und Plugin
Software und Plugin installieren
Fusion 360 herunterladen und installieren

Studenten / Schüler kostenlos.

Das Plugin "DXFSplineToPolyline-win64" installieren.

### Fusion 360 anwenden.

Neue Konstruktion erstellen

![image2017-1-9 13_52_3](https://github.com/Meisterschulen-am-Ostbahnhof-Munchen/ISOBUS-VT-Objects-docs/assets/69573151/02523f1b-a526-4239-a692-b4513f496fe7)
DXF importieren (Einfügen/DXF-Datei einfügen)
untere Ebene und Datei auswählen

![image2017-1-9 14_1_59](https://github.com/Meisterschulen-am-Ostbahnhof-Munchen/ISOBUS-VT-Objects-docs/assets/69573151/e2e82141-9fbe-4d47-8c7c-cc5a24002fef)

Optional: Nach Bedarf bearbeiten, skalieren (Skizze/Skalierungsmaßstab (Maßstab so wählen das Zielgröße z.B. 80x80) und in den Ursprung verschieben (Ändern/Verschieben)
  
Über Menüpunkt Skizze kann das Plugin "Export to DXF (Splines as Polyline)" ausgeführt werden
Als Toleranz wird 1.00 mm angegeben.

![image2017-1-9 14_25_45](https://github.com/Meisterschulen-am-Ostbahnhof-Munchen/ISOBUS-VT-Objects-docs/assets/69573151/59a5c4a6-65ba-4527-8936-3f00f9f91a5f)

Weiter mit Libre CAD