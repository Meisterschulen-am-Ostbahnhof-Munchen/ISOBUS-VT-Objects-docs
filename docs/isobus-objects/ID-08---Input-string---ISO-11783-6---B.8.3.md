# ID 8 – Input string – ISO 11783-6 – B.8.3

```{index} single: ID 8 – Input string – ISO 11783-6 – B.8.3
```

Das **Input String** Objekt mit der **ID 8** dient zur Eingabe und Anzeige von Textzeichenfolgen durch den Bediener.

## Technische Attribute (gemäß Tabelle B.17)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer im Objekt-Pool. |
| 0 | **Type** | Integer 1 | Objekttyp = 8 (Input String). |
| 1 | **Width** | Integer 2 | Breite des Eingabefeldes in Pixeln. |
| 2 | **Height** | Integer 2 | Höhe des Eingabefeldes in Pixeln. |
| 3 | **Background colour** | Integer 1 | Hintergrundfarbe (nur bei deaktivierter Transparenz). |
| 4 | **Font attributes** | Integer 2 | Verweis auf ein **Font Attributes** Objekt (Farbe, Größe, Font). |
| 5 | **Input attributes** | Integer 2 | Verweis auf ein **Input Attributes** Objekt zur Validierung der Eingabe. |
| 6 | **Options** | Bitmask 1 | **Bit 0:** Transparent, **Bit 1:** Auto-Wrap (Zeilenumbruch), **Bit 2:** Wrap on Hyphen. |
| 7 | **Variable reference** | Integer 2 | Verweis auf ein **String Variable** Objekt (ID 22). |
| 8 | **Justification** | Integer 1 | Textausrichtung (Links, Mitte, Rechts / Oben, Mitte, Unten). |
| - | **Length** | Integer 1 | Maximale Länge der Zeichenkette in Bytes (0-255). |
| 9 | **Enabled** | Integer 1 | Status: 0 = Deaktiviert, 1 = Aktiviert. |

## Funktionsweise und Optionen
Das Input String Objekt bietet flexible Möglichkeiten zur Textdarstellung:
*   **Auto-Wrap:** Wenn aktiviert (Bit 1), bricht das VT den Text automatisch um, wenn die Breite des Feldes überschritten wird.
*   **Justierung:** Über AID 8 wird sowohl die horizontale als auch die vertikale Ausrichtung gesteuert (Bitmaske für Bits 0-1 und 2-3).
*   **Validierung:** Durch die Verknüpfung mit einem `Input Attributes` Objekt kann die Eingabe auf bestimmte Zeichensätze begrenzt werden.

## Datentypen: 8-Bit vs. WideString
Das Objekt unterstützt sowohl Standard 8-Bit Zeichenketten als auch WideStrings (für Sonderzeichen oder asiatische Sprachen). Der Typ wird durch das verknüpfte Variablen-Objekt oder die Initialisierung im Pool festgelegt.

## Ereignisse (Events)
*   **On Entry of Value:** Wird ausgelöst, wenn der Bediener die Texteingabe bestätigt. Das VT sendet eine `VT Change String Value` Nachricht an die Arbeitsgruppe.
*   **On ESC:** Wird ausgelöst, wenn der Bediener die Eingabe ohne Speichern abbricht.

## Bedeutung für die Implementierung
Input Strings werden häufig für Namen (z. B. Feldnamen, Kundendaten) oder Passwörter verwendet. Da die Texteingabe auf Terminals ohne Tastatur (nur Touch oder Dreh-Drück-Steller) mühsam sein kann, sollten Standardwerte oder Auswahllisten (Input List) bevorzugt werden, wenn der Wertevorrat begrenzt ist.

Weitere Informationen und Beispiele finden sich im [ISOBUS Wiki - String (Input)](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/string-input) von Tobias Tenberg.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*