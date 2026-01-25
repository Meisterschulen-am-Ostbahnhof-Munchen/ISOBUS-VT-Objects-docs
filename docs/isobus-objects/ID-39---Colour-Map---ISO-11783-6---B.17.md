# ID 39 – Colour Map – ISO 11783-6 – B.17

```{index} single: ID 39 – Colour Map – ISO 11783-6 – B.17
```

Das **Colour Map** Objekt mit der **ID 39** (optional ab VT Version 4/5, Pflicht ab VT Version 6) ermöglicht es einer Working Set, die Farbtabelle des Terminals zur Laufzeit umzudefinieren.

### Attribute und Record Format (Tabelle B.57)

Die folgende Tabelle beschreibt den Aufbau des Colour Map Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 39 | 3 | Objekttyp = Colour Map. |
| - | **Number of colour indexes to follow** | Integer | 2 | 2, 16, 256 | 4 – 5 | Anzahl der folgenden Einträge. Muss zur Farbtiefe des VTs passen (siehe Get Hardware). |
| - | **Repeat:** {Colour Map} | Integer | var. | 0 – 255 | 6 ... | Liste von Farb-Indizes. |

### Struktur der Einträge
Die Einträge definieren eine Umleitung der Farb-Indizes.
*   **Beispiel:** Wenn der Eintrag an Index 0 den Wert 1 hat, wird überall dort, wo im Design Farbe 0 (Schwarz) verwendet wurde, nun Farbe 1 (Weiß) angezeigt.
*   Die Länge der Einträge hängt vom VT-Typ ab:
    *   **Typ 0 (Monochrom):** 2 Einträge.
    *   **Typ 1 (16 Farben):** 16 Einträge.
    *   **Typ 2 (256 Farben):** 256 Einträge.

## Funktionsweise
Normalerweise verwendet ein Terminal eine Standard-Farbpalette (z. B. 256 Farben gemäß ISO). Mit der Colour Map kann eine Working Set definieren, dass z. B. der Farbindex 1 (Standard: Rot) stattdessen als Blau dargestellt werden soll.
*   **Indirektion:** Dies bietet eine Ebene der Indirektion. Anstatt jedes Objekt einzeln zu ändern, kann durch einfaches Umschalten der Colour Map das gesamte Farbschema der Anwendung gewechselt werden (z. B. Tag-/Nacht-Modus).
*   **Aktivierung:** Eine Colour Map wird über das Kommando `Select Colour Map` aktiviert.

## Anmerkung zu VT Version 6
Ab Version 6 wird zusätzlich das *Colour Palette* Objekt (ID 45) unterstützt, mit dem die RGB-Werte der Farben selbst geändert werden können. Die Colour Map mappt Indizes auf Indizes, während die Colour Palette Indizes auf RGB-Werte mappt.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, B.17 verwiesen.*