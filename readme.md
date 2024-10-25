<p align ="center">
<img src="https://i.imgur.com/Uwno78D.png" width="680" height="150"/>
</p>

<p align ="center">Welcome to [souls.fashion](https://souls.fashion), a passion project created to make designing matching outfits in FromSoft's SoulsBorne game series easier.

The tool works by pulling the primary and secondary colors from a given set of images, then comparing them with an adjustable similarity threshold and secondary color weighting, essentially serving to enable searching through items by color. 

Deployed as a webpage and released as a public utility, the tool is primarily built using JavaScript; most of the filtration and search functions, as well as the color matching system, can be found in search_items_*gamename*.js. These javascript functions have dependencies on several JSON arrays built using included python scripts for accessibility, though rebuilding is not necessary to redeploy as all data is pulled from the existing JSON arrays.</p>



<p align ="center">
<img src="https://i.imgur.com/Jjvy4s3.png" width="680" height="100"/>
</p>

<p align="center">souls.fashion is hosted as a webapp at https://souls.fashion and therefore does not require customisation or installation to use by default. If you would like to create your own build using other files, the steps are as follows:

In each sub-directory of /pages/ you will find several scripts that can be used to generate item colors, as well as icons, provided that the source images are provided in the /images/ folder. Their uses require previous scripts to be ran in order, and are as follows:

* *getcolor3.py*  - 3rd iteration of my color generation script, revised to eliminate detection of pure black and white, and to target secondary colors based on contrast. Pulls dominant and secondary colors from images located in the /images/ folder and returns their primary and secondary colors to colors_extracted.JSON. Note that this script is not perfect for the Souls series as the item icons are pre-rendered and have a tendency to show more black and white than they actually utilise in-game.
* *generate_items.py*  - generates the items shown in the search grid, using a combination of data from typed_items_for_web.JSON (dependent on items_for_web.JSON and colors_extracted.JSON) and image names + subtypes as defined within the /icons/ folder. Once colors have been generated the /images/ folders are redundant, but contain high-resolution base images labelled by item name from each game which you may use as you please.
* *200px-icon-generator.py*  - generates downscaled preview icons for the site for improved speed & resource management. Pulls source images from /images/ and returns them in a 200px format to /icons/ 
* *generate_previews2.py*  - creates a new subfolder called 'processed-images' that will pull item icons from /images/ as well as colors from colors_extracted.JSON to create 500x500px images with a 120px bar showing the 3 most prominent colors displayed alongside eachother, as defined in colors_extracted.JSON (requires running getcolor3.py beforehand) 
* *categorise.py*  - pulls item details from items_for_web.JSON as well as their type from the subfolder of /images/, returning names, colors, icon locations and item types as a JSON array stored at typed_items_for_web.JSON.</p>
<p align="center">
<img src="https://i.imgur.com/vT5b21S.png" width="680" height="100"/>
</p>

<p align="center">souls.fashion is leased under a Creative Commons Attribution-noncommercial license (CC BY-NC). 
You may alter, adapt, or build upon the source material, as long as attribution is given to the author (Psyopgirl) and the work is not used for profit or commercial purposes.</p>


<p align="center">
<img src="https://i.imgur.com/fAYVJlW.png" width="680" height="100"/>
</p>

[ver 1.0.1] - *added functionality for searching items by name and color, currently only Elden Ring is supported.* 

> [ver 1.0.2] - *Elden Ring, Demon's Souls, and Dark Souls 1-3 supported. Working on renaming images to enable Bloodborne support.*

> [ver 1.0.3] - *search by type function added for all games. mobile device support improved.*

Upcoming changes:
- [x] Add mobile device support
- [x] Create a community discord server
- [ ] Pull textures from games to get better color values
- [ ] Implement an outfit simulator
- [ ] Highlight an item above the grid when an item is selected
- [ ] Add a reset button for color, similarity threshold and secondary color weight


<p align="center">
<img src="https://i.imgur.com/606munG.png" width="680" height="100"/>
</p>

<p align="center">

[@hoycid](https://github.com/hoycid), for providing search by type functionality, UI improvements and mobile device support as well as ongoing bugfixes for my terrible code.

[@florabtw](https://github.com/florabtw), creator of [scape.fashion](https://scape.fashion), a tool which greatly inspired this one. 

[FromSoftware](https://www.fromsoftware.jp/ww/), developers of the amazing games these tools are used for.</p>

</p>