# ID 29 – Auxiliary Function Type 1 – ISO 11783-6 – J.4.2

```{index} single: ID 29 – Auxiliary Function Type 1 – ISO 11783-6 – J.4.2
```

Das **Auxiliary Function Type 1** Objekt mit der **ID 29** definiert die Attribute und das Design eines Hilfsfunktions-Bedienelements (Auxiliary Function). 

*Hinweis: Dieses Objekt gilt ab VT Version 3 als veraltet (obsolete) und wird durch den Typ 2 (ID 31) ersetzt. Es sollte in neuen Projekten nicht mehr verwendet werden.*

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

## Technische Attribute (gemäß Tabelle J.1)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer. |
| 0 | **Type** | Integer 1 | Objekttyp = 29 (Auxiliary Function Type 1). |
| - | **Background colour** | Integer 1 | Hintergrundfarbe. |
| - | **Function type** | Integer 1 | 0 = Latching Boolean (schaltend), 1 = Analogue, 2 = Non-latching Boolean (tastend). |
| - | **Number of objects** | Integer 1 | Anzahl der folgenden Objekte, die das Designator-Symbol bilden. |

### Wiederholung für Designator-Objekte:
| Name | Typ | Beschreibung |
| :--- | :--- | :--- |
| **Object ID** | Integer 2 | ID eines Grafik-, Form- oder Ausgabefelds. |
| **X Location** | Signed Int 2 | Relative X-Position im Designator-Bereich. |
| **Y Location** | Signed Int 2 | Relative Y-Position im Designator-Bereich. |

## Funktionsweise
Das VT nutzt diese Attribute, um die Zuweisung zu einem kompatiblen Auxiliary Input zu erzwingen. Das Designator-Symbol muss in den Bereich eines Softkeys passen; überstehende Teile werden abgeschnitten (Clipped).

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, Anhang J verwiesen.*