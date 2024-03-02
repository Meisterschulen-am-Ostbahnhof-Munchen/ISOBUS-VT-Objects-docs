# ISOBUS-Objekte-Versionen

Welches Objekt ist in welcher Version vorhanden ? 

die Tabelle unter: 
[https://extranet.epec.fi/Public/Manuals/EPEC_Programming_And_Libraries/projecttopics/topic000962.htm](https://extranet.epec.fi/Public/Manuals/EPEC_Programming_And_Libraries/projecttopics/topic000962.htm)
ist leider falsch und veraltet: 

hier soll eine Aktuelle Tabelle entstehen, 
basierend auf der ISO 11783-6:2018(en)
Tractors and machinery for agriculture and forestry — Serial control and communications data network — Part 6: Virtual terminal

|  ID | Object description                                 | VT 2 | VT 3 | VT 4 | VT 5 | VT 6 | Standard                  | Jetter support    |
| :-: | -------------------------------------------------- | :--: | :--: | :--: | :--: | :--: | ------------------------- | :---------------: |
|  0  | Working set                                        |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.1             |         L3        |
|  1  | Data mask                                          |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.2             |         L3        |
|  2  | Alarm Mask                                         |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.3             |         X         |
|  3  | Container                                          |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.4             |         X         |
|  4  | Soft Key Mask                                      |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.5             |         X         |
|  5  | Key                                                |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.6             |         X         |
|  6  | Button                                             |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.7             |         X         |
|  7  | Input Boolean                                      |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.8.2           |         X         |
|  8  | Input String                                       |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.8.3           |         X         |
|  9  | Input Number                                       |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.8.4           |         X         |
|  10 | Input List                                         |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.8.5           |         X         |
|  11 | Output String                                      |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.9.2           |         X         |
|  12 | Output Number                                      |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.9.3           |         X         |
|  13 | Output Line                                        |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.10.2          |         X         |
|  14 | Output Rectangle                                   |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.10.3          |         X         |
|  15 | Output Ellipse                                     |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.10.4          |         X         |
|  16 | Output Polygon                                     |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.10.5          |         X         |
|  17 | Output Meter                                       |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.11.2          |         X         |
|  18 | Output Linear Bar Graph                            |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.11.3          |         X         |
|  19 | Output Arched Bar Graph                            |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.11.4          |         X         |
|  20 | Picture Graphic                                    |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.12.1 + B.12.2 |         X         |
|  21 | Number Variable                                    |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.13.2          |         X         |
|  22 | String Variable                                    |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.13.3          |         X         |
|  23 | Font Attributes                                    |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.14.2          |         X         |
|  24 | Line Attributes                                    |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.14.3          |         X         |
|  25 | Fill Attributes                                    |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.14.4          |         X         |
|  26 | Input Attributes                                   |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.14.5          |         X         |
|  27 | Object Pointer                                     |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.15            |         X         |
|  28 | Macro                                              |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.16            |         X         |
|  29 | Auxiliary Function Type 1                          |   X  |      |      |      |      | 11783-6 - J.4.2           |         ?         |
|  30 | Auxiliary Input Type 1                             |   X  |      |      |      |      | 11783-6 - J.4.4           |         ?         |
|  31 | Auxiliary Function Type 2                          |      |   X  |   X  |   X  |   X  | 11783-6 – J.4.3           |         X         |
|  32 | Auxiliary Input Type 2                             |      |   X  |   X  |   X  |   X  | 11783-6 – J.4.5           |         ?         |
|  33 | Auxiliary Control Designator Type 2 Object Pointer |      |   X  |   X  |   X  |   X  | 11783-6 – J.4.7           |         X         |
|  34 | Windows Mask                                       |      |      |   X  |   X  |   X  | 11783-6 – B.19            |         X         |
|  35 | Key Group                                          |      |      |   X  |   X  |   X  | 11783-6 – B.20            |         -         |
|  36 | Graphics Context Object                            |      |      |   X  |   X  |   X  | 11783-6 – B.18            |         X         |
|  37 | Output List                                        |      |      |   X  |   X  |   X  | 11783-6 – B.9.4           |         X         |
|  38 | Extended Input Attributes                          |      |      |   X  |   X  |   X  | 11783-6 – B.14.6          |         X         |
|  39 | Colour Map                                         |      |      |   X  |   X  |   X  | 11783-6 – B.17            |         X         |
|  40 | Object Label Reference List                        |      |      |   X  |   X  |   X  | 11783-6 – B.21            |         -         |
|  41 | External Object Definition                         |      |      |      |   X  |   X  | 11783-6 – B.22            |         -         |
|  42 | External reference NAME                            |      |      |      |   X  |   X  | 11783-6 – B.23            |         -         |
|  43 | External Object Pointer                            |      |      |      |   X  |   X  | 11783-6 – B.24            |         -         |
|  44 | Animation                                          |      |      |      |   X  |   X  | 11783-6 – B.25            |         -         |
|  45 | Colour Palette                                     |      |      |      |   X  |   X  | 11783-6 – B.26            |         -         |
|  46 | Graphic Data                                       |      |      |      |      |   X  | 11783-6 – B.27            |         L6        |
|  47 | Working Set Special Controls                       |      |      |      |      |   X  | 11783-6 - B.29            |         ?         |
|  48 | Scaled Graphic                                     |      |      |      |      |   X  | 11783-6 - B.28            |         ?         |