# ID 1 – Data mask – ISO 11783-6 – B.2

```{index} single: ID 1 – Data mask – ISO 11783-6 – B.2
```

![](https://user-images.githubusercontent.com/69573151/94337364-35e74300-ffea-11ea-8342-cb8bd452b89d.png)

## 🎧 Podcast

* ["Store Version" – Dein Schlüssel zur Verwaltung von Objektdatenpools im nichtflüchtigen VT-Speicher (ISO 11783-6)](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/Store-Version--Dein-Schlssel-zur-Verwaltung-von-Objektdatenpools-im-nichtflchtigen-VT-Speicher-ISO-11783-6-e36vfh0)
* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mechatronik](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISO-11783-6-Softkeys-und-das-Virtual-Terminal-verstehen--Dein-Schlssel-zur-Landmaschinen-Mechatronik-e36a8b0)
* [ISOBUS Skalierung: Wenn der Ackerschlepper-Bildschirm nicht passt – Eine Einführung in ISO 11783-6](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Skalierung-Wenn-der-Ackerschlepper-Bildschirm-nicht-passt--Eine-Einfhrung-in-ISO-11783-6-e36a8q6)
* [ISOBUS-Balkendiagramm: Das Output Linear Bar Graph Objekt der ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Balkendiagramm-Das-Output-Linear-Bar-Graph-Objekt-der-ISO-11783-6-entschlsselt-e36l0v2)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Bedienoberflchen-Wenn-Tasten-und-Hauptanzeige-unterschiedlich-skalieren--ISO-11783-6-entschlsselt-e36a8n8)

## 📺 Video

* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mecha...](https://www.youtube.com/watch?v=wf_E1DcBOMY)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 en...](https://www.youtube.com/watch?v=kQM4MLsyj5U)

----

Die **Data Mask** (Datenmaske) mit der **ID 1** ist das primäre Anzeigeelement für die Benutzeroberfläche einer Arbeitsgruppe. Sie dient als Hauptcontainer für alle visuellen Objekte (Buttons, Zahlenfelder, Grafiken), die dem Bediener auf dem Virtuellen Terminal (VT) angezeigt werden.

## Technische Attribute (gemäß Tabelle B.4)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer im Objekt-Pool. |
| 0 | **Type** | Integer 1 | Objekttyp = 1 (Data Mask). |
| 1 | **Background colour** | Integer 1 | Hintergrundfarbe der gesamten Maske. |
| 2 | **Soft Key Mask** | Integer 2 | Objekt-ID der zugehörigen Softkey-Maske. Diese wird automatisch mit der Datenmaske eingeblendet. (65535 = Keine Softkeys). |

### Struktur und Child-Objekte
Die Datenmaske definiert eine Liste von Objekten und deren absolute Position innerhalb der Maske.
*   **Objekt-Liste:** Jedes Child-Objekt besteht aus der `Object ID` (2 Byte) und der Position (`X Location`, `Y Location` je 2 Byte).
*   **Reihenfolge:** Objekte werden in der Reihenfolge gezeichnet, in der sie im Pool gelistet sind (Z-Order). Später gelistete Objekte überdecken früher gelistete.
*   **Positionierung:** Die Koordinaten beziehen sich auf die obere linke Ecke der Datenmaske.

## Ereignisse (Events - Tabelle B.3)

Die Datenmaske reagiert auf verschiedene Systemereignisse:

*   **On Show:** Wird ausgelöst, wenn die Maske auf dem Display erscheint. Das VT füllt den Bereich mit der Hintergrundfarbe und zeichnet alle Child-Objekte. Zudem wird eine `VT Status` Nachricht gesendet.
*   **On Hide:** Wird ausgelöst, wenn die Maske ausgeblendet wird (z. B. beim Wechsel zu einer anderen Maske).
*   **On Change Soft Key Mask:** Ermöglicht den dynamischen Wechsel der seitlichen Softkeys, während die Hauptmaske sichtbar bleibt.
*   **Pointing Events (Touch):** Bei VTs mit Touch-Unterstützung werden `Pointing Event press` und `Pointing Event release` Ereignisse ausgelöst und an die Arbeitsgruppe gemeldet.

## Verhalten und Einschränkungen
*   **Zusammenhang mit Softkeys:** Jede Datenmaske "besitzt" eine Softkey-Maske. Wenn die Datenmaske gewechselt wird, wechselt das VT in der Regel auch das Softkey-Layout.
*   **Refresh:** Wenn ein untergeordnetes Objekt (Child) geändert wird, sorgt das VT für ein Redraw der betroffenen Bereiche.
*   **Sichtbarkeit:** Es kann immer nur eine Datenmaske (oder Alarmmaske) pro Arbeitsgruppe aktiv und im Fokus des VT sein.

## Bedeutung für die Implementierung
Die Datenmaske ist das Herzstück des HMI-Designs. Entwickler müssen darauf achten, dass die Auflösung der Maske zu den Fähigkeiten des VTs passt (Standard-Mindestauflösung oft 200x200 Pixel, moderne VTs bieten deutlich mehr). Eine effiziente Nutzung von Makros auf Masken-Events (z. B. `On Show`) kann helfen, Initialisierungen direkt im VT auszuführen.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*