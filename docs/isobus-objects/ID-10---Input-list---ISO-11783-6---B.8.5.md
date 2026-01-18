# ID 10 – Input list – ISO 11783-6 – B.8.5

```{index} single: ID 10 – Input list – ISO 11783-6 – B.8.5
```

Das **Input List** Objekt mit der **ID 10** ermöglicht dem Bediener die Auswahl eines Elements aus einer vordefinierten Liste von Objekten. Es wird häufig für Dropdown-Menüs oder Auswahllisten verwendet.

## 🎧 Podcast

* ["Store Version" – Dein Schlüssel zur Verwaltung von Objektdatenpools im nichtflüchtigen VT-Speicher (ISO 11783-6)](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/Store-Version--Dein-Schlssel-zur-Verwaltung-von-Objektdatenpools-im-nichtflchtigen-VT-Speicher-ISO-11783-6-e36vfh0)
* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mechatronik](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISO-11783-6-Softkeys-und-das-Virtual-Terminal-verstehen--Dein-Schlssel-zur-Landmaschinen-Mechatronik-e36a8b0)
* [ISOBUS Skalierung: Wenn der Ackerschlepper-Bildschirm nicht passt – Eine Einführung in ISO 11783-6](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Skalierung-Wenn-der-Ackerschlepper-Bildschirm-nicht-passt--Eine-Einfhrung-in-ISO-11783-6-e36a8q6)
* [ISOBUS-Balkendiagramm: Das Output Linear Bar Graph Objekt der ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Balkendiagramm-Das-Output-Linear-Bar-Graph-Objekt-der-ISO-11783-6-entschlsselt-e36l0v2)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Bedienoberflchen-Wenn-Tasten-und-Hauptanzeige-unterschiedlich-skalieren--ISO-11783-6-entschlsselt-e36a8n8)

## 📺 Video

* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mecha...](https://www.youtube.com/watch?v=wf_E1DcBOMY)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 en...](https://www.youtube.com/watch?v=kQM4MLsyj5U)

## Technische Attribute (gemäß Tabelle B.20)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer im Objekt-Pool. |
| 0 | **Type** | Integer 1 | Objekttyp = 10 (Input List). |
| 1 | **Width** | Integer 2 | Breite des Feldes (im geschlossenen Zustand). |
| 2 | **Height** | Integer 2 | Höhe des Feldes (im geschlossenen Zustand). |
| 3 | **Variable reference** | Integer 2 | Verweis auf ein **Number Variable** Objekt, das den aktuell gewählten Index speichert. |
| 4 | **Value** | Integer 1 | Aktueller gewählter Index (0-254). Nur wenn AID 3 = NULL. |
| 5 | **Options** | Bitmask 1 | **Bit 0:** Enabled (0 = Deaktiviert, 1 = Aktiviert). |

## Funktionsweise und Darstellung
Die Input List zeigt im normalen Zustand nur das aktuell ausgewählte Element an. 
*   **Auswahl:** Wenn der Bediener das Objekt öffnet, zeigt das VT die Liste der verfügbaren Einträge an. Die grafische Umsetzung (z. B. Pop-up-Box, Scroll-Liste) ist herstellerspezifisch.
*   **Index:** Der übertragene Wert ist der **nullbasierte Index** des gewählten Elements in der Liste (0 für das erste Objekt, 1 für das zweite usw.).
*   **Spezialwert 255:** Der Wert 255 signalisiert "keine Auswahl". Der Bediener kann diesen Wert normalerweise nicht manuell wählen, aber die Steuerung (ECU) kann diesen Wert setzen, um die Auswahl zurückzusetzen.

## Struktur der Listeneinträge
Eine Input List enthält eine Liste von Objekt-IDs (z. B. Texte, Bitmaps oder Container), die als Optionen dienen.
*   **Relative Position:** Die Position der Listeneinträge wird innerhalb des für die Liste reservierten Bereichs (`Width`/`Height`) interpretiert.
*   **Empty Objects:** Ein Object Pointer auf NULL (65535) erzeugt einen leeren Eintrag in der Liste, der dennoch eine Indexposition belegt.

## Ereignisse (Events - Tabelle B.19)
*   **On Entry of Value:** Wird ausgelöst, wenn der Bediener eine Auswahl getroffen und bestätigt hat. Das VT sendet den neuen Index per `VT Change Numeric Value` Nachricht.
*   **On ESC:** Wird ausgelöst, wenn der Bediener die Auswahl abbricht, ohne ein neues Element zu wählen.

## Bedeutung für die Implementierung
Input Lists sind hervorragend geeignet, um Fehleingaben zu vermeiden, da der Bediener nur aus gültigen Optionen wählen kann. Da die Darstellung (z. B. Schriftgröße in der aufgeklappten Liste) vom VT gesteuert wird, ist eine gute Lesbarkeit auf verschiedenen Endgeräten gewährleistet.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*