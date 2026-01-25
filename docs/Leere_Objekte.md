# Leere Objekte (Minimum Child Objects)

```{index} single: Leere Objekte
```

In der ISO 11783-6 Norm gibt es für Container-Objekte (Objekte, die andere Objekte enthalten) eine wichtige Unterscheidung: **Darf das Objekt leer sein oder nicht?**

Diese Regel wird durch den zulässigen Wertebereich des Attributs **"Number of objects to follow"** definiert.

## Objekte, die NICHT leer sein dürfen (Minimum 1 Child)

Diese Objekte müssen zwingend mindestens ein Kind-Objekt enthalten, da sie ohne Inhalt ihre Funktion im System nicht erfüllen können (meist weil sie als **Designator** / Icon für den Benutzer sichtbar sein müssen).

| Objekt ID | Name | Grund | Norm-Referenz |
| :--- | :--- | :--- | :--- |
| **0** | **Working Set** | Muss im VT-Menü zur Auswahl angezeigt werden. Ohne grafischen Designator wäre das Gerät für den Bediener unsichtbar und nicht auswählbar. | Table B.2 |
| **29** | **Auxiliary Function Type 1** | Muss auf dem Zuweisungs-Bildschirm (Mapping Screen) dargestellt werden, damit der Benutzer die Funktion (z.B. "Heben") einem Schalter zuordnen kann. | Table J.1 |
| **30** | **Auxiliary Input Type 1** | Muss auf dem Mapping Screen dargestellt werden, um den physischen Eingang (z.B. "Joystick Taste A") zu repräsentieren. | Table J.3 |
| **31** | **Auxiliary Function Type 2** | Siehe ID 29. | Table J.2 |
| **32** | **Auxiliary Input Type 2** | Siehe ID 30. | Table J.4 |

**Fehlerfall:** Wenn ein solches Objekt mit `0` Kind-Objekten im Objektpool definiert wird, ist der Pool **ungültig** und wird vom VT (oder einem Prüftool) abgelehnt.

---

## Objekte, die leer sein dürfen (Minimum 0 Children)

Für die meisten anderen Container ist ein Inhalt von `0` erlaubt. Dies kann durchaus sinnvoll sein.

| Objekt ID | Name | Verhalten bei 0 Kindern |
| :--- | :--- | :--- |
| **1** | **Data Mask** | Zeigt nur die Hintergrundfarbe an. |
| **2** | **Alarm Mask** | Zeigt nur die Hintergrundfarbe an (Warnung ohne Inhalt). |
| **3** | **Container** | Ist effektiv unsichtbar und beansprucht keinen Platz (sofern nicht durch Width/Height eine Fläche definiert ist, die Hintergrundfarbe hat). |
| **4** | **Soft Key Mask** | Blendet alle Softkeys aus oder lässt sie unbeschriftet. |
| **5** | **Key** | Zeigt eine leere Taste in der definierten Hintergrundfarbe. |
| **6** | **Button** | Zeigt eine leere Schaltfläche in der definierten Hintergrundfarbe. |
| **35** | **Key Group** | Technisch erlaubt, aber funktional sinnlos (eine leere Gruppe). |
| **44** | **Animation** | Eine Animation ohne Frames zeigt nichts an. |

### Besonderheit: Input List (ID 10)
Auch eine `Input List` darf theoretisch leer sein (`Number of list items` = 0). In diesem Fall ist die Liste zwar vorhanden, enthält aber keine auswählbaren Optionen.
