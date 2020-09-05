%%%
title = "Game Repair Code v1"
abbrev = "GRCV1"
docName = "draft-grcv1-01"
category = "info"

ipr = "none"
area = "General"
workgroup = "Game Repair Code Workgroup"

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
[[author]]
initials="A."
surname="Parrish"
fullname="Alexander Parrish"
organization="A Force Dynamic"
 [author.address]
 email = "nuvandibe@gmail.com"
%%%

.# Abstract

This document proposes a new standard encoding method for consumer game console, software, and other related hardware
condition and repair information.

{mainmatter}

# Introduction

The GRC, Game Repair Code, is a condensed text string intended to denote the general status, details, and repair history
of consumer video game consoles, software, and peripherals. It is intended for use by collectors, curators, retailers,
resellers and enthusiasts, for any use case where a standardized way of representing the history and condition of video
game paraphernalia would be useful.

## Status of This Document

GRC v1 is currently in a develomental, RFC draft phase. It should not be used for any purpose until being finalized and
tooling has been developed.

## Terminology

The keywords **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**,
**MAY**, and **OPTIONAL**, when they appear in this document, are to be interpreted as described in [@RFC2119].

## Availability & Updates

The latest version document will always be hosted at https://gamerepair.codes

To propose changes, please submit a pull request at https://github.com/Karunamon/grc

The MASTER branch of the above-named repository is considered to be the most up-to-date version of this standard.

## Versioning
The GRC version is a monotonic counter. Any backwards-incompatible changes, such as changing the format or ordering of a
field or attribute, will be reflected by incrementing the counter by one.

# Syntax

A valid GRC string **MUST** follow this format:

`GRC Version Field|Hardware Field|Repair history field|`

Note that all fields and attributes are **REQUIRED** unless otherwise stated.

## Length
A valid GRC string **MUST NOT** exceed 1024 characters *before* encoding/compression. If a given code would be above
this limit after adding a repair record, the creator of the code **SHOULD** use their best judgment to remove old or
less-important records, paying special attention to any attributes in the `damage` fields that may no longer apply as a
result of maintenance undertaken.

## Encoding {#encoding}
A GRC string **MAY** be compressed for inclusion in tweets, QR codes, etc. 

A compressed GRC string **MUST** use the Deflate algorithm and no others.

Usable characters in a GRC string are the letters A through Z, numbers 0 through 9, and the symbols `!?;|,`. Most
characters are usable in freetext strings, however, the pipe and comma `|` `,` are reserved as separators and
**MUST NOT** be used within attributes or freetext.

Whitespace **MUST NOT** be used at all. The underscore character `_` **MAY** instead be used to indicate a word break in
freetext sections if desired. The PCRE regex `^([A-Z]|[a-z]|[0-9]|[\!\?\|,;_])+$` **MAY** be used to check whether a GRC
string contains valid characters.

## Version Field
This field **MUST** begin with an all-caps "GRC" followed by a monotonic counter indicating the revision of the standard
used. This document is the first revision, and so this field would read `GRC1`

In the case of compressed data, the original GRC string, including the number, **MUST** be compressed with Deflate,
and a new GRC string constructed with the version set to `Z`, indicating that everything after the counter is to be read
as base64-encoded Deflate data.


## Hardware Field {#hardware}
A definition of the actual physical object this code is referencing.

This field **MUST** be formatted in this order, as follows:
`B(brand),A(authenticity),F(family),R(region),T(type),C(color),V(revision),P(physical condition),D(currently known damage)`

### Brand/Manufacturer (B)
The Brand attribute is a 4-letter representation of the original manufacturer of the hardware or software. 

If the manufacturer is defunct, renamed, or was purchased by another entity, the name being used at the time of release
**MUST** be used.

If the company's name is included in the reserved list below, that abbreviation **MUST** be used.

If hardware/software is known to be released by a subsidiary of a larger company, the code creator **MUST** use the
subsidiary's name (i.e. Tengen would be its own company, not Atari, even though Tengen was an Atari subsidiary).

This does not apply in the case of identically-named regional susidiaries, such as Nintendo of Japan or Nintendo of
America. In these cases, use the code of the parent company.

Code | Company
-----|--------
NINT | Nintendo
SONY | Sony
MICR | Microsoft
SEGA | Sega
ATAR | Atari
APPL | Apple
Table: Reserved/recognized company codes


#### Special codes (Unknown or Non-Standardized Names)
Code | Meaning
-----|--------
!NONA| No-name (no brand or brand unknowable)
!UNKN| Unknown brand (but one probably exists)
?ABCD| Non-standard
Table: Special company codes

Codes prefixed with a `!` indicate missing information. `!NONA` indicates that the brand is unknown *and* unknow*able*.
This could be a "no name" devie with no meaningful brand information available, and it is unlikely that it will ever be
known. This is distinct from "I don't have the information available", which is the purpose of the code `!UNKN`.

Codes prefixed with a `?` are non-standard - i.e. they represent a company name that is not defined in this standard.
Tools that create or parse GRCs **SHOULD NOT** attempt to create a mapping of nonstandard names to full names, as 
nonstandard names can inherently be duplicated and could have multiple, conflicting meanings.

If a a company is not listed in this standard, the code creator **MUST** do one of the following:

1. If the company is publicly traded, insert a `?` prefix and follow with the first 4 characters of the company's stock
exchange ticker symbol. If the ticker symbol is shorter than 4 characters, continue prefixing `?`s up to a maximum
length of 4 letters. 

2. If the company is private or its status is unknown, insert a `?` prefix and invent a reasonable prefix based on the
company's name, taking care to not duplicate a reserved code. For example, "FooWare Ltd." could be represnted as `?FOOW`


### Authenticity \(A\)
This attribute represents the authenticity of the device. It **MUST** be one of the following:

* **O** if this is original hardware/software.
* **R** if it is a repro or bootleg.

Code creators should consider the brand/manufacturer when determining whether a device is OEM or Repro. If a piece of
hardware passes itself off as Nintendo hardware but is not made by Nintendo, its proper code is **R**. Third party 
consoles, even if they run OEM software (ex: the Retron series of systems), still do not pass themselves off as OEM
hardware, and **MUST** be given as their own company name with an authenticity of `OEM`.

This code has more to do with manufacturer than components. A Nintendo DS with sigificant modifications is still a
Nintendo-made Nintendo DS at the end of the day.

### Family \(F\)
This attribute represents the general hardware family of the device. It is composed of a 3-character ALL-CAPS
alphanumeric string.

The *first* release of any hardware system in any region defines the family, i.e. the US NES is part of the Famicom
family of systems. 

For systems with unnecessarily confusing naming schemes (Xbox 1 vs original Xbox vs Xbox One X vs Xbox), the generation
number will be used (ex XB1=Original xbox, XB2=Xbox 360/Slim, Xb3=Xbox One/Xbox One S/X) 

For software, the family indicates the primary system the software is intended to run on.

Family Code | Description
------------|-----------
FCM         | Famicom / NES
SMD         | Sega MegaDrive / Genesis
PCE         | PC Engine / TurboGrafx 16
MCD         | MegaCD / SegaCD
VCS         | Atari VCS (2800)
PSX         | Playstation
PS2         | PlayStation 2
N64         | N64
DCR         | Dreamcast
GBY         | Game Boy
GBA         | Game Boy Advance
NDS         | Nintendo DS / DSi / DS Lite
3DS         | Nintendo 3DS / 3DSXL / New 3DS / New 3DSXL
XB1         | Original Xbox
XB2         | Xbox 360/Slim
XB3         | Xbox One / Xbox One S / Xbox One X
XB4         | Xbox Series X
PC8         | NEC PC-88
IBM         | IBM PC Compatible
Table: Reserved/recognized family codes. This table is in no particular order.

### Region \(R\)
This attribute represents the original release region of the item. This field **MUST** a 1 or 2-letter GoodTools
country codes. [@goodtools-country]

### Type \(T\)
This attribute represents the general class of the device. It **MUST** be one of the following:

Type Code | Description
----------|------------
CON       | Console
DEV       | Devkit console
SFT       | Game or software (including all-in-one cheat devices like the NES Game Genie)
1ST       | First-party software-specific peripheral (ex: Super Scope, Multitap)
3RD       | 3rd-party hardware or software peripheral (ex: Konami Justifier, including non-all-in-one cheat devices such as the Gamecube Action Replay)
CNT       | Console intrinsic component (ex: power adapter, RF switch, video adapter or cables)
SNT       | Software intrinsic component (ex: standalone case or disc for a multi-disc game)
AMD       | Auxillary media device (ex: N64 Disk Drive, Famicom disk system, Sufami Turbo, Gamecube GBA player)
Table: Reserved/recognized type codes

### Color \(C\)
This attribute is **OPTIONAL** and can be ignored.

If included, this field **MUST** contain the first three letters of the official color as given by the manufacturer. If
the manufacturer calls their color "platinum", use PLT, not SLV (silver). 
 
### ReVision \(V\)
This attribute consists of 32 characters of free text, containing a model number if one sufficiently differentiates two
pieces of hardware, or a simple digit according to the release order of the hardware within the same family.


## Condition Field {#condition}
This field defines the item's *current* physical condition, including its overall status and any known damage.

### Physical Condition \(P\)
Represents an overall judgement of the physical condition of the hardware. **MUST** be one of the following:

Condition Code | Description
---------------|------------
NEW            | New, still in *unopened* factory packaging.
MNT            | Mint, opened, but in best concievable physical shape. **No damage or mods**.
USD            | Used, but fully functional. May have damage or be modified. Includes the presence of manufacturer refurbished hardware.
PNF            | Used, partially nonfunctional (system is fit for purpose but certain functions don't work)
CNF            | Completely nonfunctional (system is no longer fit for purpose)
Table: Reserved/recognized physical condition codes

### Currently Known Damage \(D\)
This attribute tracks various kinds of damage or degradation of an item. Damage consists of hardware or software
deformities, with each class of damage having its own unique 3-letter code.

If multiple classes of damage apply to the item, they **MUST** be listed consecutively, with no delimiter. Ex: For a
device with a yellowed case with smoke damage and missing fasteners, this would read `SHYSMKFST`.

If new damage occurs, or if damage is repaired by console service, such as a shell replacement, the known damage fields
**MUST** be updated to reflect the *current condition* of the item.

#### Reserved/Known Damage Codes
* **SH\***: Shell/Case issues
  * **SHC**: Shell cracks
  * **SHS**: Shell scratches
  * **SHY**: Yellowing
  * **SHF**: Faded wording or print
  * **SHL**: Missing, damaged labels or stickers
  * **SHM**: Missing shell parts, such as a battery or port cover
* **EC\***: Electrical component issues
  * **ECP**: Damage to the board itself, such as cracks or lifted traces
  * **ECC**: Visible damage to board components, such as blown capacitors or transistors
* **SMK**: Smoke (either nicotine or from fire) damage
* **WAT**: Water/moisture damage, including rust
* **BLK**: Battery leakage or corrosion
* **OL\***: Online service issues
  * **OLS**: Limited access to online services (game bans, or restriction to updates only)
  * **OLB**: No access to online services (hard console ban, updates not allowed) 
* **LC\***: Loose or intermittent connectors 
  * **LCC**: Loose controller port
  * **LCV**: Loose video port
  * **LCE**: Loose expansion or memory card port
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
  * **OMR**: Damage or holes in the data layer due to label damage or "Disc rot"
* **SC\***: Screen and digitizer issues
  * **SCS**: Screen scratches (superficial)
  * **SCR**: Screen scratches (deep)
  * **SCC**: Screen cracks (superficial)
  * **SCA**: Screen cracks (deep, functionality/readability impacted)
  * **SCU**: Screen colors are obviously incorrect
  * **SCP**: Dead pixels
  * **SCD**: Digitizer (touchscreen) issues
  * **SCX**: Screen is completely dead/nonfunctional for unknown reasons
* **REF**: Includes refurbished parts
  
* **TXT**: 24 characters of freetext follow; **MUST** come last, only one is permitted in code D.

### Modifications \(M\)
A list of the item’s aftermarket modifications, including such things as custom shells, LED modifications, software and
hardware modifications.

What constitutes a modification rather than a repair is whether the console appears or behaves differently from a stock
console. Replacing a damaged shell with an identical shell is a repair (swap), whereas replacing a shell with a
different color of shell is a modification.

If there are no modifications present, this field **MUST** be populated with "STK".

#### Reserved/Known Modification Codes
* **STK**: No known modifications present on this console

* **LED**: LED modification; lights have been added to part of the item that did not have them before, or existing colors were replaced
* **SHL**: Shell modification; replacing with a non-stock shell or painting a shell with a custom color
* **BKL**: Backlight
* **RGF**: Region-free
* **CHP**: Modchip
* **SFM**: Soft-mod / custom firmwarre
* **CNS**: Consolization
* **VID**: Video-output (rgb, hdmi)
* **STO**: Storage modification
* **BAT**: Battery modification
* **AUD**: Audio-output modifications (speakers, headphones)
* **PCB**: Circuit or PCB-level mods, not including region-free or modchip installation
* **ODE**: Optical drive emulator

### Known Repairs/Replacements \(E\)
This attribute is a list of non-modification repairs. It includes replacement of OEM parts with repro parts *that look
and perform identically to their OEM counterparts*. For instance, replacing a cracked shell with an identical one, or
replacing minor electronic components, or screen repair, etc. Generally, what differentiates an M from an R is whether
the system has been customized or substantially changed from its OEM state. If this difference is ambiguous for your use
case, you **SHOULD** default to using the M code instead.

Repairs/replacements of already-modified components **MUST** be treated as a re-modification and not included in this
field.

Repair codes **MUST** be considered permanent and never be removed for any reason unless inaccurate.

#### Reserved/Known Repair Codes {#repaircodes}
* **NR\***: No repairs, choose one of these two:
  * **NRS**: No repairs, all seals still intact
  * **NRO**: No repairs, has been opened (seals broken)
* **SHL**: Shell repair (resurfacing or crack filling) or replacement, including shell components like switches or buttons (excluding cleaning)
* **LBL**: Label or printing replacement
* **BKL**: Backlight
* **SCR**: Screens/displays
* **DIG**: Digitizer (touchscreen)
* **PRT**: Ports (controller, data, video, etc.)
* **PCB**: PCB components
* **RBT**: Retrobriting
* **SFT**: Software / filesystem
* **SPK**: Speaker / direct sound output (excluding jacks, these **MUST** be classified as **PRT**)
* **BAT**: Non-user-accessible batteries
* **RPT**: Metal replating

* **REP**: Repro (non-OEM) parts were used for any replacements
* **TXT**: 24 characters of freetext follow; **MUST** come last, only one is permitted under code E.

## Service History Field {#servicehistory}
The service history field represents a list of repair events.  A "repair event" defined as service of a single item or
directly related group of items in a subassembly.

The history list **MUST** be in chronological order, oldest events first. Each event **MUST** be comma-separated.

If a service history entry is invalidated or duplicated by a later event, such as the same component being replaced
twice, the earlier entry **SHOULD** be removed.

Code creators **MUST NOT** add new service history items that they did not either personally perform or have done on
their behalf.

The service history field format is as follows:

`(Datestamp) (Repair type) (Item repaired) (20 characters free text),`

### Note on OEM Replacements / Refurbishments
Often, when sending consoles in to OEMs, they may repair a system and send it back, *or* send an entirely new
refurbished console. Check the serial numbers in this case. If a new serial number is received, then you have received a
new console and **MUST** start a brand new code. Do not carry any history over. If the hardware you received is not in
its factory packaging, you **MUST** add a **REF** under code D, and note its status as **USD** under code

Refurbished consoles likely have had components repaired, but unless you are able to determine with certainty which
components those were, you **MUST NOT** guess.

### Date of Service
Each history entry **MUST** begin with the ISO8601 date (ex: YYYYMMDD) the action was *finished*, with no separator.
Example: 20200829 for August 29th, 2020.

If the repair date is entirely unknown, but you know a repair was done, you **MUST NOT** add a history entry for it.
Note the nature of the repaired/replaced component under code E (Repairs) instead.

### Repair Types
Denotes the general disposition of the changes made to the hardware. This **MUST** be one of the 3 following characters:

* M: Mod
* S: Swap (broken parts to new parts) 
* R: Repair (existing parts condition improved, or significant cleaning)

Swaps or repairs that require no tools, such as battery replacements or consumer-accessible cleaning (say, taking a
cotton swab to a the laser on a disc system) **MUST NOT** have a repair entry added.

### Item Repaired
Use a valid reserved code from the [list of known/reserved repair codes](#repaircodes)

# Example Code
The following is an example of a compliant GRC1 code:

```
GRC1|BNINT,AO,FNGC,RU,TCON,CPLA,V000|PUSD,DSHCSMKTXTSmoking_home,MCHPLED|20200829MCHPHyperBoot,20200829MLEDCtrlr,20200829SSHLOEMTop,20200829SSHLOEMHsd,20211224RMSCMHyperBoot,20211224SMSCOEMCtrlport3,20211224SDDA3RD|
```
Figure: A GCR1 in its regular format

By adding newlines and spaces, we break this code down into a more human-readable format:

```
GRC1                             // Code generation
|B NINT,                         // Brand: Nintendo
A OEM,                           // Authenticity: Verified OEM (Original Equipment Manufacturer)
F NGC,                           // Console family: GameCube
R U,                             // Regional variant: North America (United States)
T CON,                           // Type of hardware: Console
C PLA,                           // Color: Platinum (Brand's own naming scheme)
V 000                            // Revision: 0 / DOL-001 in the case of the GameCube
|P USD,                          // Physical condition: Used
D SHC SMK TXT Smoking_home       // Damage: Cracks in shell,  Smoke, [Freetext] Smoking home
|MCHPLED                         // Mod: Modchip and LEDs installed
|20200829 M CHP HyperBoot,       // On August 29, 2020: Mod installed / Modchip / [Freetext] Hyperboot
20200829 M LED Ctrlr,            // On August 29, 2020: Mod installed / LED(s) / [Freetext] Controller ports
20200829 S SHL OEM Top,          // On August 29, 2020: Swapped part / Shell / OEM part / [Freetext] Top shell
20200829 S SHL OEM Hsd,          // On August 29, 2020: Swapped part / Shell / OEM part / [Freetext] High speed data port cover
20211224 R MSC M HyperBoot,      // On November 24, 2021: Repaired / Miscellaneous component / [Freetext] Hyperboot modchip
20211224 S MSC OEM Ctrlport3,    // On November 24, 2021: Swapped part / Miscellaneous component / OEM part / [Freetext] Controller port 3
20211224 S DDA 3RD|              // On November 24, 2021: Swapped part / Disc Drive assembly / 3rd party component
```
Figure: A full GCR1 with history, expanded for ease of reading (note: not a valid code on its own, as newlines and spaces are not allowed characters)

# Corner Cases and Ambiguities
The organization scheme this standard sets out is suitable for nearly all purposes, yet there are specific niche pieces
of hardware that could lead to ambiguity when defining codes. Some of these will be covered here as a sort of FAQ.

**Multi-part Peripherals**
: In the case of peripherals that have multiple independent parts (example: The SNES Super Scope itself, and the IR
dongle that connects to the console), each part **MUST** be considered as its own unique peripheral. (I.e. the scope and
the dongle would have their own individual GRCs). Batching components together **MUST NOT** be done.

## Type Classification
Certain devices may defy the code T classification scheme, or have good arguments for falling under multiple categories.
These include the following:

**Cheat Devices**
: All-in-one devices (that is, the cheat hardware and software are part of a single physical unit, ex: the NES Game
Genie) are considered **SFT**. In the case of devices that have a separate cheat device as well as software, such as the
Playstation or Gamecube Action Replay, these must have their own separate GRCs. The disc is **SFT**, and the device
**3RD**. 

**Cartridge Copiers / Backup Devices**
: These are all considered **3RD**.

**Multiplayer Adapters**
: These fit under the **3RD** category, and include devices such as the XBAND for SNES or Genesis. **3RD** would
also apply to multitap-like devices.

**Cartridge Peripherals**
: These would generally fit under the category of **AMD** - devices that plug into the cartridge slot and allow you to
play additional content in a format that was not possible on the original hardware. This would include downloading from 
the internet, received over broadcast services, or alternate physical media formats. Examples would include the
Broadcast Satellaview or Sega Channel, Mega CD, Famicom Disk System, etc. It would also include retro compatibility
addons, such as the Gameboy Player for the GameCube. 

Note that the software and hardware must have their own codes if they can be separated. The Satetllaview cartridge,
memory unit, and satellite adapter are all distinct devices with distinct GRCs.

## Conflicting Codes
Generally speaking, the "rules" for a GRC code are:

1. Codes **MUST NOT** conflict with one another. Any situation which would result in a conflict is either an unforeseen
   design flaw, or a case where one or multiple codes must be adjusted.
2. Codes in the [hardware](#hardware) field should be considered historic and rarely changed. These should be written 
   according to their validity *at the time of manufacture*. For instance, a console modified with an aftermarket
   third-party shell of a different color would still be classified with the color of its origignal manufacture.
3. Codes in the [condition](#condition) field relate to the *present* condition of the hardware.
4. Codes **SHOULD** be constructed such that all pertinent information about a pice of hardware is present even if the
   [service history](#servicehistory) section is blank.

# Legal

## Safety/Security Considerations
It should be noted that nothing prevents an unscrupulous seller from misrepresenting their product. A GRC is intended
for shorthand to describe a device and its history, not as a mark of safety or trustworthiness.

## Warranty Disclaimer
The authors of GRC offer this standard and any related applications or services on a BEST EFFORT basis. It is not
warrantied to be accurate, up to date, or fit for any particular purpose.

## Copyright
Copyright 2020 - Mike Parks, Alexander Parrish, and contributors

Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation
License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections,
no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license is included in the file
[LICENSE.MD](https://raw.githubusercontent.com/Karunamon/grc/master/LICENSE.md), located in the same repository as the
standard doc.

{backmatter}

<reference anchor='goodtools-country' target='https://emulation.gametechwiki.com/index.php?title=GoodTools'>
    <front>
       <title>GoodTools Country Codes</title>
       <author fullname='GTW Contributors'><organization>Game Tech Wiki</organization></author>
       <date year='2019'/>
    </front>
</reference>