# ID 43 – External Object Pointer – ISO 11783-6 – B.24

Das **External Object Pointer** Objekt mit der **ID 43** (ab VT Version 5) ermöglicht es einer Working Set, Objekte anzuzeigen, die sich physisch im Objekt-Pool einer **anderen** Working Set befinden.

## Technische Attribute (gemäß Tabelle B.70)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer. |
| 0 | **Type** | Integer 1 | Objekttyp = 43 (External Object Pointer). |
| 1 | **Default Object ID** | Integer 2 | Lokales Ersatzobjekt (Fallback), falls die externe Referenz fehlschlägt. |
| 2 | **Ext. Ref. NAME ID** | Integer 2 | ID eines *External Reference NAME* Objekts (ID 42). |
| 3 | **External Object ID** | Integer 2 | ID des Ziel-Objekts im fremden Pool. |

## Funktionsweise und Regeln
*   **Anzeige:** Das Terminal sucht das Objekt im Pool der durch den NAME identifizierten ECU und zeichnet es an die Stelle des Pointers.
*   **Events/Macros:** Ereignisse (z. B. Tastendrücke) auf dem externen Objekt werden im Kontext der **besitzenden** ECU verarbeitet, nicht im Kontext der anzeigenden ECU.
*   **Sicherheit:** Das Ziel-Objekt muss durch die besitzende ECU via *External Object Definition* (ID 41) freigegeben worden sein.

## Anwendungsbeispiel
Ein Traktor (Working Set A) möchte in seiner Hauptmaske den Füllstand eines gezogenen Düngestreuers (Working Set B) anzeigen. Er nutzt dazu einen *External Object Pointer*, der auf die Füllstandsanzeige im Pool des Streuers verweist.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, B.24 verwiesen.*
