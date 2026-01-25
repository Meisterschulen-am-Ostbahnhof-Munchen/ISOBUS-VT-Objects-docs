# ID 21 – Number variable – ISO 11783-6 – B.13.2

```{index} single: ID 21 – Number variable – ISO 11783-6 – B.13.2
```

Das **Number Variable** Objekt mit der **ID 21** ist ein reines Datenobjekt. Es speichert einen numerischen Wert, der von anderen Anzeige- oder Eingabeobjekten referenziert werden kann.

### Attribute und Record Format (Tabelle B.43)

Die folgende Tabelle beschreibt den Aufbau des Number Variable Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 21 | 3 | Objekttyp = Number Variable. |
| [1] | **Value** | Integer | 4 | 0 – 2^32-1 | 4 – 7 | 32-Bit unsigned Integer-Wert. |

## Funktionsweise und Referenzierung
Variablen sind keine sichtbaren Objekte. Sie werden niemals direkt in eine Maske oder einen Container als "Child" eingefügt, sondern dienen als Datenquelle für andere Objekte:

*   **Referenzierung:** Objekte wie *Input Number* (ID 9), *Output Number* (ID 12) oder *Output Meter* (ID 17) verweisen über ihr Attribut `Variable reference` auf die ID einer Number Variable.
*   **Zentrale Datenhaltung:** Mehrere Anzeigeobjekte können dieselbe Variable referenzieren. Wird der Wert der Variable geändert, aktualisiert das VT automatisch alle betroffenen Anzeigen.

## Ereignisse (Events - Tabelle B.42)

Das Number Variable Objekt reagiert auf folgende Ereignisse:

*   **On Change Value:** Wird ausgelöst, wenn sich der Wert ändert (durch `Change Numeric Value` Befehl oder Eingabe des Bedieners). Das VT zeichnet alle Objekte neu, die diese Variable referenzieren.

## Bedeutung für die Implementierung
Number Variables sind das Rückgrat der Kommunikation zwischen Maschine und Terminal. 
*   **Effizienz:** Anstatt jedes Anzeigeobjekt einzeln zu aktualisieren, ändert die ECU nur den Wert der zentralen Variable.
*   **Konsistenz:** Durch die Verwendung von Variablen wird sichergestellt, dass an verschiedenen Stellen der Benutzeroberfläche (z. B. Hauptmaske und Einstellungsmenü) immer derselbe aktuelle Wert angezeigt wird.

Weitere Informationen und Beispiele finden sich im [ISOBUS Wiki - Number Variable](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/number-variable) von Tobias Tenberg.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*