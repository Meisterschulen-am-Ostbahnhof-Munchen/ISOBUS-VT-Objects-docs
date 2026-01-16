# ISOBUS Objekt IDs

Siehe auch:



Stand Jetter ISO-Designer 5.6.1

hier stimmen die Objektnummern mit den IDs in der Norm überein. 

(die Objektnummern können jeden Wert annehmen; mit Ausnahme der Makros)

die Festlegung in dieser Tabelle kann man also als Good Practice bezeichnen.

| TypeName                  | StartID | FmtStr                         | ID  | Link                                                                                                             |
| ------------------------- | ------- | ------------------------------ | --- | ---------------------------------------------------------------------------------------------------------------- |
| WorkingSet                | 0       | WorkingSet\_%ld                | 0   | [ID 0 - Working-set - ISO-11783-6 - B.1](isobus-objects/ID-00---Working-set---ISO-11783-6---B.1.md)                               |
| DataMask                  | 1000    | DataMask\_%ld                  | 1   | [ID 1 - Data-mask - ISO-11783-6 - B.2.](isobus-objects/ID-01---Data-mask---ISO-11783-6---B.2.md)                                  |
| AlarmMask                 | 2000    | AlarmMask\_%ld                 | 2   | [ID 2 – Alarm Mask – ISO 11783-6 – B.3](isobus-objects/ID-02---Alarm-Mask---ISO-11783-6---B.3.md)                                  |
| Container                 | 3000    | Container\_%ld                 | 3   | [ID 3 – Container – ISO 11783-6 – B.4](isobus-objects/ID-03---Container---ISO-11783-6---B.4.md)                                    |
| SoftKeyMask               | 4000    | SoftKeyMask\_%ld               | 4   | [ID 4 – Soft key mask – ISO 11783-6 – B.5](isobus-objects/ID-04---Soft-key-mask---ISO-11783-6---B.5.md)                            |
| SoftKey                   | 5000    | SoftKey\_%ld                   | 5   | [ID 5 – Key (Soft Key) – ISO 11783-6 – B.6](isobus-objects/ID-05---Key-(Soft-Key)---ISO-11783-6---B.6.md)                          |
| KeyGroup                  | 35000   | KeyGroup\_%ld                  | 35  | [ID 35 – Key Group – ISO 11783-6 – B.20](isobus-objects/ID-35---Key-Group---ISO-11783-6---B.20.md)              |
| Button                    | 6000    | Button\_%ld                    | 6   | [ID 6 – Button – ISO 11783-6 – B.7](isobus-objects/ID-06---Button---ISO-11783-6---B.7.md)                        |
| InputBoolean              | 7000    | InputBoolean\_%ld              | 7   | [ID 7 – Input boolean – ISO 11783-6 – B.8.2](isobus-objects/ID-07---Input-boolean---ISO-11783-6---B.8.2.md)      |
| InputString               | 8000    | InputString\_%ld               | 8   | [ID 8 – Input string – ISO 11783-6 – B.8.3](isobus-objects/ID-08---Input-string---ISO-11783-6---B.8.3.md)        |
| InputNumber               | 9000    | InputNumber\_%ld               | 9   | [ID 9 – Input number – ISO 11783-6 – B.8.4](isobus-objects/ID-09---Input-number---ISO-11783-6---B.8.4.md)        |
| InputList                 | 10000   | InputList\_%ld                 | 10  | [ID 10 – Input list – ISO 11783-6 – B.8.5](isobus-objects/ID-10---Input-list---ISO-11783-6---B.8.5.md)           |
| OutputString              | 11000   | OutputString\_%ld              | 11  | [ID 11 – Output string – ISO 11783-6 – B.9.2](isobus-objects/ID-11---Output-string---ISO-11783-6---B.9.2.md)     |
| OutputNumber              | 12000   | OutputNumber\_%ld              | 12  | [ID 12 – Output number – ISO 11783-6 – B.9.3](isobus-objects/ID-12---Output-number---ISO-11783-6---B.9.3.md)     |
| OutputList                | 37000   | OutputList\_%ld                | 37  | [ID 37 – Output List – ISO 11783-6 – B.9.4](isobus-objects/ID-37---Output-List---ISO-11783-6---B.9.4.md)         |
| Line                      | 13000   | Line\_%ld                      | 13  | [ID 13 – Output line – ISO 11783-6 – B.10.2](isobus-objects/ID-13---Output-line---ISO-11783-6---B.10.2.md)       |
| Rectangle                 | 14000   | Rectangle\_%ld                 | 14  | [ID 14 – Output rectangle – ISO 11783-6 – B.10.3](isobus-objects/ID-14---Output-rectangle---ISO-11783-6---B.10.3.md) |
| Ellipse                   | 15000   | Ellipse\_%ld                   | 15  | [ID 15 – Output ellipse – ISO 11783-6 – B.10.4](isobus-objects/ID-15---Output-ellipse---ISO-11783-6---B.10.4.md) |
| Polygon                   | 16000   | Polygon\_%ld                   | 16  | [ID 16 – Output polygon – ISO 11783-6 – B.10.5](isobus-objects/ID-16---Output-polygon---ISO-11783-6---B.10.5.md) |
| Meter                     | 17000   | Meter\_%ld                     | 17  | [ID 17 – Output meter – ISO 11783-6 – B.11.2](isobus-objects/ID-17---Output-meter---ISO-11783-6---B.11.2.md)     |
| LinearBargraph            | 18000   | LinearBargraph\_%ld            | 18  | [ID 18 – Output linear bar graph – ISO 11783-6 – B.11.3](isobus-objects/ID-18---Output-linear-bar-graph---ISO-11783-6---B.11.3.md) |
| ArchedBargraph            | 19000   | ArchedBargraph\_%ld            | 19  | [ID 19 – Output arched bar graph – ISO 11783-6 – B.11.4](isobus-objects/ID-19---Output-arched-bar-graph---ISO-11783-6---B.11.4.md) |
| PictureGraphic            | 20000   | PictureGraphic\_%ld            | 20  | [ID 20 – Picture graphic – ISO 11783-6 – B.12.2](isobus-objects/ID-20---Picture-graphic---ISO-11783-6---B.12.2.md) |
| GraphicsContext           | 36000   | GraphicsContext\_%ld           | 36  | [ID 36 – Graphics Context Object – ISO 11783-6 – B.18](isobus-objects/ID-36---Graphics-Context---ISO-11783-6---B.18.md) |
| NumberVariable            | 21000   | NumberVariable\_%ld            | 21  | [ID 21 – Number variable – ISO 11783-6 – B.13.2](isobus-objects/ID-21---Number-variable---ISO-11783-6---B.13.2.md) |
| StringVariable            | 22000   | StringVariable\_%ld            | 22  | [ID 22 – String variable – ISO 11783-6 – B.13.3](isobus-objects/ID-22---String-variable---ISO-11783-6---B.13.3.md) |
| FontAttributes            | 23000   | FontAttributes\_%ld            | 23  | [ID 23 – Font attributes – ISO 11783-6 – B.14.2](isobus-objects/ID-23---Font-attributes---ISO-11783-6---B.14.2.md) |
| LineAttributes            | 24000   | LineAttributes\_%ld            | 24  | [ID 24 – Line attributes – ISO 11783-6 – B.14.3](isobus-objects/ID-24---Line-attributes---ISO-11783-6---B.14.3.md) |
| FillAttributes            | 25000   | FillAttributes\_%ld            | 25  | [ID 25 – Fill attributes – ISO 11783-6 – B.14.4](isobus-objects/ID-25---Fill-attributes---ISO-11783-6---B.14.4.md) |
| InputAttributes           | 26000   | InputAttributes\_%ld           | 26  | [ID 26 – Input attributes – ISO 11783-6 – B.14.5](isobus-objects/ID-26---Input-attributes---ISO-11783-6---B.14.5.md) |
| ExtendedInputAttributes   | 38000   | ExtendedInputAttributes\_%ld   | 38  | [ID 38 – Extended Input Attributes – ISO 11783-6 – B.14.6](isobus-objects/ID-38---Extended-Input-Attributes---ISO-11783-6---B.14.6.md) |
| ObjectPointer             | 27000   | ObjectPointer\_%ld             | 27  | [ID 27 – Object pointer – ISO 11783-6 – B.15](isobus-objects/ID-27---Object-pointer---ISO-11783-6---B.15.md)                       |
| Macro                     | 0       | Macro\_%ld                     | 0   | [ID 28 – Macro – ISO 11783-6 – B.16](isobus-objects/ID-28---Macro---ISO-11783-6---B.16.md)                                           |
| AuxFunction2              | 31000   | AuxFunction2\_%ld              | 31  | [ID 31 – Auxiliary Function Type 2 – ISO 11783-6 – J.4.3](isobus-objects/ID-31---Auxiliary-Function-Type-2---ISO-11783-6---J.4.3.md)           |
| AuxInput2                 | 32000   | AuxInput2\_%ld                 | 32  | [ID 32 – Auxiliary Input Type 2 – ISO 11783-6 – J.4.5](isobus-objects/ID-32---Auxiliary-Input-Type-2---ISO-11783-6---J.4.5.md)                 |
| AuxObjectPointer          | 33000   | AuxObjectPointer\_%ld          | 33  | [ID 33 – Auxiliary Control Designator Type 2 Object Pointer – ISO 11783-6 – J.4.7](isobus-objects/ID-33---Auxiliary-Control-Designator-Type-2---ISO-11783-6---J.4.7.md) |
| ColorMap                  | 39000   | ColorMap\_%ld                  | 39  | [ID 39 – Colour Map – ISO 11783-6 – B.17](isobus-objects/ID-39---Colour-Map---ISO-11783-6---B.17.md)                                             |
| WindowMask                | 34000   | WindowMask\_%ld                | 34  | [ID 34 – Window Mask – ISO 11783-6 – B.19](isobus-objects/ID-34---Window-Mask---ISO-11783-6---B.19.md)                                           |
| ObjectLabelReferenceList  | 40000   | ObjectLabelReferenceList\_%ld  | 40  | [ID 40 – Object Label Reference List – ISO 11783-6 – B.21](isobus-objects/ID-40---Object-Label-Reference-List---ISO-11783-6---B.21.md)           |
| ExternalObjectDefinition  | 41000   | ExternalObjectDefinition\_%ld  | 41  | [ID 41 – External Object Definition – ISO 11783-6 – B.22](isobus-objects/ID-41---External-Object-Definition---ISO-11783-6---B.22.md)             |
| ExternalReferenceName     | 42000   | ExternalReferenceName\_%ld     | 42  | [ID 42 – External reference NAME – ISO 11783-6 – B.23](isobus-objects/ID-42---External-reference-NAME---ISO-11783-6---B.23.md)                   |
| ExternalObjectPointer     | 43000   | ExternalObjectPointer\_%ld     | 43  | [ID 43 – External Object Pointer – ISO 11783-6 – B.24](isobus-objects/ID-43---External-Object-Pointer---ISO-11783-6---B.24.md)                   |
| Animation                 | 44000   | Animation\_%ld                 | 44  | [ID 44 – Animation – ISO 11783-6 – B.25](isobus-objects/ID-44---Animation---ISO-11783-6---B.25.md)                                               |
| ScaledGraphic             | 48000   | ScaledGraphic\_%ld             | 48  | [ID 48 – Scaled Graphic – ISO 11783-6 – B.28](isobus-objects/ID-48---Scaled-Graphic---ISO-11783-6---B.28.md)                                     |
| GraphicData               | 46000   | GraphicData\_%ld               | 46  | [ID 46 – Graphic Data (PNG) – ISO 11783-6 – B.27](isobus-objects/ID-46---Graphic-Data---ISO-11783-6---B.27.md)                                   |
| ColorPalette              | 45000   | ColorPalette\_%ld              | 45  | [ID 45 – Colour Palette – ISO 11783-6 – B.26](isobus-objects/ID-45---Colour-Palette---ISO-11783-6---B.26.md)                                     |
| WorkingSetSpecialControls | 47000   | WorkingSetSpecialControls\_%ld | 47  | [ID 47 – Working Set Special Controls – ISO 11783-6 – B.29](isobus-objects/ID-47---Working-Set-Special-Controls---ISO-11783-6---B.29.md)         |
| IDsForTemporaryUse        | 64000   | IDsForTemporaryUse\_%ld        | 64  | [I](I)                                                                                                           |
| Proxy                     | 4194304 | Proxy\_%ld                     |     | [I](I)                                                                                                           |

In Versionen vor V. 5.6.0, also bis ISO-Designer 5.5.1

war folgende Benennung üblich:

hier stimmte die ID nicht mit der ObjectID zusammen. 

z.b. bei AUX Function. 

| TypeName                 | StartID | FmtStr                        |
| ------------------------ | ------- | ----------------------------- |
| WorkingSet               | 0       | WorkingSet\_%ld               |
| DataMask                 | 100     | DataMask\_%ld                 |
| AlarmMask                | 200     | AlarmMask\_%ld                |
| Container                | 300     | Container\_%ld                |
| SoftKeyMask              | 400     | SoftKeyMask\_%ld              |
| SoftKey                  | 500     | SoftKey\_%ld                  |
| KeyGroup                 | 3600    | KeyGroup\_%ld                 |
| Button                   | 600     | Button\_%ld                   |
| InputBoolean             | 700     | InputBoolean\_%ld             |
| InputString              | 800     | InputString\_%ld              |
| InputNumber              | 900     | InputNumber\_%ld              |
| InputList                | 1000    | InputList\_%ld                |
| OutputString             | 1100    | OutputString\_%ld             |
| OutputNumber             | 1200    | OutputNumber\_%ld             |
| OutputList               | 3000    | OutputList\_%ld               |
| Line                     | 1300    | Line\_%ld                     |
| Rectangle                | 1400    | Rectangle\_%ld                |
| Ellipse                  | 1500    | Ellipse\_%ld                  |
| Polygon                  | 1600    | Polygon\_%ld                  |
| Meter                    | 1700    | Meter\_%ld                    |
| LinearBargraph           | 1800    | LinearBargraph\_%ld           |
| ArchedBargraph           | 1900    | ArchedBargraph\_%ld           |
| PictureGraphic           | 2000    | \[File Name]\_%ld             |
| GraphicsContext          | 3100    | GraphicsContext\_%ld          |
| NumberVariable           | 2100    | NumberVariable\_%ld           |
| StringVariable           | 2200    | StringVariable\_%ld           |
| FontAttributes           | 2300    | FontAttributes\_%ld           |
| LineAttributes           | 2400    | LineAttributes\_%ld           |
| FillAttributes           | 2500    | FillAttributes\_%ld           |
| InputAttributes          | 2600    | InputAttributes\_%ld          |
| ExtendedInputAttributes  | 3200    | ExtendedInputAttributes\_%ld  |
| ObjectPointer            | 2700    | ObjectPointer\_%ld            |
| Macro                    | 0       | Macro\_%ld                    |
| AuxInput2                | 2800    | AuxInput2\_%ld                |
| AuxFunction2             | 2900    | AuxFunction2\_%ld             |
| AuxObjectPointer         | 3300    | AuxObjectPointer\_%ld         |
| ColorMap                 | 3400    | ColorMap\_%ld                 |
| WindowMask               | 3500    | WindowMask\_%ld               |
| ObjectLabelReferenceList | 3700    | ObjectLabelReferenceList\_%ld |
| ExternalObjectDefinition | 3800    | ExternalObjectDefinition\_%ld |
| ExternalReferenceName    | 3900    | ExternalReferenceName\_%ld    |
| ExternalObjectPointer    | 4000    | ExternalObjectPointer\_%ld    |
| Animation                | 4100    | Animation\_%ld                |
| IDsForTemporaryUse       | 64000   | IDsForTemporaryUse\_%ld       |
| Proxy                    | 4194304 | Proxy\_%ld                    |
