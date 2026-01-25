# ID 43 – External Object Pointer – ISO 11783-6 – B.24

```{index} single: ID 43 – External Object Pointer – ISO 11783-6 – B.24
```

Das **External Object Pointer** Objekt mit der **ID 43** (ab VT Version 5) ermöglicht es einer Working Set, Objekte anzuzeigen, die sich physisch im Objekt-Pool einer **anderen** Working Set befinden.

### Attribute und Record Format (Tabelle B.70)

Die folgende Tabelle beschreibt den Aufbau des External Object Pointer Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 43 | 3 | Objekttyp = External Object Pointer. |
| [1] | **Default Object ID** | Integer | 2 | 0 – 65534, 65535 | 4 – 5 | ID eines lokalen Ersatzobjekts, falls externer Zugriff fehlschlägt. |
| [2] | **External Reference NAME ID** | Integer | 2 | 0 – 65534, 65535 | 6 – 7 | ID eines External Reference NAME Objekts, das das Ziel-WS identifiziert. |
| [3] | **External Object ID** | Integer | 2 | 0 – 65534, 65535 | 8 – 9 | ID des Objekts im fremden Pool. |

## Funktionsweise und Regeln
Das Objekt ermöglicht die Anzeige von Objekten aus fremden Objektpools.
*   **Anzeige:** Das Terminal sucht das Objekt im Pool der durch den NAME identifizierten ECU und zeichnet es an die Stelle des Pointers.
*   **Kontext:** Ereignisse (z. B. Button Press) und Makros werden im Kontext des **Original-Working-Sets** (Besitzer des Objekts) ausgeführt. Nachrichten (z. B. Button Activation) gehen an den Besitzer.
*   **Fallback:** Wenn das externe Objekt nicht gefunden wird, nicht freigegeben ist oder ungültig ist, wird das `Default Object` angezeigt.
*   **Sicherheit:** Das Ziel-Objekt muss durch die besitzende ECU via *External Object Definition* (ID 41) freigegeben worden sein.

## Ereignisse (Events - Tabelle B.69)

Das External Object Pointer Objekt reagiert auf folgende Ereignisse:

*   **On Change Attribute:** Wird ausgelöst durch das Kommando `Change Attribute`. Das VT evaluiert den Pointer neu und zeichnet ggf. neu.

## Anwendungsbeispiel
Ein Traktor (Working Set A) möchte in seiner Hauptmaske den Füllstand eines gezogenen Düngestreuers (Working Set B) anzeigen. Er nutzt dazu einen *External Object Pointer*, der auf die Füllstandsanzeige im Pool des Streuers verweist.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, B.24 verwiesen.*