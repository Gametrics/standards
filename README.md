# Game Repair Code Project

[![License](https://img.shields.io/badge/License-GFDLv1.3-blue)](https://www.gnu.org/licenses/fdl-1.3.en.html) [![Last commit](https://img.shields.io/github/last-commit/karunamon/grc)](https://github.com/Karunamon/grc/commits/master) [![Latest version](https://img.shields.io/badge/Last%20Version-DRAFT-red)](http://gamerepair.codes) [![Discord](https://img.shields.io/discord/709655247357739048?logo=discord)](https://discord.gg/XF6dK2S)

The Game Repair Code (GRC) is a [Geek Code](https://github.com/telavivmakers/geek_code)-like system for efficiently storing and sharing the information about a piece of game hardware or software. It is intended for use by collectors, retailers, enthusiasts, or anyone in between with an interest in video game paraphernalia.

This repository contains the source Markdown document for the actual standard doc, which is maintained at [https://gamerepair.codes](https://gamerepair.codes).

The GRC is an open standard licensed under the [GNU Free Documentation License](https://www.gnu.org/licenses/fdl-1.3.en.html). To propose changes to the standard, please open a pull request here.

## What is it?

A GRC is used to indicate the most pertinent information about a video game device, including its brand, revision, and repair/modification history. An example would be:

```
GRC1|BNINT,AOEM,FNGC,RU,TCON,CPLA,V001|PUSD,DSHCSMKTXTSmoking_home,MCHPLED,ESHLPRTDSK|20200829MCHPHyperBoot,20200829MLEDCtrlr,20200829SSHLOEMTop,20200829SSHLOEMHsd,20211224RMSCMHyperBoot,20211224SMSCOEMCtrlport3,20211224SDDA3RD|
```

What does this code tell us? It's for a Nintendo Gamecube, OEM, United States version, DOL-001, in platinum color. It is in used condition, and has had damage to the shell and smoke damage from being in a smoking home. In the past, it has had repairs made to the shell, ports, and disk drive. It has had a HyperBoot modchip and non-stock LEDs installed. The modchip and LEDs were installed on August 29th, 2020. On the same day, the shell and data port cover were replaced with identical OEM parts. Later in 2021, the modchip was repaired, as was controller port 3 and the disk drive assembly.

All of that information was condensed into bit more than a single line of text - and that is the power of the GRC. This is information that is valuable to have on hand, either as a collector or a retailer.

## But isn't this hard to read?
The GRC is a computers-first code, meant to be read programatically by applications, but it is incidentally readable by humans. In the real world, we envision the GRC compressed and encoded into a QR code format, something that could be easily scanned and decoded by an application. In fact, such an application is part of this project and is under active development.

![Encoded GRC example](https://i.imgur.com/zC7B4mU.png)

Imagine this on a curator's shelf, or an eBay or Craigslist posting. Lots of information, very small space. That is the goal.

## How do I make one?
There will be an application, web and mobile both, to assist with this process in the future. For now, [read through the v1 RFC](http://gamerepair.codes) and simply construct each field as prompted. The spec answers many questions and considers many edge cases - but in the event that it doesn't, and you find something that's been overlooked, please consider [letting us know on Discord](https://discord.gg/XF6dK2S) or opening a pull request here.
