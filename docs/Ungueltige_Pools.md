# Ungültige Objektpools (Invalid Object Pools)

```{index} single: Ungültige Pools
```

Damit ein ISOBUS-Objektpool (IOP) vom Virtual Terminal (VT) akzeptiert und geladen wird, muss er strikten strukturellen Regeln folgen. Verletzt der Pool eine dieser Regeln, sendet das VT am Ende der Übertragung (`End of Object Pool`) einen Fehlercode und verwirft meist den gesamten Pool.

Hier sind die wichtigsten Regeln, die jeder Programmierer kennen muss:

## 1. Strukturelle Integrität (Parsing-Fehler)

Dies sind die häufigsten Fehler, die dazu führen, dass der Parser des VTs "aus dem Tritt" gerät.

*   **Falsche Längenangaben:** Wenn ein Objekt sagt "Es folgen 5 Kind-Objekte", aber im Byte-Stream folgen nur 4 (oder 6), liest das VT das nächste Objekt-Byte fälschlicherweise als Attribut des vorherigen. Der Pool ist dann "kaputt".
*   **Unbekannte Objekttypen:** Eine Objekt-Typ-ID, die in der Norm (und der unterstützten VT-Version) nicht definiert ist.
*   **Fehlendes ID 0 Objekt:** Jede Arbeitsgruppe **muss** genau ein Objekt mit der **ID 0** (Working Set) enthalten. Fehlt dieses, weiß das VT nicht, wer der Besitzer des Pools ist.

## 2. Referenzierungs-Fehler (Dangling Pointers)

Das VT prüft beim Laden (oder spätestens beim Aktivieren), ob alle Verknüpfungen gültig sind.

*   **Tote Verweise:** Ein Objekt (z. B. ein Container) verweist in seiner Child-Liste auf eine Objekt-ID (z. B. 100), aber im gesamten Pool gibt es kein Objekt mit der ID 100.
    *   *Ausnahme:* Referenzen auf `NULL` (65535 bzw. FFFFh) sind erlaubt und erwünscht (z. B. leere Softkeys).
*   **Falsche Objekttypen:** Ein Attribut verlangt einen spezifischen Typ, aber die referenzierte ID gehört zu einem anderen Typ.
    *   *Beispiel:* Ein `Input Number` Objekt verweist bei `Variable Reference` auf ein `String Variable` Objekt. -> **Ungültig!**
    *   *Beispiel:* Ein `Output Rectangle` verweist bei `Line Attributes` auf ein `Fill Attributes` Objekt. -> **Ungültig!**

## 3. Logische Fehler & Rekursion

*   **Zirkuläre Referenzen:** Ein Container A enthält Container B, und Container B enthält wieder Container A. Dies führt zu einer Endlosschleife beim Zeichnen. Das VT erkennt dies und lehnt den Pool ab oder stürzt (im schlimmsten Fall) ab.
*   **Mehrfache Definition:** Eine Objekt-ID (z. B. ID 50) darf im Pool nur ein einziges Mal definiert werden. Doppelte IDs sind verboten.

## 4. Spezifische Objekt-Regeln (Hard Constraints)

Einige Objekte haben sehr spezifische Regeln, die oft übersehen werden:

*   **Designator-Pflicht:** Objekte wie `Working Set`, `Auxiliary Function` und `Auxiliary Input` **müssen** mindestens ein Kind-Objekt haben (siehe Seite [Leere Objekte](Leere_Objekte.md)).
*   **Input Lists:** Der `Value` einer Input List darf nicht größer sein als `Anzahl der Listeneinträge - 1`.
*   **Soft Key Masks:** Dürfen nur `Key` Objekte (ID 5) oder `Object Pointer` (ID 27) enthalten, die wiederum auf Keys zeigen. Ein Button (ID 6) in einer Soft Key Mask ist ungültig.
*   **Variablen-Größe:** Wenn ein String-Objekt auf eine String-Variable verweist, sollte die definierte Länge im String-Objekt idealerweise zur Länge der Variable passen (obwohl VTs hier oft tolerant sind und clippen/padden).

## 5. Ressourcen-Limits

Auch wenn der Pool syntaktisch korrekt ist, kann er abgelehnt werden, wenn er die Hardware-Limits des VTs sprengt:
*   **Speicher voll:** Der Pool ist größer als der verfügbare Flash-Speicher des VTs (Memory Out of range).
*   **Zu viele Objekte:** Einige ältere VTs haben Limits für die absolute Anzahl an Objekten (z. B. max. 65534, was durch das 16-Bit ID-Feld vorgegeben ist, aber reale Limits liegen oft niedriger).
*   **Softkey-Limit:** Eine Softkey-Maske, die mehr Keys definiert, als das VT verwalten kann (obwohl Paging vorgeschrieben ist, gibt es oft harte Limits).

## Tipps zur Fehlersuche
Wenn das VT beim Laden "Object Pool Error" meldet:
1.  Prüfen, ob **ID 0** existiert.
2.  Prüfen, ob alle referenzierten IDs tatsächlich im Pool enthalten sind.
3.  Prüfen, ob alle `Number of objects/macros/bytes` Felder exakt mit den folgenden Daten übereinstimmen.
4.  Prüfen, ob Typ-Referenzen (Number Var vs. String Var) stimmen.
