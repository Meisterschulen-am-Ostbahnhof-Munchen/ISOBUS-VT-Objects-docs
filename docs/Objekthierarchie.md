# Objekthierarchie (Parent-Child Beziehungen)

```{index} single: Objekthierarchie
```

Diese Seite basiert auf **Tabelle A.2 — Allowed hierarchical relationships of objects** der ISO 11783-6:2018 (Annex A). Sie definiert, welche Objekte (Child) in welchen anderen Objekten (Parent) enthalten sein dürfen.

Die angegebene Zahl steht für die minimale **VT-Version**, ab der diese Beziehung unterstützt wird.

## Parent: Working Set object (ID 0)
Das Working Set Objekt ist der Wurzel-Container einer Objekt-Pool-Hierarchie.

| Child Object | Min. VT Version |
| :--- | :--- |
| Container object (ID 3) | 4 |
| Output String object (ID 11) | 2 |
| Output Number object (ID 12) | 2 |
| Output Line object (ID 13) | 2 |
| Output Rectangle object (ID 14) | 2 |
| Output Ellipse object (ID 15) | 2 |
| Output Polygon object (ID 16) | 2 |
| Output Meter object (ID 17) | 4 |
| Output Linear Bar Graph object (ID 18) | 4 |
| Output Arched Bar Graph object (ID 19) | 4 |
| Picture Graphic object (ID 20) | 2 |
| Scaled Graphic object (ID 48) | 6 |
| Object Pointer object (ID 27) | 4 |
| External Object Pointer object (ID 43) | 5 |

## Parent: Data Mask object (ID 1)
Die Datenmaske ist der Hauptanzeigebereich für die Bedienung.

| Child Object | Min. VT Version |
| :--- | :--- |
| Container object (ID 3) | 2 |
| Key object (ID 5) | 2 |
| Button object (ID 6) | 2 |
| Input Boolean object (ID 7) | 2 |
| Input String object (ID 8) | 2 |
| Input Number object (ID 9) | 2 |
| Input List object (ID 10) | 2 |
| Output String object (ID 11) | 2 |
| Output Number object (ID 12) | 2 |
| Output Line object (ID 13) | 2 |
| Output Rectangle object (ID 14) | 2 |
| Output Ellipse object (ID 15) | 2 |
| Output Polygon object (ID 16) | 2 |
| Output Meter object (ID 17) | 4 |
| Output Linear Bar Graph object (ID 18) | 4 |
| Output Arched Bar Graph object (ID 19) | 4 |
| Picture Graphic object (ID 20) | 2 |
| Animation object (ID 44) | 5 |
| Scaled Graphic object (ID 48) | 6 |
| Object Pointer object (ID 27) | 2 |
| External Object Pointer object (ID 43) | 5 |

## Parent: Alarm Mask object (ID 2)
Alarmmasken dienen zur Anzeige von Warnungen.

| Child Object | Min. VT Version |
| :--- | :--- |
| Container object (ID 3) | 2 |
| Key object (ID 5) | 2 |
| Button object (ID 6) | 2 |
| Input Boolean object (ID 7) | 2 |
| Input String object (ID 8) | 2 |
| Input Number object (ID 9) | 2 |
| Input List object (ID 10) | 2 |
| Output String object (ID 11) | 2 |
| Output Number object (ID 12) | 2 |
| Output Line object (ID 13) | 2 |
| Output Rectangle object (ID 14) | 2 |
| Output Ellipse object (ID 15) | 2 |
| Output Polygon object (ID 16) | 2 |
| Output Meter object (ID 17) | 4 |
| Output Linear Bar Graph object (ID 18) | 4 |
| Output Arched Bar Graph object (ID 19) | 4 |
| Picture Graphic object (ID 20) | 2 |
| Animation object (ID 44) | 5 |
| Scaled Graphic object (ID 48) | 6 |
| Object Pointer object (ID 27) | 2 |
| External Object Pointer object (ID 43) | 5 |

## Parent: Container object (ID 3)
Container dienen zur Gruppierung von Objekten.

| Child Object | Min. VT Version |
| :--- | :--- |
| Container object (ID 3) | 2 |
| Key object (ID 5) | 2 |
| Button object (ID 6) | 2 |
| Input Boolean object (ID 7) | 2 |
| Input String object (ID 8) | 2 |
| Input Number object (ID 9) | 2 |
| Input List object (ID 10) | 2 |
| Output String object (ID 11) | 2 |
| Output Number object (ID 12) | 2 |
| Output Line object (ID 13) | 2 |
| Output Rectangle object (ID 14) | 2 |
| Output Ellipse object (ID 15) | 2 |
| Output Polygon object (ID 16) | 2 |
| Output Meter object (ID 17) | 4 |
| Output Linear Bar Graph object (ID 18) | 4 |
| Output Arched Bar Graph object (ID 19) | 4 |
| Picture Graphic object (ID 20) | 2 |
| Animation object (ID 44) | 5 |
| Scaled Graphic object (ID 48) | 6 |
| Object Pointer object (ID 27) | 2 |
| External Object Pointer object (ID 43) | 5 |

## Parent: Window Mask object (ID 34)
Fenstermasken werden in User-Layouts verwendet.

| Child Object | Min. VT Version |
| :--- | :--- |
| Container object (ID 3) | 4 |
| Key object (ID 5) | 4 |
| Button object (ID 6) | 4 |
| Input Boolean object (ID 7) | 4 |
| Input String object (ID 8) | 4 |
| Input Number object (ID 9) | 4 |
| Input List object (ID 10) | 4 |
| Output String object (ID 11) | 4 |
| Output Number object (ID 12) | 4 |
| Output Line object (ID 13) | 4 |
| Output Rectangle object (ID 14) | 4 |
| Output Ellipse object (ID 15) | 4 |
| Output Polygon object (ID 16) | 4 |
| Output Meter object (ID 17) | 4 |
| Output Linear Bar Graph object (ID 18) | 4 |
| Output Arched Bar Graph object (ID 19) | 4 |
| Picture Graphic object (ID 20) | 4 |
| Animation object (ID 44) | 5 |
| Scaled Graphic object (ID 48) | 6 |
| Object Pointer object (ID 27) | 4 |
| External Object Pointer object (ID 43) | 5 |

## Parent: Soft Key Mask object (ID 4)
Definiert die Belegung der Softkeys.

| Child Object | Min. VT Version |
| :--- | :--- |
| Key object (ID 5) | 2 |
| Object Pointer object (ID 27) | 2 |
| External Object Pointer object (ID 43) | 5 |

## Parent: Key object (ID 5)
Inhalt einer Taste.

| Child Object | Min. VT Version |
| :--- | :--- |
| Container object (ID 3) | 2 |
| Output String object (ID 11) | 2 |
| Output Number object (ID 12) | 2 |
| Output Line object (ID 13) | 2 |
| Output Rectangle object (ID 14) | 2 |
| Output Ellipse object (ID 15) | 2 |
| Output Polygon object (ID 16) | 2 |
| Output Meter object (ID 17) | 4 |
| Output Linear Bar Graph object (ID 18) | 4 |
| Output Arched Bar Graph object (ID 19) | 4 |
| Picture Graphic object (ID 20) | 2 |
| Animation object (ID 44) | 5 |
| Scaled Graphic object (ID 48) | 6 |
| Object Pointer object (ID 27) | 2 |
| External Object Pointer object (ID 43) | 5 |

## Parent: Button object (ID 6)
Inhalt einer Schaltfläche.

| Child Object | Min. VT Version |
| :--- | :--- |
| Container object (ID 3) | 2 |
| Output String object (ID 11) | 2 |
| Output Number object (ID 12) | 2 |
| Output Line object (ID 13) | 2 |
| Output Rectangle object (ID 14) | 2 |
| Output Ellipse object (ID 15) | 2 |
| Output Polygon object (ID 16) | 2 |
| Output Meter object (ID 17) | 4 |
| Output Linear Bar Graph object (ID 18) | 4 |
| Output Arched Bar Graph object (ID 19) | 4 |
| Picture Graphic object (ID 20) | 2 |
| Animation object (ID 44) | 5 |
| Scaled Graphic object (ID 48) | 6 |
| Object Pointer object (ID 27) | 2 |
| External Object Pointer object (ID 43) | 5 |

## Parent: Key Group object (ID 35)
Gruppierung von Softkeys.

| Child Object | Min. VT Version |
| :--- | :--- |
| Key object (ID 5) | 4 |
| Object Pointer object (ID 27) | 4 |
| External Object Pointer object (ID 43) | 5 |

## Parent: Input List object (ID 10)
Optionen in einer Auswahlliste.

| Child Object | Min. VT Version |
| :--- | :--- |
| Container object (ID 3) | 4 |
| Output String object (ID 11) | 2 |
| Output Number object (ID 12) | 2 |
| Output Line object (ID 13) | 4 |
| Output Rectangle object (ID 14) | 4 |
| Output Ellipse object (ID 15) | 4 |
| Output Polygon object (ID 16) | 4 |
| Output Meter object (ID 17) | 4 |
| Output Linear Bar Graph object (ID 18) | 4 |
| Output Arched Bar Graph object (ID 19) | 4 |
| Picture Graphic object (ID 20) | 2 |
| Animation object (ID 44) | 5 |
| Scaled Graphic object (ID 48) | 6 |
| Object Pointer object (ID 27) | 4 |
| External Object Pointer object (ID 43) | 5 |

## Parent: Output List object (ID 37)
Optionen in einer Ausgabeliste.

| Child Object | Min. VT Version |
| :--- | :--- |
| Container object (ID 3) | 4 |
| Output String object (ID 11) | 4 |
| Output Number object (ID 12) | 4 |
| Output Line object (ID 13) | 4 |
| Output Rectangle object (ID 14) | 4 |
| Output Ellipse object (ID 15) | 4 |
| Output Polygon object (ID 16) | 4 |
| Output Meter object (ID 17) | 4 |
| Output Linear Bar Graph object (ID 18) | 4 |
| Output Arched Bar Graph object (ID 19) | 4 |
| Picture Graphic object (ID 20) | 4 |
| Animation object (ID 44) | 5 |
| Scaled Graphic object (ID 48) | 6 |
| Object Pointer object (ID 27) | 4 |
| External Object Pointer object (ID 43) | 5 |

## Parent: Auxiliary Function Type 1 object (ID 29)
Designator für Hilfsfunktionen (veraltet).

| Child Object | Min. VT Version |
| :--- | :--- |
| Output String object (ID 11) | 2 |
| Output Number object (ID 12) | 2 |
| Output Line object (ID 13) | 2 |
| Output Rectangle object (ID 14) | 2 |
| Output Ellipse object (ID 15) | 2 |
| Output Polygon object (ID 16) | 2 |
| Output Meter object (ID 17) | 4 |
| Output Linear Bar Graph object (ID 18) | 4 |
| Output Arched Bar Graph object (ID 19) | 4 |
| Picture Graphic object (ID 20) | 2 |
| Object Pointer object (ID 27) | 2 |
| External Object Pointer object (ID 43) | 5 |

## Parent: Auxiliary Input Type 1 object (ID 30)
Designator für Hilfseingänge (veraltet).

| Child Object | Min. VT Version |
| :--- | :--- |
| Output String object (ID 11) | 3 |
| Output Number object (ID 12) | 3 |
| Output Line object (ID 13) | 3 |
| Output Rectangle object (ID 14) | 3 |
| Output Ellipse object (ID 15) | 3 |
| Output Polygon object (ID 16) | 3 |
| Output Meter object (ID 17) | 3 |
| Output Linear Bar Graph object (ID 18) | 3 |
| Output Arched Bar Graph object (ID 19) | 3 |
| Picture Graphic object (ID 20) | 3 |
| Object Pointer object (ID 27) | 3 |
| External Object Pointer object (ID 43) | 5 |

## Parent: Auxiliary Function Type 2 object (ID 31)
Designator für Hilfsfunktionen.

| Child Object | Min. VT Version |
| :--- | :--- |
| Output String object (ID 11) | 3 |
| Output Number object (ID 12) | 3 |
| Output Line object (ID 13) | 3 |
| Output Rectangle object (ID 14) | 3 |
| Output Ellipse object (ID 15) | 3 |
| Output Polygon object (ID 16) | 3 |
| Output Meter object (ID 17) | 4 |
| Output Linear Bar Graph object (ID 18) | 4 |
| Output Arched Bar Graph object (ID 19) | 4 |
| Picture Graphic object (ID 20) | 3 |
| Animation object (ID 44) | 5 |
| Scaled Graphic object (ID 48) | 6 |
| Object Pointer object (ID 27) | 3 |
| External Object Pointer object (ID 43) | 5 |

## Parent: Auxiliary Input Type 2 object (ID 32)
Designator für Hilfseingänge.

| Child Object | Min. VT Version |
| :--- | :--- |
| Output String object (ID 11) | 3 |
| Output Number object (ID 12) | 3 |
| Output Line object (ID 13) | 3 |
| Output Rectangle object (ID 14) | 3 |
| Output Ellipse object (ID 15) | 3 |
| Output Polygon object (ID 16) | 3 |
| Output Meter object (ID 17) | 3 |
| Output Linear Bar Graph object (ID 18) | 3 |
| Output Arched Bar Graph object (ID 19) | 3 |
| Picture Graphic object (ID 20) | 3 |
| Animation object (ID 44) | 5 |
| Scaled Graphic object (ID 48) | 6 |
| Object Pointer object (ID 27) | 3 |
| External Object Pointer object (ID 43) | 5 |


## Parent: Object Label Reference List object (ID 40)
Definiert Zuweisungen von Labels zu Objekten.

| Child Object | Min. VT Version |
| :--- | :--- |
| Output String object (ID 11) | 4 |
| Output Number object (ID 12) | 4 |
| Output Line object (ID 13) | 4 |
| Output Rectangle object (ID 14) | 4 |
| Output Ellipse object (ID 15) | 4 |
| Output Polygon object (ID 16) | 4 |
| Output Meter object (ID 17) | 4 |
| Output Linear Bar Graph object (ID 18) | 4 |
| Output Arched Bar Graph object (ID 19) | 4 |
| Picture Graphic object (ID 20) | 4 |
| Animation object (ID 44) | 5 |
| Scaled Graphic object (ID 48) | 6 |
| Object Pointer object (ID 27) | 4 |
| External Object Pointer object (ID 43) | 5 |

## Parent: Animation object (ID 44)
Sequenz von Objekten.

| Child Object | Min. VT Version |
| :--- | :--- |
| Container object (ID 3) | 5 |
| Output String object (ID 11) | 5 |
| Output Number object (ID 12) | 5 |
| Output Line object (ID 13) | 5 |
| Output Rectangle object (ID 14) | 5 |
| Output Ellipse object (ID 15) | 5 |
| Output Polygon object (ID 16) | 5 |
| Output Meter object (ID 17) | 5 |
| Output Linear Bar Graph object (ID 18) | 5 |
| Output Arched Bar Graph object (ID 19) | 5 |
| Picture Graphic object (ID 20) | 5 |
| Animation object (ID 44) | 5 |
| Scaled Graphic object (ID 48) | 6 |
| Object Pointer object (ID 27) | 5 |
| External Object Pointer object (ID 43) | 5 |

## Context: Object Label Graphic Representation
Objekte, die als Icon/Grafik in einem Label (via ID 40 oder direkt) verwendet werden dürfen.

| Child Object | Min. VT Version |
| :--- | :--- |
| Container object (ID 3) | 4 |
| Output String object (ID 11) | 4 |
| Output Number object (ID 12) | 4 |
| Output Line object (ID 13) | 4 |
| Output Rectangle object (ID 14) | 4 |
| Output Ellipse object (ID 15) | 4 |
| Output Polygon object (ID 16) | 4 |
| Output Meter object (ID 17) | 4 |
| Output Linear Bar Graph object (ID 18) | 4 |
| Output Arched Bar Graph object (ID 19) | 4 |
| Picture Graphic object (ID 20) | 4 |
| Animation object (ID 44) | 5 |
| Scaled Graphic object (ID 48) | 6 |
| Object Pointer object (ID 27) | 4 |
| External Object Pointer object (ID 43) | 5 |
