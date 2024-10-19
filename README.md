# Sokoban

Sokoban Anniversary Edition. Includes Dizzy Warehouse (1996), Lens (1998) and Fortnoks (1999).

* Live demo: https://joric.github.io/sokoban

## Trivia

* The original Dizzy Warehouse and Lens games have unsolvable level 16.
* Fortnoks makes level 16 solvable by removing the wall at (5,2).
* There are two Fortnoks versions in the wild, with sound, and without sound.
* All games allow level switching with the Z and X keys while holding Shift.
* Sources are somewhat incomplete, most resource data files are pre-baked.
* Dizzy Warehouse was popularized by the Thomas Pynchon's book "Bleeding Edge" (2003).

## Games

### Dizzy Warehouse

* Walls, gems, game panel, 16x16 font use original graphics.
* Dizzy animation is original but inspired by "Fast Food" (Codemasters, 1989).
* Most of the logo graphics is from "Dizzy III - Fantazy World" (Codemasters, 1989).
* Bang animation is from "West Bank" (Gremlin Graphics, 1985).

### Lens

PC graphics was packed using `splink.exe` that links Autodesk Animator sprites (.cel) together.
It doesn't have sources, but the format is simple.
It's just width, height, data size (2 bytes each, so 6 bytes) and bitmap data, one byte per pixel.
Palette data is stored independently.

Lens uses various sources, sometimes with an altered (rotated) palette.

* Walls - orignal hand-painted grey as a stone wall (there are several sprites), then color-remapped.
* Gems - probably original (might be from an obscure DOS vectorballs intro or a DOS game).
* Ghost - from "Magicland Dizzy" (PC, The Haunted Swamp, https://yolkfolk.com/games/magicland-dizzy/)
* Font - from "Magicland Dizzy" (PC, https://youtu.be/aJp4OrPsJmI?t=1472)

### Fortnoks

* Walls - original, hand-painted.
* Font and logo - original, rendered in 3D Studio, DOS version (1990).
* Gems - gem sprites from Xixit (1995) by Optik Software, Inc.

#### Music

The Fortnoks music is from Duke Nukem 3D, called "Grab Bag" by Lee Jackson (download [here](https://leejacksonaudio.lbjackson.com/GrabbagOriginalVersionMIDI1.1.zip)).
The archive contains two files, GM1 and GS1, 28956 and 28961 bytes respectively.
The game file (FORTNOKS.MID) is smaller (14287 bytes), probably grabbed directly from the game resources.
It is subject to copyright, so it requires disclaimers:

`Grabbag (Duke Nukem Theme) - composed by Lee Jackson. Copyright (©)1995 Lee Jackson.  All rights reserved.`

```
Duke Nukem is (©) 1999-2011 - Gearbox Software, LLC. All rights reserved.
Duke Nukem, the Duke Nukem nuclear symbol, Duke Nukem Forever, Gearbox
Software and the Gearbox logo are registered trademarks of Gearbox Software,
LLC in the U.S. and/or other countries and used here under license.
```

Check out some good remixes:

* https://www.doomworld.com/forum/topic/89375-legacy-of-grabbag-duke-nukem-theme-metal-medley/
* https://darkman007.bandcamp.com/track/duke-nukem-3d-grabbag-metal-cover

I am not sure why it used Xixit sprites but not the music. It is available in s3m, rippable with ripper4.

Youtube: https://youtu.be/zQZCZ0GGZds (they are not used here).

#### Sound Effects

Fortnoks uses [BSWB (Bells, Whistles and Sound Boards)](https://www.phatcode.net/downloads.php?id=170) library for sounds.
GDM module format is BSWB proprietary and cannot be converted back.
It also includes sound samples, namely (enum value is sample number minus 1 in hex):

id | file | name | hex
---|---|---|---
17 | Yeah.wav | end_level | 0x10
18 | Brlrlrlm.wav | place_gem | 0x11
19 | hahaha.wav | fail_level | 0x12
20 | tumtum.wav | move_gem | 0x13
21 | Builthit.wav | select_item | 0x14
22 | Gbelev02.wav | move_in_menu, activate_menu | 0x15
23 | Item15.wav | deactivate_menu | 0x16

Samples use the original GDM (General Digital Music) format which is similar to S3M modules.
The easiest way to extract samples from it is to use existing converters/players, e.g. MegaZeux.
MegaZeux has gdm2s3m converter:

* https://www.digitalmzx.com/wiki/GDM
* https://github.com/AliceLR/megazeux/tree/master/contrib/gdm2s3m

After converting FORTNOKS.GDM to .s3m you can open it in OpenMPT and save samples as .wav.

## Maps

All 20 16x10 maps in these games are original (probably mostly because of the screen size limitation at the time).

* There are original "pusher" maps on GitHub: https://github.com/begoon/sokoban-maps

## Solvers

The main breakththrough is using ID (Iterative Deepening) A-star instead of a simple A-star.

* https://sokoban.dk/wp-content/uploads/2016/02/Timo-Virkkala-Solving-Sokoban-Masters-Thesis.pdf

### YASS

See [YASS solver](./tools/YASS/) directory for details (it is used in this game as a WASM binary).

YASS (Yet Another Sokoban Solver) is a GUI Sokoban with many features.
Works with YASC (Yet Another Socoban Clone). It is truly great and solves 16x10 maps instantly.

* https://sourceforge.net/projects/sokobanyasc

Output notation uses just 8 characters.

* the characters "lurd" (lowercase) indicate the movement of the player to the left, up, right, down.
* the symbols "LURD" (in uppercase) indicate that the player pushes the box left, up, right, down.

### Festival

Festival is a Sokoban solver written by Yaron Shoham. It is based on the novel FESS search algorithm (presented in CoG 2020).
Festival is the first program that solves all 90 levels of the XSokoban benchmark. It's slower than YASS.

* https://festival-solver.site

Also this page has a bunch of solvers, including Prolog Solver Generator (that's really slow):

* https://www.joriswit.nl/sokoban/en/solvers.htm
