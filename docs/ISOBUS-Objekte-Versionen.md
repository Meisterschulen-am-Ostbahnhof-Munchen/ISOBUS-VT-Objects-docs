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
|  0  | Working set                                        |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.1             |   L2 - L6         |
|  1  | Data mask                                          |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.2             |   L2 - L6         |
|  2  | Alarm Mask                                         |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.3             |   L2 - L6         |
|  3  | Container                                          |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.4             |   L2 - L6         |
|  4  | Soft Key Mask                                      |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.5             |   L2 - L6         |
|  5  | Key                                                |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.6             |   L2 - L6         |
|  6  | Button                                             |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.7             |   L2 - L6         |
|  7  | Input Boolean                                      |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.8.2           |   L2 - L6         |
|  8  | Input String                                       |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.8.3           |   L2 - L6         |
|  9  | Input Number                                       |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.8.4           |   L2 - L6         |
|  10 | Input List                                         |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.8.5           |   L2 - L6         |
|  11 | Output String                                      |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.9.2           |   L2 - L6         |
|  12 | Output Number                                      |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.9.3           |   L2 - L6         |
|  13 | Output Line                                        |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.10.2          |   L2 - L6         |
|  14 | Output Rectangle                                   |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.10.3          |   L2 - L6         |
|  15 | Output Ellipse                                     |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.10.4          |   L2 - L6         |
|  16 | Output Polygon                                     |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.10.5          |   L2 - L6         |
|  17 | Output Meter                                       |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.11.2          |   L2 - L6         |
|  18 | Output Linear Bar Graph                            |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.11.3          |   L2 - L6         |
|  19 | Output Arched Bar Graph                            |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.11.4          |   L2 - L6         |
|  20 | Picture Graphic (BMP)                              |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.12.1 + B.12.2 |   L2 - L6         |
|  21 | Number Variable                                    |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.13.2          |   L2 - L6         |
|  22 | String Variable                                    |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.13.3          |   L2 - L6         |
|  23 | Font Attributes                                    |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.14.2          |   L2 - L6         |
|  24 | Line Attributes                                    |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.14.3          |   L2 - L6         |
|  25 | Fill Attributes                                    |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.14.4          |   L2 - L6         |
|  26 | Input Attributes                                   |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.14.5          |   L2 - L6         |
|  27 | Object Pointer                                     |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.15            |   L2 - L6         |
|  28 | Macro                                              |   X  |   X  |   X  |   X  |   X  | 11783-6 – B.16            |   L2 - L6         |
|  29 | Auxiliary Function Type 1                          |   X  |      |      |      |      | 11783-6 - J.4.2           |   L6              |
|  30 | Auxiliary Input Type 1                             |   X  |      |      |      |      | 11783-6 - J.4.4           |   L6              |
|  31 | Auxiliary Function Type 2                          |      |   X  |   X  |   X  |   X  | 11783-6 – J.4.3           |   L3 - L6         |
|  32 | Auxiliary Input Type 2                             |      |   X  |   X  |   X  |   X  | 11783-6 – J.4.5           |   L3 - L6         |
|  33 | Auxiliary Control Designator<br>Type 2 Object Pointer |      |   X  |   X  |   X  |   X  | 11783-6 – J.4.7           |   L3 - L6         |
|  34 | Windows Mask                                       |      |      |   X  |   X  |   X  | 11783-6 – B.19            |   L4 - L6         |
|  35 | Key Group                                          |      |      |   X  |   X  |   X  | 11783-6 – B.20            |   L4 - L6         |
|  36 | Graphics Context Object                            |      |      |   X  |   X  |   X  | 11783-6 – B.18            |   L3 - L6         |
|  37 | Output List                                        |      |      |   X  |   X  |   X  | 11783-6 – B.9.4           |   L4 - L6         |
|  38 | Extended Input Attributes                          |      |      |   X  |   X  |   X  | 11783-6 – B.14.6          |   L4 - L6         |
|  39 | Colour Map                                         |      |      |   X  |   X  |   X  | 11783-6 – B.17            |   L5 - L6         |
|  40 | Object Label Reference List                        |      |      |   X  |   X  |   X  | 11783-6 – B.21            |   L5 - L6         |
|  41 | External Object Definition                         |      |      |      |   X  |   X  | 11783-6 – B.22            |   L5 - L6         |
|  42 | External reference NAME                            |      |      |      |   X  |   X  | 11783-6 – B.23            |   L5 - L6         |
|  43 | External Object Pointer                            |      |      |      |   X  |   X  | 11783-6 – B.24            |   L5 - L6         |
|  44 | Animation                                          |      |      |      |   X  |   X  | 11783-6 – B.25            |   L5 - L6         |
|  45 | Colour Palette                                     |      |      |      |   X  |   X  | 11783-6 – B.26            |   L6              |
|  46 | Graphic Data (PNG)                                 |      |      |      |      |   X  | 11783-6 – B.27            |   L6              |
|  47 | Working Set Special Controls                       |      |      |      |      |   X  | 11783-6 - B.29            |   L6              |
|  48 | Scaled Graphic                                     |      |      |      |      |   X  | 11783-6 - B.28            |   L6              |
