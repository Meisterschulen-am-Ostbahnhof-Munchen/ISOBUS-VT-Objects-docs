# ID 27 – Object pointer – ISO 11783-6 – B.15

```{index} single: ID 27 – Object pointer – ISO 11783-6 – B.15
```

Das **Object Pointer** Objekt mit der **ID 27** dient als dynamischer Platzhalter. Es ermöglicht es, an einer fest definierten Stelle in einer Maske oder einem Container das referenzierte Objekt zur Laufzeit auszutauschen.

### Attribute und Record Format (Tabelle B.55)

Die folgende Tabelle beschreibt den Aufbau des Object Pointer Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 27 | 3 | Objekttyp = Object Pointer. |
| [1] | **Value** | Integer | 2 | 0 – 65534, 65535 | 4 – 5 | Objekt-ID des referenzierten Objekts oder NULL (65535). |

## Funktionsweise und Anwendung
Ein Object Pointer wird wie ein normales Child-Objekt in eine Maske eingebunden. Anstatt jedoch selbst etwas zu zeichnen, "leitet" er die Anzeige an das Objekt weiter, dessen ID in AID 1 gespeichert ist.

*   **Dynamischer Austausch:** Die ECU kann den `Value` (AID 1) per `Change Numeric Value` Kommando jederzeit ändern. Das VT blendet daraufhin das alte Objekt aus und das neue an derselben Stelle ein.
*   **Platzhalter-Funktion:** Er eignet sich hervorragend für Status-Icons (z. B. wechselnde Symbole für verschiedene Maschinenzustände), ohne dass mehrere Objekte übereinandergelegt und einzeln versteckt werden müssen.
*   **NULL-Pointer:** Wird der Wert auf 65535 gesetzt, wird an dieser Stelle nichts gezeichnet.

## Ereignisse (Events - Tabelle B.54)

Das Object Pointer Objekt reagiert auf folgende Ereignisse:

*   **On Change Value:** Wird ausgelöst durch das Kommando `Change Numeric Value`. Das VT versteckt das vorherige Objekt und zeigt das neue an. Die Eltern-Maske wird aktualisiert.

## Bedeutung für die Implementierung
Object Pointer reduzieren die Komplexität der Maskensteuerung erheblich. Anstatt viele Objekte manuell per `Hide/Show` zu verwalten, muss die ECU nur eine einzige ID im Pointer ändern. Dies spart CAN-Bus-Bandbreite und vereinfacht die Programmlogik auf der Maschinensteuerung.

Weitere Informationen und Beispiele finden sich im [ISOBUS Wiki - Object Pointer](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/object-pointer) von Tobias Tenberg.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*