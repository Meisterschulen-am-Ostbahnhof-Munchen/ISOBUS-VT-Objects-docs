# ISOBUS-Objekte-Versionen

Welches Objekt ist in welcher Version vorhanden ? 

die Tabelle unter: 
[https://extranet.epec.fi/Public/Manuals/EPEC_Programming_And_Libraries/projecttopics/topic000962.htm](https://extranet.epec.fi/Public/Manuals/EPEC_Programming_And_Libraries/projecttopics/topic000962.htm)
ist leider falsch und veraltet: 

hier soll eine Aktuelle Tabelle entstehen, 
basierend auf der ISO 11783-6:2018(en)
Tractors and machinery for agriculture and forestry — Serial control and communications data network — Part 6: Virtual terminal

|  ID | Object description                                 | VT 2 | VT 3 | VT 4 | VT 5 | VT 6 | Standard         | Jetter support    |
| :-: | -------------------------------------------------- | :--: | :--: | :--: | :--: | :--: | ---------------- | :---------------: |
|  0  | Working set                                        |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.1    |         L3        |
|  1  | Data mask                                          |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.2    |         L3        |
|  2  | Alarm Mask                                         |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.3    |         X         |
|  3  | Container                                          |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.4    |         X         |
|  4  | Soft key mask                                      |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.5    |         X         |
|  5  | Key                                                |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.6    |         X         |
|  6  | Button                                             |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.7    |         X         |
|  7  | Input boolean                                      |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.8.2  |         X         |
|  8  | Input string                                       |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.8.3  |         X         |
|  9  | Input number                                       |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.8.4  |         X         |
|  10 | Input list                                         |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.8.5  |         X         |
|  11 | Output string                                      |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.9.2  |         X         |
|  12 | Output number                                      |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.9.3  |         X         |
|  13 | Output line                                        |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.10.2 |         X         |
|  14 | Output rectangle                                   |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.10.3 |         X         |
|  15 | Output ellipse                                     |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.10.4 |         X         |
|  16 | Output polygon                                     |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.10.5 |         X         |
|  17 | Output meter                                       |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.11.2 |         X         |
|  18 | Output linear bar graph                            |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.11.3 |         X         |
|  19 | Output arched bar graph                            |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.11.4 |         X         |
|  20 | Picture graphic                                    |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.12.2 |         X         |
|  21 | Number variable                                    |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.13.2 |         X         |
|  22 | String variable                                    |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.13.3 |         X         |
|  23 | Font attributes                                    |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.14.2 |         X         |
|  24 | Line attributes                                    |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.14.3 |         X         |
|  25 | Fill attributes                                    |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.14.4 |         X         |
|  26 | Input attributes                                   |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.14.5 |         X         |
|  27 | Object pointer                                     |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.15   |         X         |
|  28 | Macro                                              |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.16   |         X         |
|  31 | Auxiliary Function Type 2                          |      |   X  |   X  |   X  |   X  | 11783-6 – J.4.3  |         X         |
|  33 | Auxiliary Control Designator Type 2 Object Pointer |      |   X  |   X  |   X  |   X  | 11783-6 – J.4.7  |         X         |
|  34 | Windows mask                                       |      |      |   X  |   X  |   X  | 11783-6 – B.19   |         X         |
|  35 | Key group                                          |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.20   |         -         |
|  36 | Graphics context object                            |      |      |   X  |   X  |   X  | 11783-6 – B.18   |         X         |
|  37 | Output list                                        |      |      |   X  |   X  |   X  | 11783-6 – B.9.4  |         X         |
|  38 | Extended input attributes                          |      |      |   X  |   X  |   X  | 11783-6 – B.14.6 |         X         |
|  39 | Colour map                                         |      |      |   X  |   X  |   X  | 11783-6 – B.17   |         X         |
|  40 | Object label                                       |      |      |   X  |   X  |   X  | 11783-6 – B.21   |         -         |
|  41 | External object definition                         |      |      |      |   X  |   X  | 11783-6 – B.22   |         -         |
|  42 | External reference NAME                            |      |      |      |   X  |   X  | 11783-6 – B.23   |         -         |
|  43 | External object pointer reference                  |      |      |      |   X  |   X  | 11783-6 – B.24   |         -         |
|  44 | Animation                                          |      |      |      |   X  |   X  | 11783-6 – B.25   |         -         |
|  45 | Animation                                          |      |      |      |   X  |   X  | 11783-6 – B.25   |         -         |
|  46 | Portable Network Graphic object                    |      |      |      |      |   X  | 11783-6 – B.27   |         -         |
