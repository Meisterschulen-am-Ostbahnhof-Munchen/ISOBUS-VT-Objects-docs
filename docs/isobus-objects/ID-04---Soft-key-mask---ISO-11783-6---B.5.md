# ID 4 – Soft Key Mask – ISO 11783-6 – B.5

```{index} single: ID 4 – Soft Key Mask – ISO 11783-6 – B.5
```

Die **Soft Key Mask** (Softkey-Maske) mit der **ID 4** ist ein spezieller Container, der die Belegung der physischen oder virtuellen Softkeys am Rand des Terminals definiert. Sie wird in der Regel einer Datenmaske oder Alarmmaske fest zugeordnet.

## 🎧 Podcast

* ["Store Version" – Dein Schlüssel zur Verwaltung von Objektdatenpools im nichtflüchtigen VT-Speicher (ISO 11783-6)](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/Store-Version--Dein-Schlssel-zur-Verwaltung-von-Objektdatenpools-im-nichtflchtigen-VT-Speicher-ISO-11783-6-e36vfh0)
* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mechatronik](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISO-11783-6-Softkeys-und-das-Virtual-Terminal-verstehen--Dein-Schlssel-zur-Landmaschinen-Mechatronik-e36a8b0)
* [ISOBUS Skalierung: Wenn der Ackerschlepper-Bildschirm nicht passt – Eine Einführung in ISO 11783-6](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Skalierung-Wenn-der-Ackerschlepper-Bildschirm-nicht-passt--Eine-Einfhrung-in-ISO-11783-6-e36a8q6)
* [ISOBUS-Balkendiagramm: Das Output Linear Bar Graph Objekt der ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Balkendiagramm-Das-Output-Linear-Bar-Graph-Objekt-der-ISO-11783-6-entschlsselt-e36l0v2)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Bedienoberflchen-Wenn-Tasten-und-Hauptanzeige-unterschiedlich-skalieren--ISO-11783-6-entschlsselt-e36a8n8)

## 📺 Video

* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mecha...](https://www.youtube.com/watch?v=wf_E1DcBOMY)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 en...](https://www.youtube.com/watch?v=kQM4MLsyj5U)

## Technische Attribute (gemäß Tabelle B.10)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer im Objekt-Pool. |
| 0 | **Type** | Integer 1 | Objekttyp = 4 (Soft Key Mask). |
| 1 | **Background colour** | Integer 1 | Hintergrundfarbe der Softkey-Leiste. (Wird oft durch die Farbe der einzelnen Keys überschrieben). |

### Funktionsweise und Zuweisung
Eine Softkey-Maske enthält eine Liste von **Key Objekten** (ID 5) oder **Object Pointern**. 
*   **Reihenfolge:** Die Zuweisung zu den physischen Tasten am Terminal erfolgt strikt in der Reihenfolge, in der die Objekte in der Liste aufgeführt sind.
*   **NULL-Pointer:** Ein Verweis auf die Objekt-ID 65535 (NULL) reserviert eine Position, lässt den entsprechenden Softkey aber leer. Dies verhindert, dass nachfolgende Keys "nachrücken" und sorgt für ein konsistentes Layout.
*   **Paging:** Wenn mehr Keys definiert sind, als das VT gleichzeitig anzeigen kann, erstellt das VT automatisch Pfeiltasten zum Umblättern (Paging).

## Ereignisse (Events - Tabelle B.9)

*   **On Show:** Wird ausgelöst, wenn die Softkey-Maske (zusammen mit einer Datenmaske) eingeblendet wird. Alle enthaltenen Keys werden gezeichnet.
*   **On Hide:** Wird ausgelöst, wenn die Maske entfernt wird.
*   **On Change Background Colour:** Ermöglicht das Ändern der Hintergrundfarbe der gesamten Leiste.

## Zusammenspiel mit Datenmasken
Jede Datenmaske (ID 1) verweist auf eine Soft Key Mask (ID 4). 
*   Wird die Datenmaske gewechselt, wechselt das VT automatisch auch die Softkey-Belegung.
*   Über das Kommando `Change Soft Key Mask` kann die Belegung der Tasten auch zur Laufzeit geändert werden, ohne die Hauptmaske zu wechseln.

## Bedeutung für die Implementierung
Das Design der Softkey-Masken ist entscheidend für die Ergonomie. Entwickler sollten darauf achten, dass wichtige Funktionen (z. B. "Zurück" oder "Home") immer an der gleichen Position liegen. Durch den Einsatz von NULL-Pointern kann ein Springen der Tasten beim Wechsel zwischen verschiedenen Masken verhindert werden.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*