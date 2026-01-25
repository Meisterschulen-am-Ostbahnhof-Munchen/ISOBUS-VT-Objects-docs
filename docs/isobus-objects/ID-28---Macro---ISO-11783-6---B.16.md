# ID 28 – Macro – ISO 11783-6 – B.16

```{index} single: ID 28 – Macro – ISO 11783-6 – B.16
```

Das **Macro** Objekt mit der **ID 28** erlaubt es, eine Sequenz von Befehlen im Virtuellen Terminal zu speichern und bei bestimmten Ereignissen (Events) automatisch auszuführen. Dies reduziert die notwendige Kommunikation über den ISOBUS, da einfache UI-Logik direkt im Terminal abläuft.

### Attribute und Record Format (Tabelle B.56)

Die folgende Tabelle beschreibt den Aufbau des Macro Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 255 (VT v4)<br>0 – 65534 (VT v5+) | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 28 | 3 | Objekttyp = Macro. |
| - | **Number of bytes to follow** | Integer | 2 | 0 – 65535 | 4 – 5 | Anzahl der Bytes für die Befehlsliste. |
| - | **Repeat:** {Command} | Binary | 6 – n | - | 6 ... | Liste von Befehlspaketen. Jeder Befehl muss ein Vielfaches von 8 Bytes lang sein (Padding mit FFh). |

## Funktionsweise und Struktur
Ein Makro besteht aus einer Liste von VT-Kommandos (siehe ISO 11783-6, Anhang F).

*   **Padding:** Jeder Befehl innerhalb eines Makros muss auf eine Länge von **8 Byte** aufgefüllt werden (mit `0xFF`), falls das eigentliche Kommando kürzer ist (z.B. Change Numeric Value).
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

## Ereignisse (Events)

Makros lösen selbst keine Events aus, werden aber durch Events anderer Objekte gestartet.
Das Makro Objekt unterstützt die Kommandos:
*   `Execute Macro`
*   `Execute Extended Macro`
*   `Get Attribute Value`

## Bedeutung für die Implementierung
Makros sind ein mächtiges Werkzeug zur **Performance-Optimierung**:
1.  **Reaktionszeit:** Ein Maskenwechsel direkt nach einem Tastendruck erfolgt per Makro ohne CAN-Verzögerung.
2.  **Entlastung:** Die ECU muss sich nicht um rein grafische Belange kümmern (z. B. das Umschalten eines Icons beim Drücken eines Buttons).
3.  **Komplexität:** Mehrere Aktionen können in ein einziges Makro gepackt werden (z. B. "Variable auf 0 setzen" UND "Erfolgsmeldung einblenden" UND "Ton abspielen").

----
*Hinweis: Für detaillierte Spezifikationen zu den einzelnen Befehlscodes wird auf die offizielle ISO 11783-6:2018, Anhang F verwiesen.*