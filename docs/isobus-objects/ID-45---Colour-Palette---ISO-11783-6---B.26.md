# ID 45 – Colour Palette – ISO 11783-6 – B.26

```{index} single: ID 45 – Colour Palette – ISO 11783-6 – B.26
```

Das **Colour Palette** Objekt mit der **ID 45** (ab VT Version 6) erlaubt es einer Working Set, die Standard-Farbpalette des Terminals vollständig durch eigene ARGB-Farbdefinitionen zu ersetzen.

## Technische Attribute (gemäß Tabelle B.73)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer. |
| 0 | **Type** | Integer 1 | Objekttyp = 45 (Colour Palette). |
| - | **Number of ARGB values** | Integer 2 | Anzahl der folgenden Farbdefinitionen (bis zu 256). |

### Struktur der ARGB-Einträge
Jede Farbe wird durch 4 Bytes definiert:
*   **B (Blue):** 0–255.
*   **G (Green):** 0–255.
*   **R (Red):** 0–255.
*   **A (Alpha):** 0 (transparent) bis 255 (opak).

## Unterschied zur Colour Map (ID 39)
Während die *Colour Map* nur die Zuweisung (Indizierung) vorhandener Terminal-Farben ändert, definiert die *Colour Palette* die Farben selbst (RGB-Werte) neu. Dies ermöglicht echtes Branding in Firmenfarben oder eine optimierte Darstellung von Fotos.

## Wichtiger Hinweis
Die Verwendung des Alpha-Kanals (Transparenz) sollte vorsichtig erfolgen, da das Terminal die Hintergrundfarben untergelagerter Objekte oft nicht garantieren kann.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, B.26 verwiesen.*
