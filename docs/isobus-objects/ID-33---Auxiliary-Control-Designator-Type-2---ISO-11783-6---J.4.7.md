# ID 33 – Auxiliary Control Designator Type 2 Object Pointer – ISO 11783-6 – J.4.7

```{index} single: ID 33 – Auxiliary Control Designator Type 2 Object Pointer – ISO 11783-6 – J.4.7
```

Das **Auxiliary Control Designator Type 2 Object Pointer** Objekt mit der **ID 33** ermöglicht es einer Working Set, die aktuell zugewiesenen Hilfsfunktionen (Auxiliary Functions) und deren Bedienelemente (Inputs) grafisch in einer Maske darzustellen.

## 🎧 Podcast

* [Decoding Industrial Control: Function Blocks, Object-Oriented Principles, and the Power of IEC 61499](https://podcasters.spotify.com/pod/show/iec-61499-prime-course-en/episodes/Decoding-Industrial-Control-Function-Blocks--Object-Oriented-Principles--and-the-Power-of-IEC-61499-e3722d5)
* [ISOBUS Object Pointer: Das Geheimnis dynamischer Displays und effizienter Fehlerdiagnose](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Object-Pointer-Das-Geheimnis-dynamischer-Displays-und-effizienter-Fehlerdiagnose-e36bp75)
* [Eclipse 4diac: Revolutionizing Industrial Control with Open-Source Cyber-Physical Systems](https://podcasters.spotify.com/pod/show/eclipse-4diac-en/episodes/Eclipse-4diac-Revolutionizing-Industrial-Control-with-Open-Source-Cyber-Physical-Systems-e368lqu)
* [Simplifying Industrial Control: Your Deep Dive into Eclipse 4diac and IEC 61499](https://podcasters.spotify.com/pod/show/eclipse-4diac-en/episodes/Simplifying-Industrial-Control-Your-Deep-Dive-into-Eclipse-4diac-and-IEC-61499-e3681v8)
* [The Future of Industrial Control: Decoding IEC 61499](https://podcasters.spotify.com/pod/show/eclipse-4diac-en/episodes/The-Future-of-Industrial-Control-Decoding-IEC-61499-e36cjlj)

## 📺 Video

* [2025-02-21 15-23-28 logiBUS® mit Eclipse 4diac™ neues IO Konzept für alle Controller](https://www.youtube.com/watch?v=YUCodIng1UA)
* [2025-03-30 16-59-57 Verknüpfung von Object ID und Objektname](https://www.youtube.com/watch?v=FuZTizT48JU)
* [From Cable Chaos to Custom Control: How Logibus is Revolutionizing Agricultural Tech with Accessi...](https://www.youtube.com/watch?v=rAscABCk5ik)
* [From Control Box to Custom ISOBUS  A DIY Guide](https://www.youtube.com/watch?v=tlsRGZIfh9I)
* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mecha...](https://www.youtube.com/watch?v=wf_E1DcBOMY)

## Technische Attribute (gemäß Tabelle J.6)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer. |
| 0 | **Type** | Integer 1 | Objekttyp = 33 (Auxiliary Control Designator Type 2 Object Pointer). |
| 1 | **Pointer Type** | Integer 1 | Art der Verknüpfung (siehe unten). |
| 2 | **Auxiliary Object ID** | Integer 2 | Referenzierte Aux-Funktion oder Aux-Input ID. |

### Pointer Types
*   **0:** Zeigt den Designator des unter "Auxiliary Object ID" angegebenen Objekts.
*   **1:** Zeigt den Designator des Objekts, das dem referenzierten Objekt *zugewiesen* ist (z. B. zeige die Taste, die Funktion X steuert).
*   **2:** Zeigt den Designator des Working Sets (ECU), das dieses Objekt besitzt.
*   **3:** Zeigt den Designator des Working Sets, das dem referenzierten Objekt *zugewiesen* ist.

## Nutzen für den Entwickler
Mit diesem Objekt kann eine grafische Übersicht erstellt werden, die dem Benutzer zeigt: "Diese Funktion auf meiner Maschine wird aktuell von Taste Y am Joystick Z gesteuert". Da die Zuweisung (Mapping) oft durch den Benutzer am Terminal erfolgt, erlaubt dieser Pointer eine dynamische Anzeige ohne Vorabwissen der ECU über die tatsächliche Belegung.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, Anhang J verwiesen.*