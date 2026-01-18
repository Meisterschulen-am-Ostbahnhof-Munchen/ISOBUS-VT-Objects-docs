# ID 12 – Output number – ISO 11783-6 – B.9.3

```{index} single: ID 12 – Output number – ISO 11783-6 – B.9.3
```

Das **Output Number** Objekt mit der **ID 12** dient zur Anzeige von numerischen Werten. Wie das *Input Number* Objekt unterstützt es automatische Skalierung und Formatierung, ist jedoch rein für die Anzeige (Read-only für den Bediener) konzipiert.

## 🎧 Podcast

* [ISOBUS-Balkendiagramm: Das Output Linear Bar Graph Objekt der ISO 11783-6 entschlüsselt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Balkendiagramm-Das-Output-Linear-Bar-Graph-Objekt-der-ISO-11783-6-entschlsselt-e36l0v2)
* [ISOBUS-Terminals: Zahlen verstehen – NumberVariable, InputNumber & OutputNumber erklärt](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Terminals-Zahlen-verstehen--NumberVariable--InputNumber--OutputNumber-erklrt-e36aatd)
* ["Store Version" – Dein Schlüssel zur Verwaltung von Objektdatenpools im nichtflüchtigen VT-Speicher (ISO 11783-6)](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/Store-Version--Dein-Schlssel-zur-Verwaltung-von-Objektdatenpools-im-nichtflchtigen-VT-Speicher-ISO-11783-6-e36vfh0)
* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mechatronik](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISO-11783-6-Softkeys-und-das-Virtual-Terminal-verstehen--Dein-Schlssel-zur-Landmaschinen-Mechatronik-e36a8b0)
* [ISOBUS Output Meter: Dynamische Anzeigen meistern – vom Zeiger bis zur Visualisierung auf dem VT](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISOBUS-Output-Meter-Dynamische-Anzeigen-meistern--vom-Zeiger-bis-zur-Visualisierung-auf-dem-VT-e36t2tp)

## 📺 Video

* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mecha...](https://www.youtube.com/watch?v=wf_E1DcBOMY)
* [ISOBUS-Bedienoberflächen: Wenn Tasten und Hauptanzeige unterschiedlich skalieren – ISO 11783-6 en...](https://www.youtube.com/watch?v=kQM4MLsyj5U)

## Technische Attribute (gemäß Tabelle B.23)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer im Objekt-Pool. |
| 0 | **Type** | Integer 1 | Objekttyp = 12 (Output Number). |
| 1 | **Width** | Integer 2 | Breite des Anzeigefeldes in Pixeln. |
| 2 | **Height** | Integer 2 | Höhe des Anzeigefeldes in Pixeln. |
| 3 | **Background colour** | Integer 1 | Hintergrundfarbe (nur aktiv, wenn Bit 0 in Options = 0). |
| 4 | **Font attributes** | Integer 2 | Verweis auf ein **Font Attributes** Objekt. |
| 5 | **Options** | Bitmask 1 | **Bit 0:** Transparent, **Bit 1:** Führende Nullen, **Bit 2:** Null als Leerzeichen, **Bit 3:** Runden (0) oder Abschneiden (1). |
| 6 | **Variable reference** | Integer 2 | Verweis auf ein **Number Variable** Objekt (ID 21). |
| 12 | **Value** | Integer 4 | Aktueller Rohwert (32-Bit unsigned). Nur wenn AID 6 = NULL. |
| 7 | **Offset** | Integer 4 | Offset für die Skalierung (32-Bit signed). |
| 8 | **Scale** | Float 4 | Skalierungsfaktor (Multiplikator). |
| 9 | **Number of decimals** | Integer 1 | Anzahl der anzuzeigenden Nachkommastellen (0-7). |
| 10 | **Format** | Boolean 1 | 0 = Festkomma (####.nn), 1 = Exponentialdarstellung. |
| 11 | **Justification** | Integer 1 | Textausrichtung (Horizontal: Bits 0-1, Vertikal: Bits 2-3). |

## Die Skalierungslogik
Das VT berechnet den angezeigten Wert automatisch nach folgender Formel:

**Angezeigter Wert = (Rohwert + Offset) × Skalierungsfaktor**

Beispiel: Ein Rohwert von 2500 mit einem Offset von 0 und einem Skalierungsfaktor von 0.01 wird als **25.00** angezeigt (bei 2 Nachkommastellen).

## Formatierungsoptionen
*   **Führende Nullen (Bit 1):** Das Feld wird links mit Nullen aufgefüllt (z. B. "0012").
*   **Null als Leerzeichen (Bit 2):** Wenn der skalierte Wert exakt Null ist, bleibt das Feld komplett leer.
*   **Runden vs. Abschneiden (Bit 3):** Steuert, wie mit Werten verfahren wird, die mehr Nachkommastellen haben, als in AID 9 definiert sind.

## Bedeutung für die Implementierung
Output Numbers sind ideal für die Anzeige von Sensordaten (Druck, Temperatur, Geschwindigkeit). Da die ECU lediglich Ganzzahlen (Rohwerte) übertragen muss, wird die CAN-Bus-Last minimiert und die Komplexität der Formatierung auf das Terminal verlagert. Die pixelgenaue Justierung (AID 11) sorgt dafür, dass die Zahlen auch bei verschiedenen Schriftarten exakt im Designrahmen ausgerichtet sind.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*