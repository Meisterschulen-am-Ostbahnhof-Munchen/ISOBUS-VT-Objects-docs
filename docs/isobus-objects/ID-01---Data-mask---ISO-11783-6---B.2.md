# ID 1 – Data mask – ISO 11783-6 – B.2

```{index} single: ID 1 – Data mask – ISO 11783-6 – B.2
```

![](https://user-images.githubusercontent.com/69573151/94337364-35e74300-ffea-11ea-8342-cb8bd452b89d.png)

----

Die **Data Mask** (Datenmaske) mit der **ID 1** ist das primäre Anzeigeelement für die Benutzeroberfläche einer Arbeitsgruppe. Sie dient als Hauptcontainer für alle visuellen Objekte (Buttons, Zahlenfelder, Grafiken), die dem Bediener auf dem Virtuellen Terminal (VT) angezeigt werden.

### Attribute und Record Format (Tabelle B.4)

Die folgende Tabelle beschreibt den Aufbau des Data Mask Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 1 | 3 | Objekttyp = Data mask. |
| [1] | **Background colour** | Integer | 1 | 0 – 255 | 4 | Hintergrundfarbe der Maske. |
| [2] | **Soft Key Mask** | Integer | 2 | 0 – 65534, 65535 | 5 – 6 | Objekt-ID der zugehörigen Soft Key Mask (65535 = NULL). |
| - | **Number of objects to follow** | Integer | 1 | 0 – 255 | 7 | Anzahl der direkt enthaltenen Objekte. |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 8 | Anzahl der folgenden Makro-Referenzen. |
| - | **Repeat:** {Object ID} | Integer | 2 | 0 – 65534 | 9 + ... | Objekt-ID eines enthaltenen Objekts. |
| - | {X Location} | Signed Integer | 2 | -32768 bis +32767 | 11 + ... | X-Position relativ zur Maske (Pixel). |
| - | {Y Location} | Signed Integer | 2 | -32768 bis +32767 | 13 + ... | Y-Position relativ zur Maske (Pixel). |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | (Nach Objekten) Event ID, die das Makro auslöst. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Makro ID des auszuführenden Makros. |

### Struktur und Child-Objekte
Die Datenmaske dient als Container für alle sichtbaren Elemente.
*   **Objekt-Liste:** Jedes Kind-Objekt wird mit seiner ID und seiner Position (X/Y) definiert. Jedes Set aus ID und Position belegt 6 Bytes.
*   **Reihenfolge:** Objekte werden in der gelisteten Reihenfolge gezeichnet (Z-Order). Höhere Indizes liegen über niedrigeren.
*   **Koordinaten:** Die Positionierung erfolgt absolut in VT-Pixeln, bezogen auf die obere linke Ecke der Maske (0,0).

## Ereignisse (Events - Tabelle B.3)

Die Datenmaske reagiert auf folgende Ereignisse:

*   **On Show:** Ausgelöst, wenn die Maske sichtbar wird. Das VT zeichnet den Hintergrund, die Kinder und die Soft Key Mask.
*   **On Hide:** Ausgelöst, wenn die Maske vom Display entfernt wird.
*   **On Refresh:** Ausgelöst bei Änderungen an Kind-Objekten, die ein Neuzeichnen erfordern.
*   **On Change Background Colour:** Reaktion auf eine Änderung der Hintergrundfarbe.
*   **On Change Soft Key Mask:** Reaktion auf den Wechsel der zugewiesenen Soft Key Mask.
*   **Pointing Events:** `press` und `release` bei Touch-Bedienung auf der Maskenfläche.

## Verhalten und Einschränkungen
*   **Zusammenhang mit Softkeys:** Jede Datenmaske "besitzt" eine Softkey-Maske. Wenn die Datenmaske gewechselt wird, wechselt das VT in der Regel auch das Softkey-Layout.
*   **Refresh:** Wenn ein untergeordnetes Objekt (Child) geändert wird, sorgt das VT für ein Redraw der betroffenen Bereiche.
*   **Sichtbarkeit:** Es kann immer nur eine Datenmaske (oder Alarmmaske) pro Arbeitsgruppe aktiv und im Fokus des VT sein.

## Bedeutung für die Implementierung
Die Datenmaske ist das Herzstück des HMI-Designs. Entwickler müssen darauf achten, dass die Auflösung der Maske zu den Fähigkeiten des VTs passt (Standard-Mindestauflösung oft 200x200 Pixel, moderne VTs bieten deutlich mehr). Eine effiziente Nutzung von Makros auf Masken-Events (z. B. `On Show`) kann helfen, Initialisierungen direkt im VT auszuführen.

Weitere Informationen und Beispiele finden sich im [ISOBUS Wiki - Data Mask](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/datamask) von Tobias Tenberg.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*