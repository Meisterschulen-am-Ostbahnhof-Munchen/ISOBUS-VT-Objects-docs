# ID 45 – Colour Palette – ISO 11783-6 – B.26

```{index} single: ID 45 – Colour Palette – ISO 11783-6 – B.26
```

Das **Colour Palette** Objekt mit der **ID 45** (ab VT Version 6) erlaubt es einer Working Set, die Standard-Farbpalette des Terminals vollständig durch eigene ARGB-Farbdefinitionen zu ersetzen.

### Attribute und Record Format (Tabelle B.73)

Die folgende Tabelle beschreibt den Aufbau des Colour Palette Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 45 | 3 | Objekttyp = Colour Palette. |
| [1] | **Options** | Bitmask | 1 | 0 | 4 | Reserviert (sollte 0 sein). |
| - | **Number of ARGB values to follow** | Integer | 2 | 0 – 256 | 5 – 6 | Anzahl der folgenden Farbdefinitionen. |
| - | **Repeat:** {B} | Integer | 1 | 0 – 255 | 7 + ... | Blau-Wert. |
| - | {G} | Integer | 1 | 0 – 255 | 8 + ... | Grün-Wert. |
| - | {R} | Integer | 1 | 0 – 255 | 9 + ... | Rot-Wert. |
| - | {A} | Integer | 1 | 0 – 255 | 10 + ... | Alpha-Wert (0=Transparent, 255=Opak). |

## Funktionsweise
Wenn ein Colour Palette Objekt aktiv ist, ersetzt es die Standardfarben des VTs für dieses Working Set. Die Farben werden beginnend bei Index 0 aufgefüllt.
*   **Aktivierung:** Eine Colour Palette kann über das *Working Set Special Controls* Objekt (ID 47) als Standard gesetzt oder zur Laufzeit per `Select Colour Map or Palette` Kommando aktiviert werden.
*   **Transparenz:** Der Alpha-Kanal ermöglicht halbtransparente Farben. Dies sollte jedoch mit Vorsicht genutzt werden, insbesondere bei überlagerten Objekten.

## Unterschied zur Colour Map (ID 39)
Während die *Colour Map* nur die Zuweisung (Indizierung) vorhandener Terminal-Farben ändert, definiert die *Colour Palette* die physikalischen Farben (ARGB-Werte) neu. Dies ermöglicht echtes Branding in Firmenfarben.

## Ereignisse (Events)
Das Objekt selbst löst keine Events aus, beeinflusst aber die Darstellung aller Objekte, die Farben verwenden.
*   **On Change Attribute:** Wird ausgelöst, wenn Attribute geändert werden. Das VT muss ggf. den gesamten Bildschirm neu zeichnen.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, B.26 verwiesen.*