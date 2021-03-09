%%%
title = "Video Game Condition Code v1"
abbrev = "VGCCv1"
docName = "draft-vgccv1-01"
category = "info"

ipr = "none"
area = "General"
workgroup = "Video Game Condition Report Workgroup"

[seriesInfo] 
name = "RFC"
value = "draft-vgccv1-01"
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

This document proposes a new encoding method for video game hardware/software identity and condition, and optionally, repair history.

{mainmatter}

# Introduction

The VGCC, Video Game Condition Code, is a condensed text string intended to denote the general status, details, and repair history of consumer video game consoles, software, and peripherals. It is intended for use by collectors, curators, retailers, resellers and enthusiasts, for any use case where a standardized way of representing the history and condition of video game paraphernalia would be beneficial.

## The Need for a Standard

Most who have tried curating their own collection of video games understands that doing so has historically been a hassle. Whereas there are clearly-defined, community-accepted guidelines for collecting in other fields, such as coins, comics, and artwork, video games have been notably lacking in this department.

The Video Game Condition Report aims to standardize the way that video game hardware and software is described insofar as the actual status of the collectible, as well as provide a method for encoding concise information into a QR code, NFC tag, or any similar medium for decoding by a portable device such as a phone or scanner.

By creating and releasing this standard we, The VGCR Foundation, hope to help mitigate and misunderstandings where it comes to sales, trading, and describing collectibles.

## Status of This Document

VGCC is currently in a developmental, RFC draft phase. It should not be used for any purpose until it has been finalized and tooling has been developed.

## Terminology

The keywords **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **MAY**, and **OPTIONAL**, when they appear in this document, are to be interpreted as described in the IETF's [@RFC2119] when, and only when, they appear in bolded all-caps as shown here.

## Availability & Updates

The latest version document will always be hosted at https://gamerepair.codes

To propose changes, please submit a pull request at https://github.com/Karunamon/grc

The latest release tag of the above-named repository is considered to be the most up-to-date version of this standard. The `MASTER` branch represents work in progress.

## Versioning

The VGCC version is a monotonic integer. There are no point releases.

The version number will be given:

* In the title of this document
* In a tag with the prefix `v` in the above-mentioned git repository
* In the version field in a compliant VGCC

Any backward-incompatible changes, such as changing the format or ordering of a field or attribute, will be reflected by incrementing the counter by one.

## Scope

The VGCC is intended as a standard for encoding and displaying the condition of *only* physical video game hardware, software, and peripherals. 

The following specific types of items are explicitly considered out-of-scope despite their categorical relationship with video games. This standard **MAY** be used for classification of these items, but the specific needs of these items will not be considered by the VGCR working group, either in this standard or any supporting documentation or tooling:

Item type                           | Reasoning
------------------------------------|---------------------------------------------------
Pinball tables                      | Not considered video games
Electronically-assisted board games | Not considered video games
IBM-compatible PCs or software      | Impossible to determine a specific brand or model
Arcade machines                     | Planned for a future version of the standard

# General Syntax

A valid VGCC string **MUST** follow this format:

`VGCC Version Field|Hardware Identity Field|Condition Field|Repair history field|`

All fields and attributes are **REQUIRED** unless otherwise stated.

## Length

A VGCC string **MUST NOT** exceed 1024 characters *before* compression. If a given code would be above this limit after adding a repair record, the creator of the code **Must** use their best judgment to remove old or less-important records, paying special attention to any attributes in the `Condition` field that may no longer apply as a result of maintenance undertaken.

## Encoding

Usable characters in a VGCC string are the ASCII letters A through Z in mixed case, numbers 0 through 9, and the symbols `!?;-|_,`.  

The pipe (`|`) and comma (`,`) characters are reserved as field and attribute separators respectively, and **MUST NOT** appear in any other context. "Escaping" these characters is not permitted.

The PCRE regular expression `^([A-Z]|[a-z]|[0-9]|[\!\?\|\-,;_])+$` **MAY** be used to check whether a VGCC string contains invalid characters.

## Free-text attributes

Certain attributes in a field are designated as free-text. A free-text attribute contains 32 characters or less of alphanumeric characters subject to the encoding rules above. This text **SHOULD** be understood by tools that create or parse codes as arbitrary and conforming to no standard save for the description here.

Since whitespace is not allowed per the encoding rules, the underscore (`_`) **MAY** be used as a word separator if desired.

## Optional fields

Any field designated as "optional" **MUST** still include its field designator (M for model, C for color, etc).

# Design Philosophy

The syntax of a VGCC hardware identity field is laid out in a hierarchical structure, starting broadly and then narrowing down to the identity of an individual item.

Consider the example of a launch day US Playstation 2. The hardware field could look like:

`|BSONY,AO,FPS2,RU,TCON,MPS2,CBLK,VSCPH-90001,SU3565655,I|`

Hierarchically, this breaks down as

```
Sony
  Original OEM
    Playstation 2
      USA
        Console
          Original Playstation 2 (Fat)
            Black
              SCPH-90001
                U3565655
```

This broad-to-narrow design was chosen because it allows for maximum flexibility in describing different types of items. 

# Field Syntax

## Version Field

This field **MUST** begin with an all-caps "VGCC" followed by a digit indicating the revision of the standard used:

`VGCC(version number)`

### Compression

For representation in QR codes or in a space-constrained medium, a VGCC **MAY** be compressed. This is accomplished by taking an entire valid code, running it through the Deflate algorithm, and base64 encoding the result. The compressed data is then placed in a new code with the version set to `Z`, in the format:

`VGCCZ|(compressed data)`

## Hardware Identity Field

The hardware identity field defines, hierarchically, the identity of the item the code is being written for. 

This field **MUST** be ordered as follows:

`B(brand),A(authenticity),F(family),R(region),T(type),M(model),C(color),V(variant),S(serial),I(information)`

### Brand/Manufacturer \(B\)

The Brand attribute is a four-letter representation of the original manufacturer of the hardware or software.

Owing to the large number of possible brands, the VGCC standard will not attempt to define a list of all brands. Nevertheless, it is **RECOMMENDED** that companies appearing in the following table use the given brand code:

Code | Company
-----|--------
NINT | Nintendo
SONY | Sony
MICR | Microsoft
SEGA | Sega
ATAR | Atari
COMM | Commodore

Codes prefixed with a `!` indicate missing information. These special codes **MUST NOT** be used for any other purpose.

Code | Meaning
-----|--------
!NONA| No-name (no brand or brand unknowable)
!UNKN| Unknown brand (but one probably exists)


- `!NONA` indicates that the brand is unknown *and* unknow*able*. This could be a "no name" item with no meaningful brand information available, and it is unlikely that it will ever be known.
- `!UNKN` indicates that there probably is a brand, but that the information is not known to the creator of the code

When creating brand codes, it is **RECOMMENDED** that the following considerations apply:

- If an item is known to be released by a subsidiary of a larger company, use the subsidiary's name (and so Tengen would be its own company, not Atari, even though Tengen was an Atari subsidiary).
- For similarly-named regional subsidiaries, such as Nintendo of Japan or Nintendo of America, use the code of the parent company. Splitting regional subsidiaries into their own brands may represent too much granularity.

### Authenticity \(A\)

This attribute represents the authenticity of the device, i.e if the hardware is made by who it claims to be made by.

The attribute takes the form of:

- **`O`** if this is original or OEM hardware/software.
- **`R`** if it is a repro or bootleg.

Consider the brand/manufacturer when determining whether a device is original or repro. For example, if a piece of hardware passes itself off as Nintendo hardware but is not made by Nintendo, its proper code is **`R`**. Third-party consoles, even if they run OEM software (example: [the RetroN series of consoles](https://en.wikipedia.org/wiki/RetroN)), still do not pass themselves off as OEM hardware, and **MUST** be given as their own company name with an authenticity attribute of `O`


### Family \(F\)

This attribute represents the general hardware family of the item. It is composed of a 3-character ALL-CAPS alphanumeric string.

The *first* release of any hardware system in any region defines the family. For example, the US NES is part of the Famicom family of systems.

For software, the family indicates the primary system the software is intended to run on.

Owing to the large number of possible brands, the VGCC standard will not attempt to define all possible families. Nevertheless, it is **RECOMMENDED** that hardware appearing in the following table use the given family code:

Family Code | Description
------------|-----------
FCM         | Famicom / NES
SFC         | Super Famicom / SNES
SMD         | Sega MegaDrive / Genesis
PCE         | PC Engine / TurboGrafx 16
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

### Region \(R\)

This attribute represents the original release region of the item. 

This field **MUST** be a recognized 1 to 3-letter GoodTools country code. [@goodtools-country]

### Type \(T\)

This attribute represents the general type of the item ("This is a: ____").

All items **MUST** fall into one of these recognized categories:

Type Code | Description
----------|------------
CON       | Console
DEV       | Devkit console
1PA       | First-party or OEM component (ex: controller, av cables, power adapters)
3PA       | Third-party component (ex: a Madcatz AV cable or controller)
SFT       | Game or software media (including integrated cheat devices like the NES Game Genie, or a complete media package)
SNT       | Software intrinsic component (box or manuals, including separated cheat devices like the Gamecube action replay)
AMD       | Alternate media device (ex: N64 Disk Drive, Famicom disk system, Sufami Turbo, Gamecube GBA player)

### Model \(M\)

This attribute is considered free-text.

This attribute represents different releases of a given set of hardware of the same type and family with different features or functionality. For example, the Sega Genesis models 1, 2, or 3, or the PS2 fat or slim.

It is **RECOMMENDED** that, if a VGCC is describing a piece of hardware that is the first in its family, that this attribute be set to the same value as the family attribute.

### Color \(C\)

This attribute is **OPTIONAL** and may be left empty.

Represents the official color of the device as given by the manufacturer at manufacture time. 

If provided, this attribute **MUST** contain the first three letters of the official color as given by the manufacturer. If the manufacturer calls their color "platinum", use PLA rather than SIL (silver).

### Variant/Revision \(V\)

This attribute is **OPTIONAL** and may be left empty. If provided, it is considered free-text.

Represents a distinct hardware variant of a given model. For example, the "standard" Sega Dreamcast has the VA0, VA1, and VA2 variants

### Serial number \(S\)

This attribute is **OPTIONAL** and may be left empty. If provided, it is considered free-text.

Represents the full manufacturer serial number (*not* model number) of the device. If the serial number is unknown or non-existent, this field **MUST** be left blank.

### Information \(I\)

This attribute is **OPTIONAL** and may be left empty. If provided, it is considered free-text.

Contains any other special information the code creator wishes to share. This field **SHOULD** be used sparingly and only when the information provided is not duplicated by any other field and is significantly important to the identity of the item being cataloged.

## Condition Field

This field defines the item's *current* physical condition, including its overall status and any known damage.

The condition field is formatted as:

`P(condition code),D(damage codes),M(modification codes),E(repair codes)`

### Physical Condition \(P\)

This attribute represents an overall judgment of the physical condition of the item. It **MUST** be one of the following:

Condition Code | Description
---------------|------------
NEW            | New, still in *unopened* factory packaging.
MNT            | Mint, opened, but in best concievable OEM physical condition. **No damage or mods**.
USD            | Used, but fully functional. May have damage or be modified. Includes the presence of manufacturer refurbished hardware.
PNF            | Used, partially nonfunctional (system is fit for purpose but certain functions are degraded)
CNF            | Completely nonfunctional (system is no longer fit for purpose)

### Currently Known Damage \(D\)

This attribute tracks various kinds of damage or degradation of an item. Damage consists of hardware or software deficiencies, with each class of damage having its own unique 3-letter code.

If multiple damage classes apply to the item, they **MUST** be listed consecutively, with no delimiter. For example, an item with a yellowed case, smoke damage, and missing fasteners would have a damage attribute of `SHYSMKFST`.

If new damage occurs, or if the damage is repaired by servicing, such as a shell replacement, the known damage fields **MUST** be updated to reflect the item's ***current*** condition.

The list below is formatted for ease of reading. Consecutive types of the same class of damage **MUST** be coded consecutively, so for a yellowed and cracked shell, the code is `SHCSHY` rather than  `SHYC`.

Additionally, a digit from 1 to 3 representing the severity of the class of damage may **OPTIONALLY** be added to the codes which call out a distinction below. Codes that support a severity have a `#` in their description. Codes without this designation **MUST NOT** have a digit added.

The list of acceptable damage codes is as follows:

- **SH_**: Shell/case issues
    - **SHC#**: Shell cracks 
    - **SHS#**: Shell scratches (1/2/3)
    - **SHY#**: Yellowing
    - **SHF#**: Faded wording or print
    - **SHK#**: Missing, damaged labels or stickers
    - **SHM**: Missing shell parts, such as a battery or port cover
    - **SHZ**: Shell is missing outright
- **EC_**: Electrical component issues
    - **ECP**: Damage to the board or substrate itself, such as cracks or lifted traces
    - **ECC**: Visible damage to board components, such as blown capacitors or transistors
    - **ECX**: Known but invisible damage, such as a damaged IC (explain in `TXT`)
    - **ECZ**: Electrical components are missing (explain in `TXT`)
- **SMK#**: Smoke damage, including fire or nicotine contamination
- **WAT#**: Water/moisture damage, including rust
- **BLK#**: Battery leakage or corrosion
- **LCP#**: Partially or completely nonfunctional PCB edge connector (cartridge slot or similar)
- **OL_**: Online service issues
    - **OLX**: Limited access to online services (game bans, or restriction to updates only)
    - **OLZ**: No access to online services (hard console ban, updates not allowed)
- **LM_:** Loose, missing, or intermittent connectors
    - **LMC#**: Loose controller port
    - **LMV#**: Loose video port
    - **LME#**: Loose expansion or memory card port
    - **LMP#**: Loose power connector
    - **LMC#**: Loose or damaged PCB edge connector (cartridge slot, etc)
    - **LMS#**: Loose switch of any kind (power/mode/etc.)
    - **LMZ**: Outright missing connectors (explain which ones in TXT)
- **DNS**: Does not save. Battery backup/saving failure
- **FST**: Missing fasteners (clips, screws, etc)
- **SFT**: Software failure (functional issues due to missing/corrupt files)
- **OM_**: Optical media issues
    - **OMS#**: Scratches
    - **OMC#**: Cracks
    - **OMR**: Visible damage or holes in the data layer due to label damage or "Disc rot"
    - **OMX**: Cracks, deep (disc is likely destroyed)
- **OD_**: Optical drive issues
    - **ODX#**: Optical drive damaged (intermittent, unreliable, or non-functional)
    - **ODZ**: Optical drive missing   
- **OS_**: On-board storage (HD/SSD, NVRAM, or permanent battery-backed RAM) issues
    - **OSX**: On-board storage is corrupt or non-functional
    - **OSZ**: On-board storage is missing
- **SC_**: Screen and digitizer issues
    - **SCS#**: Screen scratches (superficial)
    - **SCR#**: Screen scratches (deep)
    - **SCC#**: Screen cracks
    - **SCU#**: Screen colors are incorrect or shifted
    - **SCP#**: Dead pixels
    - **SCD#**: Digitizer (touchscreen) issues
    - **SCX**: Screen is completely dead/nonfunctional
    - **SCZ**: Screen is missing
- **REF**: Includes refurbished parts (explain in TXT)
- **XXX**: This item has been irreperably destroyed.
- **TXT**: Free-text follows. **MUST** come last.


### Modifications \(M\)

This attribute represents a list of the item's aftermarket modifications, including custom shells, LED modifications, etc., including those done to the item's software.

What constitutes a modification rather than a repair is whether the console appears or behaves differently from a stock console. Replacing a damaged shell with an identical shell is a repair (swap), whereas replacing a shell with a different colored shell is a modification.

If there are no known modifications present, this field **MUST** be populated with "STK".

Code | Meaning
-----|------------
STK  | No known modifications present on this console
LED  | LED modification; lights have been added to part of the item that did not have them before, or existing colors were replaced
SHL  | Shell modification; replacing with a non-stock shell or painting a shell with a custom color
BKL  | Backlight
RGF  | Region-free
CHP  | Modchip
SFM  | Soft-mod / custom firmware
CNS  | Consolization
VID  | Video-output (rgb, hdmi)
STO  | Storage modification
BAT  | Battery modification
AUD  | Audio-output modifications (speakers, headphones)
PCB  | Circuit or PCB-level mods, not including region-free or modchip installation
ODE  | Optical drive emulator
INT  | Integration, installing normally external peripherals into a shell (ex: Genesis Neptune mod [@Neptune]) 

### Known Repairs/Replacements \(E\)

This attribute represents a list of non-modification repairs. It includes replacing OEM parts with reproduction parts that look and perform identically to their OEM counterparts.

For instance, replacing a cracked shell with an identical one, replacing minor electronic components, screen repair, etc.

Generally, what differentiates a `M` (mod) from an `E` (repair) is whether the system has been customized or substantially changed from its OEM state. If this difference is ambiguous for your use case, you **SHOULD** default to using the `M` code instead.

- Repairs/replacements of already-modified components **MUST** be treated as a re-modification and not included in this field.
- Repair codes **MUST** be considered permanent and never be removed for any reason unless inaccurate.

The list of repair codes is as follows:

* **NR\***: No repairs, choose one of these two:
  * **NRS**: No repairs, all seals still intact
  * **NRO**: No repairs, has been opened (seals broken, use if unsure)
* **SHL**: Shell repair (resurfacing or crack filling) or replacement, including shell components like switches or buttons (excluding cleaning)
* **LBL**: Label or printing replacement
* **BKL**: Backlight
* **SCR**: Screens/displays
* **DIG**: Digitizer (touchscreen)
* **PRT**: Ports (controller, data, video, etc.)
* **PCB**: PCB components
* **RBT**: Retrobriting
* **SFT**: Software / file system
* **SPK**: Speaker / direct sound output (excluding jacks, these **MUST** be classified as `PRT`)
* **BAT**: Non-user-accessible batteries
* **RPT**: Metal replating
* **REP**: Repro (non-OEM) parts were used for any replacements
* **TXT**: Free-text follows. **MUST** come last

## Service History Field

This field is **OPTIONAL** and may be skipped.

The service history field represents a list of repair events. A "repair event" defined as service of a single item or directly related group of items in a sub-assembly.

The format for a repair event is as follows:

`(Datestamp)(Repair type)(Item repaired)(Free-text),`

- The history list **MUST** be in chronological order, oldest events first.
- Each event **MUST** be comma-separated.
- If a service history entry is invalidated or duplicated by a later event, such as the same component being replaced twice, the earlier entry **SHOULD** be removed.
- Code creators **MUST NOT** add new service history items that they did not either personally perform or have performed on their behalf, unless a specific record of the repair or modification is consulted, such as an invoice.

### Date of Service

Each history entry **MUST** begin with the ISO8601 date (in the YYYYMMDD format) when the action was *finished*, with no separator. Example: 20200829 for August 29th, 2020.

If the repair date is entirely unknown, but you know a repair was made, you **MUST NOT** add a history entry for it. Note the nature of the repaired/replaced component under code `E` (Repairs) instead.

### Repair Types

Represents the general disposition of the changes made to the item. This **MUST** be one of the codes below:

Code | Meaning
-----|---------
M    | Mod
SO   | Swapped in an OEM part
SR   | Swapped in a third-party or reproduction part
R    | Repair (existing parts condition improved, or significant cleaning that resolves a concrete functional problem)

Swaps or repairs that require no tools, such as battery replacements or cleaning intended to be done by the end user (for example, taking a cotton swab to a the laser on a disc system) **MUST NOT** have a repair entry added.

### Item Repaired

Use a valid code from the [list of repair codes](#repaircodes)

# Example Code

The following is an example of a compliant VGCC1 code:

```
VGCC1|BNINT,AO,FNGC,RU,TCON,MNGC,CIND,VDOL-001,SDS315060768,I|PUSD,DSHCSMKTXTSmoking_home,MCHPLED,ESHLPRTDDAREPTXTRepro_Shell|20200829MCHPHyperBoot,20200829MLEDCtrlr,20200829SOSHLTop,20200829SOSHLHsd,20211224RMSCMHyperBoot,20211224SOMSCCtrlport3,20211224SRDDA|
```

This given code breaks down as follows. Note that the field separator in this table is an underscore `_` rather than a pipe `|` for formatting reasons:

Code Block | Meaning
-----------|---------
VGCC1 | VGCC standard version: 1
 _ | **Field separator, hardware section begins**
BNINT | Brand: Nintendo
AO | Authenticity: OEM (authentic Nintendo hardware)
FNGC | Hardware family: GameCube
RU | Regional variant: North America (United States)
TCON | Type of hardware: Console
MNGC | Model: GameCube (original release)
CIND | Color: Indigo (official name)
VDOL-001| Variant: DOL-001
SDS315060768 | Serial number: DS315060768
I | Information field blank
_ | **Field separator, physical condition section begins**
PUSD | Physical condition: Used
DSHCSMKTXTSmoking_home | Damage: Cracks in shell, smoke. Free-text: Smoking home
MCHPLED | Modifications: Modchip and LEDs installed
ESHLPRTDDAREPTXTRepro_Shell | Repairs made: Shell, port(s), disc drive assembly, refurbished parts used. Free-text: Repro Shell
 _ | **Field separator, repair history section begins**
20200829MCHPHyperBoot | August 29, 2020: Mod installed / Modchip / Free-text: Hyperboot
20200829MLEDCtrlr | August 29, 2020: Mod installed / LED(s) / Free-text: Controller ports
20200829SOSHLTop | August 29, 2020: Swapped part / OEM part / Shell / Free-text: Top shell
20200829SOSHLHsd | August 29, 2020: Swapped part / OEM part / Shell / Free-text: High speed data port cover
20211224RMSCHyperBoot_wiring | December 24, 2021: Repaired / Miscellaneous component / Hyperboot wiring
20211224SOPRTCtrlport3 | December 24, 2021: Swapped part / OEM part / Port / Controller port 3
20211224SRDDA | December 24, 2021: Swapped part / Third party part / Disc Drive assembly


# Corner Cases and Ambiguities

The organization scheme this standard sets out is suitable for nearly all purposes, yet there are specific niche pieces of hardware that could lead to ambiguity when defining codes. Some of these will be covered here as a sort of FAQ.

**Multi-part Peripherals:** In the case of peripherals that have multiple independent parts (example: The SNES Super Scope itself, and the IR dongle that connects to the console), each part **MUST** be considered as its own unique peripheral, so the scope and the dongle would have their own individual VGCCs. Batching components together **MUST NOT** be done.

## Type Classification

Certain items may defy the code `T` classification scheme, or have good arguments for falling under multiple categories. The VGCR working group **RECOMMENDS** the following:

**Cheat Devices:** All-in-one devices (that is, the cheat hardware and software are part of a single physical unit, ex: the NES Game Genie) are considered `SFT`. In the case of devices that have a separate cheat device as well as software, such as the PlayStation or Gamecube Action Replay, these must have their own separate VGCCs. The disc is `SFT`, and the hardware is `SNT` (as the device is intrinsic to the function of the software).

**Cartridge Copiers / Backup Devices:** These are all considered `3PA`.

**Multiplayer Adapters:** These fit under the `3PA` category, and include devices such as the XBAND for SNES or Genesis. Multitap devices made by the console OEM are considered `1PA`.

**Cartridge Peripherals:** These would generally fit under the category of `AMD` - devices that plug into the cartridge slot and allow you to play additional content in a format that was not possible on the original hardware. This would include devices where content is downloaded from the internet, received over broadcast services, or alternate physical media formats. Examples would include the Broadcast Satellaview or Sega Channel, Mega CD, Famicom Disk System, etc. It would also include retro compatibility add-ons, such as the Game Boy Player for the GameCube.

Note that the software and hardware must have their own codes if they can be separated. The Satellaview cartridge, memory unit, and satellite adapter are all distinct devices with distinct VGCCs.

**Software for Alternate Media Devices:** Use the family code of the parent console. "Sonic CD" would have a family code of `SMD`. 

## Ambiguity in Authenticity

To avoid "ship of Theseus" situations when determining authenticity, it is **RECOMMENDED** to think in terms of non-replaceable components. For instance, it is quite possible to replace the shell and a number of electronic components on an NES, but it still contains a OEM NES CPU and PPU at the en of the day. If those components are replaced with an FPGA of some kind, and the device still claims to be made by Nintendo, then it is clearly a repro.

The VGCR working group can not hope to objectively determine the line between "real" and "repro". Code creators are encouraged to consider the expectations of the human readers of their codes and encode information according to the principle of least astonishment [@POLA].

## Refurbishment

When sending consoles into OEMs, they may repair a system and send it back *or* send an entirely new refurbished console. Check the serial numbers in this case. If a new serial number is received, you have received a new console and **MUST** start a brand new VGCC. **Do not carry any history over.** If the hardware you received is not in its factory packaging, you **MUST** add a `REF` under code `D` and note its status as `USD` under code `C`

Refurbished consoles likely have had components repaired. Even so, code creators **MUST NOT** guess which components are repaired/refurbished.

## Conflicting Codes & other considerations

Generally speaking, the "rules" for a VGCC are:

1. Codes **MUST NOT** conflict with one another under any circumstances. Any situation which would result in a conflict is a case where one or multiple codes must be adjusted, or is an unforeseen design flaw with the VGCC standard.
2. Codes in the [hardware identity](#hardware) field are considered intrinsic to the identity of the item being cataloged, and are never changed unless correcting an error. The attributes should be written according to their validity *at the time of manufacture*.
3. Codes in the [condition](#condition) field relate to the *present* condition of the item and should be updated often.
4. Codes **SHOULD** be constructed such that all pertinent information about a piece of hardware is present even if the [service history](#servicehistory) field is blank.
5. Ambiguities **SHOULD** be resolved in a way that is *least favorable to the value of the item*. In other words, if you're not sure if something is a swap or a mod, default to considering it a mod.
6. VGCCs are intended to classify individual items, not retail bundles. For instance, it is common for OEMs to sell different console bundles with different hardware, peripherals, and software. Each item in the bundle would have its own VGCC, not the bundle as a whole.

# Legal

## Safety/Security Considerations

Nothing prevents an unscrupulous seller from misrepresenting their product. A VGCC is intended for shorthand to describe an item and its history, not as a mark of safety or trustworthiness. The VGCR working group take no responsibility for its use by third parties or the accuracy of the information encoded.

## Warranty Disclaimer

The VGCC working group offers this standard and any related applications or services on a BEST EFFORT basis. It is not warrantied to be accurate, up to date, or fit for any particular purpose.

## Forks

As the VGCC is licensed under the GFDL (see next section), you are free to copy, modify, and share this document under those terms.

We specifically note that any related logos, artwork, and the names "Video Game Condition Code" and "Video Game Condition Report", and the acronyms VGCR and VGCC are owned by the VGCR working group and may not be used without the group's prior written consent.

**In brief: feel free to use this project as a base for something else, but you must call it something else and use your own artwork.**

## Copyright

Copyright 2021 - Mike Parks, Alexander Parrish, and contributors

Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts. A copy of the license is included in the file [LICENSE.MD](https://raw.githubusercontent.com/Karunamon/grc/master/LICENSE.md), located in the same repository as this standard doc.

{backmatter}

<reference anchor='goodtools-country' target='https://emulation.gametechwiki.com/index.php?title=GoodTools'>
    <front>
       <title>GoodTools Country Codes</title>
       <author><organization>Game Tech Wiki</organization></author>
       <date year='2019'/>
    </front>
</reference>

<reference anchor='POLA' target='https://en.wikipedia.org/w/index.php?title=Principle_of_least_astonishment'>
    <front>
       <title>Principle of least astonishment</title>
       <author><organization>Wikipedia</organization></author>
       <date month='January' year='2021'/>
    </front>
</reference>

<reference anchor='Neptune' target='https://hackinformer.com/2019/09/15/review-sega-neptune-mod-from-retrohacks-net/'>
    <front>
       <title>Review: Sega Neptune Mod from Retrohacks.net</title>
       <author name="V1RACY"><organization>Hack Informer</organization></author>
       <date month='September' day="15" year='2019'/>
    </front>
</reference>

