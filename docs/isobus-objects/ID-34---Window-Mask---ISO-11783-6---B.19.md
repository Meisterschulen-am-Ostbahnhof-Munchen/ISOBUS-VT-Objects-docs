# ID 34 – Window Mask – ISO 11783-6 – B.19

```{index} single: ID 34 – Window Mask – ISO 11783-6 – B.19
```

Das **Window Mask** Objekt mit der **ID 34** (eingeführt mit VT Version 4) ermöglicht es, einen Teilbereich des Bildschirms zu definieren, der unabhängig von der Haupt-Datenmaske aktualisiert oder von anderen Working Sets mit Inhalten gefüllt werden kann.

## 🎧 Podcast

* ["Store Version" – Dein Schlüssel zur Verwaltung von Objektdatenpools im nichtflüchtigen VT-Speicher (ISO 11783-6)](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/Store-Version--Dein-Schlssel-zur-Verwaltung-von-Objektdatenpools-im-nichtflchtigen-VT-Speicher-ISO-11783-6-e36vfh0)
* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mechatronik](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISO-11783-6-Softkeys-und-das-Virtual-Terminal-verstehen--Dein-Schlssel-zur-Landmaschinen-Mechatronik-e36a8b0)
* [ISOBUS Skalierung: Wenn der Ackerschlepper-Bildschirm nicht passt – Eine Einführung in ISO 11783-6](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Skalierung-Wenn-der-Ackerschlepper-Bildschirm-nicht-passt--Eine-Einfhrung-in-ISO-11783-6-e36a8q6)
* [ISOBUS-Balkendiagramm: Das Output Linear Bar Graph Objekt der ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Balkendiagramm-Das-Output-Linear-Bar-Graph-Objekt-der-ISO-11783-6-entschlsselt-e36l0v2)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Bedienoberflchen-Wenn-Tasten-und-Hauptanzeige-unterschiedlich-skalieren--ISO-11783-6-entschlsselt-e36a8n8)

## 📺 Video

* [2025-01-29 09-27-56 Windows Defender exclusion check in der Eclipse 4diac™ IDE](https://www.youtube.com/watch?v=8k8-QnbTPxk)
* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mecha...](https://www.youtube.com/watch?v=wf_E1DcBOMY)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 en...](https://www.youtube.com/watch?v=kQM4MLsyj5U)
* [unter Windows 10 mit 2 WLAN Verbindungen arbeiten](https://www.youtube.com/watch?v=a5Re1vOtmww)
* [Zwei WLANs gleichzeitig in Windows 10: Die geniale USB-Stick-Lösung für IoT-Geräte ohne Internet-...](https://www.youtube.com/watch?v=FyYy78XhWHE)

## Technische Attribute (gemäß Tabelle B.61)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer. |
| 0 | **Type** | Integer 1 | Objekttyp = 34 (Window Mask). |
| - | **Window Type** | Integer 1 | Vordefinierter Fenstertyp (0-18, siehe unten). |
| - | **Background colour** | Integer 1 | Hintergrundfarbe des Fensters. |
| - | **Options** | Bitmask 1 | Optionen (z. B. Rahmen, Sichtbarkeit). |
| - | **Number of objects** | Integer 1 | Anzahl der Kind-Objekte im Fenster. |

### Fenstertypen (Auszug aus B.19.2)
*   **0:** Free Form (Freie Gestaltung).
*   **1:** 1x1 Numeric Output mit Einheiten.
*   **3:** 1x1 String Output.
*   **9:** 1x1 Button.
*   (Typen 11-19 sind meist größere 2x1 Varianten).

## Funktionsweise
Window Masks sind essenziell für **User-Layout Data Masks**. Hierbei kann der Benutzer am Terminal selbst entscheiden, welche Informationen (Fenster) er an welcher Stelle sehen möchte. Eine ECU stellt die Window Masks zur Verfügung, und das Terminal übernimmt die Anordnung.

## Ereignisse (Events)
*   **On Refresh:** Wird ausgelöst, wenn das Fenster neu gezeichnet werden muss.
*   **On Change Attribute:** Bei Änderung technischer Parameter.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, B.19 verwiesen.*