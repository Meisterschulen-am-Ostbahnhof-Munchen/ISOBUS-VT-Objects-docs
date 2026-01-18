# ISOBUS Objekte

```{index} single: ISOBUS Objekte
```

schauen Sie sich diesen Link genau an. 

## 🎧 Podcast

* [Das Working Set Objekt: Das Gehirn der ISOBUS-Bedienoberfläche verstehen – Von der Norm zur Praxis im ISO-Designer](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/Das-Working-Set-Objekt-Das-Gehirn-der-ISOBUS-Bedienoberflche-verstehen--Von-der-Norm-zur-Praxis-im-ISO-Designer-e36cl5v)
* [ISOBUS Button: Mehr als nur ein Klick – Die Standardisierung der Landtechnik](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Button-Mehr-als-nur-ein-Klick--Die-Standardisierung-der-Landtechnik-e3673rb)
* [ISOBUS Object Pointer: Das Geheimnis dynamischer Displays und effizienter Fehlerdiagnose](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Object-Pointer-Das-Geheimnis-dynamischer-Displays-und-effizienter-Fehlerdiagnose-e36bp75)
* [ISOBUS Output Meter: Dynamische Anzeigen meistern – vom Zeiger bis zur Visualisierung auf dem VT](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Output-Meter-Dynamische-Anzeigen-meistern--vom-Zeiger-bis-zur-Visualisierung-auf-dem-VT-e36t2tp)
* [ISOBUS Skalierung: Wenn der Ackerschlepper-Bildschirm nicht passt – Eine Einführung in ISO 11783-6](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Skalierung-Wenn-der-Ackerschlepper-Bildschirm-nicht-passt--Eine-Einfhrung-in-ISO-11783-6-e36a8q6)

## 📺 Video

* [Das Working Set Objekt: Das Gehirn der ISOBUS-Bedienoberfläche verstehen – Von der Norm zur Praxi...](https://www.youtube.com/watch?v=SiRvrecE_7I)
* [From Control Box to Custom ISOBUS  A DIY Guide](https://www.youtube.com/watch?v=tlsRGZIfh9I)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 en...](https://www.youtube.com/watch?v=kQM4MLsyj5U)
* [ISOBUS: The Secret Language](https://www.youtube.com/watch?v=Fezbc5Acd24)

## Programming

[Programming\_And\_Libraries](https://extranet.epec.fi/Public/Manuals/EPEC_Programming_And_Libraries/projecttopics/topic000962.htm)

künftig: [ISOBUS-Objekte-Versionen](ISOBUS-Objekte-Versionen.md)

ISOBUS Wiki von Tobias Tenberg:

* <https://isobus-studio.com/en/isobus-wiki>
* [ISOBUS Wiki - Colours](https://isobus-studio.com/isobus-wiki/isobus-colours)
* [ISOBUS Wiki - Objectpool Objects Database](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects-database)

Wie Sie sehen gibt es verschiedenen Objekte, aber nicht alle werden in jeder ISOBUS Version unterstützt. 

![](https://user-images.githubusercontent.com/69573151/94335435-08939880-ffdc-11ea-92e7-662f2ff7779f.png)

Wenn Sie mit ISO-Designer ein neues Projekt anlegen würden dann fragt er Sie nach dem "VT Level"

Wenn Sie in der AEF Datenbank nach Geräten suchen werden Sie sowas hier sehen:

![](https://user-images.githubusercontent.com/69573151/94335523-5f996d80-ffdc-11ea-9032-8de45bd5b318.png)

Was ist also der Unterschied zwischen UT und VT ? 

oder ist es etwa dasselbe ? 

ist VT 2.0 dasselbe wie UT 2.0 ? 

hier kommt die Auflösung:

## VT Levels

|   | ISO 11783-06 | Jetter ISO-Designer | UT laut AEF Datenbank | AUX laut AEF Datenbank |
| --- | --- | --- | --- | --- |
| 1 | Unbenannt | \< nicht wählbar > | \< nicht zertifizierbar> | kein AUX |
| 2 | VT Version 2 | VT Level 2 | UT 1.0 | AUX-O 1.0 |
| 3 | VT Version 3 | VT Level 3 | UT 2.0 | AUX-N 1.0 |
| 4 | VT Version 4 | VT Level 4 | UT 2.0  | AUX-N 1.0  |
| 5 | VT Version 5 | VT Level 5 | UT 2.0  | AUX-N 1.0  |
| 6 | VT Version 6 | VT Level 6 | UT 2.0  | AUX-N 1.0  |
| 7 | VT Version 7 | \< nicht wählbar > | UT 3.0   | AUX-N 1.0  |

man begann also mit der ersten Version der Norm, und veröffentlichte diese. 

in der 2. Version war von einem VT Version 2 die Rede ... und so fort. Schauen Sie das bitte in der Norm nach. 

die AEF hält sich nicht an dieses Schema, sondern führt für Marketingzwecke eigene Versionen ein. an UT 3.0 wird gerade gearbeitet, und wird wohl VT 4 und 5 einschließen. 

AUX ist in der ISOBUS Norm nur zum jeweiligen VT Standard erwähnt, die AEF hat daraus AUX-O und AUX-N gemacht.