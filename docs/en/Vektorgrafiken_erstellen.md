# Creating Vector Graphics
## CorelDRAW X5
If you need to extract the file from, for example, a PDF file, you can use CorelDRAW X5.
The size can also be changed via Arrange --> Modify --> Resize.
Caution: This is very imprecise and will require a few attempts to achieve the desired size.
If there's another way, please correct it here (smile)

## Solid Edge
- If something doesn't work, it helps to simply redo each line,
- to ensure clear connections between the lines. Time-consuming, but it should work. (wink)
- When drawing symbols for the displays, they must be 72x72. Quickly draw a rectangle and check it; that way you're on the safe side.
- When drawing symbols for the displays, they must have dimensions of 72x72. * Select the entire object → Block → Ungroup all

![image2015-10-21 10_4_0](https://github.com/Meisterschulen-am-Ostbahnhof-Munchen/ISOBUS-VT-Objects-docs/assets/69573151/8c3efd93-6903-4d12-93b1-c1be96ed3976)

Save the finished, scaled vector file

Then Save As → Save as Translated (in .dxf format)

Attention! The object must not contain any curves. Everything must be a "Polygon over Center Point". Ideally, nine sides.

Continuing to work with curves would otherwise cause problems in LibreCAD or ISO Designer!

## LibreCAD

Open the saved .dxf file in LibreCAD

All lines must be connected:

Select the entire object → Draw (Tools) → Polyline → Create Polyline from Existing Objects

Attention: It is possible that only fragments of the object will be connected as a polygon,

and this will cause problems in ISO Designer (next step). The object will only be visible in these parts!

In this case, it helps to go through the object step by step again in Solid Edge.

If clicking on the line doesn't produce a purple/pink line, but instead a dashed "purple" line, you may have already found the problem.

Remove this dashed line using, for example, the Trim tool in Solid Edge, and connect the points with a new line.

![image2015-10-21 10_6_24](https://github.com/Meisterschulen-am-Ostbahnhof-Munchen/ISOBUS-VT-Objects-docs/assets/69573151/ca471324-0a91-4cec-92c1-65b72c1f22f5)

Repeat this process with all individual objects.

Save
Close

## ISO-Designer
- Jetter has removed support for DXF vector graphics import.
- ISO-Designer 5.3.1 is the last version that can still import DXF files.

File → New → Workspace: Name of the .dfx file

File → New → Project:
Select the newest platform (2010)
Highest resolution (480x480)
Name the Display name and Project name with the name of the .dfx file

Draw a line or anything else in WorkingSet.jvi

Right-click in DataMask.jvi → Import DXF → Check "create container around drawing"

IMPORTANT: The line/dash must remain in the WorkingSet until the end.

The symbol is also inserted in DataMask. Two different tabs!!!

Otherwise, an error message will appear and it won't work!!!

![image2015-10-21 10_10_43](https://github.com/Meisterschulen-am-Ostbahnhof-Munchen/ISOBUS-VT-Objects-docs/assets/69573151/dcdfbdc6-2b03-4250-802a-85bacef2d1ac)

Save

Close Workspace (due to a bug)

Reopen via Recent Workspaces

Fill in the fill attributes

Build → Build All

Build → Deploy

You should now see "0 Error(s)" under "Deployment".

If this is not the case, check the line under WorkingSet. (see above)

## Alternative with Autodesk Fusion 360 and Plugin
Install the software and plugin
Download and install Fusion 360

Free for students.

Install the "DXFSplineToPolyline-win64" plugin.

### Use Fusion 360.

Create a new design

![image2017-1-9 13_52_3](https://github.com/Meisterschulen-am-Ostbahnhof-Munchen/ISOBUS-VT-Objects-docs/assets/69573151/02523f1b-a526-4239-a692-b4513f496fe7)
Import DXF (Insert/Insert DXF File)
Select the lower layer and file

![image2017-1-9 14_1_59](https://github.com/Meisterschulen-am-Ostbahnhof-Munchen/ISOBUS-VT-Objects-docs/assets/69573151/e2e82141-9fbe-4d47-8c7c-cc5a24002fef)

Optional: Edit as needed, scale (Sketch/Scale Scale (select the scale to match the target size, e.g., 80x80)) and move to the origin (Modify/Move)

The "Export to DXF (Splines as Polyline)" plugin can be run via the Sketch menu.

The tolerance is set to 1.00 mm.

![image2017-1-9 14_25_45](https://github.com/Meisterschulen-am-Ostbahnhof-Munchen/ISOBUS-VT-Objects-docs/assets/69573151/59a5c4a6-65ba-4527-8936-3f00f9f91a5f)

Continue with LibreCAD