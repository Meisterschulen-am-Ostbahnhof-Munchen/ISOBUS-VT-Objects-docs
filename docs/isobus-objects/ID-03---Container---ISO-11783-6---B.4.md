# ID 3 – Container – ISO 11783-6 – B.4

```{index} single: ID 3 – Container – ISO 11783-6 – B.4
```

Das **Container** Objekt mit der **ID 3** dient dazu, mehrere Objekte logisch zu gruppieren. Ein Container selbst ist nicht sichtbar, ermöglicht aber das gemeinsame Verschieben, Ein-/Ausblenden oder Teilen einer gesamten Gruppe von Objekten.

### Attribute und Record Format (Tabelle B.8)

Die folgende Tabelle beschreibt den Aufbau des Container Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 3 | 3 | Objekttyp = Container. |
| [1] | **Width** | Integer | 2 | 0 – 65535 | 4 – 5 | Maximale Breite des Containers in Pixeln. Clipping erfolgt außerhalb dieses Bereichs. |
| [2] | **Height** | Integer | 2 | 0 – 65535 | 6 – 7 | Maximale Höhe des Containers in Pixeln. Clipping erfolgt außerhalb dieses Bereichs. |
| [3] | **Hidden** | Boolean | 1 | 0 oder 1 | 8 | 0 = FALSE (Sichtbar), 1 = TRUE (Versteckt). Gibt an, ob der Container initial ausgeblendet ist. |
| - | **Number of objects to follow** | Integer | 1 | 0 – 255 | 9 | Anzahl der direkt enthaltenen Objekte. |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 10 | Anzahl der folgenden Makro-Referenzen. |
| - | **Repeat:** {Object ID} | Integer | 2 | 0 – 65534 | 11 + ... | Objekt-ID eines enthaltenen Objekts. |
| - | {X Location} | Signed Integer | 2 | -32768 bis +32767 | 13 + ... | X-Position relativ zum Container (Pixel). |
| - | {Y Location} | Signed Integer | 2 | -32768 bis +32767 | 15 + ... | Y-Position relativ zum Container (Pixel). |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | (Nach Objekten) Event ID, die das Makro auslöst. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Makro ID des auszuführenden Makros. |

### Relative Positionierung und Clipping
Innerhalb eines Containers beginnt ein **eigenes Koordinatensystem**:
*   **Relative Koordinaten:** Die X- und Y-Positionen der Child-Objekte beziehen sich auf die obere linke Ecke des Containers.
*   **Clipping:** Alle Objekte oder Teile von Objekten, die außerhalb der durch `Width` und `Height` definierten Fläche liegen, werden vom VT abgeschnitten und nicht angezeigt.
*   **Gruppen-Verschiebung:** Wenn der Container verschoben wird (z. B. per `Change Child Position`), verschieben sich alle darin enthaltenen Objekte automatisch mit.

## Ereignisse (Events - Tabelle B.7)

Der Container reagiert auf folgende Ereignisse:

*   **On Show:** Ausgelöst durch das Kommando `Show Object` (auch wenn der Container bereits sichtbar ist). Das VT zeichnet die enthaltenen Objekte neu.
*   **On Hide:** Ausgelöst durch das Kommando `Hide Object`. Der Container wird mit der Hintergrundfarbe der Eltern-Maske überzeichnet.
*   **On Refresh:** Ausgelöst bei Änderungen an untergeordneten Objekten, die ein Neuzeichnen erfordern.
*   **On Change Child Location / Position:** Aktualisierung der Position von Kind-Objekten.
*   **On Change Size:** Reaktion auf Größenänderung des Containers.

## Nutzung in der Praxis
Container sind essenziell für dynamische Benutzeroberflächen:
*   **Ein-/Ausblenden:** Mit dem Kommando `IsoVtcCmd_ObjHideShow` können komplexe Bedienfelder oder Statusanzeigen auf Knopfdruck erscheinen oder verschwinden.
*   **Platzersparnis:** Mehrere Container können an der gleichen Stelle liegen; durch geschicktes Umschalten der Sichtbarkeit lassen sich verschiedene "Registerkarten" oder Modi realisieren.

### Beispiele aus dem ISO-Designer
![](https://user-images.githubusercontent.com/69573151/94602403-17f13b00-0295-11eb-8216-34070ca1bca8.png)
![](https://user-images.githubusercontent.com/69573151/94606853-5f7ac580-029b-11eb-9293-18570b481dbf.png)

## Bedeutung für die Implementierung
Da der Container ein logisches Element ist, verbraucht er selbst kaum Rechenleistung, ist aber mächtig in der Steuerung der Z-Order und Gruppierung. Entwickler sollten darauf achten, dass die `Width` und `Height` korrekt gesetzt sind, um ungewolltes Clipping zu vermeiden.

Weitere Informationen und Beispiele finden sich im [ISOBUS Wiki - Container](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/container) von Tobias Tenberg.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*