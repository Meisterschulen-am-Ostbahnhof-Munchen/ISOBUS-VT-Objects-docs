# ID 7 – Input boolean – ISO 11783-6 – B.8.2

```{index} single: ID 7 – Input boolean – ISO 11783-6 – B.8.2
```

Das **Input Boolean** Objekt mit der **ID 7** ermöglicht dem Bediener die Eingabe eines TRUE/FALSE-Wertes (z. B. in Form eines Kontrollkästchens).

## 🎧 Podcast

* ["Store Version" – Dein Schlüssel zur Verwaltung von Objektdatenpools im nichtflüchtigen VT-Speicher (ISO 11783-6)](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/Store-Version--Dein-Schlssel-zur-Verwaltung-von-Objektdatenpools-im-nichtflchtigen-VT-Speicher-ISO-11783-6-e36vfh0)
* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mechatronik](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISO-11783-6-Softkeys-und-das-Virtual-Terminal-verstehen--Dein-Schlssel-zur-Landmaschinen-Mechatronik-e36a8b0)
* [ISOBUS Skalierung: Wenn der Ackerschlepper-Bildschirm nicht passt – Eine Einführung in ISO 11783-6](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Skalierung-Wenn-der-Ackerschlepper-Bildschirm-nicht-passt--Eine-Einfhrung-in-ISO-11783-6-e36a8q6)
* [ISOBUS-Balkendiagramm: Das Output Linear Bar Graph Objekt der ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Balkendiagramm-Das-Output-Linear-Bar-Graph-Objekt-der-ISO-11783-6-entschlsselt-e36l0v2)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Bedienoberflchen-Wenn-Tasten-und-Hauptanzeige-unterschiedlich-skalieren--ISO-11783-6-entschlsselt-e36a8n8)

## 📺 Video

* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mecha...](https://www.youtube.com/watch?v=wf_E1DcBOMY)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 en...](https://www.youtube.com/watch?v=kQM4MLsyj5U)

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

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*