# ID 31 – Auxiliary Function Type 2 – ISO 11783-6 – J.4.3

```{index} single: ID 31 – Auxiliary Function Type 2 – ISO 11783-6 – J.4.3
```

Das **Auxiliary Function Type 2** Objekt mit der **ID 31** ist die moderne Definition für Hilfsfunktionen im ISOBUS (ab VT Version 3). Es bietet erweiterte Möglichkeiten zur Zuweisung von Bedienelementen.

## 🎧 Podcast

* [Decoding Industrial Control: Function Blocks, Object-Oriented Principles, and the Power of IEC 61499](https://podcasters.spotify.com/pod/show/iec-61499-prime-course-en/episodes/Decoding-Industrial-Control-Function-Blocks--Object-Oriented-Principles--and-the-Power-of-IEC-61499-e3722d5)
* [Decoding the E_SR Function Block: The Unsung Hero of Industrial Automation](https://podcasters.spotify.com/pod/show/iec-61499-prime-course-en/episodes/Decoding-the-E_SR-Function-Block-The-Unsung-Hero-of-Industrial-Automation-e3681qo)
* [Function Blocks The Future of Automation](https://podcasters.spotify.com/pod/show/iec-61499-prime-course-en/episodes/Function-Blocks-The-Future-of-Automation-e3722k9)
* ["Store Version" – Dein Schlüssel zur Verwaltung von Objektdatenpools im nichtflüchtigen VT-Speicher (ISO 11783-6)](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/Store-Version--Dein-Schlssel-zur-Verwaltung-von-Objektdatenpools-im-nichtflchtigen-VT-Speicher-ISO-11783-6-e36vfh0)
* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mechatronik](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISO-11783-6-Softkeys-und-das-Virtual-Terminal-verstehen--Dein-Schlssel-zur-Landmaschinen-Mechatronik-e36a8b0)

## 📺 Video

* [Frustration to Function  Agri Tech s Evolution](https://www.youtube.com/watch?v=SNnJKxEPUpA)
* [Function Blocks  The Future of Automation](https://www.youtube.com/watch?v=0Lo2AsQIEzA)
* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mecha...](https://www.youtube.com/watch?v=wf_E1DcBOMY)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 en...](https://www.youtube.com/watch?v=kQM4MLsyj5U)

## Technische Attribute (gemäß Tabelle J.2)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer. |
| 0 | **Type** | Integer 1 | Objekttyp = 31 (Auxiliary Function Type 2). |
| 1 | **Background colour** | Integer 1 | Hintergrundfarbe. |
| 2 | **Function attributes** | Integer 1 | Bitmaske für Eigenschaften (siehe unten). |
| - | **Number of objects** | Integer 1 | Anzahl der Designator-Objekte. |

### Function Attributes (Bitmaske)
*   **Bit 0–4:** Auxiliary function type (z. B. 0=Latching Boolean, 1=Analogue, etc. gemäß Tabelle J.5).
*   **Bit 5:** Critical Control (0 = unkritisch, 1 = sicherheitskritisch gemäß ISO 15077).
*   **Bit 6:** Assignment Restriction (0 = frei zuweisbar, 1 = eingeschränkt durch Preferred Assignment).
*   **Bit 7:** Single-assignment (1 = darf nur alleine auf einen Input gelegt werden).

### Wiederholung für Designator-Objekte:
| Name | Typ | Beschreibung |
| :--- | :--- | :--- |
| **Object ID** | Integer 2 | ID des Objekts für das Symbol. |
| **X Location** | Signed Int 2 | Relative X-Position. |
| **Y Location** | Signed Int 2 | Relative Y-Position. |

## Besonderheiten
Dieses Objekt wird aktiv für das "Auxiliary Mapping" im Terminal genutzt. Es erlaubt der ECU, dem Terminal mitzuteilen, welche Funktionen (z. B. "Heber auf/ab") zur Verfügung stehen, damit der Benutzer diese auf Tasten oder Joysticks legen kann.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, Anhang J verwiesen.*