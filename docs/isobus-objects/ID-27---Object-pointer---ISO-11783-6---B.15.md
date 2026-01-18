# ID 27 – Object pointer – ISO 11783-6 – B.15

```{index} single: ID 27 – Object pointer – ISO 11783-6 – B.15
```

Das **Object Pointer** Objekt mit der **ID 27** dient als dynamischer Platzhalter. Es ermöglicht es, an einer fest definierten Stelle in einer Maske oder einem Container das referenzierte Objekt zur Laufzeit auszutauschen.

## Technische Attribute (gemäß Tabelle B.55)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer im Objekt-Pool. |
| 0 | **Type** | Integer 1 | Objekttyp = 27 (Object Pointer). |
| 1 | **Value** | Integer 2 | Die Objekt-ID des aktuell anzuzeigenden Objekts (oder 65535 für NULL/unsichtbar). |

## Funktionsweise und Anwendung
Ein Object Pointer wird wie ein normales Child-Objekt in eine Maske eingebunden. Anstatt jedoch selbst etwas zu zeichnen, "leitet" er die Anzeige an das Objekt weiter, dessen ID in AID 1 gespeichert ist.

*   **Dynamischer Austausch:** Die ECU kann den `Value` (AID 1) per `Change Numeric Value` Kommando jederzeit ändern. Das VT blendet daraufhin das alte Objekt aus und das neue an derselben Stelle ein.
*   **Platzhalter-Funktion:** Er eignet sich hervorragend für Status-Icons (z. B. wechselnde Symbole für verschiedene Maschinenzustände), ohne dass mehrere Objekte übereinandergelegt und einzeln versteckt werden müssen.
*   **NULL-Pointer:** Wird der Wert auf 65535 gesetzt, wird an dieser Stelle nichts gezeichnet.

## Ereignisse (Events - Tabelle B.54)
*   **On Change Value:** Tritt ein, wenn die ECU die Ziel-Objekt-ID ändert. Das VT führt automatisch das "Hide" für das bisherige und das "Show" für das neue Objekt aus und aktualisiert die Maske.

## Bedeutung für die Implementierung
Object Pointer reduzieren die Komplexität der Maskensteuerung erheblich. Anstatt viele Objekte manuell per `Hide/Show` zu verwalten, muss die ECU nur eine einzige ID im Pointer ändern. Dies spart CAN-Bus-Bandbreite und vereinfacht die Programmlogik auf der Maschinensteuerung.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*