# ID 47 – Working Set Special Controls – ISO 11783-6 – B.29

```{index} single: ID 47 – Working Set Special Controls – ISO 11783-6 – B.29
```

Das **Working Set Special Controls** Objekt mit der **ID 47** (ab VT Version 6) dient zur zentralen Steuerung von pool-weiten Einstellungen wie Farben und Sprachen.

## 🎧 Podcast

* ["Store Version" – Dein Schlüssel zur Verwaltung von Objektdatenpools im nichtflüchtigen VT-Speicher (ISO 11783-6)](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/Store-Version--Dein-Schlssel-zur-Verwaltung-von-Objektdatenpools-im-nichtflchtigen-VT-Speicher-ISO-11783-6-e36vfh0)
* [Das Working Set Objekt: Das Gehirn der ISOBUS-Bedienoberfläche verstehen – Von der Norm zur Praxis im ISO-Designer](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/Das-Working-Set-Objekt-Das-Gehirn-der-ISOBUS-Bedienoberflche-verstehen--Von-der-Norm-zur-Praxis-im-ISO-Designer-e36cl5v)
* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mechatronik](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISO-11783-6-Softkeys-und-das-Virtual-Terminal-verstehen--Dein-Schlssel-zur-Landmaschinen-Mechatronik-e36a8b0)
* [ISOBUS Skalierung: Wenn der Ackerschlepper-Bildschirm nicht passt – Eine Einführung in ISO 11783-6](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Skalierung-Wenn-der-Ackerschlepper-Bildschirm-nicht-passt--Eine-Einfhrung-in-ISO-11783-6-e36a8q6)
* [ISOBUS-Balkendiagramm: Das Output Linear Bar Graph Objekt der ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Balkendiagramm-Das-Output-Linear-Bar-Graph-Objekt-der-ISO-11783-6-entschlsselt-e36l0v2)

## 📺 Video

* [Das Working Set Objekt: Das Gehirn der ISOBUS-Bedienoberfläche verstehen – Von der Norm zur Praxi...](https://www.youtube.com/watch?v=SiRvrecE_7I)
* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mecha...](https://www.youtube.com/watch?v=wf_E1DcBOMY)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 en...](https://www.youtube.com/watch?v=kQM4MLsyj5U)

## Technische Attribute (gemäß Tabelle B.78)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer. |
| 0 | **Type** | Integer 1 | Objekttyp = 47 (Working Set Special Controls). |
| 1 | **Number of Bytes** | Integer 2 | Ermöglicht das Überspringen zukünftiger Erweiterungen. |
| 2 | **Colour Map ID** | Integer 2 | ID der initial zu verwendenden *Colour Map* (ID 39). |
| 3 | **Colour Palette ID** | Integer 2 | ID der initial zu verwendenden *Colour Palette* (ID 45). |
| - | **Num. of Lang. pairs** | Integer 1 | Anzahl der folgenden Sprach/Länder-Kürzel. |

### Sprachen-Liste (Wiederholung)
*   **Language Code:** 2-Buchstaben Code gemäß ISO 639-1 (z. B. "de", "en").
*   **Country Code:** 2-Buchstaben Code gemäß ISO 3166-1 (z. B. "DE", "US").

## Bedeutung
Dieses Objekt ist der zentrale Anlaufpunkt für das Terminal beim Laden des Pools. Es überschreibt beispielsweise die Sprachenliste im *Working Set* Objekt (ID 0), falls hier detailliertere Informationen hinterlegt sind. Es sorgt dafür, dass die richtigen Farben und Sprachen von der ersten Sekunde an korrekt geladen werden.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, B.29 verwiesen.*