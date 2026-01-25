# ID 5 – Key (Soft Key) – ISO 11783-6 – B.6

```{index} single: ID 5 – Key (Soft Key) – ISO 11783-6 – B.6
```

![](https://user-images.githubusercontent.com/69573151/95071971-c7e9fc80-070a-11eb-8261-f87394d32fb4.png)

## 🎧 Podcast

* [ISO 11783-6: Softkeys und das Virtual Terminal verstehen – Dein Schlüssel zur Landmaschinen-Mechatronik](https://podcasters.spotify.com/pod/show/isobus-vt-objects/episodes/ISO-11783-6-Softkeys-und-das-Virtual-Terminal-verstehen--Dein-Schlssel-zur-Landmaschinen-Mechatronik-e36a8b0)

----

Das **Key Objekt** (ID 5) definiert das Aussehen und den funktionalen Code eines Softkeys. Es ist das interaktive Element innerhalb einer Softkey-Maske.

## Technische Attribute (gemäß Tabelle B.12)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer im Objekt-Pool. |
| 0 | **Type** | Integer 1 | Objekttyp = 5 (Key). |
| 1 | **Background colour** | Integer 1 | Hintergrundfarbe der Taste. |
| 2 | **Key code** | Integer 1 | Der numerische Code (1-255), den das VT in der `Soft Key Activation` Nachricht sendet, wenn diese Taste betätigt wird. (Code 0 ist reserviert). |

### Designator und Child-Objekte
Ein Key-Objekt fungiert als Container für die grafischen Inhalte der Taste (z. B. Symbole oder Texte).
*   **Koordinaten:** X- und Y-Positionen der Child-Objekte beziehen sich auf die obere linke Ecke des Softkey-Designators.
*   **Clipping:** Alle Objekte, die außerhalb des physischen Bereichs des Softkeys liegen, werden vom VT abgeschnitten. Die Größe der Softkeys ist VT-abhängig, weshalb Symbole zentral platziert werden sollten.

## Ereignisse (Events - Tabelle B.11)

Das Key-Objekt reagiert auf die physische Interaktion des Bedieners:

*   **On Key Press:** Wird ausgelöst, wenn die Taste gedrückt wird. Das VT sendet eine `Soft Key Activation` Nachricht mit dem Status "pressed".
*   **On Key Release:** Wird beim Loslassen der Taste ausgelöst (Status "released").
*   **On Input Field Selection:** Falls das VT eine Navigation per Cursor/Encoder unterstützt, wird dieses Event beim Fokussieren des Keys ausgelöst.

## Der Key Code
Der **Key Code** (AID 2) ist das entscheidende Bindeglied zur Softwarelogik (C-Code). Während die `Object ID` die Taste im Grafik-Pool identifiziert, nutzt die Applikation den `Key Code`, um die Funktion zuzuordnen. Dies erlaubt es, verschiedene grafische Tasten (unterschiedliche IDs) mit demselben funktionalen Code zu belegen.

## Bedeutung für die Implementierung
Da die tatsächliche Größe und Form der Softkeys von VT zu VT variieren kann (z. B. Hochformat vs. Querformat, Touch vs. Hardwaretasten), ist es Best Practice, grafische Inhalte (Bitmaps) innerhalb des Keys klein genug zu wählen und mittig zu positionieren. Ein Key-Objekt ohne Child-Objekte erscheint als leere Fläche in der gewählten Hintergrundfarbe.

Weitere Informationen und Beispiele finden sich im [ISOBUS Wiki - Softkey](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/softkey) von Tobias Tenberg.

----
*Hinweis: Für detaillierte Spezifikationen zu Datentypen und Nachrichtenformaten wird auf die offizielle ISO 11783-6:2018 verwiesen.*