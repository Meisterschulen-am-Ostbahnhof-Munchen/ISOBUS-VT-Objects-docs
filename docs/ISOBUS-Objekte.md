# ISOBUS Objekte

schauen Sie sich diesen Link genau an. 

[Programming\_And\_Libraries](https://extranet.epec.fi/Public/Manuals/EPEC_Programming_And_Libraries/projecttopics/topic000962.htm)

Wie Sie sehen gibt es verschiedenen Objekte, aber nicht alle werden in jeder ISOBUS Version unterstützt. 

![](https://user-images.githubusercontent.com/69573151/94335435-08939880-ffdc-11ea-92e7-662f2ff7779f.png)

Wenn Sie mit ISO-Designer ein neues Projekt anlegen würden dann fragt er Sie nach dem "VT Level"

Wenn Sie in der AEF Datenbank nach Geräten suchen werden Sie sowas hier sehen:

![](https://user-images.githubusercontent.com/69573151/94335523-5f996d80-ffdc-11ea-9032-8de45bd5b318.png)

Was ist also der Unterschied zwischen UT und VT ? 

oder ist es etwa dasselbe ? 

ist VT 2.0 dasselbe wie UT 2.0 ? 

hier kommt die Auflösung:

|   | ISO 11783-06 | Jetter ISO-Designer | UT laut AEF Datenbank | AUX laut AEF Datenbank |
| --- | --- | --- | --- | --- |
| 1 | Unbenannt | \< nicht wählbar > | \< nicht zertifizierbar> | kein AUX |
| 2 | VT Version 2 | VT Level 2 | UT 1.0 | AUX-O 1.0 |
| 3 | VT Version 3 | VT Level 3 | UT 2.0 | AUX-N 1.0 |
| 4 | VT Version 4 | VT Level 4 |   |   |
| 5 | VT Version 5 | VT Level 5 |   |   |
| 6 | VT Version 6 | VT Level 6 |   |   |

man begann also mit der ersten Version der Norm, und veröffentlichte diese. 

in der 2. Version war von einem VT Version 2 die Rede ... und so fort. Schauen Sie das bitte in der Norm nach. 

die AEF hält sich nicht an dieses Schema, sondern führt für Marketingzwecke eigene Versionen ein. an UT 3.0 wird gerade gearbeitet, und wird wohl VT 4 und 5 einschließen. 

AUX ist in der ISOBUS Norm nur zum jeweiligen VT Standard erwähnt, die AEF hat daraus AUX-O und AUX-N gemacht.
