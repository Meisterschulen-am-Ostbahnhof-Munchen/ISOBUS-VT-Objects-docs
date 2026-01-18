# ID 41 – External Object Definition – ISO 11783-6 – B.22

```{index} single: ID 41 – External Object Definition – ISO 11783-6 – B.22
```

Das **External Object Definition** Objekt mit der **ID 41** (ab VT Version 5) ist Teil des Mechanismus für **Working-Set-übergreifende Objektreferenzen**. Es definiert, welche Objekte eines eigenen Pools von anderen Working Sets referenziert werden dürfen.

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

## Technische Attribute (gemäß Tabelle B.66)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer. |
| 0 | **Type** | Integer 1 | Objekttyp = 41 (External Object Definition). |
| 1 | **Options** | Bitmask 1 | Bit 0 = Enabled (Freigabe der Referenzierung). |
| 2 | **NAME 0** | Integer 4 | Erste 4 Bytes des NAME-Attributs des Working Sets, das zugreifen darf. |
| 3 | **NAME 1** | Integer 4 | Letzte 4 Bytes des NAME-Attributs des berechtigten Working Sets. |
| - | **Number of objects** | Integer 1 | Anzahl der freigegebenen Objekte. |

## Funktionsweise
Damit Working Set A ein Objekt von Working Set B anzeigen kann (via *External Object Pointer*), muss Working Set B dieses Objekt explizit in einer *External Object Definition* für Working Set A freigeben. Dies dient der Sicherheit und Kontrolle über die eigenen Pool-Ressourcen.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, B.22 verwiesen.*