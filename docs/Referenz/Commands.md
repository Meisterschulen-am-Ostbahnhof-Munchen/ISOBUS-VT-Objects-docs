# Kommando-Übersicht (ISO 11783-6 Table A.5)

```{index} single: Commands
```

Diese Tabelle listet alle Befehle (Messages), die zwischen ECU (Working Set) und VT ausgetauscht werden können.

*   **Function (Decimal/Hex):** Der Code im ersten Byte der Nachricht (bei Destination Specific PGN).
*   **Allowed in Macro:** Ob der Befehl in einem Makro-Objekt gespeichert werden darf.

| Clause | Message Name | PGN | Function (Hex) | Macro? | VT Vers. |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **C.2.3** | Object Pool Transfer | ECU->VT | 11 | No | 2 |
| **C.2.4** | End of Object Pool | ECU->VT | 12 | No | 2 |
| **D.4** | Get Number of Soft Keys | ECU->VT | C2 | No | 2 |
| **D.6** | Get Text Font Data | ECU->VT | C3 | No | 2 |
| **D.8** | Get Hardware Message | ECU->VT | C7 | No | 2 |
| **D.12** | Get Window Mask Data | ECU->VT | C4 | No | 4 |
| **D.14** | Get Supported Objects | ECU->VT | C5 | No | 4 |
| **D.16** | Screen Capture | ECU->VT | C6 | No | 6 |
| **D.18** | Identify VT | ECU->VT | BB | No | 4 |
| **E.2** | Get Versions | ECU->VT | DF | No | 2 |
| **E.4** | Store Version | ECU->VT | D0 | No | 2 |
| **E.6** | Load Version | ECU->VT | D1 | No | 2 |
| **E.8** | Delete Version | ECU->VT | D2 | No | 2 |
| **E.10** | Extended Get Versions | ECU->VT | D3 | No | 5 |
| **E.12** | Extended Store Version | ECU->VT | D4 | No | 5 |
| **E.14** | Extended Load Version | ECU->VT | D5 | No | 5 |
| **E.16** | Extended Delete Version | ECU->VT | D6 | No | 5 |
| **F.2** | Hide/Show Object | ECU->VT | A0 | **Yes** | 2 |
| **F.4** | Enable/Disable Object | ECU->VT | A1 | **Yes** | 2 |
| **F.6** | Select Input Object | ECU->VT | A2 | **Yes** | 2 |
| **F.8** | ESC Command | ECU->VT | 92 | No | 2 |
| **F.10** | Control Audio Signal | ECU->VT | A3 | **Yes** | 2 |
| **F.12** | Set Audio Volume | ECU->VT | A4 | **Yes** | 2 |
| **F.14** | Change Child Location | ECU->VT | A5 | **Yes** | 2 |
| **F.16** | Change Child Position | ECU->VT | B4 | **Yes** | 2 |
| **F.18** | Change Size | ECU->VT | A6 | **Yes** | 2 |
| **F.20** | Change Background Colour| ECU->VT | A7 | **Yes** | 2 |
| **F.22** | Change Numeric Value | ECU->VT | A8 | **Yes** | 2 |
| **F.24** | Change String Value | ECU->VT | B3 | **Yes** | 2 |
| **F.26** | Change End Point | ECU->VT | A9 | **Yes** | 2 |
| **F.28** | Change Font Attributes | ECU->VT | AA | **Yes** | 2 |
| **F.30** | Change Line Attributes | ECU->VT | AB | **Yes** | 2 |
| **F.32** | Change Fill Attributes | ECU->VT | AC | **Yes** | 2 |
| **F.34** | Change Active Mask | ECU->VT | AD | **Yes** | 2 |
| **F.36** | Change Soft Key Mask | ECU->VT | AE | **Yes** | 2 |
| **F.38** | Change Attribute | ECU->VT | AF | **Yes** | 2 |
| **F.40** | Change Priority | ECU->VT | B0 | **Yes** | 2 |
| **F.42** | Change List Item | ECU->VT | B1 | **Yes** | 2 |
| **F.44** | Delete Object Pool | ECU->VT | B2 | No | 2 |
| **F.46** | Lock/Unlock Mask | ECU->VT | BD | **Yes** | 4 |
| **F.48** | Execute Macro | ECU->VT | BE | **Yes** | 4 |
| **F.50** | Change Object Label | ECU->VT | B5 | **Yes** | 4 |
| **F.52** | Change Polygon Point | ECU->VT | B6 | **Yes** | 4 |
| **F.54** | Change Polygon Scale | ECU->VT | B7 | **Yes** | 4 |
| **F.56** | Graphics Context Command | ECU->VT | B8 | No | 4 |
| **F.58** | Get Attribute Value | ECU->VT | B9 | No | 4 |
| **F.60** | Select Colour Map/Palette | ECU->VT | BA | **Yes** | 4 |
| **F.62** | Execute Extended Macro | ECU->VT | BC | **Yes** | 5 |
| **F.64** | Select Active Working Set | ECU->VT | 90 | **Yes** | 6 |
