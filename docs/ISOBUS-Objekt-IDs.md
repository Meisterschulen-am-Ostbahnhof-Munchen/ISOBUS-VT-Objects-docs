# ISOBUS Objekt IDs

Siehe auch:



Stand Jetter ISO-Designer 5.6.1

hier stimmen die Objektnummern mit den IDs in der Norm überein. 

(die Objektnummern können jeden Wert annehmen; mit Ausnahme der Makros)

die Festlegung in dieser Tabelle kann man also als Good Practice bezeichnen.

| TypeName                  | StartID | FmtStr                         | ID  | Link                                                                                                             |
| ------------------------- | ------- | ------------------------------ | --- | ---------------------------------------------------------------------------------------------------------------- |
| WorkingSet                | 0       | WorkingSet\_%ld                | 0   | [ID 0 - Working-set - ISO-11783-6 - B.1](ID-00---Working-set---ISO-11783-6---B.1)                               |
| DataMask                  | 1000    | DataMask\_%ld                  | 1   | [ID 1 - Data-mask - ISO-11783-6 - B.2.](ID-01---Data-mask---ISO-11783-6---B.2)                                  |
| AlarmMask                 | 2000    | AlarmMask\_%ld                 | 2   | [ID 2 – Alarm Mask – ISO 11783-6 – B.3](ID-02---Alarm-Mask---ISO-11783-6---B.3)                                  |
| Container                 | 3000    | Container\_%ld                 | 3   | [ID 3 – Container – ISO 11783-6 – B.4](ID-03---Container---ISO-11783-6---B.4)                                    |
| SoftKeyMask               | 4000    | SoftKeyMask\_%ld               | 4   | [ID 4 – Soft key mask – ISO 11783-6 – B.5](ID-04---Soft-key-mask---ISO-11783-6---B.5)                            |
| SoftKey                   | 5000    | SoftKey\_%ld                   | 5   | [ID 5 – Key (Soft Key) – ISO 11783-6 – B.6](ID-05---Key-(Soft-Key)---ISO-11783-6---B.6)                          |
| KeyGroup                  | 35000   | KeyGroup\_%ld                  | 35  | [I](I)                                                                                                           |
| Button                    | 6000    | Button\_%ld                    | 6   | [ID 6 – Button – ISO 11783-6 – B.7](D-06---Button---ISO-11783-6---B.7)                                           |
| InputBoolean              | 7000    | InputBoolean\_%ld              | 7   | [ID 7 – Input boolean – ISO 11783-6 – B.8.2](ID-07---Input-boolean---ISO-11783-6---B.8.2)                        |
| InputString               | 8000    | InputString\_%ld               | 8   | [ID 8 – Input string – ISO 11783-6 – B.8.3](ID-08---Input-string---ISO-11783-6---B.8.3)                          |
| InputNumber               | 9000    | InputNumber\_%ld               | 9   | [ID 9 – Input number – ISO 11783-6 – B.8.4](ID-09---Input-number---ISO-11783-6---B.8.4)                          |
| InputList                 | 10000   | InputList\_%ld                 | 10  | [ID 10 – Input list – ISO 11783-6 – B.8.5](ID-10---Input-list---ISO-11783-6---B.8.5)                             |
| OutputString              | 11000   | OutputString\_%ld              | 11  | [ID 11 – Output string – ISO 11783-6 – B.9.2](ID-11---Output-string---ISO-11783-6---B.9.2)                       |
| OutputNumber              | 12000   | OutputNumber\_%ld              | 12  | [ID 12 – Output number – ISO 11783-6 – B.9.3](ID-12---Output-number---ISO-11783-6---B.9.3)                       |
| OutputList                | 37000   | OutputList\_%ld                | 37  | [I](I)                                                                                                           |
| Line                      | 13000   | Line\_%ld                      | 13  | [ID 13 – Output line – ISO 11783-6 – B.10.2](ID-13---Output-line---ISO-11783-6---B.10.2)                         |
| Rectangle                 | 14000   | Rectangle\_%ld                 | 14  | [ID 14 – Output rectangle – ISO 11783-6 – B.10.3](ID-14---Output-rectangle---ISO-11783-6---B.10.3)               |
| Ellipse                   | 15000   | Ellipse\_%ld                   | 15  | [ID 15 – Output ellipse – ISO 11783-6 – B.10.4](ID-15---Output-ellipse---ISO-11783-6---B.10.4)                   |
| Polygon                   | 16000   | Polygon\_%ld                   | 16  | [ID 16 – Output polygon – ISO 11783-6 – B.10.5](ID-16---Output-polygon---ISO-11783-6---B.10.5)                   |
| Meter                     | 17000   | Meter\_%ld                     | 17  | [ID 17 – Output meter – ISO 11783-6 – B.11.2](ID-17---Output-meter---ISO-11783-6---B.11.2)                       |
| LinearBargraph            | 18000   | LinearBargraph\_%ld            | 18  | [ID 18 – Output linear bar graph – ISO 11783-6 – B.11.3](ID-18---Output-linear-bar-graph---ISO-11783-6---B.11.3) |
| ArchedBargraph            | 19000   | ArchedBargraph\_%ld            | 19  | [ID 19 – Output arched bar graph – ISO 11783-6 – B.11.4](ID-19---Output-arched-bar-graph---ISO-11783-6---B.11.4) |
| PictureGraphic            | 20000   | PictureGraphic\_%ld            | 20  | [ID 20 – Picture graphic – ISO 11783-6 – B.12.2](ID-20---Picture-graphic---ISO-11783-6---B.12.2)                 |
| GraphicsContext           | 36000   | GraphicsContext\_%ld           | 36  | [I](I)                                                                                                           |
| NumberVariable            | 21000   | NumberVariable\_%ld            | 21  | [ID 21 – Number variable – ISO 11783-6 – B.13.2](ID-21---Number-variable---ISO-11783-6---B.13.2)                 |
| StringVariable            | 22000   | StringVariable\_%ld            | 22  | [ID 22 – String variable – ISO 11783-6 – B.13.3](ID-22---String-variable---ISO-11783-6---B.13.3)                 |
| FontAttributes            | 23000   | FontAttributes\_%ld            | 23  | [ID 23 – Font attributes – ISO 11783-6 – B.14.2](ID-23---Font-attributes---ISO-11783-6---B.14.2)                 |
| LineAttributes            | 24000   | LineAttributes\_%ld            | 24  | [ID 24 – Line attributes – ISO 11783-6 – B.14.3](ID-24---Line-attributes---ISO-11783-6---B.14.3)                 |
| FillAttributes            | 25000   | FillAttributes\_%ld            | 25  | [ID 25 – Fill attributes – ISO 11783-6 – B.14.4](ID-25---Fill-attributes---ISO-11783-6---B.14.4)                 |
| InputAttributes           | 26000   | InputAttributes\_%ld           | 26  | [ID 26 – Input attributes – ISO 11783-6 – B.14.5](ID-26---Input-attributes---ISO-11783-6---B.14.5)               |
| ExtendedInputAttributes   | 38000   | ExtendedInputAttributes\_%ld   | 38  | [I](I)                                                                                                           |
| ObjectPointer             | 27000   | ObjectPointer\_%ld             | 27  | [ID 27 – Object pointer – ISO 11783-6 – B.15](ID-27---Object-pointer---ISO-11783-6---B.15)                       |
| Macro                     | 0       | Macro\_%ld                     | 0   | [I](I)                                                                                                           |
| AuxFunction2              | 31000   | AuxFunction2\_%ld              | 31  | [I](I)                                                                                                           |
| AuxInput2                 | 32000   | AuxInput2\_%ld                 | 32  | [I](I)                                                                                                           |
| AuxObjectPointer          | 33000   | AuxObjectPointer\_%ld          | 33  | [I](I)                                                                                                           |
| ColorMap                  | 39000   | ColorMap\_%ld                  | 39  | [I](I)                                                                                                           |
| WindowMask                | 34000   | WindowMask\_%ld                | 34  | [I](I)                                                                                                           |
| ObjectLabelReferenceList  | 40000   | ObjectLabelReferenceList\_%ld  | 40  | [I](I)                                                                                                           |
| ExternalObjectDefinition  | 41000   | ExternalObjectDefinition\_%ld  | 41  | [I](I)                                                                                                           |
| ExternalReferenceName     | 42000   | ExternalReferenceName\_%ld     | 42  | [I](I)                                                                                                           |
| ExternalObjectPointer     | 43000   | ExternalObjectPointer\_%ld     | 43  | [I](I)                                                                                                           |
| Animation                 | 44000   | Animation\_%ld                 | 44  | [I](I)                                                                                                           |
| ScaledGraphic             | 48000   | ScaledGraphic\_%ld             | 48  | [I](I)                                                                                                           |
| GraphicData               | 46000   | GraphicData\_%ld               | 46  | [I](I)                                                                                                           |
| ColorPalette              | 45000   | ColorPalette\_%ld              | 45  | [I](I)                                                                                                           |
| WorkingSetSpecialControls | 47000   | WorkingSetSpecialControls\_%ld | 47  | [I](I)                                                                                                           |
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
