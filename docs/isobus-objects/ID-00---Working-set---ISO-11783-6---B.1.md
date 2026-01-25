# ID 0 – Working set – ISO 11783-6 – B.1

```{index} single: ID 0 – Working set – ISO 11783-6 – B.1
```

![](https://user-images.githubusercontent.com/69573151/94337326-edc82080-ffe9-11ea-93d7-61752b51d9cf.png)

----

Das **Working Set** (Arbeitsset) Objekt mit der **ID 0** ist das zentrale Verwaltungselement einer Arbeitsgruppe (Working Set) im ISOBUS. Es definiert, wie sich die Arbeitsgruppe gegenüber dem Virtuellen Terminal (VT) präsentiert und welche Maske initial angezeigt wird.

## Wichtige Eigenschaften (gemäß ISO 11783-6, Anhang B.1)

Jede Arbeitsgruppe muss **genau ein** Working Set Objekt in ihrem Objektpool definieren. Nur das VT kann dieses Objekt aktivieren.

### Attribute und Record Format (Tabelle B.2)

Die folgende Tabelle beschreibt den Aufbau des Working Set Objekts im Objektpool (Byte-Stream).

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 0 | 3 | Objekttyp = Working Set. |
| [1] | **Background colour** | Integer | 1 | 0 – 255 | 4 | Hintergrundfarbe. |
| [2] | **Selectable** | Boolean | 1 | 0 oder 1 | 5 | 0 = FALSE, 1 = TRUE. Gibt an, ob das Working Set vom Bediener ausgewählt werden kann. |
| [3] | **Active mask** | Integer | 2 | 0 – 65534 | 6 – 7 | Objekt-ID der Data oder Alarm Mask, die angezeigt wird, wenn das Working Set aktiv ist. |
| - | **Number of objects to follow** | Integer | 1 | 1 – 255 | 8 | Anzahl der folgenden Kind-Objekte (Designator). Muss mindestens 1 sein. |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 9 | Anzahl der folgenden Makro-Referenzen. |
| - | **Number of languages to follow** | Integer | 1 | 0 – 255 | 10 | Anzahl der folgenden Sprachcodes. |
| - | **Repeat:** {Object ID} | Integer | 2 | 0 – 65534 | 11 + ... | Objekt-ID eines Kind-Objekts (Teil des Designators). Liste aller Objekte erfolgt *vor* den Makros. |
| - | {X Location} | Signed Integer | 2 | -32768 bis +32767 | 13 + ... | Relative X-Position des Kind-Objekts (Pixel). |
| - | {Y Location} | Signed Integer | 2 | -32768 bis +32767 | 15 + ... | Relative Y-Position des Kind-Objekts (Pixel). |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | (Nach den Objekten) Event ID, die das Makro auslöst. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Makro ID des auszuführenden Makros (oder Referenz auf 16-Bit Makro ID). |
| - | **Repeat:** {Language Code} | String | 2 | - | var. | (Nach den Makros) Zweistelliger Sprachcode gemäß ISO 639 (z.B. "de", "en"). |

### Designator (Child-Objekte)
Das Working Set Objekt dient als Container für eine grafische Kennung (Designator), die das Gerät repräsentiert (z. B. Icon und Name).
*   **Struktur:** Die unter `Number of objects to follow` angegebene Anzahl von Objekten folgt direkt im Record. Jedes Kind-Objekt wird durch ID, X-Pos und Y-Pos definiert.
*   **Platzbeschränkung:** Die Gesamtheit dieser Objekte muss in den Bereich eines **Softkeys** passen. Das VT schneidet alles ab, was über diesen Bereich hinausragt.
*   **Koordinaten:** Relativ zur oberen linken Ecke des Working Set Objekts.

### Makros (Events)
Das Working Set definiert Ereignisse, die Makros auslösen können. Siehe Tabelle B.1 für die Event-Definitionen.
*   **On Activate:** Ausgelöst bei Auswahl des Working Sets durch den Bediener.
*   **On Deactivate:** Ausgelöst beim Verlassen des Working Sets.
*   **On Change Active Mask:** Ausgelöst durch das Kommando `Change Active Mask`.

### Sprachenunterstützung
Die Liste der Sprachcodes (`Language Code`) informiert das VT, welche Sprachen das Working Set unterstützt. Jeder Code besteht aus 2 ASCII-Zeichen (z.B. "de", "en", "fr"). Dies dient der Information; die eigentliche Sprachumschaltung erfolgt durch das Laden entsprechender Sprach-Objekte oder Texte.

## Bedeutung für die Implementierung
Das Working Set Objekt ist der "Anker" einer Applikation auf dem VT. Ohne ein korrekt definiertes Objekt ID 0 kann das VT die Arbeitsgruppe nicht identifizieren oder die erste Maske laden. Entwickler müssen sicherstellen, dass die `Active mask` AID auf eine gültige Datenmaske im Pool verweist.

Weitere Informationen und Beispiele finden sich im [ISOBUS Wiki - Working Set](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/working-set) von Tobias Tenberg.

----
*Hinweis: Für detaillierte Implementierungsinformationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*