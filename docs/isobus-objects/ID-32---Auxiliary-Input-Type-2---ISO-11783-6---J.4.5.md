# ID 32 – Auxiliary Input Type 2 – ISO 11783-6 – J.4.5

```{index} single: ID 32 – Auxiliary Input Type 2 – ISO 11783-6 – J.4.5
```

Das **Auxiliary Input Type 2** Objekt mit der **ID 32** definiert ein physisches Bedienelement eines Auxiliary Input Geräts (z. B. eine Taste auf einem Joystick) ab VT Version 3.

## 🎧 Podcast

* ["Store Version" – Dein Schlüssel zur Verwaltung von Objektdatenpools im nichtflüchtigen VT-Speicher (ISO 11783-6)](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/Store-Version--Dein-Schlssel-zur-Verwaltung-von-Objektdatenpools-im-nichtflchtigen-VT-Speicher-ISO-11783-6-e36vfh0)
* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mechatronik](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISO-11783-6-Softkeys-und-das-Virtual-Terminal-verstehen--Dein-Schlssel-zur-Landmaschinen-Mechatronik-e36a8b0)
* [ISOBUS Skalierung: Wenn der Ackerschlepper-Bildschirm nicht passt – Eine Einführung in ISO 11783-6](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Skalierung-Wenn-der-Ackerschlepper-Bildschirm-nicht-passt--Eine-Einfhrung-in-ISO-11783-6-e36a8q6)
* [ISOBUS-Balkendiagramm: Das Output Linear Bar Graph Objekt der ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Balkendiagramm-Das-Output-Linear-Bar-Graph-Objekt-der-ISO-11783-6-entschlsselt-e36l0v2)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Bedienoberflchen-Wenn-Tasten-und-Hauptanzeige-unterschiedlich-skalieren--ISO-11783-6-entschlsselt-e36a8n8)

## 📺 Video

* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mecha...](https://www.youtube.com/watch?v=wf_E1DcBOMY)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 en...](https://www.youtube.com/watch?v=kQM4MLsyj5U)

## Technische Attribute (gemäß Tabelle J.4)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer. |
| 0 | **Type** | Integer 1 | Objekttyp = 32 (Auxiliary Input Type 2). |
| 1 | **Background colour** | Integer 1 | Hintergrundfarbe. |
| 2 | **Function attributes** | Integer 1 | Bitmaske für Eigenschaften (siehe unten). |
| - | **Number of objects** | Integer 1 | Anzahl der Designator-Objekte. |

### Function Attributes (Bitmaske)
*   **Bit 0–4:** Auxiliary function type (muss mit der Funktion übereinstimmen).
*   **Bit 5:** Critical Control (1 = kann sicherheitskritische Funktionen steuern).
*   **Bit 7:** Single-assignment (1 = kann nur einer einzigen Funktion zugewiesen werden).

### Wiederholung für Designator-Objekte:
| Name | Typ | Beschreibung |
| :--- | :--- | :--- |
| **Object ID** | Integer 2 | ID des Objekts für das Symbol. |
| **X Location** | Signed Int 2 | Relative X-Position. |
| **Y Location** | Signed Int 2 | Relative Y-Position. |

## Funktionsweise
Das Terminal nutzt diese Informationen, um dem Benutzer die verfügbaren Tasten und deren physikalische Eigenschaften anzuzeigen. Wenn der Benutzer eine Taste drückt, sendet das Eingabegerät eine Statusmeldung mit dem aktuellen Wert (Boolean oder Analog) an den ISOBUS.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, Anhang J verwiesen.*