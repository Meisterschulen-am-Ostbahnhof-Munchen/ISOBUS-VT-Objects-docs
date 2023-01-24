# ISOBUS Objekt IDs

Siehe auch:

[https://extranet.epec.fi/Public/Manuals/EPEC_Programming_And_Libraries/projecttopics/topic000962.htm](https://extranet.epec.fi/Public/Manuals/EPEC_Programming_And_Libraries/projecttopics/topic000962.htm)

Stand Jetter ISO-Designer 5.6.1

hier stimmen die Objektnummern mit den IDs in der Norm überein. 

(die Objektnummern können jeden Wert annehmen; mit Ausnahme der Makros)

die Festlegung in dieser Tabelle kann man also als Good Practice bezeichnen.

| TypeName | StartID | FmtStr | ID | Link |
| --- | --- | --- | --- | --- |
| WorkingSet | 0 | WorkingSet\_%ld | 0 | [ID-00---Working-set---ISO-11783-6---B.1](ID-00---Working-set---ISO-11783-6---B.1) |
| DataMask | 1000 | DataMask\_%ld | 1 | [I](I) |
| AlarmMask | 2000 | AlarmMask\_%ld | 2 | [I](I) |
| Container | 3000 | Container\_%ld | 3 | [I](I) |
| SoftKeyMask | 4000 | SoftKeyMask\_%ld | 4 | [I](I) |
| SoftKey | 5000 | SoftKey\_%ld | 5 | [I](I) |
| KeyGroup | 35000 | KeyGroup\_%ld | 35 | [I](I) |
| Button | 6000 | Button\_%ld | 6 | [I](I) |
| InputBoolean | 7000 | InputBoolean\_%ld | 7 | [I](I) |
| InputString | 8000 | InputString\_%ld | 8 | [I](I) |
| InputNumber | 9000 | InputNumber\_%ld | 9 | [I](I) |
| InputList | 10000 | InputList\_%ld | 10 | [I](I) |
| OutputString | 11000 | OutputString\_%ld | 11 | [I](I) |
| OutputNumber | 12000 | OutputNumber\_%ld | 12 | [I](I) |
| OutputList | 37000 | OutputList\_%ld | 37 | [I](I) |
| Line | 13000 | Line\_%ld | 13 | [I](I) |
| Rectangle | 14000 | Rectangle\_%ld | 14 | [I](I) |
| Ellipse | 15000 | Ellipse\_%ld | 15 | [I](I) |
| Polygon | 16000 | Polygon\_%ld | 16 | [I](I) |
| Meter | 17000 | Meter\_%ld | 17 | [I](I) |
| LinearBargraph | 18000 | LinearBargraph\_%ld | 18 | [I](I) |
| ArchedBargraph | 19000 | ArchedBargraph\_%ld | 19 | [I](I) |
| PictureGraphic | 20000 | PictureGraphic\_%ld | 20 | [I](I) |
| GraphicsContext | 36000 | GraphicsContext\_%ld | 36 | [I](I) |
| NumberVariable | 21000 | NumberVariable\_%ld | 21 | [I](I) |
| StringVariable | 22000 | StringVariable\_%ld | 22 | [I](I) |
| FontAttributes | 23000 | FontAttributes\_%ld | 23 | [I](I) |
| LineAttributes | 24000 | LineAttributes\_%ld | 24 | [I](I) |
| FillAttributes | 25000 | FillAttributes\_%ld | 25 | [I](I) |
| InputAttributes | 26000 | InputAttributes\_%ld | 26 | [I](I) |
| ExtendedInputAttributes | 38000 | ExtendedInputAttributes\_%ld | 38 | [I](I) |
| ObjectPointer | 27000 | ObjectPointer\_%ld | 27 | [I](I) |
| Macro | 0 | Macro\_%ld | 0 | [I](I) |
| AuxFunction2 | 31000 | AuxFunction2\_%ld | 31 | [I](I) |
| AuxInput2 | 32000 | AuxInput2\_%ld | 32 | [I](I) |
| AuxObjectPointer | 33000 | AuxObjectPointer\_%ld | 33 | [I](I) |
| ColorMap | 39000 | ColorMap\_%ld | 39 | [I](I) |
| WindowMask | 34000 | WindowMask\_%ld | 34 | [I](I) |
| ObjectLabelReferenceList | 40000 | ObjectLabelReferenceList\_%ld | 40 | [I](I) |
| ExternalObjectDefinition | 41000 | ExternalObjectDefinition\_%ld | 41 | [I](I) |
| ExternalReferenceName | 42000 | ExternalReferenceName\_%ld | 42 | [I](I) |
| ExternalObjectPointer | 43000 | ExternalObjectPointer\_%ld | 43 | [I](I) |
| Animation | 44000 | Animation\_%ld | 44 | [I](I) |
| ScaledGraphic | 48000 | ScaledGraphic\_%ld | 48 | [I](I) |
| GraphicData | 46000 | GraphicData\_%ld | 46 | [I](I) |
| ColorPalette | 45000 | ColorPalette\_%ld | 45 | [I](I) |
| WorkingSetSpecialControls | 47000 | WorkingSetSpecialControls\_%ld | 47 | [I](I) |
| IDsForTemporaryUse | 64000 | IDsForTemporaryUse\_%ld | 64 | [I](I) |
| Proxy | 4194304 | Proxy\_%ld |   | [I](I) |

In Versionen vor V. 5.6.0, also bis ISO-Designer 5.5.1

war folgende Benennung üblich:

hier stimmte die ID nicht mit der ObjectID zusammen. 

z.b. bei AUX Function. 

| TypeName | StartID | FmtStr |
| --- | --- | --- |
| WorkingSet | 0 | WorkingSet\_%ld |
| DataMask | 100 | DataMask\_%ld |
| AlarmMask | 200 | AlarmMask\_%ld |
| Container | 300 | Container\_%ld |
| SoftKeyMask | 400 | SoftKeyMask\_%ld |
| SoftKey | 500 | SoftKey\_%ld |
| KeyGroup | 3600 | KeyGroup\_%ld |
| Button | 600 | Button\_%ld |
| InputBoolean | 700 | InputBoolean\_%ld |
| InputString | 800 | InputString\_%ld |
| InputNumber | 900 | InputNumber\_%ld |
| InputList | 1000 | InputList\_%ld |
| OutputString | 1100 | OutputString\_%ld |
| OutputNumber | 1200 | OutputNumber\_%ld |
| OutputList | 3000 | OutputList\_%ld |
| Line | 1300 | Line\_%ld |
| Rectangle | 1400 | Rectangle\_%ld |
| Ellipse | 1500 | Ellipse\_%ld |
| Polygon | 1600 | Polygon\_%ld |
| Meter | 1700 | Meter\_%ld |
| LinearBargraph | 1800 | LinearBargraph\_%ld |
| ArchedBargraph | 1900 | ArchedBargraph\_%ld |
| PictureGraphic | 2000 | \[File Name\]\_%ld |
| GraphicsContext | 3100 | GraphicsContext\_%ld |
| NumberVariable | 2100 | NumberVariable\_%ld |
| StringVariable | 2200 | StringVariable\_%ld |
| FontAttributes | 2300 | FontAttributes\_%ld |
| LineAttributes | 2400 | LineAttributes\_%ld |
| FillAttributes | 2500 | FillAttributes\_%ld |
| InputAttributes | 2600 | InputAttributes\_%ld |
| ExtendedInputAttributes | 3200 | ExtendedInputAttributes\_%ld |
| ObjectPointer | 2700 | ObjectPointer\_%ld |
| Macro | 0 | Macro\_%ld |
| AuxInput2 | 2800 | AuxInput2\_%ld |
| AuxFunction2 | 2900 | AuxFunction2\_%ld |
| AuxObjectPointer | 3300 | AuxObjectPointer\_%ld |
| ColorMap | 3400 | ColorMap\_%ld |
| WindowMask | 3500 | WindowMask\_%ld |
| ObjectLabelReferenceList | 3700 | ObjectLabelReferenceList\_%ld |
| ExternalObjectDefinition | 3800 | ExternalObjectDefinition\_%ld |
| ExternalReferenceName | 3900 | ExternalReferenceName\_%ld |
| ExternalObjectPointer | 4000 | ExternalObjectPointer\_%ld |
| Animation | 4100 | Animation\_%ld |
| IDsForTemporaryUse | 64000 | IDsForTemporaryUse\_%ld |
| Proxy | 4194304 | Proxy\_%ld |
