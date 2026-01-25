# ID 40 – Object Label Reference List – ISO 11783-6 – B.21

```{index} single: ID 40 – Object Label Reference List – ISO 11783-6 – B.21
```

Das **Object Label Reference List** Objekt mit der **ID 40** (ab VT Version 5) wird verwendet, um Objekten (wie Variablen oder Eingabefeldern) eine Liste von Beschriftungsobjekten (Labels) zuzuordnen.

### Attribute und Record Format (Tabelle B.64)

Die folgende Tabelle beschreibt den Aufbau des Object Label Reference List Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 40 | 3 | Objekttyp = Object Label Reference List. |
| [1] | **Number of Labelled objects** | Integer | 2 | 0 – 65535 | 4 – 5 | Anzahl der folgenden Label-Zuweisungen. |
| - | **Repeat:** {Object ID} | Integer | 2 | 0 – 65534 | 6 – 7 ... | Objekt-ID des zu beschriftenden Objekts (z. B. Input Number). |
| - | {String Variable reference} | Integer | 2 | 0 – 65535 | 8 – 9 ... | Objekt-ID einer String Variable mit dem Labeltext (oder FFFFh = kein Text). |
| - | {Font type} | Integer | 1 | 0 – 255 | 10 ... | Schriftart (siehe Annex K). Ignoriert bei WideString oder NULL. |
| - | {Object Label graphic representation} | Integer | 2 | 0 – 65535 | 11 – 12 ... | Objekt-ID einer Grafik (Icon) für das Label (oder FFFFh = keine Grafik). |

## Bedeutung und Funktionsweise
Das Objekt dient dazu, anderen Objekten (z. B. Working Set, Input-Felder) einen Namen (Text) und ein Icon (Grafik) zuzuweisen. Diese "Labels" werden vom VT verwendet:
*   **Working Set Label:** Das Label für das Working Set Objekt wird in der Liste der aktiven Arbeitsgruppen angezeigt.
*   **Input Labels:** Bei Eingabefeldern zeigt das VT das Label (Text/Grafik) im Popup-Editor an, damit der Benutzer weiß, welchen Wert er gerade bearbeitet (z. B. "Sämenge" statt nur "120").

Es ist nur **eine** Object Label Reference List pro Objektpool erlaubt.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, B.21 verwiesen.*