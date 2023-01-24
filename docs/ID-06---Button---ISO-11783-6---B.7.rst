ID 6 – Button – ISO 11783-6 – B.7
===================================

.. image:: https://user-images.githubusercontent.com/69573151/94337426-7d6dcf00-ffea-11ea-8ab0-ca710054a888.png

Auswertung des Buttons:

wird der Button gedrückt so werden folgende Nachrichten am ISOBUS abgesetzt:

*   BUTTON\_STATE\_PRESSED
    *   in dem Moment wo der Knopf gedrückt wurde
*   BUTTON\_STATE\_HELD
    *   falls der Knopf länger gehalten wurde
    *   TODO Verweis auf ISO
*   BUTTON\_STATE\_RELEASED
    *   wenn der Knopf losgelassen wurde
*   BUTTON\_STATE\_ABORTED
    *   wenn der Knopf gedrückt, aber dann abgebrochen wurde
    *   TODO besser beschreiben.

daraus ergibt sich:

normale "Knopfdrücke" dürfen nur auf "released" oder "held" ausgewertet werden, 

weil ein auswerten von "pressed" die Abort Möglichkeit nehmen würde. 

TODO: verweis auf internationale Standards, Safety etc.. 

es gibt 2 Wege der Auswertung: 

1.  Makro (ISO-Designer)
2.  über einen Callback im C-Code (Eclipse)

Call Hierarchy:

.. image:: https://user-images.githubusercontent.com/69573151/94337621-210baf00-ffec-11ea-9ec0-fe4a7e7c418b.png

.. code-block:: C
    :caption: Code Blocks can have captions.

    {
    iso_u32 Tageszaehler = 0;
    iso_u32 Gesamtzaehler = 0;
    iso_u32 Hugo = 0;
    
    void VTC_handleSoftkeysAndButtons_RELEASED(const struct ButtonActivation_S *pButtonData) {
    
       // what button was released
        switch (pButtonData->objectIdOfButtonObject) {
    
        case SoftKey_PlusPlus:
        case Button_PlusPlus:
            Tageszaehler++;
            Gesamtzaehler++;
            break;
    
        case SoftKey_Reset_Gesamtzaehler:
        case Button_Reset_Gesamtzaehler:
            Gesamtzaehler = 0;
            break;
    
        case SoftKey_Reset_Tageszaehler:
        case Button_Reset_Tageszaehler:
            Tageszaehler = 0;
            break;
    
        default:
            break;
        }
        IsoVtcCmd_NumericValue(pButtonData->u8Instance, NumberVariable_Tageszaehler, Tageszaehler);
        IsoVtcCmd_NumericValue(pButtonData->u8Instance, NumberVariable_Gesamtzaehler, Gesamtzaehler);
        setU32("CF-A", "Tageszaehler", Tageszaehler);
        setU32("CF-A", "Gesamtzaehler", Gesamtzaehler);
    }

End of Code


.. image:: https://user-images.githubusercontent.com/69573151/94602909-cbf2c600-0295-11eb-946a-a68b45b3eccc.png
