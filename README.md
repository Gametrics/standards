# Video Game Condition Code Project

[![License](https://img.shields.io/badge/License-GFDLv1.3-blue)](https://www.gnu.org/licenses/fdl-1.3.en.html) [![Last commit](https://img.shields.io/github/last-commit/karunamon/grc)](https://github.com/Karunamon/grc/commits/master) [![Latest version](https://img.shields.io/badge/Last%20Version-DRAFT-red)](http://gamerepair.codes) [![Discord](https://img.shields.io/discord/709655247357739048?logo=discord)](https://discord.gg/XF6dK2S)

The Video Game Condition Code (VGCC) is a [Geek Code](https://github.com/telavivmakers/geek_code)-like system for efficiently storing and sharing the information about a piece of game hardware or software. It is intended for use by collectors, retailers, enthusiasts, or anyone in between with an interest in video game paraphernalia.

This repository contains the source Markdown document for the actual standard doc, which is maintained at [https://gamerepair.codes](https://gamerepair.codes).

The VGCC is an open standard licensed under the [GNU Free Documentation License](https://www.gnu.org/licenses/fdl-1.3.en.html). To propose changes to the standard, please open a pull request here.

## What is it?

A VGCC is used to indicate the most pertinent information about a video game device, including its brand, revision, and repair/modification history. An example would be:

```
VGCC1|BNINT,AO,FNGC,RU,TCON,MNGC,CIND,VDOL-001,SDS315060768,I|PUSD,DSHCSMKTXTSmoking_home,MCHPLED,ESHLPRTDDA,U|20200829MCHPHyperBoot,20200829MLEDCtrlr,20200829OSHLTop,20200829OSHLHsd_cover,20211224RCHPHyperBoot_wiring,20211224OPRTtrlport3,20211224TDDA|
```

What does this code tell us? It's for an OEM Nintendo Gamecube console, United States version, DOL-001, in indigo color. It is in used condition, and has had damage to the shell and smoke damage from being in a smoking home. Its serial number is DS315060768. In the past, it has had repairs made to the shell, ports, and disk drive. It has a HyperBoot modchip and non-stock LEDs installed. The modchip and LEDs were installed on August 29th, 2020. On the same day, the shell and data port cover were replaced with identical OEM parts. Later in 2021, the modchip was repaired, controller port 3 was replaced with an OEM part, and the disc drive assembly was replaced with a third party version.

All of that information was condensed into bit more than a single line of text; that is the power of the VGCC.

## But isn't this hard to read?

The VGCC is a computers-first code, meant to be read programatically by applications, but it is incidentally readable by humans. In the real world, we envision the VGCC compressed and encoded into a QR code, something that could be easily scanned and decoded by an application. In fact, such an application is part of this project and is under active development.

![Encoded GRC example](https://i.imgur.com/zC7B4mU.png)

Imagine this on a curator's shelf, or an eBay or Craigslist posting. Lots of information, very small space. That is the goal.

## How do I make one?

There will be an application, web and mobile both, to assist with this process in the future. For now, [read through the v1 RFC](http://gametrics.org) and simply construct each field as prompted. The spec answers many questions and considers many edge cases - but in the event that it doesn't, and you find something that's been overlooked, please consider [letting us know on Discord](https://discord.gg/XF6dK2S) or opening a pull request here.
