%%%
title = "Game Repair Code v1"
abbrev = "GRCV1"
docName = "draft-grcv1-01"
category = "info"

ipr = "none"
area = "General"
workgroup = "Retro Gaming Broadcast Workgroup"

[seriesInfo]
name = "RFC"
value = "draft-grcv1-01"
stream = "IETF"
status = "informational"


[[author]]
initials="M."
surname="Parks"
fullname="Michael Parks"
organization="TKWare Enterprises"
 [author.address]
 email = "mparks@tkware.info"
 phone = "+1 (307)335-3132"
[[author]]
initials="A."
surname="Parrish"
fullname="Alexander Parrish"
organization="A Force Dynamic"
 [author.address]
 email = "nuvandibe@gmail.com"
%%%

.# Abstract

This document proposes a new standard encoding method for consumer game console, software, and other related hardware condition and repair information.

{mainmatter}

# Introduction

The GRC is an ASCII, pipe ("|") delimited string intended to denote the general status, details, and repair history of consumer video game consoles, software, and peripherals.

## Terminology

The keywords **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**,
**SHOULD NOT**, **RECOMMENDED**, **MAY**, and **OPTIONAL**, when they appear in this document, are
 to be interpreted as described in [@RFC2119].

## Versioning
The GRC follows semantic versioning. Minor changes such as additions to company codes **MAY** be published as a point release (ex: 1.1). Any backwards-incompatible changes, such as changing the format or ordering of a field, will require bumping the major version number.

A version number without a period (".") and another number **SHOULD** be assumed to be point release zero, i.e. GRC1 is version 1.0

# Syntax

A valid GRC string **MUST** follow this format:

`GRC Version|Hardware Field|Repair history field`

## Length
A valid GRC string **MUST NOT** exceed 1024 characters *before* encoding/compression. If a given code would be above this limit after adding a repair record, the creator of the code **MAY** use their best judgment to remove old or less-important records.

## Encoding {#encoding}
A GRC string **MAY** be compressed for inclusion in tweets, QR codes, etc. 

A compressed GRC string **MUST NOT** use any algorithm other than Deflate.

Usable characters in a GRC string are the letters A through Z, numbers zero through 9, and the symbols "!?|,". The PCRE regex `([A-Z][a-z][0-9][\!\?\|,])+` **MAY** be used to check whether a GRC string contains valid characters.

## Version field
This field **MUST** begin with an all-caps "GRC" followed by a monotonic counter indicating the revision of the standard used. This document is the first revision, and so this field would read `GRC1`


## Hardware field
A definition of the actual physical object this code is referencing.

This field **MUST** be formatted in this order, as follows:
`B(brand),A(authenticity),F(family),R(region),T(type),C(color),V(revision),P(physical condition),D(currently known damage)`

### Brand/Manufacturer (B)
A four letter representation of the original manufacturer of the hardware or software. 

If the manufacturer is defunct, renamed, or was purchased by another entity, the name being used at the time of release **MUST** be used.

If the company's name is included in the reserved list below, that abbreviation **MUST** be used.

#### Subsidiaries and regional branches
If hardware/software is known to be released by a subsidiary of a larger company, the code creator **MUST** use the subsidiary's name (i.e. Tengen would be its own company, not Atari, even though Tengen was an Atari subsidiary).

This does not apply in the case of identically-named regional susidiaries, such as Nintendo of Japan or Nintendo of America, or Rockstar North  In these cases, use the code of the parent company.

Code | Company
-----|--------
NINT | Nintendo
SONY | Sony
MICR | Microsoft
SEGA | Sega
ATAR | Atari
APPL | Apple
Table: Reserved/recognized company codes


Code | Meaning
-----|--------
UNKN | Unknowable
?ABCD| Non-standard
Table: Special company codes

UNKN: Brand is unknow*able* (third party "no name" with no meaningful brand information available, and it is unlikely that it will ever be known. This is distinct from "unknown but knowable", which is covered below.)

?abcd: Prefix for non-standard name (see next section)


#### Unknown or non-standardized names
Company codes prefixed with a "?" are non-standard. Tools that create or parse GRCs **SHOULD NOT** attempt to create a mapping of nonstandard names to full names, as nonstandard names could be duplicated.

If a a company is not listed in this standard, the code creator **MUST** do one of the following:

1. If the company is publicly traded, insert a "?" prefix and follow with the first 4 characters of the company's stock exchange ticker symbol. If the ticker symbol is shorter than 4 characters, invent

2. If the company is private or its status is unknown insert a "?" prefix and invent a reasonable prefix based on the company's name, taking care to not duplicate a reserved code. For example, "FooWare Ltd." could be represnted as `?FOOW`


### Authenticity
Represents the authenticity of the device. **MUST** be one of the following:

* **OEM** if this is original hardware/software.
* **REP** if it is a repro or bootleg.

Code creators **SHOULD** use the brand/manufacturer when determining whether a device is OEM or Repro. If a piece of hardware passes itself off as Nintendo hardware but is not made by Nintendo, its proper code is REP. Third party consoles do not pass themselves off as OEM hardware, and **MUST** be given as their own company name with an authenticity of OEM.

### Family (F)
The *first* release of any hardware system in any region defines the family, i.e. the US NES is still part of the Famicom family of systems. Use three-letter abbreviation based on these rules.

For systems with unnecessarily confusing naming schemes (Xbox 1 vs original Xbox vs Xbox One X vs Xbox smfh), the generation number willb be used (ex XB1=Original xbox, XB2=Xbox 360/Slim, Xb3=Xbox One/Xbox One S/X) 

For software, the family indicates the primary system the software is intended to run on.

Family Code | Description
------------|-----------
FCM         | Famicom / NES
SMD         | Sega MegaDrive / Genesis
PCE         | PC Engine / TurboGrafx 16
MCD         | MegaCD / SegaCD
N64         | N64
DCR         | Dreamcast
GBY         | Game Boy
XB1         | Original Xbox
XB2         | Xbox 360/Slim
XB3         | Xbox One / Xbox One S / Xbox One X
XB4         | Xbox Series X
PC8         | NEC PC-88
Table: Reserved/recognized family codes

### Region (R)
This field **MUST** be one of the one or two-letter GoodTools country codes. [@goodtools-country]

### Type (T) (Console/Accessory)
Represents the general class of the device. **MUST** be one of the following:

Type Code | Description
----------|------------
CON       | Console
DEV       | Devkit console
SFT       | Game or software
1st       | First-party software peripheral (ex: Super Scope)
3rd       | 3rd-party software peripheral (ex: Konami Justifier)
Cnt       | Console intrinsic component (ex: power adapter, RF switch, video adapter)
Snt       | Software intrinsic component (ex: standalone case or disc for a multi-disc game)
Table: Reserved/recognized type codes

In the case of peripherals that have multiple independent parts (example: Super Scope itself, and the IR dongle that connects to the console), each part **MUST** be considered as its own unique peripheral. (I.e. the scope and the dongle would have their own individual codes). Batching components together **MUST NOT** be done.

### Color (C) (optional)
This field is **OPTIONAL** and can be ignored.

If included, this field **MUST** contain the first three letters of the official color as given by the manufacturer. If the manufacturer calls their color "platinum", use PLT, not SLV (silver). 
 

### ReVision (V)
Revision 


### Physical Condition (P)
Represents the quality of the physical condition of the hardware. **MUST** be one of the following:

Condition Code | Description
---------------|------------
NEW            | New, still in *unopened* factory packaging.
MNT            | Mint, opened, but in best concievable physical shape. No damage or mods.
USD            | Used, but fully functional. May have damage or be modified.
PNF            | Used, partially nonfunctional (system is fit for purpose but certain functions don't work)
CNF            | Completely nonfunctional (system is no longer fit for purpose)
Table: Reserved/recognized physical condition codes

### Currently known damage (D)
Damage consists of hardware or software deformities, with each class of damage having its own unique 3-letter code. If multiple classes of damage apply to the hardware, list them consecutively with no delimiter. For a yellowed case with smoke damage and missing fasteners, this would read `SHYSMKFST`.

#### Reserved/known damage codes
* **SH\***: Shell/Case issues
  * **SHC**: Shell cracks
  * **SHS**: Shell scratches
  * **SHY**: Yellowing
  * **SHF**: Faded wording or print
* **PCB or components**
  * **PCB**: Damage to the board itself, such as cracks or lifted traces
  * **PCC**: Visible damage to board components, such as blown capacitors or transistors
* **SMK**: Smoke (either nicotine or from fire) damage
* **WAT**: Water/moisture damage, including rust
* **BLK**: Battery leakage or corrosion
* **OL\***: Online service issues
  * **OLS**: Limited access to online services (game bans, or restriction to updates only)
  * **OLB**: No access to online services (hard console ban, updates not allowed) 
* **LC\***: Lose or intermittent connectors 
  * **LCC**: Loose controller port
  * **LCV**: Loose video port
  * **LCE**: Loose expansion port
  * **LCP**: Loose power connector
  * **LCS**: Loose switch of any kind (power/mode/etc.)
* **DNS**: Does not save. Battery backup/saving failure
* **FST**: Missing fasteners (clips, screws, etc)
* **SFT**: Software failure (functional issues due to missing/corrupt files)
* **OM\***: Optical media issues
  * **OMS**: Scratches, superficial (reading is not impacted)
  * **OMD**: Scratches, deep (reading is impacted)
  * **OMC**: Cracks, superficial (in the center ring or not-reading area)
  * **OMX**: Cracks, deep (disc is likely destroyed)

* **TXT**: None of the known items matches, 24 characters of freetext follows 

## Service History Field
The service history field represents a list of repair events. This list **MUST** be in chronological order, each event **MUST** be comma-separated.

A single repair is defined as a single item or directly related group of items.

A history entry **MUST** begin with the ISO8601 date (ex: YYYYMMDD) the action was *finished*, with no separator. Example: 20200829 for August 8th, 2020.

If the month or date is unknown, a double zero ("00") **MUST** be used for that section of the date instead.

Example: 20200000 for "some time in 2020", or 20200100 for "some time in January in 2020"

If the entire date is unknown, the date should be given as a single zero.

The service history field format is as follows:
`(Datestamp) (Repair type) (repair item shorthand) (20 characters free text),`


### Repair types
Denotes the general disposition of the changes made to the hardware. This **MUST** be one of the 3 following characters:

* M: Mod
* S: Swap (broken parts to new parts) 
* R: Repair (existing parts condition improved, or significant cleaning)

Swaps or repairs that require no tools, such as battery replacements or consumer-accessible cleaning (say, taking a cotton swab to a the laser on a disc system) **MUST NOT** have a repair entry added.

### Repair item shorthand
This attribute represents the nature of the repair or replacement made. It **MUST** be one of the following:

* Oem: First party
* 3rd: Third party
* Rep: Reproduction (third party, looks like OEM)
* Chp: Modchip
* Shl: Shell/case
* Pnt: Paint
* Rbt: Retrobrite
* Rpt: Metal replating
* Msc: Miscellaneous component

After each item, you **SHOULD** include a space character and up to 20 characters of free-form text with any other pertinent details.

# Example code
```
GRC1|BN,GNGC,RU,TC,CPL,V1.0|PU,DCS|20200829 M Chp HyperBoot,20200829 M LED Ctrlr,20200829 S Shl Oem Top,20200829 S Shl Oem Hsd,20200829 R DDL Clean,20211224 R Msc M HyperBoot,20211224 S Msc OEM Ctrlport3,20211224 S DDA 3rd`
```
Figure: A GCR1 in its regular format

## Human-readable:

```
GRC1                            // Code generation
|BNIN,                          // Brand: Nintendo
GNGC,                           // Console: Gamecube
RU,                             // Region: North America
TC,                             // Type: Console
CPL,                            // Color: Platinum // Should reflect brand official color names. Dandelion instead of yellow, Platinum instead of Silver
V1.0                            // Revision: 0 / DOL-001
|PU,                            // Physical condition: Used
DCS                             // Damages: Cracks, smoke
|20200829 M Chp HyperBoot,      // On August 29, 2020: Mod installed / Modchip / Hyperboot
20200829 M LED Ctrlr,           // On August 29, 2020: Mod installed / LED(s) / Controller ports
20200829 S Shl Oem Top,         // On August 29, 2020: Swapped part / Shell / OEM part / Top shell
20200829 S Shl Oem Hsd,         // On August 29, 2020: Swapped part / Shell / OEM part / High speed data port cover
20200829 R DDL Clean,           // * On August 29, 2020: Repaired / Disc drive laser / Cleaned
20211224 R Msc M HyperBoot,     // On November 24, 2021: Repaired / Miscellaneous component / Hyperboot modchip 
20211224 S Msc OEM Ctrlport3,   // On November 24, 2021: Swapped part / Miscellaneous component / OEM part / Controller port 3
20211224 S DDA 3rd              // On November 24, 2021: Swapped part / Disc Drive assembly / 3rd party component
```
Figure: A full GCR1 with history, expanded for ease of reading (note: not a valid code on its own, as newlines are not an allowed character {#encoding})

# Safety/security considerations
It should be noted that nothing prevents an unscrupulous seller from misrepresenting their product. A GRC is intended for shorthand to describe a device and its history, not as a mark of safety or trustworthiness.

# Legal notice
 The authors of GRC offer this standard on a BEST EFFORT basis. It is not warrantied to be free from defects or for fitness for any particular purpose.

{backmatter}

<reference anchor='goodtools-country' target='https://emulation.gametechwiki.com/index.php?title=GoodTools'>
    <front>
       <title>GoodTools Country Codes</title>
       <author fullname='contributors'><organization>Game Tech Wiki</organization></author>
       <date year='2019'/>
    </front>
</reference>