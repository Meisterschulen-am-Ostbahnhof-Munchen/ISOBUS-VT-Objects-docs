# ID 25 – Fill attributes – ISO 11783-6 – B.14.4

```{index} single: ID 25 – Fill attributes – ISO 11783-6 – B.14.4
```

Das **Fill Attributes** Objekt mit der **ID 25** definiert, wie geschlossene geometrische Formen (Rechtecke, Ellipsen, Polygone) gefüllt werden.

## 🎧 Podcast

* ["Store Version" – Dein Schlüssel zur Verwaltung von Objektdatenpools im nichtflüchtigen VT-Speicher (ISO 11783-6)](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/Store-Version--Dein-Schlssel-zur-Verwaltung-von-Objektdatenpools-im-nichtflchtigen-VT-Speicher-ISO-11783-6-e36vfh0)
* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mechatronik](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISO-11783-6-Softkeys-und-das-Virtual-Terminal-verstehen--Dein-Schlssel-zur-Landmaschinen-Mechatronik-e36a8b0)
* [ISOBUS Skalierung: Wenn der Ackerschlepper-Bildschirm nicht passt – Eine Einführung in ISO 11783-6](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Skalierung-Wenn-der-Ackerschlepper-Bildschirm-nicht-passt--Eine-Einfhrung-in-ISO-11783-6-e36a8q6)
* [ISOBUS-Balkendiagramm: Das Output Linear Bar Graph Objekt der ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Balkendiagramm-Das-Output-Linear-Bar-Graph-Objekt-der-ISO-11783-6-entschlsselt-e36l0v2)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Bedienoberflchen-Wenn-Tasten-und-Hauptanzeige-unterschiedlich-skalieren--ISO-11783-6-entschlsselt-e36a8n8)

## 📺 Video

* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mecha...](https://www.youtube.com/watch?v=wf_E1DcBOMY)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 en...](https://www.youtube.com/watch?v=kQM4MLsyj5U)

## Technische Attribute (gemäß Tabelle B.50)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer im Objekt-Pool. |
| 0 | **Type** | Integer 1 | Objekttyp = 25 (Fill Attributes). |
| 1 | **Fill type** | Integer 1 | Art der Füllung: **0:** Keine, **1:** Linienfarbe, **2:** Eigene Farbe, **3:** Muster. |
| 2 | **Fill colour** | Integer 1 | Farbe der Füllung (nur bei Fill type = 2). |
| 3 | **Fill pattern** | Integer 2 | Verweis auf ein **Picture Graphic** Objekt (ID 20) als Muster. |

## Fülltypen und Logik
Über AID 1 wird gesteuert, welche Quelle für die Flächenfüllung genutzt wird:

*   **No Fill (0):** Die Fläche bleibt transparent; nur der Umriss (falls definiert) wird gezeichnet.
*   **Line Colour (1):** Die Fläche wird in derselben Farbe gefüllt wie die Umrandung (aus den Line Attributes).
*   **Specified Colour (2):** Es wird die in AID 2 definierte Farbe verwendet.
*   **Pattern (3):** Die Fläche wird mit einer sich wiederholenden Grafik gefüllt (Kachelung).

## Verwendung von Füllmustern (Wichtig!)
Wenn ein Muster (AID 3) verwendet wird, gelten strenge Regeln für die referenzierte Grafik:
*   **Ausrichtung:** Bei monochromen Grafiken muss die Breite durch 8 teilbar sein. Bei 16-Farben-Grafiken muss sie durch 2 teilbar sein.
*   **Reihenfolge:** Bei dynamischen Änderungen muss erst das `Fill pattern` und dann der `Fill type` gesetzt werden, um Fehler im VT zu vermeiden.
*   **Transparenz:** Wenn das Muster-Objekt selbst Transparenz enthält, scheint der Hintergrund der Maske durch das Muster hindurch.

## Ereignisse (Events - Tabelle B.49)
*   **On Change Fill Attributes:** Wird ausgelöst, wenn die Fülleigenschaften per ECU-Kommando `Change Fill Attributes` geändert werden. Alle betroffenen geometrischen Objekte werden sofort aktualisiert.

## Bedeutung für die Implementierung
Fill Attributes sind unverzichtbar für die Gestaltung der Benutzeroberfläche. Sie ermöglichen es, Flächen hervorzuheben (z. B. gelbe Füllung für einen Warnbereich in einem Balkendiagramm) oder texturierte Hintergründe zu schaffen. Durch den Wechsel des Fülltyps zur Laufzeit können Zustände (z. B. "Tank leer" -> rot blinkende Füllung) sehr auffällig visualisiert werden.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*