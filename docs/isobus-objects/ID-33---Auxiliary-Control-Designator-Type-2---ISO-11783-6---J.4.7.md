# ID 33 – Auxiliary Control Designator Type 2 Object Pointer – ISO 11783-6 – J.4.7

```{index} single: ID 33 – Auxiliary Control Designator Type 2 Object Pointer – ISO 11783-6 – J.4.7
```

Das **Auxiliary Control Designator Type 2 Object Pointer** Objekt mit der **ID 33** ermöglicht es einer Working Set, die aktuell zugewiesenen Hilfsfunktionen (Auxiliary Functions) und deren Bedienelemente (Inputs) grafisch in einer Maske darzustellen.

## Technische Attribute (gemäß Tabelle J.6)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer. |
| 0 | **Type** | Integer 1 | Objekttyp = 33 (Auxiliary Control Designator Type 2 Object Pointer). |
| 1 | **Pointer Type** | Integer 1 | Art der Verknüpfung (siehe unten). |
| 2 | **Auxiliary Object ID** | Integer 2 | Referenzierte Aux-Funktion oder Aux-Input ID. |

### Pointer Types
*   **0:** Zeigt den Designator des unter "Auxiliary Object ID" angegebenen Objekts.
*   **1:** Zeigt den Designator des Objekts, das dem referenzierten Objekt *zugewiesen* ist (z. B. zeige die Taste, die Funktion X steuert).
*   **2:** Zeigt den Designator des Working Sets (ECU), das dieses Objekt besitzt.
*   **3:** Zeigt den Designator des Working Sets, das dem referenzierten Objekt *zugewiesen* ist.

## Nutzen für den Entwickler
Mit diesem Objekt kann eine grafische Übersicht erstellt werden, die dem Benutzer zeigt: "Diese Funktion auf meiner Maschine wird aktuell von Taste Y am Joystick Z gesteuert". Da die Zuweisung (Mapping) oft durch den Benutzer am Terminal erfolgt, erlaubt dieser Pointer eine dynamische Anzeige ohne Vorabwissen der ECU über die tatsächliche Belegung.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, Anhang J verwiesen.*
