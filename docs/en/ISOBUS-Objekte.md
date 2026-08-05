# ISOBUS Objects
Take a close look at this link.
## Programming
[Programming\_And\_Libraries](https://extranet.epec.fi/Public/Manuals/EPEC_Programming_And_Libraries/projecttopics/topic000962.htm)]
Future: [ISOBUS Objects Versions](ISOBUS-Objekte-Versionen.md)]
ISOBUS Wiki by Tobias Tenberg:

* <https://isobus-studio.com/en/isobus-wiki>
* [ISOBUS Wiki - Colors](https://isobus-studio.com/isobus-wiki/isobus-colours)]
* [ISOBUS Wiki - Objectpool Objects Database](https://isobus-studio.com/isobus-wiki/isobus-objectpool-objects-database)]

As you can see, there are various objects, but not all are supported in every ISOBUS version.

`` ![](https://user-images.githubusercontent.com/69573151/94335435-08939880-ffdc-11ea-92e7-662f2ff7779f.png)

If you were to create a new project with ISO Designer, it would ask you for the "VT Level."

If you search for devices in the AEF database, you will see something like this:

![](https://user-images.githubusercontent.com/69573151/94335523-5f996d80-ffdc-11ea-9032-8de45bd5b318.png)

So what is the difference between UT and VT?

Or are they the same thing?

Is VT 2.0 the same as UT 2.0?

Here's the answer:

## VT Levels

| | ISO 11783-06 | Jetter ISO Designer | UT according to AEF database | AUX according to AEF database |

| --- | --- | --- | --- | --- |

| 1 | Unnamed | < nicht wählbar > | < nicht zertifizierbar> | no AUX |

| 2 | VT Version 2 | VT Level 2 | UT 1.0 | AUX-N 1.0 |

3 | VT Version 3 | VT Level 3 | UT 2.0 | AUX-N 1.0 |

4 | VT Version 4 | VT Level 4 | UT 2.0 | AUX-N 1.0 |

5 | VT Version 5 | VT Level 5 | UT 2.0 | AUX-N 1.0 |

6 | VT Version 6 | VT Level 6 | UT 2.0 | AUX-N 1.0 |

7 | VT Version 7 | \< nicht wählbar > | UT 3.0 | AUX-N 1.0 |

So, they started with the first version of the standard and published it.

In the second version, VT version 2 was mentioned... and so on. Please refer to the standard for details.

The AEF does not adhere to this scheme but introduces its own versions for marketing purposes. UT 3.0 is currently under development and will likely include VT 4 and 5.

AUX is only mentioned in the ISOBUS standard in relation to the respective VT standard; the AEF has created AUX-O and AUX-N from this.
