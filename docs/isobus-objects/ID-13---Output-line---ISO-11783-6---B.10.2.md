# ID 13 – Output line – ISO 11783-6 – B.10.2

```{index} single: ID 13 – Output line – ISO 11783-6 – B.10.2
```

Das **Output Line** Objekt mit der **ID 13** wird verwendet, um eine einfache Linie zwischen zwei Punkten innerhalb eines virtuellen Rechtecks zu zeichnen.

### Attribute und Record Format (Tabelle B.27)

Die folgende Tabelle beschreibt den Aufbau des Output Line Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 13 | 3 | Objekttyp = Output Line. |
| [1] | **Line attributes** | Integer | 2 | 0 – 65534 | 4 – 5 | Objekt-ID eines Line Attributes Objekts (Farbe, Breite, Stil). |
| [2] | **Width** | Integer | 2 | 0 – 65535 | 6 – 7 | Breite des umschließenden virtuellen Rechtecks. |
| [3] | **Height** | Integer | 2 | 0 – 65535 | 8 – 9 | Höhe des umschließenden virtuellen Rechtecks. |
| [4] | **Line Direction** | Integer | 1 | 0 oder 1 | 10 | 0 = Oben-Links nach Unten-Rechts<br>1 = Unten-Links nach Oben-Rechts. |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 11 | Anzahl der folgenden Makro-Referenzen. |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | Event ID, die das Makro auslöst. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Makro ID des auszuführenden Makros. |

## Funktionsweise und Geometrie
Die Linie wird innerhalb eines gedachten Rechtecks gespannt, das durch die Position des Objekts sowie `Width` und `Height` definiert ist.

*   **Line Direction 0:** Die Linie verläuft diagonal fallend.
    *   Startpunkt: (X, Y)
    *   Endpunkt: (X + Width - Line Width, Y + Height - Line Width)
*   **Line Direction 1:** Die Linie verläuft diagonal steigend.
    *   Startpunkt: (X, Y + Height - Line Width)
    *   Endpunkt: (X + Width - Line Width, Y)

## Ereignisse (Events - Tabelle B.26)

Das Output Line Objekt reagiert auf folgende Ereignisse:

*   **On Change End Point:** Wird ausgelöst, wenn die Geometrie der Linie geändert wird.
*   **On Change Attribute:** Wird ausgelöst, wenn sich die Linien-Eigenschaften (z. B. Farbe) ändern.
*   **On Change Size:** Reaktion auf Größenänderung (z. B. durch `Change Size` Kommando).
*   **On Refresh:** Wird ausgelöst, wenn das VT das Objekt neu zeichnen muss.

## Bedeutung für die Implementierung
Linien werden häufig als Trennelemente in Masken oder zur einfachen grafischen Darstellung von Zusammenhängen genutzt. Durch die Verknüpfung mit Variablen (über die Line Attributes) können Linien zur Laufzeit ihre Farbe ändern, um Zustände (z. B. Aktiv/Inaktiv) zu signalisieren.

Weitere Informationen und Beispiele finden sich im [ISOBUS Wiki - Line (Output)](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/line-output) von Tobias Tenberg.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*