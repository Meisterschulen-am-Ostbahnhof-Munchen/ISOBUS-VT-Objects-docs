# ID 7 – Input boolean – ISO 11783-6 – B.8.2

```{index} single: ID 7 – Input boolean – ISO 11783-6 – B.8.2
```

Das **Input Boolean** Objekt mit der **ID 7** ermöglicht dem Bediener die Eingabe eines TRUE/FALSE-Wertes (z. B. in Form eines Kontrollkästchens).

## Technische Attribute (gemäß Tabelle B.16)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer im Objekt-Pool. |
| 0 | **Type** | Integer 1 | Objekttyp = 7 (Input Boolean). |
| 1 | **Background colour** | Integer 1 | Hintergrundfarbe des Eingabefeldes. |
| 2 | **Width** | Integer 2 | Breite und Höhe des quadratischen Feldes in Pixeln. |
| 3 | **Foreground colour** | Integer 2 | **Object ID eines Font Attributes Objekts**. Hier wird nur die Schriftfarbe für die Darstellung des Indikators (z. B. das Häkchen) verwendet. |
| 4 | **Variable reference** | Integer 2 | ID eines **Number Variable** Objekts. Der Wert wird dort gespeichert. (65535 = direkter Wert in AID 5). |
| 5 | **Value** | Integer 1 | Aktueller Wert: 0 = FALSE, >0 = TRUE. (Nur aktiv, wenn AID 4 = NULL). |
| 6 | **Enabled** | Integer 1 | Status: 0 = Deaktiviert, 1 = Aktiviert. |

## Funktionsweise und Darstellung
Das VT ist für die grafische Darstellung des Zustands verantwortlich (z. B. ein Kreuz oder Haken).
*   **Zustand FALSE (0):** Das Feld wird in der Hintergrundfarbe (AID 1) dargestellt.
*   **Zustand TRUE (>0):** Der Indikator wird mit der Vordergrundfarbe (aus dem Font Attribute Objekt AID 3) gezeichnet.
*   **Wertebereich:** In neueren VT-Versionen gilt jeder Wert größer als 0 als TRUE. Bei einer Änderung sendet das VT jedoch standardmäßig nur 0 oder 1 an die Arbeitsgruppe.

## Ereignisse (Events - Tabelle B.15)
Wie alle Eingabeobjekte reagiert das Input Boolean auf:
*   **On Input Field Selection:** Wenn der Bediener das Feld zur Bearbeitung auswählt.
*   **On Entry of Value:** Sobald der Bediener die Änderung bestätigt (z. B. durch Drücken von ENTER). Das VT sendet eine `VT Change Numeric Value` Nachricht.

## Bedeutung für die Implementierung
Das Input Boolean ist ideal für einfache Ja/Nein-Optionen oder das Aktivieren/Deaktivieren von Maschinenfunktionen. Da die grafische Ausprägung (Häkchen-Stil) vom VT-Hersteller abhängt, sorgt dieses Objekt für ein konsistentes Erscheinungsbild innerhalb der Terminal-Oberfläche.

Weitere Informationen und Beispiele finden sich im [ISOBUS Wiki - Boolean](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/boolean) von Tobias Tenberg.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*