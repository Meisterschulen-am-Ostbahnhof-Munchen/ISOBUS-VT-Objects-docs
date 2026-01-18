# ID 11 – Output string – ISO 11783-6 – B.9.2

```{index} single: ID 11 – Output string – ISO 11783-6 – B.9.2
```

Das **Output String** Objekt mit der **ID 11** dient zur rein visuellen Anzeige von Textzeichenfolgen auf dem Virtuellen Terminal. Im Gegensatz zum *Input String* erlaubt dieses Objekt keine direkte Bearbeitung durch den Bediener.

## 🎧 Podcast

* [ISOBUS-Balkendiagramm: Das Output Linear Bar Graph Objekt der ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Balkendiagramm-Das-Output-Linear-Bar-Graph-Objekt-der-ISO-11783-6-entschlsselt-e36l0v2)
* ["Store Version" – Dein Schlüssel zur Verwaltung von Objektdatenpools im nichtflüchtigen VT-Speicher (ISO 11783-6)](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/Store-Version--Dein-Schlssel-zur-Verwaltung-von-Objektdatenpools-im-nichtflchtigen-VT-Speicher-ISO-11783-6-e36vfh0)
* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mechatronik](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISO-11783-6-Softkeys-und-das-Virtual-Terminal-verstehen--Dein-Schlssel-zur-Landmaschinen-Mechatronik-e36a8b0)
* [ISOBUS Output Meter: Dynamische Anzeigen meistern – vom Zeiger bis zur Visualisierung auf dem VT](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Output-Meter-Dynamische-Anzeigen-meistern--vom-Zeiger-bis-zur-Visualisierung-auf-dem-VT-e36t2tp)
* [ISOBUS Skalierung: Wenn der Ackerschlepper-Bildschirm nicht passt – Eine Einführung in ISO 11783-6](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Skalierung-Wenn-der-Ackerschlepper-Bildschirm-nicht-passt--Eine-Einfhrung-in-ISO-11783-6-e36a8q6)

## 📺 Video

* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mecha...](https://www.youtube.com/watch?v=wf_E1DcBOMY)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 en...](https://www.youtube.com/watch?v=kQM4MLsyj5U)

## Technische Attribute (gemäß Tabelle B.22)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer im Objekt-Pool. |
| 0 | **Type** | Integer 1 | Objekttyp = 11 (Output String). |
| 1 | **Width** | Integer 2 | Breite des Textfeldes in Pixeln. |
| 2 | **Height** | Integer 2 | Höhe des Textfeldes in Pixeln. |
| 3 | **Background colour** | Integer 1 | Hintergrundfarbe (nur aktiv, wenn Bit 0 in Options = 0). |
| 4 | **Font attributes** | Integer 2 | Verweis auf ein **Font Attributes** Objekt (Farbe, Größe, Font). |
| 5 | **Options** | Bitmask 1 | **Bit 0:** Transparent, **Bit 1:** Auto-Wrap (Automatischer Zeilenumbruch), **Bit 2:** Wrap on Hyphen. |
| 6 | **Variable reference** | Integer 2 | Verweis auf ein **String Variable** Objekt (ID 22). |
| 7 | **Justification** | Integer 1 | Textausrichtung (Horizontal: Bits 0-1, Vertikal: Bits 2-3). |
| - | **Length** | Integer 2 | Länge der Zeichenkette in Bytes. |
| - | **Value** | String | Der statische Textinhalt (nur wenn AID 6 = NULL). |

## Funktionsweise und Besonderheiten
*   **Transparenz:** Wenn Bit 0 gesetzt ist, ist der Hintergrund des Textfeldes transparent, und die Hintergrundfarbe der Maske oder eines darunterliegenden Objekts bleibt sichtbar.
*   **Auto-Wrap:** Ermöglicht die Darstellung mehrzeiliger Texte innerhalb der definierten `Width` und `Height`.
*   **Justierung:** Die Ausrichtung erfolgt pixelgenau innerhalb des Rahmens. Dies ist besonders wichtig für die vertikale Zentrierung bei unterschiedlichen Schriftarten.
*   **Clipping:** Text, der über die definierte `Width` oder `Height` hinausgeht, wird vom VT abgeschnitten.

## Statischer Text vs. Dynamische Variable
*   **Statischer Text:** Der Text wird direkt im Objekt-Pool definiert und kann zur Laufzeit nur über das Kommando `Change Attribute` (AID 5 oder 7) in seinen Eigenschaften geändert werden.
*   **Dynamischer Text:** Durch die Verknüpfung mit einer **String Variable** (AID 6) kann die Steuerung (ECU) den Textinhalt jederzeit per `Change String Value` aktualisieren, ohne das Objekt selbst neu laden zu müssen.

## Ereignisse (Events - Tabelle B.21)
*   **On Change Value:** Wird ausgelöst, wenn sich der Textinhalt ändert (entweder durch die ECU oder durch eine Variablenaktualisierung). Das VT zeichnet den Text neu.
*   **On Refresh:** Wird ausgelöst, wenn das VT das Objekt aufgrund von Maskenaktualisierungen neu zeichnen muss.

## Bedeutung für die Implementierung
Output Strings sind die primäre Methode für Statusmeldungen, Beschriftungen und Einheitenanzeigen. Für Texte, die in vielen Sprachen vorliegen, empfiehlt es sich, die Texte über Variablen einzusteuern oder für jede Sprache eine eigene Maske/einen eigenen Pool vorzuhalten.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*