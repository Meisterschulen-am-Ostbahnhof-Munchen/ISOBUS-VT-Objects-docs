# ID 22 – String variable – ISO 11783-6 – B.13.3

```{index} single: ID 22 – String variable – ISO 11783-6 – B.13.3
```

Das **String Variable** Objekt mit der **ID 22** dient zur Speicherung von Textzeichenfolgen, die von Anzeige- oder Eingabeobjekten referenziert werden können.

### Attribute und Record Format (Tabelle B.44)

Die folgende Tabelle beschreibt den Aufbau des String Variable Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 22 | 3 | Objekttyp = String Variable. |
| - | **Length** | Integer | 2 | 0 – 65535 | 4 – 5 | Maximale feste Länge der Zeichenkette in Bytes. |
| - | **Value** | String | Length | - | 6 ... | String aus Zeichen. Muss mit Leerzeichen aufgefüllt werden, um die Länge zu erreichen. |

## Funktionsweise und Besonderheiten
Wie die *Number Variable* ist auch die *String Variable* ein reines Datenobjekt ohne eigene visuelle Darstellung.

*   **Feste Länge:** Die Länge der Variable wird bei der Erstellung im Pool festgelegt und kann zur Laufzeit nicht mehr vergrößert werden.
*   **Padding:** Wenn ein kürzerer String als die definierte Länge gespeichert wird, füllt das VT den Rest automatisch mit Leerzeichen auf.
*   **Datentypen:** Unterstützt sowohl 8-Bit Zeichen (Standard) als auch WideStrings (für Sonderzeichen). Die Steuerung (ECU) kann den Typ zur Laufzeit zwischen diesen Formaten umschalten.

## Referenzierung und Aktualisierung
*   **Referenzierung:** Objekte wie *Input String* (ID 8) oder *Output String* (ID 11) verweisen über ihr Attribut `Variable reference` auf die ID einer String Variable.
*   **Automatisches Redraw:** Sobald die ECU den Wert der Variable per `Change String Value` Kommando ändert, aktualisiert das VT automatisch alle sichtbaren Objekte, die diese Variable nutzen.

## Ereignisse (Events - Tabelle B.42)

Das String Variable Objekt reagiert auf folgende Ereignisse:

*   **On Change Value:** Wird ausgelöst, wenn sich der Wert ändert (durch `Change String Value` Befehl oder Eingabe des Bedieners). Das VT zeichnet alle Objekte neu, die diese Variable referenzieren.

## Bedeutung für die Implementierung
String Variablen sind essenziell für dynamische Texte wie Fehlermeldungen im Klartext, Namen von Arbeitsaufträgen oder Fahrernamen. Da Texteingaben und -änderungen über den CAN-Bus (ISOBUS) ressourcenintensiv sind, sollten String Variablen so kurz wie möglich definiert werden.

Weitere Informationen und Beispiele finden sich im [ISOBUS Wiki - String Variable](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/string-variable) von Tobias Tenberg.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*