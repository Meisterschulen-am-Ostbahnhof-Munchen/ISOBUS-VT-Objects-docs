# Object Hierarchy (Parent-Child Relationships)
This page is based on **Table A.2 — Allowed hierarchical relationships of objects** of ISO 11783-6:2018 (Annex A). It defines which objects (child) may be contained within which other objects (parent).
The specified number represents the minimum **VT version** required for this relationship to be supported.
## Parent: Working Set object (ID 0)
The working set object is the root container of an object pool hierarchy.
| Child Object | Min. VT Version |
| :--- | :--- |
| Container object (ID 3) | 4 |
| Output String object (ID 11) | 2 |
| Output Number object (ID 12) | 2 |
| Output List object (ID 37) | 4 |
| Output Line object (ID 13) | 2 |
| Output Rectangle object (ID 14) | 2 |
| Output Ellipse object (ID 15) | 2 |
| Output Polygon object (ID 16) | 2 |
| Output Meter object (ID 17) | 4 |
| Output Linear Bar Graph object (ID 18) | 4 |
| Output Arched Bar Graph object (ID 19) | 4 |
| Graphics Context object (ID 36) | 4 |
| Picture Graphic object (ID 20) | 2 |
| Scaled Graphic object (ID 48) | 6 |
| Object Pointer object (ID 27) | 4 |

## Parent: Data Mask object (ID 1)
The data mask is the main display area for operation.

| Child Object | Min. VT version |
| :--- | :--- |
| Working Set object (ID 0) | 3 |
| Container object (ID 3) | 2 |
| Button object (ID 6) | 2 |
| Input Boolean object (ID 7) | 2 |
| Input String object (ID 8) | 2 |
| Input Number object (ID 9) | 2 |
| Input List object (ID 10) | 2 |
| Output String object (ID 11) | 2 |
| Output Number object (ID 12) | 2 |
| Output List object (ID 37) | 4 |
| Output Line object (ID 13) | 2 |
| Output Rectangle object (ID 14) | 2 |
| Output Ellipse object (ID 15) | 2 |
| Output Polygon object (ID 16) | 2 |
| Output Meter object (ID 17) | 2 |
| Output Linear Bar Graph object (ID 18) | 2 |
| Output Arched Bar Graph object (ID 19) | 2 |
| Graphics Context object (ID 36) | 4 |
| Animation object (ID 44) | 5 |
| Picture Graphic object (ID 20) | 2 |
| Scaled Graphic object (ID 48) | 6 |
| Object Pointer object (ID 27) | 2 |
| External Object Pointer object (ID 43) | 5 |
| Auxiliary Function Type 2 object (ID 31) | 3 |
| Auxiliary Input Type 2 object (ID 32) | 3 |
| Auxiliary Control Designator Type 2 Object Pointer (ID 33) | 3 |

## Parent: Alarm Mask object (ID 2)
Alarm masks are used to display warnings.

| Child Object | Min. VT version |
| :--- | :--- |
| Working Set object (ID 0) | 3 |
| Output String object (ID 11) | 2 |
| Output Number object (ID 12) | 2 |
| Output List object (ID 37) | 4 |
| Output Line object (ID 13) | 2 |
| Output Rectangle object (ID 14) | 2 |
| Output Ellipse object (ID 15) | 2 |
| Output Polygon object (ID 16) | 2 |
| Output Meter object (ID 17) | 2 |
| Output Linear Bar Graph object (ID 18) | 2 |
| Output Arched Bar Graph object (ID 19) | 2 |
| Graphics Context object (ID 36) | 4 |
| Animation object (ID 44) | 5 |
| Picture Graphic object (ID 20) | 2 |
| Scaled Graphic object (ID 48) | 6 |
| Object Pointer object (ID 27) | 2 |
| External Object Pointer object (ID 43) | 5 |
| Auxiliary Function Type 2 object (ID 31) | 3 |
| Auxiliary Input Type 2 object (ID 32) | 3 |
| Auxiliary Control Designator Type 2 Object Pointer (ID 33) | 3 |

## Parent: Container object (ID 3)
Containers are used to group objects.

| Child Object | Min. VT version |
| :--- | :--- |
| Working Set object (ID 0) | 3 |
| Container object (ID 3) | 2 |
| Button object (ID 6) | 2 |
| Input Boolean object (ID 7) | 2 |
| Input String object (ID 8) | 2 |
| Input Number object (ID 9) | 2 |
| Input List object (ID 10) | 2 |
| Output String object (ID 11) | 2 |
| Output Number object (ID 12) | 2 |
| Output List object (ID 37) | 4 |
| Output Line object (ID 13) | 2 |
| Output Rectangle object (ID 14) | 2 |
| Output Ellipse object (ID 15) | 2 |
| Output Polygon object (ID 16) | 2 |
| Output Meter object (ID 17) | 2 |
| Output Linear Bar Graph object (ID 18) | 2 |
| Output Arched Bar Graph object (ID 19) | 2 |
| Graphics Context object (ID 36) | 4 |
| Animation object (ID 44) | 5 |
| Picture Graphic object (ID 20) | 2 |
| Scaled Graphic object (ID 48) | 6 |
| Object Pointer object (ID 27) | 2 |
| External Object Pointer object (ID 43) | 5 |
| Auxiliary Function Type 2 object (ID 31) | 3 |
| Auxiliary Input Type 2 object (ID 32) | 3 |
| Auxiliary Control Designator Type 2 Object Pointer (ID 33) | 3 |

## Parent: Window Mask object (ID 34)
Window masks are used in user layouts.

| Child Object | Min. VT version |
| :--- | :--- |
| Working Set object (ID 0) | 4 |
| Container object (ID 3) | 4 |
| Button object (ID 6) | 4 |
| Input Boolean object (ID 7) | 4 |
| Input String object (ID 8) | 4 |
| Input Number object (ID 9) | 4 |
| Input List object (ID 10) | 4 |
| Output String object (ID 11) | 4 |
| Output Number object (ID 12) | 4 |
| Output List object (ID 37) | 4 |
| Output Line object (ID 13) | 4 |
| Output Rectangle object (ID 14) | 4 |
| Output Ellipse object (ID 15) | 4 |
| Output Polygon object (ID 16) | 4 |
| Output Meter object (ID 17) | 4 |
| Output Linear Bar Graph object (ID 18) | 4 |
| Output Arched Bar Graph object (ID 19) | 4 |
| Graphics Context object (ID 36) | 4 |
| Animation object (ID 44) | 5 |
| Picture Graphic object (ID 20) | 4 |
| Scaled Graphic object (ID 48) | 6 |
| Object Pointer object (ID 27) | 4 |
| External Object Pointer object (ID 43) | 5 |
| Auxiliary Function Type 2 object (ID 31) | 6 |
| Auxiliary Input Type 2 object (ID 32) | 6 |
| Auxiliary Control Designator Type 2 Object Pointer (ID 33) | 4 |

## Parent: Soft Key Mask object (ID 4)
Defines the assignment of the softkeys.

| Child Object | Min. VT version |
| :--- | :--- |
| Key object (ID 5) | 2 |
| Object Pointer object (ID 27) | 2 |
| External Object Pointer object (ID 43) | 5 |

## Parent: Key object (ID 5)
Content of a key.

| Child Object | Min. VT version |
| :--- | :--- |
| Working Set object (ID 0) | 4 |
| Container object (ID 3) | 2 |
| Output String object (ID 11) | 2 |
| Output Number object (ID 12) | 2 |
| Output List object (ID 37) | 4 |
| Output Line object (ID 13) | 2 |
| Output Rectangle object (ID 14) | 2 |
| Output Ellipse object (ID 15) | 2 |
| Output Polygon object (ID 16) | 2 |
| Output Meter object (ID 17) | 4 |
| Output Linear Bar Graph object (ID 18) | 4 |
| Output Arched Bar Graph object (ID 19) | 4 |
| Graphics Context object (ID 36) | 4 |
| Animation object (ID 44) | 5 |
| Picture Graphic object (ID 20) | 2 |
| Scaled Graphic object (ID 48) | 6 |
| Object Pointer object (ID 27) | 2 |
| External Object Pointer object (ID 43) | 5 |

## Parent: Button object (ID 6)
Content of a button.

| Child Object | Min. VT version |
| :--- | :--- |
| Working Set object (ID 0) | 4 |
| Container object (ID 3) | 2 |
| Output String object (ID 11) | 2 |
| Output Number object (ID 12) | 2 |
| Output List object (ID 37) | 4 |
| Output Line object (ID 13) | 2 |
| Output Rectangle object (ID 14) | 2 |
| Output Ellipse object (ID 15) | 2 |
| Output Polygon object (ID 16) | 2 |
| Output Meter object (ID 17) | 4 |
| Output Linear Bar Graph object (ID 18) | 4 |
| Output Arched Bar Graph object (ID 19) | 4 |
| Graphics Context object (ID 36) | 4 |
| Animation object (ID 44) | 5 |
| Picture Graphic object (ID 20) | 2 |
| Scaled Graphic object (ID 48) | 6 |
| Object Pointer object (ID 27) | 2 |
| External Object Pointer object (ID 43) | 5 |

## Parent: Key Group object (ID 35)
Grouping of softkeys.

| Child Object | Min. VT version |
| :--- | :--- |
| Key object (ID 5) | 4 |
| Object Pointer object (ID 27) | 4 |
| External Object Pointer object (ID 43) | 5 |

## Parent: Input List object (ID 10)
Options in a selection list.

| Child Object | Min. VT version |
| :--- | :--- |
| Working Set object (ID 0) | 4 |
| Container object (ID 3) | 4 |
| Output String object (ID 11) | 2 |
| Output Number object (ID 12) | 2 |
| Output List object (ID 37) | 4 |
| Output Line object (ID 13) | 4 |
| Output Rectangle object (ID 14) | 4 |
| Output Ellipse object (ID 15) | 4 |
| Output Polygon object (ID 16) | 4 |
| Output Meter object (ID 17) | 4 |
| Output Linear Bar Graph object (ID 18) | 4 |
| Output Arched Bar Graph object (ID 19) | 4 |
| Graphics Context object (ID 36) | 4 |
| Picture Graphic object (ID 20) | 2 |
| Scaled Graphic object (ID 48) | 6 |
| Object Pointer object (ID 27) | 4 |
| External Object Pointer object (ID 43) | 5 |

## Parent: Output List object (ID 37)
Options in an output list.

| Child Object | Min. VT version |
| :--- | :--- |
| Working Set object (ID 0) | 4 |
| Container object (ID 3) | 4 |
| Button object (ID 6) | 4 |
| Input Boolean object (ID 7) | 4 |
| Input String object (ID 8) | 4 |
| Input Number object (ID 9) | 4 |
| Input List object (ID 10) | 4 |
| Output String object (ID 11) | 4 |
| Output Number object (ID 12) | 4 |
| Output List object (ID 37) | 4 |
| Output Line object (ID 13) | 4 |
| Output Rectangle object (ID 14) | 4 |
| Output Ellipse object (ID 15) | 4 |
| Output Polygon object (ID 16) | 4 |
| Output Meter object (ID 17) | 4 |
| Output Linear Bar Graph object (ID 18) | 4 |
| Output Arched Bar Graph object (ID 19) | 4 |
| Graphics Context object (ID 36) | 4 |
| Animation object (ID 44) | 5 |
| Picture Graphic object (ID 20) | 4 |
| Scaled Graphic object (ID 48) | 6 |
| Object Pointer object (ID 27) | 4 |
| External Object Pointer object (ID 43) | 5 |
| Auxiliary Function Type 2 object (ID 31) | 6 |
| Auxiliary Input Type 2 object (ID 32) | 6 |
| Auxiliary Control Designator Type 2 Object Pointer (ID 33) | 4 |

## Parent: Auxiliary Function Type 1 object (ID 29)
Auxiliary function designator (deprecated).

| Child Object | Min. VT version |
| :--- | :--- |
| Output String object (ID 11) | 2 |
| Output Number object (ID 12) | 2 |
| Output Line object (ID 13) | 2 |
| Output Rectangle object (ID 14) | 2 |
| Output Ellipse object (ID 15) | 2 |
| Output Polygon object (ID 16) | 2 |
| Picture Graphic object (ID 20) | 2 |

## Parent: Auxiliary Input Type 1 object (ID 30)
Auxiliary input designator (deprecated).

| Child Object | Min. VT version |
| :--- | :--- |
| Output String object (ID 11) | 2 |
| Output Number object (ID 12) | 2 |
| Output Line object (ID 13) | 2 |
| Output Rectangle object (ID 14) | 2 |
| Output Ellipse object (ID 15) | 2 |
| Output Polygon object (ID 16) | 2 |
| Picture Graphic object (ID 20) | 2 |

## Parent: Auxiliary Function Type 2 object (ID 31)
Auxiliary function designator.

| Child Object | Min. VT version |
| :--- | :--- |
| Container object (ID 3) | 3 |
| Output String object (ID 11) | 3 |
| Output Number object (ID 12) | 3 |
| Output List object (ID 37) | 4 |
| Output Line object (ID 13) | 3 |
| Output Rectangle object (ID 14) | 3 |
| Output Ellipse object (ID 15) | 3 |
| Output Polygon object (ID 16) | 3 |
| Output Meter object (ID 17) | 3 |
| Output Linear Bar Graph object (ID 18) | 3 |
| Output Arched Bar Graph object (ID 19) | 3 |
| Graphics Context object (ID 36) | 4 |
| Picture Graphic object (ID 20) | 3 |
| Scaled Graphic object (ID 48) | 6 |
| Object Pointer object (ID 27) | 3 |

## Parent: Auxiliary Input Type 2 object (ID 32)
Designator for auxiliary inputs.

| Child Object | Min. VT version |
| :--- | :--- |
| Container object (ID 3) | 3 |
| Output String object (ID 11) | 3 |
| Output Number object (ID 12) | 3 |
| Output List object (ID 37) | 4 |
| Output Line object (ID 13) | 3 |
| Output Rectangle object (ID 14) | 3 |
| Output Ellipse object (ID 15) | 3 |
| Output Polygon object (ID 16) | 3 |
| Output Meter object (ID 17) | 3 |
| Output Linear Bar Graph object (ID 18) | 3 |
| Output Arched Bar Graph object (ID 19) | 3 |
| Graphics Context object (ID 36) | 4 |
| Picture Graphic object (ID 20) | 3 |
| Scaled Graphic object (ID 48) | 6 |
| Object Pointer object (ID 27) | 3 |

## Parent: Object Label graphic representation
Objects that may be used as icons/graphics in a label.

| Child Object | Min. VT version |
| :--- | :--- |
| Container object (ID 3) | 4 |
| Output String object (ID 11) | 4 |
| Output Number object (ID 12) | 4 |
| Output List object (ID 37) | 4 |
| Output Line object (ID 13) | 4 |
| Output Rectangle object (ID 14) | 4 |
| Output Ellipse object (ID 15) | 4 |
| Output Polygon object (ID 16) | 4 |
| Output Meter object (ID 17) | 4 |
| Output Linear Bar Graph object (ID 18) | 4 |
| Output Arched Bar Graph object (ID 19) | 4 |
| Graphics Context object (ID 36) | 4 |
| Picture Graphic object (ID 20) | 4 |
| Scaled Graphic object (ID 48) | 6 |
| Object Pointer object (ID 27) | 4 |

## Parent: Object Label Reference List object (ID 40)
Defines assignments of labels to objects.

| Child Object | Min. VT version |
| :--- | :--- |
| Working Set object (ID 0) | 4 |
| Data Mask object (ID 1) | 4 |
| Alarm Mask object (ID 2) | 4 |
| Container object (ID 3) | 4 |
| Window Mask object (ID 34) | 4 |
| Soft Key Mask object (ID 4) | 4 |
| Key object (ID 5) | 4 |
| Button object (ID 6) | 4 |
| Input Boolean object (ID 7) | 4 |
| Input String object (ID 8) | 4 |
| Input Number object (ID 9) | 4 |
| Input List object (ID 10) | 4 |
| Output String object (ID 11) | 4 |
| Output Number object (ID 12) | 4 |
| Output List object (ID 37) | 4 |
| Output Line object (ID 13) | 4 |
| Output Rectangle object (ID 14) | 4 |
| Output Ellipse object (ID 15) | 4 |
| Output Polygon object (ID 16) | 4 |
| Output Meter object (ID 17) | 4 |
| Output Linear Bar Graph object (ID 18) | 4 |
| Output Arched Bar Graph object (ID 19) | 4 |
| Graphics Context object (ID 36) | 4 |
| Animation object (ID 44) | 5 |
| Picture Graphic object (ID 20) | 4 |
| Scaled Graphic object (ID 48) | 6 |
| Number Variable object (ID 21) | 5 |
| String Variable object (ID 22) | 5 |
| Font Attributes object (ID 23) | 5 |
| Line Attributes object (ID 24) | 5 |
| Fill Attributes object (ID 25) | 5 |
| Input Attributes object (ID 26) | 5 |
| Extended Input Attributes object (ID 41) | 5 |
| Color Map object (ID 42) | 5 |
| Object Label Reference List object (ID 40) | 5 |
| Object Pointer object (ID 27) | 5 |
| External Object Definition object (ID 45) | 5 |
| External Reference NAME object (ID 46) | 5 |
| External Object Pointer object (ID 43) | 5 |
| Macro object (ID 47) | 5 |
| Auxiliary Function Type 1 object (ID 29) | 5 |
| Auxiliary Input Type 1 object (ID 30) | 5 |
| Auxiliary Function Type 2 object (ID 31) | 4 |
| Auxiliary Input Type 2 object (ID 32) | 4 |
| Auxiliary Control Designator Type 2 Object Pointer (ID 33) | 5 |
| Color Palette object (ID 49) | 6 |
| Graphic Data object (ID 50) | 6 |
| Working Set Special Controls object (ID 51) | 6 |

## Parent: Animation object (ID 44)
Sequence of objects.

| Child Object | Min. VT version |
| :--- | :--- |
| Container object (ID 3) | 5 |
| Output String object (ID 11) | 5 |
| Output Number object (ID 12) | 5 |
| Output List object (ID 37) | 5 |
| Output Line object (ID 13) | 5 |
| Output Rectangle object (ID 14) | 5 |
| Output Ellipse object (ID 15) | 5 |
| Output Polygon object (ID 16) | 5 |
| Output Meter object (ID 17) | 5 |
| Output Linear Bar Graph object (ID 18) | 5 |
| Output Arched Bar Graph object (ID 19) | 5 |
| Graphics Context object (ID 36) | 5 |
| Animation object (ID 44) | 5 |
| Picture Graphic object (ID 20) | 5 |
| Scaled Graphic object (ID 48) | 6 |
| Object Pointer object (ID 27) | 5 |
