# ID 41 – External Object Definition – ISO 11783-6 – B.22

```{index} single: ID 41 – External Object Definition – ISO 11783-6 – B.22
```

Das **External Object Definition** Objekt mit der **ID 41** (ab VT Version 5) ist Teil des Mechanismus für **Working-Set-übergreifende Objektreferenzen**. Es definiert, welche Objekte eines eigenen Pools von anderen Working Sets referenziert werden dürfen.

## Technische Attribute (gemäß Tabelle B.66)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer. |
| 0 | **Type** | Integer 1 | Objekttyp = 41 (External Object Definition). |
| 1 | **Options** | Bitmask 1 | Bit 0 = Enabled (Freigabe der Referenzierung). |
| 2 | **NAME 0** | Integer 4 | Erste 4 Bytes des NAME-Attributs des Working Sets, das zugreifen darf. |
| 3 | **NAME 1** | Integer 4 | Letzte 4 Bytes des NAME-Attributs des berechtigten Working Sets. |
| - | **Number of objects** | Integer 1 | Anzahl der freigegebenen Objekte. |

## Funktionsweise
Damit Working Set A ein Objekt von Working Set B anzeigen kann (via *External Object Pointer*), muss Working Set B dieses Objekt explizit in einer *External Object Definition* für Working Set A freigeben. Dies dient der Sicherheit und Kontrolle über die eigenen Pool-Ressourcen.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, B.22 verwiesen.*
