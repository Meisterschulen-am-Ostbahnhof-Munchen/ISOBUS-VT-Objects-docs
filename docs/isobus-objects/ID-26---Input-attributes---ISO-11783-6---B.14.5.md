# ID 26 – Input attributes – ISO 11783-6 – B.14.5

```{index} single: ID 26 – Input attributes – ISO 11783-6 – B.14.5
```

Das **Input Attributes** Objekt mit der **ID 26** dient zur Validierung von Texteingaben. Es legt fest, welche Zeichen ein Bediener in ein verknüpftes *Input String* Objekt eingeben darf.

### Attribute und Record Format (Tabelle B.52)

Die folgende Tabelle beschreibt den Aufbau des Input Attributes Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 26 | 3 | Objekttyp = Input Attributes. |
| [1] | **Validation type** | Integer | 1 | 0 – 1 | 4 | 0=Erlaubte Zeichen (Liste), 1=Verbotene Zeichen (Liste). |
| - | **Length** | Integer | 1 | 0 – 255 | 5 | Länge des Validierungs-Strings in Bytes. |
| - | **Validation string** | String | Length | - | 6 ... | Liste der Zeichen (8-Bit String). |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | var. | Anzahl der folgenden Makro-Referenzen. |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | Event ID, die das Makro auslöst. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Makro ID des auszuführenden Makros. |

## Funktionsweise und Validierung
Das Objekt wirkt als Filter für die Tastatureingabe am VT:

*   **Referenzierung:** Ein *Input String* Objekt (ID 8) verweist auf dieses Objekt.
*   **Filter-Logik:** Wenn der `Validation type` auf 0 steht, lässt das VT nur die Zeichen zu, die im `Validation string` enthalten sind. Steht er auf 1, werden alle Zeichen außer den gelisteten akzeptiert.
*   **Einschränkung:** Dieses Objekt unterstützt ausschließlich **8-Bit Strings**. Wenn das verknüpfte Eingabefeld einen WideString verwendet, findet keine Validierung statt.

## Ereignisse (Events - Tabelle B.51)

Das Input Attributes Objekt reagiert auf folgende Ereignisse:

*   **On Change Value:** Wird ausgelöst durch das Kommando `Change String Value`. Das VT aktualisiert den Validierungs-String.

## Bedeutung für die Implementierung
Input Attributes sind ein wichtiges Werkzeug zur Vermeidung von Fehlbedienungen.
*   **Beispiel Numerisch:** Ein Validierungsstring "0123456789.," begrenzt ein Textfeld auf rein numerische Zeichen.
*   **Beispiel Sonderzeichen:** Verbot von Zeichen wie ";" oder "'", die in Datenbanken oder Dateisystemen Probleme verursachen könnten.

### Hinweis: Extended Input Attributes (ID 38)
Für die Validierung von WideStrings (Unicode) muss das *Extended Input Attributes* Objekt verwendet werden, welches die Definition ganzer Code-Bereiche (Code Planes) erlaubt.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*