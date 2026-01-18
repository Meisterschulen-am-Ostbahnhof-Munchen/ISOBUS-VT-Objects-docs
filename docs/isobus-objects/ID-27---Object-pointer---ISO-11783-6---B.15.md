# ID 27 – Object pointer – ISO 11783-6 – B.15

```{index} single: ID 27 – Object pointer – ISO 11783-6 – B.15
```

Das **Object Pointer** Objekt mit der **ID 27** dient als dynamischer Platzhalter. Es ermöglicht es, an einer fest definierten Stelle in einer Maske oder einem Container das referenzierte Objekt zur Laufzeit auszutauschen.

## 🎧 Podcast

* [ISOBUS Object Pointer: Das Geheimnis dynamischer Displays und effizienter Fehlerdiagnose](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Object-Pointer-Das-Geheimnis-dynamischer-Displays-und-effizienter-Fehlerdiagnose-e36bp75)
* [Decoding Industrial Control: Function Blocks, Object-Oriented Principles, and the Power of IEC 61499](https://podcasters.spotify.com/pod/show/iec-61499-prime-course-en/episodes/Decoding-Industrial-Control-Function-Blocks--Object-Oriented-Principles--and-the-Power-of-IEC-61499-e3722d5)
* ["Store Version" – Dein Schlüssel zur Verwaltung von Objektdatenpools im nichtflüchtigen VT-Speicher (ISO 11783-6)](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/Store-Version--Dein-Schlssel-zur-Verwaltung-von-Objektdatenpools-im-nichtflchtigen-VT-Speicher-ISO-11783-6-e36vfh0)
* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mechatronik](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISO-11783-6-Softkeys-und-das-Virtual-Terminal-verstehen--Dein-Schlssel-zur-Landmaschinen-Mechatronik-e36a8b0)
* [ISOBUS Skalierung: Wenn der Ackerschlepper-Bildschirm nicht passt – Eine Einführung in ISO 11783-6](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Skalierung-Wenn-der-Ackerschlepper-Bildschirm-nicht-passt--Eine-Einfhrung-in-ISO-11783-6-e36a8q6)

## 📺 Video

* [2025-03-30 16-59-57 Verknüpfung von Object ID und Objektname](https://www.youtube.com/watch?v=FuZTizT48JU)
* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mecha...](https://www.youtube.com/watch?v=wf_E1DcBOMY)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 en...](https://www.youtube.com/watch?v=kQM4MLsyj5U)

## Technische Attribute (gemäß Tabelle B.55)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer im Objekt-Pool. |
| 0 | **Type** | Integer 1 | Objekttyp = 27 (Object Pointer). |
| 1 | **Value** | Integer 2 | Die Objekt-ID des aktuell anzuzeigenden Objekts (oder 65535 für NULL/unsichtbar). |

## Funktionsweise und Anwendung
Ein Object Pointer wird wie ein normales Child-Objekt in eine Maske eingebunden. Anstatt jedoch selbst etwas zu zeichnen, "leitet" er die Anzeige an das Objekt weiter, dessen ID in AID 1 gespeichert ist.

*   **Dynamischer Austausch:** Die ECU kann den `Value` (AID 1) per `Change Numeric Value` Kommando jederzeit ändern. Das VT blendet daraufhin das alte Objekt aus und das neue an derselben Stelle ein.
*   **Platzhalter-Funktion:** Er eignet sich hervorragend für Status-Icons (z. B. wechselnde Symbole für verschiedene Maschinenzustände), ohne dass mehrere Objekte übereinandergelegt und einzeln versteckt werden müssen.
*   **NULL-Pointer:** Wird der Wert auf 65535 gesetzt, wird an dieser Stelle nichts gezeichnet.

## Ereignisse (Events - Tabelle B.54)
*   **On Change Value:** Tritt ein, wenn die ECU die Ziel-Objekt-ID ändert. Das VT führt automatisch das "Hide" für das bisherige und das "Show" für das neue Objekt aus und aktualisiert die Maske.

## Bedeutung für die Implementierung
Object Pointer reduzieren die Komplexität der Maskensteuerung erheblich. Anstatt viele Objekte manuell per `Hide/Show` zu verwalten, muss die ECU nur eine einzige ID im Pointer ändern. Dies spart CAN-Bus-Bandbreite und vereinfacht die Programmlogik auf der Maschinensteuerung.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*