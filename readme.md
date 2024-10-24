<p align ="center">
<img src="https://i.imgur.com/Uwno78D.png" width="680" height="150" border="10"/>
</p>

Welcome to souls.fashion, a passion project created to make designing outfits in FromSoft's SoulsBorne game series easier.

The tool itself primarily utilises JavaScript, particularly most of the functions can be found in search_items.js. It is, however, dependent on several python scripts in order to build JSON files and serve data to the web pages.

<p align ="center">
<img src="https://i.imgur.com/Jjvy4s3.png" width="680" height="100" border="10"/>
</p>

souls.fashion is hosted as a web-app at https://souls.fashion and therefore does not require customisation or installation to use by default. If you would like to create your own build using other files, the steps are as follows:

In each sub-directory of /pages/ you will find several scripts that can be used to generate item colors, as well as icons, provided that the source images are provided in the /images/ folder. Their uses are as follows:

* *getcolor3.py*  - 3rd iteration of my color generation script. Pulls dominant and secondary colors from images located in the /images/ folder and returns their primary and secondary colors to colors_extracted.json
* *generate_items.py*  - generates the items used by the web interface, using a combination of data from colors_extracted.json and image names + subtypes as defined within the /images/ folder. 
* *200px-icon-generator.py*  - generates the preview icons for the site so it loads faster and uses fewer resources while open. pulls images from /images/ and returns them in a 200px format to /icons/ 
* *generate_previews2.py*  - creates a new subfolder called 'processed-images' that will pull images from /images/ as well as colors from colors_extracted.json to create 500x500px images with a 120px bar showing the 3 most prominent colors from the given images, as defined in colors_extracted.json (requires running getcolor3.py beforehand) 
* *categorise.py*  - pulls item details from items_for_web.json as well as their type from the subfolder of /images/, returning colors and item types as a JSON array.
<p align="center">
<img src="https://i.imgur.com/vT5b21S.png" width="680" height="100" border="10"/>
</p>

souls.fashion is leased under a Creative Commons Attribution-noncommercial license (CC BY-NC). 
You may alter, adapt, or build upon the source material, as long as attribution is given to the author (Psyopgirl) and the work is not used for profit or commercial purposes.

<p align="center">
<img src="https://i.imgur.com/fAYVJlW.png" width="680" height="100" border="10"/>
</p>

> [ver 1.0.1] - *added functionality for searching items by name and color, currently only Elden Ring is supported.* 

> [ver 1.0.2] - *Elden Ring, Demon's Souls, and Dark Souls 1-3 supported. Working on renaming images to enable Bloodborne support.*

> [ver 1.0.3] - *search by type function added for all games. mobile device support improved.*

Upcoming changes:
- [x] Add mobile device support
- [ ] Pull textures from games to get better color values
- [ ] Create a community discord server
- [ ] Implement an outfit simulator
- [ ] Highlight an item above the grid when an item is selected
- [ ] Add a reset button for color, similarity threshold and secondary color weight

<p align="center">
<img src="https://i.imgur.com/606munG.png" width="680" height="100" border="10"/>
</p>

[@hoycid](https://github.com/hoycid), for providing search by type functionality, UI improvements and mobile device support as well as ongoing bugfixes for my terrible code.

FromSoftware, for developing the amazing games these tools are used for.

</p>