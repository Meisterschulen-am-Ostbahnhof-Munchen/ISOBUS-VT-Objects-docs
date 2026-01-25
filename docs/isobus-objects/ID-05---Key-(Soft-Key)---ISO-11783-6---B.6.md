# ID 5 – Key (Soft Key) – ISO 11783-6 – B.6

```{index} single: ID 5 – Key (Soft Key) – ISO 11783-6 – B.6
```

![](https://user-images.githubusercontent.com/69573151/95071971-c7e9fc80-070a-11eb-8261-f87394d32fb4.png)

## 🎧 Podcast

* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mechatronik](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISO-11783-6-Softkeys-und-das-Virtual-Terminal-verstehen--Dein-Schlssel-zur-Landmaschinen-Mechatronik-e36a8b0)

----

Das **Key Objekt** (ID 5) definiert das Aussehen und den funktionalen Code eines Softkeys. Es ist das interaktive Element innerhalb einer Softkey-Maske.

### Attribute und Record Format (Tabelle B.12)

Die folgende Tabelle beschreibt den Aufbau des Key Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 5 | 3 | Objekttyp = Key. |
| [1] | **Background colour** | Integer | 1 | 0 – 255 | 4 | Hintergrundfarbe der Taste. |
| [2] | **Key code** | Integer | 1 | 1 – 255 | 5 | Code, der in der `Soft Key Activation` Nachricht gesendet wird. (0 ist für ACK reserviert). |
| - | **Number of objects to follow** | Integer | 1 | 0 – 255 | 6 | Anzahl der direkt enthaltenen Objekte (Symbole, Texte). |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 7 | Anzahl der folgenden Makro-Referenzen. |
| - | **Repeat:** {Object ID} | Integer | 2 | 0 – 65534 | 8 + ... | Objekt-ID eines enthaltenen Objekts. |
| - | {X Location} | Signed Integer | 2 | -32768 bis +32767 | 10 + ... | X-Position relativ zur Taste (Pixel). |
| - | {Y Location} | Signed Integer | 2 | -32768 bis +32767 | 12 + ... | Y-Position relativ zur Taste (Pixel). |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | (Nach Objekten) Event ID, die das Makro auslöst. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Makro ID des auszuführenden Makros. |

### Designator und Child-Objekte
Ein Key-Objekt fungiert als Container für die grafischen Inhalte der Taste (z. B. Symbole oder Texte).
*   **Koordinaten:** X- und Y-Positionen der Child-Objekte beziehen sich auf die obere linke Ecke des Softkey-Designators.
*   **Clipping:** Alle Objekte, die außerhalb des physischen Bereichs des Softkeys liegen, werden vom VT abgeschnitten. Da die Softkey-Größen variieren, sollten Inhalte zentral platziert werden.

## Ereignisse (Events - Tabelle B.11)

Das Key-Objekt reagiert auf folgende Ereignisse:

*   **On Key Press:** Ausgelöst beim Drücken der Taste. Sendet `Soft Key Activation`.
*   **On Key Release:** Ausgelöst beim Loslassen der Taste. Sendet `Soft Key Activation`.
*   **On Change Background Colour:** Reaktion auf Änderung der Tastenfarbe.
*   **On Change Child Location / Position:** Aktualisierung der grafischen Inhalte.
*   **On Change Attribute:** Reaktion auf generelle Attributänderungen.
*   **On Input Field Selection / De-selection:** Ausgelöst, wenn die Taste den Fokus erhält oder verliert (bei Navigation via Encoder/Cursor).

## Der Key Code
Der **Key Code** (AID 2) ist das entscheidende Bindeglied zur Softwarelogik (C-Code). Während die `Object ID` die Taste im Grafik-Pool identifiziert, nutzt die Applikation den `Key Code`, um die Funktion zuzuordnen. Dies erlaubt es, verschiedene grafische Tasten (unterschiedliche IDs) mit demselben funktionalen Code zu belegen.

## Bedeutung für die Implementierung
Da die tatsächliche Größe und Form der Softkeys von VT zu VT variieren kann (z. B. Hochformat vs. Querformat, Touch vs. Hardwaretasten), ist es Best Practice, grafische Inhalte (Bitmaps) innerhalb des Keys klein genug zu wählen und mittig zu positionieren. Ein Key-Objekt ohne Child-Objekte erscheint als leere Fläche in der gewählten Hintergrundfarbe.

Weitere Informationen und Beispiele finden sich im [ISOBUS Wiki - Softkey](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/softkey) von Tobias Tenberg.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*