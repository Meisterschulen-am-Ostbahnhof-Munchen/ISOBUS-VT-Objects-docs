# ID 20 – Picture graphic – ISO 11783-6 – B.12.2

## Podcast

<iframe src="https://creators.spotify.com/pod/profile/isobus-vt-objects/embed/episodes/ISOBUS-Wie-Logos-auf-euer-Traktor-Terminal-kommen--Das-Picture-Graphic-Objekt-erklrt-e36aagf/a-ac33t6i" height="102px" width="400px" frameborder="0" scrolling="no"></iframe>

## Empfohlene Lektüre Picture graphic:

*   Hilfe Jetter ISO-Designer.
    *   ISO-Objekte
        *   Die einzelnen ISO-Objekte
            *   Das Objekt Picture Graphic

![](https://user-images.githubusercontent.com/69573151/94602532-4838d980-0295-11eb-8bce-d3751aaf8551.png)



## Picture Graphic (Grafikobjekt)

Das **Picture Graphic**-Objekt ist ein grundlegendes Element in **ISO 11783-6** und dem **ISO-Designer**, das zur **Anzeige von Pixelgrafiken (Bitmaps)** auf einem Virtuellen Terminal (VT) verwendet wird. Es ermöglicht die Integration visueller Elemente wie Bilder oder Icons in die Benutzeroberfläche land- und forstwirtschaftlicher Maschinen.

### Funktionsweise und Darstellung

Das Picture Graphic-Objekt speichert Pixelgrafiken in **binärer Form** innerhalb der .IOP-Datei (ISO-Objektpool-Datei). Das Virtuelle Terminal ist dafür verantwortlich, die Grafik zur Laufzeit basierend auf den definierten Eigenschaften zu skalieren und darzustellen.

*   **Skalierung**: Die Grafik wird von ihrer tatsächlichen Breite und Höhe auf die im Objekt definierte **Zielbreite** skaliert, wobei das **Seitenverhältnis beibehalten** wird, um Verzerrungen zu vermeiden. Für eine Pixel-genaue Darstellung sollte die definierte Breite des Objekts der tatsächlichen Breite der Rohdaten entsprechen.
*   **Formate**: Das Objekt unterstützt verschiedene Grafikformate, die durch das Format-Attribut definiert werden:
    *   **Monochrom** (8 Pixel pro Byte).
    *   **16-Bit-Farbe** (2 Pixel pro Byte).
    *   **256-Farben** (1 Pixel pro Byte).
    *   Ab ISO-Designer Version 5.1 und für VTs der Version 6 und höher wird auch die Verwendung von **PNG-Grafiken** unterstützt, sofern die entsprechende Compiler-Option aktiviert ist.
*   **Transparenz**: Ein Picture Graphic-Objekt kann **transparent** oder **opak** sein. Wenn die Transparenzoption aktiviert ist, zeigen Pixel, die den definierten **Transparenzfarbindex** aufweisen, den Hintergrund oder darunterliegende Objekte an.
*   **Blinken (Flashing)**: Objekte können so konfiguriert werden, dass sie blinken. Der Stil und die Rate des Blinkens werden vom VT-Design bestimmt. Im ISO-Designer ist das Blinken nur im Component-Editor sichtbar.
*   **Rohdatenformat und Komprimierung**: Die Rohdaten des Bildes werden Zeile für Zeile von links nach rechts und von oben nach unten interpretiert. Ungenutzte Bits am Ende eines Bytes werden mit Nullen aufgefüllt und vom VT ignoriert. Es kann eine **Run-Length Encoding (RLE)**-Methode zur Komprimierung der Daten verwendet werden, was jedoch bei komplexen Bildern die Dateigröße erhöhen kann. Wenn die Daten nach der Definition der Pixel kürzer als erwartet sind, meldet das VT einen Fehler.

### Attribute und Eigenschaften

Die Eigenschaften eines Picture Graphic-Objekts können im ISO-Designer im **Properties-Fenster** konfiguriert werden.

*   **Allgemeine Attribute (ISO 11783-6)**:
    *   **Object ID**: Eindeutige Kennung des Objekts.
    *   **Type **: Objekttyp (Wert 20).
    *   **Width (AID 1)**: Die **Zielbreite** der Grafik in Pixeln, auf die das VT die Grafik skaliert.
    *   **Actual width / Actual height**: Die tatsächliche Breite und Höhe der Rohdaten in Pixeln. Diese Attribute sind schreibgeschützt und dienen dem VT als Referenz für die Skalierung.
    *   **Format**: Definiert den Pixeltiefen-Typ der Grafik (Monochrom, 4-Bit-Farbe, 8-Bit-Farbe).
    *   **Options (AID 2)**: Eine Bitmaske, die verschiedene Optionen steuert:
        *   Bit 0: **Opaque / Transparent**.
        *   Bit 1: **Normal / Flashing** (Blinken).
        *   Bit 2: **Raw data / Run-Length Encoded** (Komprimierung). Dieser Wert kann zur Laufzeit nicht geändert werden.
    *   **Transparency colour (AID 3)**: Der Farbindex, der als transparent behandelt wird.
    *   **Number of bytes in raw data**: Anzahl der Bytes in den Rohdaten.
    *   **Raw data**: Die eigentlichen Bilddaten.

*   **Spezifische Eigenschaften (ISO-Designer)**:
    *   **Resource ID**: Auswahl einer grafischen Ressource.
    *   **Path**: Der Dateipfad zur Originalgrafikdatei.
    *   **Retain Aspect Ratio**: Option, um das Seitenverhältnis beim Erstellen oder Ändern der Größe beizubehalten.
    *   **Use Transparency / (Transparent Color)**: Ermöglicht die Verwendung einer Transparenzfarbe.
    *   **Flashing**: Lässt das Objekt blinken (nur im Component-Editor sichtbar).
    *   **Bits Per Pixel / Encoding / Byte Size**: Zeigen Informationen zum Grafikformat und zur Kodierung an.

### Erstellung und Konfiguration (im ISO-Designer)

Im **ISO-Designer** kann ein Picture Graphic-Objekt einfach über die **Drawing-Symbolleiste** erstellt werden. Nach der Auswahl des Werkzeugs wählt der Benutzer eine Grafikdatei aus dem Dateisystem aus.

*   **Größenanpassung**: Die Größe des Objekts kann interaktiv mit der Maus oder durch Eingabe von Werten in den Eigenschaften im **Properties-Fenster** angepasst werden. Das Objekt wird in der definierten Größe in die .IOP-Datei übernommen, nicht in seiner Originalgröße.
*   **Kontextmenü-Funktionen**: Das Kontextmenü bietet Funktionen wie "Resize To Original Format" (Größe auf Original zurücksetzen) und "Reload Image" (Grafikdatei bei Änderung aktualisieren).
*   **Lokale Speicherung**: Zur Erleichterung der Projektweitergabe können Grafiken in einem lokalen Projektordner gespeichert werden, indem die Option "Copy image files to local project folder" in den Einstellungen aktiviert wird (Tools/Option/General).
*   **PNG-Unterstützung**: Ab ISO-Designer 5.1 können PNG-Grafiken für VTs der Version 6 und höher erstellt werden, wenn die Option "Compile Picture Graphics as PNG" unter Project/Properties/Compiler ausgewählt ist.

### Verwendung in anderen Objekten

Picture Graphic-Objekte sind vielseitig einsetzbar und können von anderen Objekten referenziert werden:

*   **Füllmuster**: Sie können als **Füllmuster (Fill Pattern)** für **Fill Attributes**-Objekte verwendet werden, um Formen mit Texturen oder Mustern zu füllen.
*   **Skalierte Grafiken**: Das **Scaled Graphic**-Objekt (verfügbar ab VT Version 6) dient dazu, eine skalierte Darstellung eines referenzierten Picture Graphic-Objekts anzuzeigen, wobei verschiedene Skalierungs- und Ausrichtungsoptionen zur Verfügung stehen.
*   **Animationen**: Das **Animation**-Objekt (verfügbar ab VT Version 5) kann eine Liste von Objekten, einschließlich Picture Graphic-Objekten, nacheinander darstellen, um einfache Animationen zu erzeugen.
*   **Icons und Designatoren**: Picture Graphic-Objekte werden oft als **Icons** oder **Designatoren** verwendet, z. B. für Soft Keys, Key Groups, Window Masks, Auxiliary Functions und Auxiliary Inputs, um visuelle Kennzeichnungen bereitzustellen.

### Ereignisse und Befehle

Picture Graphic-Objekte können auf bestimmte Ereignisse reagieren und mit spezifischen Befehlen manipuliert werden:

*   **Ereignisse**: Das Objekt kann "On Refresh"-Ereignisse auslösen, wenn sich Attribute wie Opaque/Transparent oder Flashing-Optionen ändern.
*   **Befehle**: Die Hauptbefehle zur Interaktion mit einem Picture Graphic-Objekt sind `Change Attribute` und `Get Attribute Value`.

### Kompatibilität

Das Picture Graphic-Objekt ist in **VT Version 2 und höher** verfügbar. Spezifische Funktionen, wie die Unterstützung von 256-Farben und PNG-Formaten, sind in **VT Version 6 und höher** vollständig implementiert.

---
