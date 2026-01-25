# ID 33 – Auxiliary Control Designator Type 2 Object Pointer – ISO 11783-6 – J.4.7

```{index} single: ID 33 – Auxiliary Control Designator Type 2 Object Pointer – ISO 11783-6 – J.4.7
```

Das **Auxiliary Control Designator Type 2 Object Pointer** Objekt mit der **ID 33** ermöglicht es einer Working Set, die aktuell zugewiesenen Hilfsfunktionen (Auxiliary Functions) und deren Bedienelemente (Inputs) grafisch in einer Maske darzustellen.

### Attribute und Record Format (Tabelle J.6)

Die folgende Tabelle beschreibt den Aufbau des Auxiliary Control Designator Type 2 Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 33 | 3 | Objekttyp = Auxiliary Control Designator Type 2 Object Pointer. |
| [1] | **Pointer Type** | Integer | 1 | 0 – 3 | 4 | Typ der Referenz (siehe unten). |
| [2] | **Auxiliary Object ID** | Integer | 2 | 0 – 65534, 65535 | 5 – 6 | Objekt-ID einer Auxiliary Function (Type 2) oder eines Auxiliary Inputs (Type 2). |

### Pointer Types (AID 1)
*   **0:** Das VT zeigt den Designator des durch `Auxiliary Object ID` angegebenen Objekts.
*   **1:** Das VT zeigt den Designator des Objekts, das dem durch `Auxiliary Object ID` referenzierten Objekt zugewiesen ist (z. B. wenn AID 2 eine Funktion ist, wird der zugewiesene Input gezeigt).
*   **2:** Das VT zeigt den Designator des Working Sets, das Besitzer des durch `Auxiliary Object ID` angegebenen Objekts ist.
*   **3:** Das VT zeigt den Designator des Working Sets, das Besitzer des Objekts ist, welches dem durch `Auxiliary Object ID` referenzierten Objekt zugewiesen ist.

## Ereignisse (Events - Tabelle J.7)

Das Objekt reagiert auf folgende Ereignisse:

*   **On Change Value:** Wird ausgelöst, wenn die Zuweisung (Mapping) geändert wird oder das referenzierte Objekt geändert wird. Das VT aktualisiert die Anzeige.

## Nutzen für den Entwickler
Mit diesem Objekt kann eine grafische Übersicht erstellt werden, die dem Benutzer zeigt: "Diese Funktion auf meiner Maschine wird aktuell von Taste Y am Joystick Z gesteuert". Da die Zuweisung (Mapping) oft durch den Benutzer am Terminal erfolgt, erlaubt dieser Pointer eine dynamische Anzeige ohne Vorabwissen der ECU über die tatsächliche Belegung.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, Anhang J verwiesen.*