# ID 22 – String variable – ISO 11783-6 – B.13.3

```{index} single: ID 22 – String variable – ISO 11783-6 – B.13.3
```

Das **String Variable** Objekt mit der **ID 22** dient zur Speicherung von Textzeichenfolgen, die von Anzeige- oder Eingabeobjekten referenziert werden können.

## 🎧 Podcast

* ["Store Version" – Dein Schlüssel zur Verwaltung von Objektdatenpools im nichtflüchtigen VT-Speicher (ISO 11783-6)](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/Store-Version--Dein-Schlssel-zur-Verwaltung-von-Objektdatenpools-im-nichtflchtigen-VT-Speicher-ISO-11783-6-e36vfh0)
* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mechatronik](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISO-11783-6-Softkeys-und-das-Virtual-Terminal-verstehen--Dein-Schlssel-zur-Landmaschinen-Mechatronik-e36a8b0)
* [ISOBUS Skalierung: Wenn der Ackerschlepper-Bildschirm nicht passt – Eine Einführung in ISO 11783-6](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Skalierung-Wenn-der-Ackerschlepper-Bildschirm-nicht-passt--Eine-Einfhrung-in-ISO-11783-6-e36a8q6)
* [ISOBUS-Balkendiagramm: Das Output Linear Bar Graph Objekt der ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Balkendiagramm-Das-Output-Linear-Bar-Graph-Objekt-der-ISO-11783-6-entschlsselt-e36l0v2)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Bedienoberflchen-Wenn-Tasten-und-Hauptanzeige-unterschiedlich-skalieren--ISO-11783-6-entschlsselt-e36a8n8)

## 📺 Video

* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mecha...](https://www.youtube.com/watch?v=wf_E1DcBOMY)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 en...](https://www.youtube.com/watch?v=kQM4MLsyj5U)

## Technische Attribute (gemäß Tabelle B.44)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer im Objekt-Pool. |
| 0 | **Type** | Integer 1 | Objekttyp = 22 (String Variable). |
| - | **Length** | Integer 2 | Maximale feste Länge der Zeichenkette in Bytes. |
| - | **Value** | String | Der aktuelle Textinhalt. Kürzere Texte werden mit Leerzeichen aufgefüllt. |

## Funktionsweise und Besonderheiten
Wie die *Number Variable* ist auch die *String Variable* ein reines Datenobjekt ohne eigene visuelle Darstellung.

*   **Feste Länge:** Die Länge der Variable wird bei der Erstellung im Pool festgelegt und kann zur Laufzeit nicht mehr vergrößert werden.
*   **Padding:** Wenn ein kürzerer String als die definierte Länge gespeichert wird, füllt das VT den Rest automatisch mit Leerzeichen auf.
*   **Datentypen:** Unterstützt sowohl 8-Bit Zeichen (Standard) als auch WideStrings (für Sonderzeichen). Die Steuerung (ECU) kann den Typ zur Laufzeit zwischen diesen Formaten umschalten.

## Referenzierung und Aktualisierung
*   **Referenzierung:** Objekte wie *Input String* (ID 8) oder *Output String* (ID 11) verweisen über ihr Attribut `Variable reference` auf die ID einer String Variable.
*   **Automatisches Redraw:** Sobald die ECU den Wert der Variable per `Change String Value` Kommando ändert, aktualisiert das VT automatisch alle sichtbaren Objekte, die diese Variable nutzen.

## Ereignisse (Events - Tabelle B.42)
*   **On Change Value:** Tritt bei jeder inhaltlichen Änderung des Textes ein und triggert die Aktualisierung der Anzeige.

## Bedeutung für die Implementierung
String Variablen sind essenziell für dynamische Texte wie Fehlermeldungen im Klartext, Namen von Arbeitsaufträgen oder Fahrernamen. Da Texteingaben und -änderungen über den CAN-Bus (ISOBUS) ressourcenintensiv sind, sollten String Variablen so kurz wie möglich definiert werden.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*