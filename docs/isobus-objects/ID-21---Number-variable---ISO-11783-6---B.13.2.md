# ID 21 – Number variable – ISO 11783-6 – B.13.2

```{index} single: ID 21 – Number variable – ISO 11783-6 – B.13.2
```

Das **Number Variable** Objekt mit der **ID 21** ist ein reines Datenobjekt. Es speichert einen numerischen Wert, der von anderen Anzeige- oder Eingabeobjekten referenziert werden kann.

## 🎧 Podcast

* [ISOBUS-Terminals: Zahlen verstehen – NumberVariable, InputNumber & OutputNumber erklärt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Terminals-Zahlen-verstehen--NumberVariable--InputNumber--OutputNumber-erklrt-e36aatd)
* ["Store Version" – Dein Schlüssel zur Verwaltung von Objektdatenpools im nichtflüchtigen VT-Speicher (ISO 11783-6)](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/Store-Version--Dein-Schlssel-zur-Verwaltung-von-Objektdatenpools-im-nichtflchtigen-VT-Speicher-ISO-11783-6-e36vfh0)
* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mechatronik](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISO-11783-6-Softkeys-und-das-Virtual-Terminal-verstehen--Dein-Schlssel-zur-Landmaschinen-Mechatronik-e36a8b0)
* [ISOBUS Skalierung: Wenn der Ackerschlepper-Bildschirm nicht passt – Eine Einführung in ISO 11783-6](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Skalierung-Wenn-der-Ackerschlepper-Bildschirm-nicht-passt--Eine-Einfhrung-in-ISO-11783-6-e36a8q6)
* [ISOBUS-Balkendiagramm: Das Output Linear Bar Graph Objekt der ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Balkendiagramm-Das-Output-Linear-Bar-Graph-Objekt-der-ISO-11783-6-entschlsselt-e36l0v2)

## 📺 Video

* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mecha...](https://www.youtube.com/watch?v=wf_E1DcBOMY)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 en...](https://www.youtube.com/watch?v=kQM4MLsyj5U)

## Technische Attribute (gemäß Tabelle B.43)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer im Objekt-Pool. |
| 0 | **Type** | Integer 1 | Objekttyp = 21 (Number Variable). |
| 1 | **Value** | Integer 4 | Aktueller 32-Bit unsigned Ganzzahlwert (0 bis 4.294.967.295). |

## Funktionsweise und Referenzierung
Variablen sind keine sichtbaren Objekte. Sie werden niemals direkt in eine Maske oder einen Container als "Child" eingefügt, sondern dienen als Datenquelle für andere Objekte:

*   **Referenzierung:** Objekte wie *Input Number* (ID 9), *Output Number* (ID 12) oder *Output Meter* (ID 17) verweisen über ihr Attribut `Variable reference` auf die ID einer Number Variable.
*   **Zentrale Datenhaltung:** Mehrere Anzeigeobjekte können dieselbe Variable referenzieren. Wird der Wert der Variable geändert, aktualisiert das VT automatisch alle betroffenen Anzeigen.

## Ereignisse (Events - Tabelle B.42)
*   **On Change Value:** Dieses Event tritt ein, wenn die Steuerung (ECU) den Wert der Variable per `Change Numeric Value` Kommando ändert oder der Bediener über ein Eingabeobjekt einen neuen Wert speichert. Das VT sorgt daraufhin für ein Redraw aller Objekte, die diese Variable nutzen.

## Bedeutung für die Implementierung
Number Variables sind das Rückgrat der Kommunikation zwischen Maschine und Terminal. 
*   **Effizienz:** Anstatt jedes Anzeigeobjekt einzeln zu aktualisieren, ändert die ECU nur den Wert der zentralen Variable.
*   **Konsistenz:** Durch die Verwendung von Variablen wird sichergestellt, dass an verschiedenen Stellen der Benutzeroberfläche (z. B. Hauptmaske und Einstellungsmenü) immer derselbe aktuelle Wert angezeigt wird.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*