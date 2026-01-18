# ID 23 – Font attributes – ISO 11783-6 – B.14.2

```{index} single: ID 23 – Font attributes – ISO 11783-6 – B.14.2
```

Das **Font Attributes** Objekt mit der **ID 23** definiert das Erscheinungsbild von Texten (Schriftart, Größe, Farbe, Stil). Es ist ein zentrales Attribut-Objekt, das von allen textbasierten Anzeige- und Eingabeobjekten referenziert wird.

## 🎧 Podcast

* ["Store Version" – Dein Schlüssel zur Verwaltung von Objektdatenpools im nichtflüchtigen VT-Speicher (ISO 11783-6)](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/Store-Version--Dein-Schlssel-zur-Verwaltung-von-Objektdatenpools-im-nichtflchtigen-VT-Speicher-ISO-11783-6-e36vfh0)
* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mechatronik](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISO-11783-6-Softkeys-und-das-Virtual-Terminal-verstehen--Dein-Schlssel-zur-Landmaschinen-Mechatronik-e36a8b0)
* [ISOBUS Skalierung: Wenn der Ackerschlepper-Bildschirm nicht passt – Eine Einführung in ISO 11783-6](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Skalierung-Wenn-der-Ackerschlepper-Bildschirm-nicht-passt--Eine-Einfhrung-in-ISO-11783-6-e36a8q6)
* [ISOBUS-Balkendiagramm: Das Output Linear Bar Graph Objekt der ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Balkendiagramm-Das-Output-Linear-Bar-Graph-Objekt-der-ISO-11783-6-entschlsselt-e36l0v2)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Bedienoberflchen-Wenn-Tasten-und-Hauptanzeige-unterschiedlich-skalieren--ISO-11783-6-entschlsselt-e36a8n8)

## 📺 Video

* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mecha...](https://www.youtube.com/watch?v=wf_E1DcBOMY)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 en...](https://www.youtube.com/watch?v=kQM4MLsyj5U)

## Technische Attribute (gemäß Tabelle B.46)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer im Objekt-Pool. |
| 0 | **Type** | Integer 1 | Objekttyp = 23 (Font Attributes). |
| 1 | **Font colour** | Integer 1 | Textfarbe (Farbindex 0-255). |
| 2 | **Font size** | Integer 1 | Schriftgröße (0-14 für Fixfonts, oder Pixelhöhe für Proportionalfonts). |
| 3 | **Font type** | Integer 1 | Schriftart-Index (siehe ISO-Norm Tabelle K.1). |
| 4 | **Font style** | Bitmask 1 | Stil-Optionen (Fett, Kursiv, Unterstrichen, Blinken, Proportional). |

## Schriftgrößen und Render-Modi
Die Interpretation von AID 2 hängt stark von Bit 7 in den `Font style` Optionen ab:

### Nicht-proportionale Schriftarten (Bit 7 = 0)
Hier werden vordefinierte Rastergrößen verwendet (Breite x Höhe in Pixeln):
*   **0:** 6x8, **1:** 8x8, **2:** 8x12, **3:** 12x16, **4:** 16x16, **5:** 16x24, **6:** 24x32, ..., **14:** 128x192.

### Proportionale Schriftarten (Bit 7 = 1)
In diesem Modus repräsentiert der Wert in AID 2 direkt die **Schrifthöhe in Pixeln**. Die Breite der einzelnen Zeichen variiert (ein 'i' ist schmaler als ein 'W'). Dies ermöglicht eine modernere und besser lesbare Textdarstellung.

## Stil-Optionen (AID 4)
Mehrere Stile können durch Kombination der Bits gleichzeitig aktiviert werden:
*   **Bit 0:** Fett (Bold)
*   **Bit 3:** Kursiv (Italic)
*   **Bit 2:** Unterstrichen (Underlined)
*   **Bit 4:** Invertiert (Tauscht Vorder- und Hintergrundfarbe)
*   **Bit 5/6:** Blinken (In verschiedenen Varianten)
*   **Bit 7:** Proportionaler Modus (Wichtig für modernes Design)

## Ereignisse (Events - Tabelle B.45)
*   **On Change Font Attributes:** Wird ausgelöst, wenn die Schrifteigenschaften per ECU-Kommando `Change Font Attributes` geändert werden. Das VT aktualisiert daraufhin alle betroffenen Textobjekte.

## Bedeutung für die Implementierung
Font Attributes erlauben ein konsistentes Design. Anstatt bei jedem Textobjekt Farbe und Größe einzeln zu definieren, verweisen alle Objekte auf ein gemeinsames Attribut-Objekt. Ändert man dieses eine Objekt (z. B. von weißer auf gelbe Schrift), ändert sich das gesamte HMI-Erscheinungsbild sofort.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*