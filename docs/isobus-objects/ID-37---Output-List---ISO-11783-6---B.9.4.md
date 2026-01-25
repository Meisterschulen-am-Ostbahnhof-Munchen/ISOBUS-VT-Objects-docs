# ID 37 – Output List – ISO 11783-6 – B.9.4

```{index} single: ID 37 – Output List – ISO 11783-6 – B.9.4
```

Das **Output List** Objekt mit der **ID 37** (ab VT Version 4) wird verwendet, um eines von mehreren Objekten aus einer Liste anzuzeigen. Welches Objekt aktuell sichtbar ist, wird über einen Index (Value) gesteuert.

## Technische Attribute (gemäß Tabelle B.25)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer. |
| 0 | **Type** | Integer 1 | Objekttyp = 37 (Output List). |
| 1 | **Width** | Integer 2 | Breite des Anzeigebereichs. |
| 2 | **Height** | Integer 2 | Höhe des Anzeigebereichs. |
| - | **Value** | Integer 1 | Aktueller Index des anzuzeigenden Objekts (0-254). 255 = nichts anzeigen. |
| - | **Number of objects** | Integer 1 | Anzahl der in der Liste enthaltenen Objekte. |

## Funktionsweise
Die Output List verhält sich ähnlich wie eine Animation, wird aber manuell über den Index gesteuert. Sie eignet sich hervorragend für:
*   **Statusanzeigen:** z. B. verschiedene Symbole für "Bereit", "In Betrieb", "Fehler".
*   **Sprachumschaltung:** Anzeige unterschiedlicher Grafiken je nach Zustand.

## Besonderheiten
Wenn der Index auf ein Objekt verweist, das größer als die definierte `Width`/`Height` der Liste ist, wird es abgeschnitten (Clipped).

Weitere Informationen und Beispiele finden sich im [ISOBUS Wiki - List (Output)](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects/list-output) von Tobias Tenberg.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, B.9.4 verwiesen.*