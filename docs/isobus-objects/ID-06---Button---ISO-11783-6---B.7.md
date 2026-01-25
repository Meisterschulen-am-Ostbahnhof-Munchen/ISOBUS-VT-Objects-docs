# ID 6 – Button – ISO 11783-6 – B.7

```{index} single: ID 6 – Button – ISO 11783-6 – B.7
```

![](https://user-images.githubusercontent.com/69573151/94337426-7d6dcf00-ffea-11ea-8ab0-ca710054a888.png)

**Anhang B.7 – Button (Schaltfläche)**

Anhang B.7 der ISO 11783-6:2018 widmet sich der detaillierten Definition des "Button" (Schaltfläche) Objekts im Kontext des Virtuellen Terminals (VT). Schaltflächen sind grundlegende interaktive Elemente der Benutzeroberfläche, die es dem Bediener ermöglichen, Aktionen auszulösen oder Befehle an die landwirtschaftliche Maschine oder das Anbaugerät zu senden.

**Überblick über das Button Objekt**

Das Button Objekt, wie in B.7 definiert, ist ein grafisches Element, das auf der Datenmaske des VT angezeigt wird. Es ist so konzipiert, dass der Bediener durch Berührung (auf Touchscreens) oder Auswahl mit einem Navigationsmittel (wie z.B. Cursor-Tasten) damit interagieren kann. Jede Schaltfläche ist mit einer bestimmten Funktion oder einem Befehl verknüpft, der ausgeführt wird, wenn die Schaltfläche betätigt wird.

### Attribute und Record Format (Tabelle B.14)

Die folgende Tabelle beschreibt den Aufbau des Button Objekts im Objektpool.

| AID | Name | Typ | Größe (Bytes) | Bereich / Wert | Record Byte | Beschreibung |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer | 2 | 0 – 65534 | 1 – 2 | Eindeutige ID im Objektpool. |
| [0] | **Type** | Integer | 1 | 6 | 3 | Objekttyp = Button. |
| [1] | **Width** | Integer | 2 | 0 – 65535 | 4 – 5 | Maximale Breite des Button Area in Pixeln. |
| [2] | **Height** | Integer | 2 | 0 – 65535 | 6 – 7 | Maximale Höhe des Button Area in Pixeln. |
| [3] | **Background colour** | Integer | 1 | 0 – 255 | 8 | Hintergrundfarbe. |
| [4] | **Border colour** | Integer | 1 | 0 – 255 | 9 | Farbe des Rahmens (wenn nicht unterdrückt). |
| [5] | **Key Code** | Integer | 1 | 0 – 255 | 10 | Code, der in der `Button Activation` Nachricht gesendet wird. |
| [6] | **Options** | Bitmask | 1 | 0 – 63 | 11 | Bit 0: Latchable (0=Tastend, 1=Rastend)<br>Bit 1: State (nur bei Latchable: 0=Gelöst, 1=Gedrückt)<br>Bit 2: Suppress Border (1=Kein Rahmen gezeichnet)<br>Bit 3: Transparent (1=Hintergrund transparent)<br>Bit 4: Disabled (1=Deaktiviert/Ausgegraut)<br>Bit 5: No Border (1=Rahmenfläche entfällt, Button Face = Button Area). |
| - | **Number of objects to follow** | Integer | 1 | 0 – 255 | 12 | Anzahl der direkt enthaltenen Objekte (Symbole, Texte). |
| - | **Number of macros to follow** | Integer | 1 | 0 – 255 | 13 | Anzahl der folgenden Makro-Referenzen. |
| - | **Repeat:** {Object ID} | Integer | 2 | 0 – 65534 | 14 + ... | Objekt-ID eines enthaltenen Objekts. |
| - | {X Location} | Signed Integer | 2 | -32768 bis +32767 | 16 + ... | X-Position relativ zur oberen linken Ecke der Button Face. |
| - | {Y Location} | Signed Integer | 2 | -32768 bis +32767 | 18 + ... | Y-Position relativ zur oberen linken Ecke der Button Face. |
| - | **Repeat:** {Event ID} | Integer | 1 | 0 – 255 | var. | (Nach Objekten) Event ID, die das Makro auslöst. |
| - | {Macro ID} | Integer | 1 | 0 – 255 | var. | Makro ID des auszuführenden Makros. |

### Aufbau und Darstellung
Der Button besteht aus drei Bereichen:
1.  **Button Area:** Die gesamte durch Width/Height definierte Fläche.
2.  **Button Border:** Ein proprietärer 8-Pixel-Rahmen (wenn nicht durch Option Bit 5 entfernt).
3.  **Button Face:** Die innere Fläche für Inhalte (Button Area minus Border).

### Container-Struktur
Der Button ist ein Container. Er kann andere Objekte enthalten, die im **Button Face** dargestellt werden. Objekte, die über diesen Bereich hinausragen, werden abgeschnitten (Clipping).

## Ereignisse (Events - Tabelle B.13)

Der Button reagiert auf folgende Ereignisse:

*   **On Key Press:** Ausgelöst beim Betätigen des Buttons. Sendet `Button Activation`.
*   **On Key Release:** Ausgelöst beim Loslassen. Sendet `Button Activation`.
*   **On Enable:** Wenn der Button per Kommando aktiviert wird.
*   **On Disable:** Wenn der Button deaktiviert wird.
*   **On Input Field Selection:** Wenn der Button fokussiert wird (Navigation).
*   **On Input Field De-selection:** Wenn der Fokus verloren geht.
*   **On Change Background Colour:** Reaktion auf Farbänderung.
*   **On Change Size:** Reaktion auf Größenänderung (löscht alten Bereich, zeichnet neu).
*   **On Change Attribute:** Reaktion auf generelle Attributänderungen.

**Rolle des Button Objekts im Virtuellen Terminal**

Schaltflächen sind entscheidend für die Interaktion des Bedieners mit dem Virtuellen Terminal und den angeschlossenen landwirtschaftlichen Geräten. Sie ermöglichen:

- **Auslösen von Funktionen:** Starten oder Stoppen von Prozessen, Aktivieren von Anbaugeräten, Umschalten von Betriebsmodi.
- **Senden von Befehlen:** Steuern von Aktuatoren, Anpassen von Einstellungen, Navigieren in Menüs.
- **Bestätigung von Eingaben:** Quittieren von Alarmen, Bestätigen von Einstellungen.

Durch die standardisierte Definition des Button Objekts in Anhang B.7 wird sichergestellt, dass Schaltflächen auf verschiedenen Virtuellen Terminals und von verschiedenen Herstellern konsistent funktionieren und dargestellt werden. Dies trägt zur Interoperabilität und Benutzerfreundlichkeit des ISO 11783 Systems bei.

**Bedeutung für die Implementierung**

Für Entwickler von Virtuellen Terminals, Anbaugeräten oder Softwarekomponenten, die mit dem ISO 11783-Standard arbeiten, ist die genaue Kenntnis der Spezifikationen in Anhang B.7 unerlässlich. Sie müssen sicherstellen, dass ihre Implementierung des Button Objekts den normativen Anforderungen entspricht, um eine korrekte Funktion und Kompatibilität im ISO 11783 Netzwerk zu gewährleisten.

**Hinweis**

Für die vollständigen und detaillierten Spezifikationen aller Attribute und Eigenschaften des Button Objekts, einschließlich der genauen Datentypen, Wertebereiche und Verknüpfungsmechanismen, wird auf das offizielle Dokument "ISO 11783-6:2018" verwiesen. Anhang B.7 liefert die normative Grundlage für die Implementierung von Schaltflächen im Virtuellen Terminal.

Auswertung des Buttons:

wird der Button gedrückt so werden folgende Nachrichten am ISOBUS abgesetzt:

*   BUTTON\_STATE\_PRESSED
    *   in dem Moment wo der Knopf gedrückt wurde
*   BUTTON\_STATE\_HELD
    *   falls der Knopf länger gehalten wurde
    *   TODO Verweis auf ISO
*   BUTTON\_STATE\_RELEASED
    *   wenn der Knopf losgelassen wurde
*   BUTTON\_STATE\_ABORTED
    *   wenn der Knopf gedrückt, aber dann abgebrochen wurde
    *   TODO besser beschreiben.

daraus ergibt sich:

normale "Knopfdrücke" dürfen nur auf "released" oder "held" ausgewertet werden, 

weil ein auswerten von "pressed" die Abort Möglichkeit nehmen würde. 

TODO: verweis auf internationale Standards, Safety etc.. 

es gibt 2 Wege der Auswertung: 

1.  Makro (ISO-Designer)
2.  über einen Callback im C-Code (Eclipse)

Call Hierarchy:

![](https://user-images.githubusercontent.com/69573151/94337621-210baf00-ffec-11ea-9ec0-fe4a7e7c418b.png)

```c
iso_u32 Tageszaehler = 0;
iso_u32 Gesamtzaehler = 0;
iso_u32 Hugo = 0;

void VTC_handleSoftkeysAndButtons_RELEASED(const struct ButtonActivation_S *pButtonData) {

    // what button was released
    switch (pButtonData->objectIdOfButtonObject) {

    case SoftKey_PlusPlus:
    case Button_PlusPlus:
        Tageszaehler++;
        Gesamtzaehler++;
        break;

    case SoftKey_Reset_Gesamtzaehler:
    case Button_Reset_Gesamtzaehler:
        Gesamtzaehler = 0;
        break;

    case SoftKey_Reset_Tageszaehler:
    case Button_Reset_Tageszaehler:
        Tageszaehler = 0;
        break;

    default:
        break;
    }
    IsoVtcCmd_NumericValue(pButtonData->u8Instance, NumberVariable_Tageszaehler, Tageszaehler);
    IsoVtcCmd_NumericValue(pButtonData->u8Instance, NumberVariable_Gesamtzaehler, Gesamtzaehler);
    setU32("CF-A", "Tageszaehler", Tageszaehler);
    setU32("CF-A", "Gesamtzaehler", Gesamtzaehler);
}
```

![](https://user-images.githubusercontent.com/69573151/94602909-cbf2c600-0295-11eb-946a-a68b45b3eccc.png)

Weitere Informationen und Beispiele finden sich im [ISOBUS Wiki - Button](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/button) von Tobias Tenberg.