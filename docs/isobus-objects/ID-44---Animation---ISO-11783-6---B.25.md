# ID 44 – Animation – ISO 11783-6 – B.25

```{index} single: ID 44 – Animation – ISO 11783-6 – B.25
```

Das **Animation** Objekt mit der **ID 44** (ab VT Version 5) ermöglicht die automatische oder manuelle Wiedergabe einer Sequenz von Objekten (Frames).

## Technische Attribute (gemäß Tabelle B.72)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer. |
| 0 | **Type** | Integer 1 | Objekttyp = 44 (Animation). |
| 1 | **Width** | Integer 2 | Breite des Animationsbereichs. |
| 2 | **Height** | Integer 2 | Höhe des Animationsbereichs. |
| 3 | **Refresh Interval** | Integer 2 | Zeit in ms zwischen den Frames (0 = Timer aus). |
| 4 | **Value** | Integer 1 | Aktueller Index des sichtbaren Objekts. |
| 5 | **Enabled** | Integer 1 | 0 = Stop, 1 = Läuft. |
| 6 | **First Child Index** | Integer 1 | Index des ersten Frames der Sequenz. |
| 7 | **Last Child Index** | Integer 1 | Index des letzten Frames der Sequenz. |
| 8 | **Default Child Index**| Integer 1 | Anzeige-Index, wenn die Animation gestoppt ist. |
| 9 | **Options** | Bitmask 1 | Bit 0: 0=Single Shot, 1=Loop. Bits 1-2: Verhalten bei Deaktivierung (Pause, Reset, etc.). |

## Funktionsweise
Das Animationsobjekt verwaltet eine Liste von Kind-Objekten. Wenn `Enabled` auf 1 steht, inkrementiert das Terminal den `Value` (Index) automatisch im Rhythmus des `Refresh Interval`.
*   **Loop:** Nach Erreichen des `Last Child Index` wird wieder beim `First Child Index` begonnen.
*   **Single Shot:** Die Animation stoppt beim letzten Frame.

## Empfehlung
Um die Performance des Terminals nicht zu überlasten, sollten die Einzelobjekte klein gehalten werden. Ein Refresh-Intervall von mindestens 200 ms wird empfohlen.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, B.25 verwiesen.*