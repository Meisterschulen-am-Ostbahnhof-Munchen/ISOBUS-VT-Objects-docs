# ID 40 – Object Label Reference List – ISO 11783-6 – B.21

```{index} single: ID 40 – Object Label Reference List – ISO 11783-6 – B.21
```

Das **Object Label Reference List** Objekt mit der **ID 40** (ab VT Version 5) wird verwendet, um Objekten (wie Variablen oder Eingabefeldern) eine Liste von Beschriftungsobjekten (Labels) zuzuordnen.

## 🎧 Podcast

* [Decoding Industrial Control: Function Blocks, Object-Oriented Principles, and the Power of IEC 61499](https://podcasters.spotify.com/pod/show/iec-61499-prime-course-en/episodes/Decoding-Industrial-Control-Function-Blocks--Object-Oriented-Principles--and-the-Power-of-IEC-61499-e3722d5)
* ["Store Version" – Dein Schlüssel zur Verwaltung von Objektdatenpools im nichtflüchtigen VT-Speicher (ISO 11783-6)](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/Store-Version--Dein-Schlssel-zur-Verwaltung-von-Objektdatenpools-im-nichtflchtigen-VT-Speicher-ISO-11783-6-e36vfh0)
* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mechatronik](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISO-11783-6-Softkeys-und-das-Virtual-Terminal-verstehen--Dein-Schlssel-zur-Landmaschinen-Mechatronik-e36a8b0)
* [ISOBUS Object Pointer: Das Geheimnis dynamischer Displays und effizienter Fehlerdiagnose](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Object-Pointer-Das-Geheimnis-dynamischer-Displays-und-effizienter-Fehlerdiagnose-e36bp75)
* [ISOBUS Skalierung: Wenn der Ackerschlepper-Bildschirm nicht passt – Eine Einführung in ISO 11783-6](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Skalierung-Wenn-der-Ackerschlepper-Bildschirm-nicht-passt--Eine-Einfhrung-in-ISO-11783-6-e36a8q6)

## 📺 Video

* [2025-03-30 16-59-57 Verknüpfung von Object ID und Objektname](https://www.youtube.com/watch?v=FuZTizT48JU)
* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mecha...](https://www.youtube.com/watch?v=wf_E1DcBOMY)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 en...](https://www.youtube.com/watch?v=kQM4MLsyj5U)

## Technische Attribute (gemäß Tabelle B.64)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer. |
| 0 | **Type** | Integer 1 | Objekttyp = 40 (Object Label Reference List). |
| - | **Number of objects** | Integer 1 | Anzahl der Referenzen in der Liste. |

### Struktur der Liste (Wiederholung)
*   **Object ID:** Die ID des Objekts, dem ein Label zugewiesen werden soll (z. B. ein *Input Number* Objekt).
*   **Label String Object ID:** Die ID eines *String Variable* oder *Output String* Objekts, das als Label fungiert.
*   **Font Attributes Object ID:** Optionale Schriftattribute für das Label.

## Bedeutung
Dieses Objekt hilft dem Terminal, kontextsensitive Hilfetexte oder Beschriftungen anzuzeigen, besonders wenn das Terminal selbst Layout-Entscheidungen trifft (z. B. in User-Layouts).

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, B.21 verwiesen.*