# ID 42 – External Reference NAME – ISO 11783-6 – B.23

```{index} single: ID 42 – External Reference NAME – ISO 11783-6 – B.23
```

Das **External Reference NAME** Objekt mit der **ID 42** (ab VT Version 5) identifiziert ein anderes Working Set auf dem Bus über seinen eindeutigen ISO-NAME.

## Technische Attribute (gemäß Tabelle B.68)

| AID | Name | Typ | Beschreibung |
| :--- | :--- | :--- | :--- |
| - | **Object ID** | Integer 2 | Eindeutige Identifikationsnummer. |
| 0 | **Type** | Integer 1 | Objekttyp = 42 (External Reference NAME). |
| 1 | **Options** | Bitmask 1 | Bit 0 = Enabled (Gültigkeit der Referenz). |
| 2 | **NAME 0** | Integer 4 | Erste 4 Bytes des Ziel-ISO-NAMEs. |
| 3 | **NAME 1** | Integer 4 | Letzte 4 Bytes des Ziel-ISO-NAMEs. |

## Funktionsweise
Dieses Objekt fungiert als "Adressbucheintrag". Wenn eine ECU ein Objekt von einer anderen ECU einbinden möchte, nutzt sie diesen Eintrag, um dem Terminal mitzuteilen, von welcher ECU (identifiziert durch den NAME) das Objekt stammt.

----
*Hinweis: Für detaillierte Spezifikationen wird auf die offizielle ISO 11783-6:2018, B.23 verwiesen.*