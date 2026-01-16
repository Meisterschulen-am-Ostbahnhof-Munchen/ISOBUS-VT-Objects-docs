# ID 4 – Soft key mask – ISO 11783-6 – B.5



![](https://user-images.githubusercontent.com/69573151/94337388-52837b00-ffea-11ea-996a-0752344ebacd.png)



Eine **Soft Key Mask** ist ein zentrales Element in der Benutzeroberfläche von Virtual Terminals (VTs) gemäß dem Standard ISO 11783-6. Sie dient dazu, **Soft Keys** zu gruppieren und darzustellen, deren Bezeichnungen (Designatoren) sich je nach angezeigter Maske ändern können.

## Allgemeine Beschreibung und Zweck

Die Soft Key Mask ist ein **Containerobjekt**, das primär **Key-Objekte**, aber auch **Object Pointer** oder **External Object Pointer-Objekte** enthalten kann. Sie ist dazu gedacht, am Rand eines Virtual Terminals angezeigt zu werden. Das Hauptziel ist die Bereitstellung einer flexiblen und kontextabhängigen Bedienelementegruppe für den Bediener.

## Anzeigebereiche und Design

Das VT reserviert einen speziellen **Anzeigebereich für Soft Key-Beschriftungen**, der als Soft Key Mask-Bereich bezeichnet wird. Dieser Bereich ist vom Data Mask-Bereich getrennt und darf nicht Teil davon sein. Jedes Soft Key-Objekt innerhalb dieser Maske hat einen reservierten Anzeigebereich, den **Soft Key Designator**, zur Anzeige einer Beschriftung.

**Größenanforderungen (VT Version 6 und später):**
*   **Minimalgröße des Designators:** 60 × 60 Pixel.
*   Die VT soll eine **klar sichtbare Trennung** zwischen einzelnen Soft Key Designatoren gewährleisten, z. B. durch eine ein Pixel breite Linie außerhalb des Designatorbereichs.

Soft Key Designatoren können **Text, Grafiken oder beides** enthalten. Das Erscheinungsbild und die physische Umsetzung der Soft Keys (z.B. als physische Tasten oder auf einem Touchscreen) liegen im Ermessen des VT-Herstellers.

## Soft Key Varianten und Navigation

Die Soft Key Mask unterstützt verschiedene Konzepte von Soft Keys:
*   **Physische Soft Keys:** Die Anzahl der fest zugewiesenen Tasten, die das VT aktiven Working Sets zur Verfügung stellt. Bei Touchscreen-VTs können dies auch direkt auf dem Bildschirm platzierte Tasten sein.
    *   VT Version 4 und spätere VTs müssen mindestens 6 physische Soft Keys bereitstellen.
    *   Die Anordnung der physischen Soft Keys ist standardisiert (z.B. Key 1 oben rechts bei vertikaler Anordnung).
*   **Virtuelle Soft Keys:** Die maximale Anzahl von Soft Keys, die ein VT pro Soft Key Mask für ein aktives Working Set unterstützt.
    *   VT Version 3 und frühere Versionen unterstützen maximal 64 virtuelle Soft Keys.
    *   VT Version 4 und spätere Versionen müssen genau 64 virtuelle Soft Keys pro Soft Key Mask unterstützen.
*   **Navigations-Soft Keys:** Physische Soft Keys, die das VT zur Navigation zwischen den Soft Keys nutzen kann. Ihre Anzahl muss kleiner sein als die Gesamtzahl der physischen Soft Keys.

Wenn ein Working Set mehr Soft Keys auf einer Soft Key Mask bereitstellt, als physische Soft Keys vorhanden sind, muss das VT eine **Paging-Funktion** zur Navigation bereitstellen. Die Soft Keys werden dabei in Gruppen angezeigt, nicht durch Scrollen. Navigations-Soft Keys belegen immer dieselben physischen Positionen auf allen Seiten. **Pointer auf das NULL-Objekt ID** reservieren eine Soft Key-Position, während Pointer auf NULL am Ende der Liste nicht angezeigt und nicht für die Paging-Berechnung berücksichtigt werden.

## Verknüpfung und Verhalten

Eine Soft Key Mask ist über ein Attribut im Data Mask- oder Alarm Mask-Objekt mit diesen verknüpft. Wenn die zugehörige Data Mask oder Alarm Mask angezeigt wird, wird die Soft Key Mask ebenfalls angezeigt. Wird die Data Mask oder Alarm Mask ausgeblendet, wird auch die Soft Key Mask ausgeblendet.

**Wichtige Verhaltensweisen:**
*   Das VT sendet eine **Soft Key Activation-Nachricht** an das Working Set, wenn ein Soft Key gedrückt, losgelassen oder arretiert wird.
*   Wenn ein Macro mit dem Tastendruck verknüpft ist, wird es vom VT ausgeführt.
*   Bei einem Maskenwechsel, der zum **Entfernen eines aktivierten Soft Keys** vom Bildschirm führt, sendet das VT eine „released“-Nachricht für diesen Soft Key.
*   Das VT kann nur die Aktivierung einer einzelnen Soft Key gleichzeitig unterstützen, es sei denn, die Funktion **„VT supports simultaneous activation of all combinations of Physical Soft Keys“** ist aktiviert.
*   Die **Hintergrundfarbe** einer Soft Key Mask kann geändert werden, wobei die individuelle Hintergrundfarbe eines Key-Objekts diese Einstellung überschreibt.

## User-Layout Soft Key Mask (VT Version 4 und später)

Zusätzlich zu den Standard-Soft Key Masks gibt es ab VT Version 4 **User-Layout Soft Key Masks**.
*   Diese Masken werden vom VT gesteuert, aber vom Bediener angelegt und können **Key Group-Objekte** aufnehmen.
*   Das VT ist der Eigentümer dieser Masken.
*   Die Anzahl der unterstützten Key Cells ist proprietär für das VT-Design, bis zu maximal 64.
*   Das VT muss einen Paging-Mechanismus bereitstellen, wenn die Anzahl der unterstützten Tasten die Anzahl der physischen Soft Keys überschreitet.
*   **Key Group-Objekte**, die von Working Sets bereitgestellt werden, können vom Bediener in diese Masken platziert werden. Eine Key Group kann ein bis vier Key-Objekte enthalten und die gesamte Gruppe muss zusammen abgebildet werden.
*   Die VT speichert das vom Bediener ausgewählte Layout im nicht-flüchtigen Speicher.
*   Wenn ein Key Group-Objekt aufgrund seiner Optionen nicht verfügbar ist oder das zugehörige Working Set nicht vorhanden ist, werden die entsprechenden Key Cells **leer** (mit Hintergrundfarbe gefüllt) angezeigt.
*   Die **Zeichnungsregeln** für User-Layout Soft Key Masks sind dieselben wie für Soft Key Mask-Objekte.

## Erstellung und Verwaltung im ISO-Designer

Im **ISO-Designer**, einer Software zur Erstellung von ISO-konformen Masken für Virtual Terminals, können Soft Key Masks und die darin enthaltenen Objekte erstellt und konfiguriert werden.

**Erstellung einer Soft Key Mask:**
1.  Im Menü "Project" den Menüeintrag "Add New Mask" auswählen.
2.  Im Dialog "Add mask" den Typ "2 - Soft Key Mask" wählen.
3.  Die Auswahl bestätigen.

**Eigenschaften im ISO-Designer:**
Soft Key Masks haben allgemeine Eigenschaften, die im **Properties-Fenster** angepasst werden können, darunter:
*   **Background Color** (Hintergrundfarbe).
*   **Width** (Gesamtbreite in Pixel).
*   **Height** (Gesamthöhe in Pixel).
*   **Type**, **Object Name** und **Object ID**.

**Hinzufügen und Beschriften von Soft Keys:**
*   Soft Keys können auf einer Soft Key Mask hinzugefügt werden, indem man im Menü "Drawing" den Eintrag "Soft Key" wählt und auf einen Designator klickt. Der Soft Key passt sich automatisch an die Größe des Designators an.
*   Zum Beschriften eines Soft Keys muss dieser im **Component Editor** geöffnet werden. Hier können Unterobjekte wie **Output String-Objekte** oder **Picture Graphic-Objekte** als Beschriftung hinzugefügt werden.

## Events und Makros

Soft Keys können mit **Events** und **Makros** verknüpft werden, um Funktionen auszuführen, wenn sie betätigt werden.
*   Häufig verwendete Events für Soft Keys sind **OnKeyPress** (beim Drücken) und **OnKeyRelease** (beim Loslassen).
*   Makros, die mit diesen Events verknüpft sind, können Befehle wie **ShowHideObject** ausführen, um Objekte auf anderen Masken ein- oder auszublenden.

---
