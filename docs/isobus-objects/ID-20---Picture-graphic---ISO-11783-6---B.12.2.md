# ID 20 – Picture graphic – ISO 11783-6 – B.12.2

```{index} single: ID 20 – Picture graphic – ISO 11783-6 – B.12.2
```

Das **Picture Graphic** Objekt mit der **ID 20** dient zur Anzeige von Rastergrafiken (Bitmaps) auf dem Virtuellen Terminal. Es ermöglicht die Integration von Logos, Icons und komplexen visuellen Elementen.

## Technische Attribute (gemäß Tabelle B.41)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer im Objekt-Pool. |
| 0 | **Type** | Integer 1 | Objekttyp = 20 (Picture Graphic). |
| 1 | **Width** | Integer 2 | **Zielbreite** am VT. Die Höhe wird automatisch skaliert, um das Seitenverhältnis beizubehalten. |
| 4 | **Actual width** | Integer 2 | Tatsächliche Breite der Rohdaten in Pixeln (Read-only). |
| 5 | **Actual height** | Integer 2 | Tatsächliche Höhe der Rohdaten in Pixeln (Read-only). |
| 6 | **Format** | Integer 1 | **0:** Monochrom (1 Bit), **1:** 16 Farben (4 Bit), **2:** 256 Farben (8 Bit). |
| 2 | **Options** | Bitmask 1 | **Bit 0:** Transparenz (0=Opak, 1=Transparent), **Bit 1:** Blinken, **Bit 2:** Komprimierung (0=Raw, 1=RLE). |
| 3 | **Transp. colour** | Integer 1 | Farbindex, der als transparent behandelt wird. |
| - | **Raw data size** | Integer 4 | Anzahl der Bytes in den Bilddaten. |

## Funktionsweise und Darstellung

Das Picture Graphic-Objekt speichert Pixelgrafiken in binärer Form innerhalb der Objektpool-Datei (.IOP). 

### Skalierung und Formate
*   **Seitenverhältnis:** Das VT skaliert die Grafik basierend auf der Ziel-Breite (`Width`). Um Verzerrungen zu vermeiden, berechnet das VT die Ziel-Höhe automatisch aus dem Verhältnis von `Actual width` zu `Actual height`.
*   **Farbtiefe:** Unterstützt werden 1-Bit (Monochrom), 4-Bit (16 Farben) und 8-Bit (256 Farben). 
*   **PNG-Unterstützung:** Moderne VTs (ab Version 6) unterstützen auch PNG-Grafiken, was eine bessere Qualität bei geringerer Dateigröße ermöglicht.

### Transparenz und Effekte
*   **Transparency (Bit 0):** Wenn aktiviert, wird die in AID 3 definierte Farbe nicht gezeichnet; stattdessen scheint der Hintergrund durch.
*   **Flashing (Bit 1):** Das Bild kann blinken (Frequenz und Stil hängen vom VT ab).
*   **RLE-Komprimierung (Bit 2):** Run-Length Encoding kann bei einfachen Grafiken (viele gleichfarbige Flächen) Speicherplatz sparen.

## Ereignisse (Events - Tabelle B.40)
*   **On Refresh:** Wird ausgelöst, wenn sich Anzeigeoptionen (Transparenz, Blinken) ändern oder die Maske neu gezeichnet wird.
*   **On Change Attribute:** Wird bei Änderungen an den Attributen per ECU-Kommando ausgelöst.

## Bedeutung für die Implementierung
Picture Graphics sind essenziell für ein modernes HMI. 
*   **Verschwendung vermeiden:** Da Bitmaps viel Speicher im VT belegen, sollten sie so klein wie möglich gehalten werden. 
*   **Ziederverwendung:** Ein Bild kann im Pool einmal definiert und von vielen Objekten (z. B. mehreren Buttons) referenziert werden.
*   **Icons:** Sie werden häufig als "Designatoren" für Softkeys (ID 5) oder als Symbole in Containern (ID 3) verwendet.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*