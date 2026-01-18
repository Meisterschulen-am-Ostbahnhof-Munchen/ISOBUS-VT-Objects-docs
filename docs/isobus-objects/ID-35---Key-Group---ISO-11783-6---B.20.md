# ID 35 – Key Group – ISO 11783-6 – B.20

```{index} single: ID 35 – Key Group – ISO 11783-6 – B.20
```

Das **Key Group** Objekt mit der **ID 35** dient dazu, eine Gruppe von Softkeys zusammenzufassen. Dies wird primär in Verbindung mit **User-Layout Soft Key Masks** verwendet (ab VT Version 4).

## Technische Attribute (gemäß Tabelle B.63)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer. |
| 0 | **Type** | Integer 1 | Objekttyp = 35 (Key Group). |
| - | **Options** | Bitmask 1 | 1 = Enabled (Sichtbar/Aktiv). |
| - | **Number of objects** | Integer 1 | Anzahl der Tasten (Keys) in dieser Gruppe. |

### Wiederholung für Key-Objekte:
| Name | Typ | Beschreibung |
| :--- | :--- | :--- |
| **Object ID** | Integer 2 | ID eines Key-Objekts (ID 5). |

## Bedeutung
Ähnlich wie bei Window Masks für den Datenbereich, erlauben Key Groups es dem Terminal-Benutzer, ganze Funktionsblöcke (z. B. "Hydrauliksteuerung") als Gruppe in seine individuell zusammengestellte Softkey-Leiste zu ziehen.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, B.20 verwiesen.*