# ID 28 – Macro – ISO 11783-6 – B.16

```{index} single: ID 28 – Macro – ISO 11783-6 – B.16
```

Das **Macro** Objekt mit der **ID 28** erlaubt es, eine Sequenz von Befehlen im Virtuellen Terminal zu speichern und bei bestimmten Ereignissen (Events) automatisch auszuführen. Dies reduziert die notwendige Kommunikation über den ISOBUS, da einfache UI-Logik direkt im Terminal abläuft.

## 🎧 Podcast

* ["Store Version" – Dein Schlüssel zur Verwaltung von Objektdatenpools im nichtflüchtigen VT-Speicher (ISO 11783-6)](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/Store-Version--Dein-Schlssel-zur-Verwaltung-von-Objektdatenpools-im-nichtflchtigen-VT-Speicher-ISO-11783-6-e36vfh0)
* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mechatronik](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISO-11783-6-Softkeys-und-das-Virtual-Terminal-verstehen--Dein-Schlssel-zur-Landmaschinen-Mechatronik-e36a8b0)
* [ISOBUS Skalierung: Wenn der Ackerschlepper-Bildschirm nicht passt – Eine Einführung in ISO 11783-6](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Skalierung-Wenn-der-Ackerschlepper-Bildschirm-nicht-passt--Eine-Einfhrung-in-ISO-11783-6-e36a8q6)
* [ISOBUS-Balkendiagramm: Das Output Linear Bar Graph Objekt der ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Balkendiagramm-Das-Output-Linear-Bar-Graph-Objekt-der-ISO-11783-6-entschlsselt-e36l0v2)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Bedienoberflchen-Wenn-Tasten-und-Hauptanzeige-unterschiedlich-skalieren--ISO-11783-6-entschlsselt-e36a8n8)

## 📺 Video

* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mecha...](https://www.youtube.com/watch?v=wf_E1DcBOMY)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 en...](https://www.youtube.com/watch?v=kQM4MLsyj5U)

## Technische Attribute (gemäß Tabelle B.56)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer (0-255 bis VT v4, bis 65534 ab VT v5). |
| 0 | **Type** | Integer 1 | Objekttyp = 28 (Macro). |
| - | **Number of bytes** | Integer 2 | Gesamtzahl der folgenden Befehls-Bytes. |
| - | **Commands** | Binary | Sequenz von Befehlspaketen (jeweils auf 8 Byte aufgefüllt). |

## Funktionsweise und Struktur
Ein Makro besteht aus einer Liste von VT-Kommandos (siehe ISO 11783-6, Anhang F). 

*   **Padding:** Jeder Befehl innerhalb eines Makros muss auf eine Länge von **8 Byte** aufgefüllt werden (mit `0xFF`), falls das eigentliche Kommando kürzer ist.
*   **Ausführung:** Makros können durch Events (z. B. `On Press` eines Buttons) oder durch das Kommando `Execute Macro` von der ECU gestartet werden.
*   **Konsistenz:** Die ECU ist dafür verantwortlich, dass Makros nur auf Objekte verweisen, die tatsächlich im Pool existieren.

## Verfügbare Makro-Befehle (Auszug)

Makros können fast alle kommandierenden VT-Funktionen nutzen:

*   **Sichtbarkeit:** `Hide/Show Object` (Ein-/Ausblenden von Containern).
*   **Interaktion:** `Enable/Disable Object` (Sperren von Buttons/Eingaben), `Select Input Object` (Fokus setzen).
*   **Werte:** `Change Numeric Value` (Variablen oder Pointer ändern), `Change String Value`.
*   **Geometrie:** `Change Child Location/Position` (Objekte verschieben/scrollen), `Change Size`, `Change End Point`.
*   **Darstellung:** `Change Background Color`, `Change Font/Line/Fill Attributes`.
*   **Navigation:** `Change Active Mask` (Maskenwechsel), `Change Soft Key Mask`.
*   **Audio:** `Control Audio Device` (Signaltöne ausgeben).
*   **Listen:** `Change List Item` (Inhalt von Input-Listen ändern).

## Ereignisse (Events - Tabelle B.56)
*   Makros selbst lösen keine Events aus, sie werden durch Events *anderer* Objekte (Buttons, Masken, Variablen) referenziert und ausgeführt.

## Bedeutung für die Implementierung
Makros sind ein mächtiges Werkzeug zur **Performance-Optimierung**:
1.  **Reaktionszeit:** Ein Maskenwechsel direkt nach einem Tastendruck erfolgt per Makro ohne CAN-Verzögerung.
2.  **Entlastung:** Die ECU muss sich nicht um rein grafische Belange kümmern (z. B. das Umschalten eines Icons beim Drücken eines Buttons).
3.  **Komplexität:** Mehrere Aktionen können in ein einziges Makro gepackt werden (z. B. "Variable auf 0 setzen" UND "Erfolgsmeldung einblenden" UND "Ton abspielen").

----
*Hinweis: Für detaillierte Spezifikationen zu den einzelnen Befehlscodes wird auf die offizielle ISO 11783-6:2018, Anhang F verwiesen.*