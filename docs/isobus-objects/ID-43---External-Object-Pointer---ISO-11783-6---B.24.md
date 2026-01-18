# ID 43 – External Object Pointer – ISO 11783-6 – B.24

```{index} single: ID 43 – External Object Pointer – ISO 11783-6 – B.24
```

Das **External Object Pointer** Objekt mit der **ID 43** (ab VT Version 5) ermöglicht es einer Working Set, Objekte anzuzeigen, die sich physisch im Objekt-Pool einer **anderen** Working Set befinden.

## 🎧 Podcast

* [ISOBUS Object Pointer: Das Geheimnis dynamischer Displays und effizienter Fehlerdiagnose](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Object-Pointer-Das-Geheimnis-dynamischer-Displays-und-effizienter-Fehlerdiagnose-e36bp75)
* [Decoding Industrial Control: Function Blocks, Object-Oriented Principles, and the Power of IEC 61499](https://podcasters.spotify.com/pod/show/iec-61499-prime-course-en/episodes/Decoding-Industrial-Control-Function-Blocks--Object-Oriented-Principles--and-the-Power-of-IEC-61499-e3722d5)
* ["Store Version" – Dein Schlüssel zur Verwaltung von Objektdatenpools im nichtflüchtigen VT-Speicher (ISO 11783-6)](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/Store-Version--Dein-Schlssel-zur-Verwaltung-von-Objektdatenpools-im-nichtflchtigen-VT-Speicher-ISO-11783-6-e36vfh0)
* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mechatronik](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISO-11783-6-Softkeys-und-das-Virtual-Terminal-verstehen--Dein-Schlssel-zur-Landmaschinen-Mechatronik-e36a8b0)
* [ISOBUS Skalierung: Wenn der Ackerschlepper-Bildschirm nicht passt – Eine Einführung in ISO 11783-6](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Skalierung-Wenn-der-Ackerschlepper-Bildschirm-nicht-passt--Eine-Einfhrung-in-ISO-11783-6-e36a8q6)

## 📺 Video

* [2025-03-30 16-59-57 Verknüpfung von Object ID und Objektname](https://www.youtube.com/watch?v=FuZTizT48JU)
* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mecha...](https://www.youtube.com/watch?v=wf_E1DcBOMY)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 en...](https://www.youtube.com/watch?v=kQM4MLsyj5U)

## Technische Attribute (gemäß Tabelle B.70)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer. |
| 0 | **Type** | Integer 1 | Objekttyp = 43 (External Object Pointer). |
| 1 | **Default Object ID** | Integer 2 | Lokales Ersatzobjekt (Fallback), falls die externe Referenz fehlschlägt. |
| 2 | **Ext. Ref. NAME ID** | Integer 2 | ID eines *External Reference NAME* Objekts (ID 42). |
| 3 | **External Object ID** | Integer 2 | ID des Ziel-Objekts im fremden Pool. |

## Funktionsweise und Regeln
*   **Anzeige:** Das Terminal sucht das Objekt im Pool der durch den NAME identifizierten ECU und zeichnet es an die Stelle des Pointers.
*   **Events/Macros:** Ereignisse (z. B. Tastendrücke) auf dem externen Objekt werden im Kontext der **besitzenden** ECU verarbeitet, nicht im Kontext der anzeigenden ECU.
*   **Sicherheit:** Das Ziel-Objekt muss durch die besitzende ECU via *External Object Definition* (ID 41) freigegeben worden sein.

## Anwendungsbeispiel
Ein Traktor (Working Set A) möchte in seiner Hauptmaske den Füllstand eines gezogenen Düngestreuers (Working Set B) anzeigen. Er nutzt dazu einen *External Object Pointer*, der auf die Füllstandsanzeige im Pool des Streuers verweist.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, B.24 verwiesen.*