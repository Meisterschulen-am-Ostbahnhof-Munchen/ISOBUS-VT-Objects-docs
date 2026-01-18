# ID 26 – Input attributes – ISO 11783-6 – B.14.5

```{index} single: ID 26 – Input attributes – ISO 11783-6 – B.14.5
```

Das **Input Attributes** Objekt mit der **ID 26** dient zur Validierung von Texteingaben. Es legt fest, welche Zeichen ein Bediener in ein verknüpftes *Input String* Objekt eingeben darf.

## Technische Attribute (gemäß Tabelle B.52)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer im Objekt-Pool. |
| 0 | **Type** | Integer 1 | Objekttyp = 26 (Input Attributes). |
| 1 | **Validation type** | Integer 1 | **0:** Erlaubte Zeichen (Allow-List), **1:** Verbotene Zeichen (Block-List). |
| - | **Length** | Integer 1 | Länge der Validierungs-Zeichenkette in Bytes. |
| - | **Validation string**| String | Die Liste der (in-)validen Zeichen. |

## Funktionsweise und Validierung
Das Objekt wirkt als Filter für die Tastatureingabe am VT:

*   **Referenzierung:** Ein *Input String* Objekt (ID 8) verweist auf dieses Objekt.
*   **Filter-Logik:** Wenn der `Validation type` auf 0 steht, lässt das VT nur die Zeichen zu, die im `Validation string` enthalten sind. Steht er auf 1, werden alle Zeichen außer den gelisteten akzeptiert.
*   **Einschränkung:** Dieses Objekt unterstützt ausschließlich **8-Bit Strings**. Wenn das verknüpfte Eingabefeld einen WideString verwendet, findet keine Validierung statt.

## Ereignisse (Events - Tabelle B.51)
*   **On Change Value:** Tritt ein, wenn die ECU den `Validation string` per Kommando ändert. Das VT passt die Eingabeprüfung für das aktive Feld sofort an.

## Bedeutung für die Implementierung
Input Attributes sind ein wichtiges Werkzeug zur Vermeidung von Fehlbedienungen.
*   **Beispiel Numerisch:** Ein Validierungsstring "0123456789.," begrenzt ein Textfeld auf rein numerische Zeichen.
*   **Beispiel Sonderzeichen:** Verbot von Zeichen wie ";" oder "'", die in Datenbanken oder Dateisystemen Probleme verursachen könnten.

### Hinweis: Extended Input Attributes (ID 38)
Für die Validierung von WideStrings (Unicode) muss das *Extended Input Attributes* Objekt verwendet werden, welches die Definition ganzer Code-Bereiche (Code Planes) erlaubt.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*
