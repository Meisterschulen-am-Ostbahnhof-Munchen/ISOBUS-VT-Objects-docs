# ID 3 – Container – ISO 11783-6 – B.4

```{index} single: ID 3 – Container – ISO 11783-6 – B.4
```

Das **Container** Objekt mit der **ID 3** dient dazu, mehrere Objekte logisch zu gruppieren. Ein Container selbst ist nicht sichtbar, ermöglicht aber das gemeinsame Verschieben, Ein-/Ausblenden oder Teilen einer gesamten Gruppe von Objekten.

## Technische Attribute (gemäß Tabelle B.8)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer im Objekt-Pool. |
| 0 | **Type** | Integer 1 | Objekttyp = 3 (Container). |
| 1 | **Width** | Integer 2 | Maximale Breite des Containers in Pixeln. |
| 2 | **Height** | Integer 2 | Maximale Höhe des Containers in Pixeln. |
| 3 | **Hidden** | Boolean 1 | Sichtbarkeitsstatus: 0 = Sichtbar, 1 = Versteckt (Hidden). |

### Relative Positionierung und Clipping
Innerhalb eines Containers beginnt ein **eigenes Koordinatensystem**:
*   **Relative Koordinaten:** Die X- und Y-Positionen der Child-Objekte beziehen sich auf die obere linke Ecke des Containers.
*   **Clipping:** Alle Objekte oder Teile von Objekten, die außerhalb der durch `Width` und `Height` definierten Fläche liegen, werden vom VT abgeschnitten und nicht angezeigt.
*   **Gruppen-Verschiebung:** Wenn der Container verschoben wird (z. B. per `Change Child Position`), verschieben sich alle darin enthaltenen Objekte automatisch mit.

## Ereignisse (Events - Tabelle B.7)

Der Container bietet spezifische Ereignisse, um auf Sichtbarkeitsänderungen zu reagieren:

*   **On Show:** Wird ausgelöst, wenn der Container eingeblendet wird (Kommando `Hide/Show Object`). Alle enthaltenen Objekte werden gezeichnet.
*   **On Hide:** Wird ausgelöst, wenn der Container ausgeblendet wird. Die Fläche wird mit der Hintergrundfarbe der übergeordneten Maske überschrieben.
*   **On Refresh:** Wird bei Änderungen an untergeordneten Objekten (Child/Grandchild) ausgelöst, um die Anzeige zu aktualisieren.

## Nutzung in der Praxis
Container sind essenziell für dynamische Benutzeroberflächen:
*   **Ein-/Ausblenden:** Mit dem Kommando `IsoVtcCmd_ObjHideShow` können komplexe Bedienfelder oder Statusanzeigen auf Knopfdruck erscheinen oder verschwinden.
*   **Platzersparnis:** Mehrere Container können an der gleichen Stelle liegen; durch geschicktes Umschalten der Sichtbarkeit lassen sich verschiedene "Registerkarten" oder Modi realisieren.

### Beispiele aus dem ISO-Designer
![](https://user-images.githubusercontent.com/69573151/94602403-17f13b00-0295-11eb-8216-34070ca1bca8.png)
![](https://user-images.githubusercontent.com/69573151/94606853-5f7ac580-029b-11eb-9293-18570b481dbf.png)

## Bedeutung für die Implementierung
Da der Container ein logisches Element ist, verbraucht er selbst kaum Rechenleistung, ist aber mächtig in der Steuerung der Z-Order und Gruppierung. Entwickler sollten darauf achten, dass die `Width` und `Height` korrekt gesetzt sind, um ungewolltes Clipping zu vermeiden.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*
