# ID 6 – Button – ISO 11783-6 – B.7

![](https://user-images.githubusercontent.com/69573151/94337426-7d6dcf00-ffea-11ea-8ab0-ca710054a888.png)


**Anhang B.7 – Button (Schaltfläche)**

Anhang B.7 der ISO 11783-6:2018 widmet sich der detaillierten Definition des "Button" (Schaltfläche) Objekts im Kontext des Virtuellen Terminals (VT). Schaltflächen sind grundlegende interaktive Elemente der Benutzeroberfläche, die es dem Bediener ermöglichen, Aktionen auszulösen oder Befehle an die landwirtschaftliche Maschine oder das Anbaugerät zu senden.

**Überblick über das Button Objekt**

Das Button Objekt, wie in B.7 definiert, ist ein grafisches Element, das auf der Datenmaske des VT angezeigt wird. Es ist so konzipiert, dass der Bediener durch Berührung (auf Touchscreens) oder Auswahl mit einem Navigationsmittel (wie z.B. Cursor-Tasten) damit interagieren kann. Jede Schaltfläche ist mit einer bestimmten Funktion oder einem Befehl verknüpft, der ausgeführt wird, wenn die Schaltfläche betätigt wird.

**Wichtige Attribute und Eigenschaften (gemäß B.7)**

Anhang B.7 spezifiziert eine Reihe von Attributen, die das Verhalten und die Darstellung des Button Objekts definieren. Diese Attribute umfassen unter anderem:

- **Objekt-ID:** Eine eindeutige Identifikationsnummer für jede Schaltfläche innerhalb des Objektpools einer Arbeitsgruppe.
- **Position und Größe:** Koordinaten und Abmessungen, die festlegen, wo die Schaltfläche auf der Datenmaske platziert ist und wie groß sie ist.
- **Darstellung:** Attribute, die das Erscheinungsbild der Schaltfläche beeinflussen, wie z.B.
    - **Farbe:** Die Farbe der Schaltfläche im Normalzustand und möglicherweise auch im aktivierten oder gedrückten Zustand.
    - **Text oder Grafik:** Die Möglichkeit, Text (z.B. eine Beschriftung, die die Funktion der Schaltfläche angibt) oder eine Grafik (ein Symbol) auf der Schaltfläche anzuzeigen.
    - **Schriftart und -größe:** Für Textbeschriftungen können Schriftart und -größe festgelegt werden.
- **Verhalten:** Attribute, die das reaktive Verhalten der Schaltfläche steuern, z.B.
    - **Aktivierbarkeit:** Definiert, ob die Schaltfläche in einem bestimmten Zustand aktiviert (d.h. anklickbar oder auswählbar) ist oder nicht.
    - **Wiederholungsfunktion:** Die Option, einen Befehl wiederholt zu senden, solange die Schaltfläche gedrückt gehalten wird.
- **Verknüpfung mit Ereignissen und Befehlen:** Jede Schaltfläche ist mit einem oder mehreren Ereignissen oder Befehlen verknüpft. Wenn die Schaltfläche betätigt wird, wird das entsprechende Ereignis ausgelöst oder der Befehl gesendet. Anhang B.7 beschreibt die Mechanismen, wie diese Verknüpfungen hergestellt und verwaltet werden.

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
