# ID 2 – Alarm Mask – ISO 11783-6 – B.3

Die **Alarm Mask** (Alarmmaske) mit der **ID 2** dient zur Anzeige kritischer Informationen oder Warnungen. Sie hat Vorrang vor normalen Datenmasken und kann je nach Priorität das gesamte Display oder Teile davon überlagern.

## Technische Attribute (gemäß Tabelle B.6)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer im Objekt-Pool. |
| 0 | **Type** | Integer 1 | Objekttyp = 2 (Alarm Mask). |
| 1 | **Background colour** | Integer 1 | Hintergrundfarbe der Maske. |
| 2 | **Soft Key Mask** | Integer 2 | Zugehörige Softkey-Maske (65535 = keine). |
| 3 | **Priority** | Integer 1 | Alarm-Priorität: **0 = High**, **1 = Medium**, **2 = Low**. |
| 4 | **Acoustic signal** | Integer 1 | Akustisches Signal: 0 = Höchste Prio, 1 = Mittel, 2 = Niedrig, 3 = Lautlos. |

### Prioritätsstufen und Darstellung
Die Priorität steuert nicht nur die Reihenfolge der Alarme, sondern oft auch deren visuelle Darstellung auf dem VT:

*   **High Priority (0):** Der Bediener ist in Gefahr oder es liegt eine schwere Fehlfunktion vor. Diese Alarme müssen sofort quittiert werden oder erzwingen den Fokus des Terminals.
*   **Medium Priority (1):** Normale Fehlfunktion der Maschine.
*   **Low Priority (2):** Nur zur Information (Statusmeldungen).

## Beispiele für Alarmmasken

### High Priority Alarm Mask (Priorität 0)
Wird oft für sicherheitskritische Warnungen verwendet.
![](https://user-images.githubusercontent.com/69573151/94601878-68b46400-0294-11eb-8eb6-2e652956ab6e.png)

### Medium Priority Alarm Mask (Priorität 1)
![](https://user-images.githubusercontent.com/69573151/94605730-cf884c00-0299-11eb-96e5-45c61989fc56.png)
![](https://user-images.githubusercontent.com/69573151/94601845-5cc8a200-0294-11eb-82a9-4d544eb7cb92.png)

### Low Priority Alarm Mask (Priorität 2)
![](https://user-images.githubusercontent.com/69573151/94605669-bb444f00-0299-11eb-95b0-30519cb9f03b.png)
![](https://user-images.githubusercontent.com/69573151/94601812-4e7a8600-0294-11eb-9a61-621ad998a191.png)

## Ereignisse (Events - Tabelle B.5)

*   **On Show:** Die Maske wird sichtbar. Das VT sendet eine `VT Status` Nachricht.
*   **On Change Priority:** Wenn die Priorität zur Laufzeit geändert wird, bewertet das VT alle aktiven Alarme neu und zeigt den Alarm mit der höchsten Priorität an.
*   **On Change Soft Key Mask:** Erlaubt den Wechsel der Softkeys bei aktivem Alarm.

## Verhalten bei mehreren Alarmen
Wenn mehrere Alarmmasken von verschiedenen Arbeitsgruppen gleichzeitig aktiv sind, bestimmt die Priorität (AID 3), welche Maske im Vordergrund steht. Bei gleicher Priorität liegt die Entscheidung meist beim VT (oft zeitliche Abfolge).

## Bedeutung für die Implementierung
Alarmmasken sollten sparsam und nur für echte Warnungen eingesetzt werden, da sie den Arbeitsfluss des Bedieners unterbrechen. Es ist wichtig, die passende akustische Unterstützung (AID 4) zu wählen, um die Aufmerksamkeit zu steuern, ohne den Bediener zu stressen.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*