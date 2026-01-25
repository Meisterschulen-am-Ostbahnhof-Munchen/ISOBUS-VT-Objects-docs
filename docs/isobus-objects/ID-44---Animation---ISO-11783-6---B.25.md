# ID 44 – Animation – ISO 11783-6 – B.25

```{index} single: ID 44 – Animation – ISO 11783-6 – B.25
```

Das **Animation** Objekt mit der **ID 44** (ab VT Version 5) ermöglicht die automatische oder manuelle Wiedergabe einer Sequenz von Objekten (Frames).

### Attribute und Record Format (Tabelle B.72)

Die folgende Tabelle beschreibt den Aufbau des Animation Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 44 | 3 | Objekttyp = Animation. |
| [1] | **Width** | Integer | 2 | 0 – 65535 | 4 – 5 | Breite des Animationsbereichs in Pixeln. |
| [2] | **Height** | Integer | 2 | 0 – 65535 | 6 – 7 | Höhe des Animationsbereichs in Pixeln. |
| [3] | **Refresh Interval** | Integer | 2 | 0 – 65535 | 8 – 9 | Zeit in ms zwischen den Frames (0 = Timer aus). |
| [4] | **Value** | Integer | 1 | 0 – 255 | 10 | Aktueller Listenindex des angezeigten Objekts (0-254). |
| [5] | **Enabled** | Integer | 1 | 0 oder 1 | 11 | 0=Stopped (Deaktiviert), 1=Animating (Aktiviert). |
| [6] | **First Child Index** | Integer | 1 | 0 – 254 | 12 | Startindex der Animationssequenz. |
| [7] | **Last Child Index** | Integer | 1 | 0 – 254 | 13 | Endindex der Animationssequenz. |
| [8] | **Default Child Index** | Integer | 1 | 0 – 254 | 14 | Index des Objekts, das angezeigt wird, wenn die Animation deaktiviert ist (abhängig von Options). |
| [9] | **Options** | Bitmask | 1 | 0 – 7 | 15 | Bit 0: Sequence (0=Single Shot, 1=Loop)<br>Bits 1–2: Disabled Behaviour (0=Pause, 1=Reset to First, 2=Default Object, 3=Blank). |
| - | **Number of objects to follow** | Integer | 1 | 0 – 255 | 16 | Anzahl der enthaltenen Frames (Objekte). |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 17 | Anzahl der folgenden Makro-Referenzen. |
| - | **Repeat:** {Object ID} | Integer | 2 | 0 – 65534 | 18 + ... | Objekt-ID eines Frames (Child-Objekt). |
| - | {X Location} | Signed Integer | 2 | -32768 bis +32767 | 20 + ... | X-Position relativ zur Animation. |
| - | {Y Location} | Signed Integer | 2 | -32768 bis +32767 | 22 + ... | Y-Position relativ zur Animation. |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | Event ID, die das Makro auslöst. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Makro ID des auszuführenden Makros. |

## Funktionsweise
Das Animationsobjekt verwaltet eine Liste von Kind-Objekten. Wenn `Enabled` auf 1 steht, inkrementiert das Terminal den `Value` (Index) automatisch im Rhythmus des `Refresh Interval`.
*   **Loop:** Nach Erreichen des `Last Child Index` wird wieder beim `First Child Index` begonnen.
*   **Single Shot:** Die Animation stoppt beim letzten Frame.
*   **Deaktivierung:** Das Verhalten beim Stoppen (Pause, Reset auf 1. Frame, Default-Bild oder Leer) wird über die Optionen gesteuert.

## Ereignisse (Events - Tabelle B.71)

Das Animation Objekt reagiert auf folgende Ereignisse:

*   **On Enable / On Disable:** Zustandsänderung.
*   **On Change Value:** Wenn der Index (manuell oder automatisch) geändert wird. Das VT zeichnet das neue Objekt.
*   **On Change Attribute:** Reaktion auf generelle Attributänderungen.
*   **On Change Size:** Reaktion auf Größenänderung.
*   **On Refresh:** Wird ausgelöst durch den Timer (Refresh Interval) oder andere Refresh-Bedingungen.

## Empfehlung
Um die Performance des Terminals nicht zu überlasten, sollten die Einzelobjekte klein gehalten werden. Ein Refresh-Intervall von mindestens 200 ms wird empfohlen.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, B.25 verwiesen.*