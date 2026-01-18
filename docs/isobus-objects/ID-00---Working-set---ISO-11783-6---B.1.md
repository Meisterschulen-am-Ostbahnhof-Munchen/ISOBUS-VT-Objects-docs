# ID 0 – Working set – ISO 11783-6 – B.1

```{index} single: ID 0 – Working set – ISO 11783-6 – B.1
```

![](https://user-images.githubusercontent.com/69573151/94337326-edc82080-ffe9-11ea-93d7-61752b51d9cf.png)

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

----

Das **Working Set** (Arbeitsset) Objekt mit der **ID 0** ist das zentrale Verwaltungselement einer Arbeitsgruppe (Working Set) im ISOBUS. Es definiert, wie sich die Arbeitsgruppe gegenüber dem Virtuellen Terminal (VT) präsentiert und welche Maske initial angezeigt wird.

## Wichtige Eigenschaften (gemäß ISO 11783-6, Anhang B.1)

Jede Arbeitsgruppe muss **genau ein** Working Set Objekt in ihrem Objektpool definieren. Nur das VT kann dieses Objekt aktivieren.

### Technische Attribute (Tabelle B.2)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige ID im Pool (immer ID 0 für das Working Set Objekt). |
| 0 | **Type** | Integer 1 | Objekttyp = 0 (Working Set). |
| 1 | **Background colour** | Integer 1 | Hintergrundfarbe des Working Set Designators. |
| 2 | **Selectable** | Boolean 1 | Bestimmt, ob der Bediener dieses Working Set manuell auswählen kann (0 = Nein, 1 = Ja). |
| 3 | **Active mask** | Integer 2 | Die Objekt-ID der Datenmaske (Data Mask) oder Alarmmaske, die angezeigt wird, wenn das Working Set aktiv wird. |

### Designator und Child-Objekte
Das Working Set Objekt fungiert als Container für eine kleine grafische Kennung (Designator), die z. B. in der Liste der verfügbaren Geräte oder in Alarmmeldungen angezeigt wird.
*   **Anzahl der Child-Objekte:** Muss mindestens 1 enthalten.
*   **Platzbeschränkung:** Die enthaltenen Objekte müssen in einen **Softkey-Designator** passen. Alles, was darüber hinausragt, wird vom VT abgeschnitten (Clipping).
*   **Positionierung:** X- und Y-Koordinaten der Child-Objekte beziehen sich auf die obere linke Ecke des Working Set Objekts.

## Ereignisse (Events - Tabelle B.1)

Das Working Set Objekt reagiert auf zentrale Statusänderungen:

*   **On Activate:** Wird ausgelöst, wenn der Bediener zu diesem Working Set wechselt. Das VT sendet eine `VT Status` Nachricht.
*   **On Deactivate:** Wird ausgelöst, wenn der Bediener zu einem anderen Working Set wechselt.
*   **On Change Active Mask:** Wird durch das Kommando `Change Active Mask` ausgelöst und wechselt die aktuell sichtbare Maske.

## Sprachenunterstützung
Das Objekt enthält eine Liste von Sprachcodes (z. B. "de", "en"), die das Working Set unterstützt. Dies ermöglicht dem VT, die passende Sprache für die Benutzeroberfläche auszuwählen.

## Bedeutung für die Implementierung
Das Working Set Objekt ist der "Anker" einer Applikation auf dem VT. Ohne ein korrekt definiertes Objekt ID 0 kann das VT die Arbeitsgruppe nicht identifizieren oder die erste Maske laden. Entwickler müssen sicherstellen, dass die `Active mask` AID auf eine gültige Datenmaske im Pool verweist.

----
*Hinweis: Für detaillierte Implementierungsinformationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*