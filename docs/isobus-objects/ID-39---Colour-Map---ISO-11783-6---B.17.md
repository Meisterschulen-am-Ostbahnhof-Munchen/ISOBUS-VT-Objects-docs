# ID 39 – Colour Map – ISO 11783-6 – B.17

```{index} single: ID 39 – Colour Map – ISO 11783-6 – B.17
```

Das **Colour Map** Objekt mit der **ID 39** (optional ab VT Version 4/5, Pflicht ab VT Version 6) ermöglicht es einer Working Set, die Farbtabelle des Terminals zur Laufzeit umzudefinieren.

## Technische Attribute (gemäß Tabelle B.57)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer. |
| 0 | **Type** | Integer 1 | Objekttyp = 39 (Colour Map). |
| - | **Number of colour indexes**| Integer 2 | 2 (Monochrom), 16 oder 256. |
| - | **Colour Map entries** | Integer Array| Die Liste der Farben, die den Indizes zugewiesen werden. |

## Funktionsweise
Normalerweise verwendet ein Terminal eine Standard-Farbpalette (z. B. 256 Farben gemäß ISO). Mit der Colour Map kann eine Working Set definieren, dass z. B. der Farbindex 1 (Standard: Rot) stattdessen als Blau dargestellt werden soll. 
*   **Indirektion:** Dies bietet eine Ebene der Indirektion. Anstatt jedes Objekt einzeln zu ändern, kann durch einfaches Umschalten der Colour Map das gesamte Farbschema der Anwendung gewechselt werden (z. B. Tag-/Nacht-Modus).

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, B.17 verwiesen.*
