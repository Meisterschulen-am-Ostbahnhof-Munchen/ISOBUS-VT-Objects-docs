# ID 38 – Extended Input Attributes – ISO 11783-6 – B.14.6

```{index} single: ID 38 – Extended Input Attributes – ISO 11783-6 – B.14.6
```

Das **Extended Input Attributes** Objekt mit der **ID 38** (ab VT Version 4) dient der Validierung von Texteingaben (Input String) bei Verwendung von **WideStrings** (Unicode).

## 🎧 Podcast

* ["Store Version" – Dein Schlüssel zur Verwaltung von Objektdatenpools im nichtflüchtigen VT-Speicher (ISO 11783-6)](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/Store-Version--Dein-Schlssel-zur-Verwaltung-von-Objektdatenpools-im-nichtflchtigen-VT-Speicher-ISO-11783-6-e36vfh0)
* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mechatronik](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISO-11783-6-Softkeys-und-das-Virtual-Terminal-verstehen--Dein-Schlssel-zur-Landmaschinen-Mechatronik-e36a8b0)
* [ISOBUS Skalierung: Wenn der Ackerschlepper-Bildschirm nicht passt – Eine Einführung in ISO 11783-6](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Skalierung-Wenn-der-Ackerschlepper-Bildschirm-nicht-passt--Eine-Einfhrung-in-ISO-11783-6-e36a8q6)
* [ISOBUS-Balkendiagramm: Das Output Linear Bar Graph Objekt der ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Balkendiagramm-Das-Output-Linear-Bar-Graph-Objekt-der-ISO-11783-6-entschlsselt-e36l0v2)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Bedienoberflchen-Wenn-Tasten-und-Hauptanzeige-unterschiedlich-skalieren--ISO-11783-6-entschlsselt-e36a8n8)

## 📺 Video

* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mecha...](https://www.youtube.com/watch?v=wf_E1DcBOMY)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 en...](https://www.youtube.com/watch?v=kQM4MLsyj5U)

## Technische Attribute (gemäß Tabelle B.53)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer. |
| 0 | **Type** | Integer 1 | Objekttyp = 38 (Extended Input Attributes). |
| 1 | **Validation type** | Integer 1 | 0 = Erlaubte Zeichen (Whitelist), 1 = Verbotene Zeichen (Blacklist). |
| - | **Number of code planes**| Integer 1 | Anzahl der Unicode-Ebenen (0-16). |

### Struktur der Code-Planes
Innerhalb jeder Code-Plane werden Bereiche von Zeichen definiert:
*   **Code plane number:** Die Nummer der Unicode-Ebene (z. B. 0 für die Basic Multilingual Plane).
*   **Number of character ranges:** Anzahl der folgenden Bereiche.
*   **First character / Last character:** Start und Ende des Zeichensatzes als WideChar (2 Byte).

## Bedeutung
Während das einfache *Input Attributes* Objekt (ID 26) nur 8-Bit Zeichen unterstützt, ermöglicht dieses Objekt die feingranulare Steuerung erlaubter Unicode-Zeichen, was besonders für den asiatischen oder kyrillischen Markt wichtig ist.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, B.14.6 verwiesen.*