# ID 9 – Input number – ISO 11783-6 – B.8.4

```{index} single: ID 9 – Input number – ISO 11783-6 – B.8.4
```

Das **Input Number** Objekt mit der **ID 9** ist eines der komplexesten und wichtigsten Eingabeobjekte. Es dient zur Eingabe und Anzeige von numerischen Werten und unterstützt automatische Skalierung, Formatierung und Grenzwertprüfung direkt im Terminal.

## Technische Attribute (gemäß Tabelle B.18)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer im Objekt-Pool. |
| 0 | **Type** | Integer 1 | Objekttyp = 9 (Input Number). |
| 1 | **Width** | Integer 2 | Breite des Feldes in Pixeln. |
| 2 | **Height** | Integer 2 | Höhe des Feldes in Pixeln. |
| 3 | **Background colour** | Integer 1 | Hintergrundfarbe. |
| 4 | **Font attributes** | Integer 2 | Verweis auf ein **Font Attributes** Objekt. |
| 5 | **Options** | Bitmask 1 | **Bit 0:** Transparent, **Bit 1:** Führende Nullen, **Bit 2:** Null als Leerzeichen, **Bit 3:** Runden (0) oder Abschneiden (1). |
| 6 | **Variable reference** | Integer 2 | Verweis auf ein **Number Variable** Objekt (ID 21). |
| 14 | **Value** | Integer 4 | Aktueller Rohwert (32-Bit unsigned). Nur wenn AID 6 = NULL. |
| 7 | **Min value** | Integer 4 | Minimaler zulässiger Rohwert. |
| 8 | **Max value** | Integer 4 | Maximaler zulässiger Rohwert. |
| 9 | **Offset** | Integer 4 | Offset für die Skalierung (32-Bit signed). |
| 10 | **Scale** | Float 4 | Skalierungsfaktor (Multiplikator). |
| 11 | **Number of decimals** | Integer 1 | Anzahl der anzuzeigenden Nachkommastellen (0-7). |
| 12 | **Format** | Boolean 1 | 0 = Festkomma (####.nn), 1 = Exponentialdarstellung. |
| 13 | **Justification** | Integer 1 | Textausrichtung im Feld. |
| 15 | **Options 2** | Bitmask 1 | **Bit 0:** Enabled, **Bit 1:** Real Time Editing. |

## Die Skalierungslogik
Das VT berechnet den angezeigten Wert automatisch nach folgender Formel:

**Angezeigter Wert = (Rohwert + Offset) × Skalierungsfaktor**

Dies erlaubt es, physikalische Werte (z. B. 12,5 bar) als einfache Ganzzahlen im Speicher (z. B. 125) zu verarbeiten, während das VT die Umrechnung und Kommadarstellung übernimmt.

## Validierung
Grenzwerte werden ebenfalls auf Basis der skalierten Werte geprüft. Das VT lässt das Schließen des Eingabefeldes (ENTER) nur zu, wenn der neue Wert innerhalb der skalierten Min/Max-Grenzen liegt.

## Real Time Editing (AID 15, Bit 1)
Wenn dieses Bit gesetzt ist, sendet das VT bei jeder Änderung (z. B. bei jedem Tastendruck am Inkrementalgeber) den aktuellen Zwischenwert an die Arbeitsgruppe. Dies ermöglicht es der Maschine, sofort auf Änderungen zu reagieren (z. B. Drehzahlregelung in Echtzeit), noch bevor der Bediener die Eingabe final bestätigt.

## Bedeutung für die Implementierung
Das Input Number Objekt nimmt der Maschinensteuerung (ECU) viel Arbeit bei der Formatierung und Validierung ab. Entwickler sollten darauf achten, den Skalierungsfaktor und die Nachkommastellen so zu wählen, dass keine Rundungsfehler die Anzeige verfälschen.

Weitere Informationen und Beispiele finden sich im [ISOBUS Wiki - Number (Input)](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/number-input) von Tobias Tenberg.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*