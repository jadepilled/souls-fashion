<p align ="center">
<img src="https://i.imgur.com/Uwno78D.png" width="680" height="150"/>
</p>

<p align ="center">Welcome to souls.fashion, a passion project created to make designing matching outfits in FromSoft's SoulsBorne game series easier.</p>

<p align ="center">The tool works by pulling the primary and secondary colors from a given set of images, then comparing them with an adjustable similarity threshold and secondary color weighting, essentially serving to enable searching through items by color.</p> 

<p align ="center">Deployed as a webpage and released as a public utility, the tool is primarily built using JavaScript; most of the filtration and search functions, as well as the color matching system, can be found in search_items_*gamename*.js. These javascript functions have dependencies on several JSON arrays built using included python scripts for accessibility, though rebuilding is not necessary to redeploy as all data is pulled from the existing JSON arrays.</p>



<p align ="center">
<img src="https://i.imgur.com/Jjvy4s3.png" width="680" height="100"/>
</p>

<p align="center">souls.fashion is hosted as a webapp at https://souls.fashion and therefore does not require customisation or installation to use by default. If you would like to create your own build using other files, the steps are as follows:</p>

<p align="center">In each sub-directory of /pages/ you will find several scripts that can be used to generate item colors, as well as icons, provided that the source images are provided in the /images/ folder. Their uses require previous scripts to be ran in order, and are as follows:</p>

* *getcolor3.py*  - 3rd iteration of my color generation script, revised to eliminate detection of pure black and white, and to target secondary colors based on contrast. Pulls dominant and secondary colors from images located in the /images/ folder and returns their primary and secondary colors to colors_extracted.JSON. Note that this script is not perfect for the Souls series as the item icons are pre-rendered and have a tendency to show more black and white than they actually utilise in-game.
* *generate_items.py*  - generates the items shown in the search grid, using a combination of data from typed_items_for_web.JSON (dependent on items_for_web.JSON and colors_extracted.JSON) and image names + subtypes as defined within the /icons/ folder. Once colors have been generated the /images/ folders are redundant, but contain high-resolution base images labelled by item name from each game which you may use as you please.
* *200px-icon-generator.py*  - generates downscaled preview icons for the site for improved speed & resource management. Pulls source images from /images/ and returns them in a 200px format to /icons/ 
* *generate_previews2.py*  - creates a new subfolder called 'processed-images' that will pull item icons from /images/ as well as colors from colors_extracted.JSON to create 500x500px images with a 120px bar showing the 3 most prominent colors displayed alongside eachother, as defined in colors_extracted.JSON (requires running getcolor3.py beforehand) 
* *categorise.py*  - pulls item details from items_for_web.JSON as well as their type from the subfolder of /images/, returning names, colors, icon locations and item types as a JSON array stored at typed_items_for_web.JSON.


<p align="center">
<img src="https://i.imgur.com/vT5b21S.png" width="680" height="100"/>
</p>

<p align="center">souls.fashion is leased under a Creative Commons Attribution-noncommercial license (CC BY-NC). 
You may alter, adapt, or build upon the source material, as long as attribution is given to the author (Psyopgirl) and the work is not used for profit or commercial purposes.</p>


<p align="center">
<img src="https://i.imgur.com/fAYVJlW.png" width="680" height="100"/>
</p>

>[ver 1.0.1] - *added functionality for searching items by name and color, currently only Elden Ring is supported.* 

> [ver 1.0.2] - *Elden Ring, Demon's Souls, and Dark Souls 1-3 supported. Working on renaming images to enable Bloodborne support.*

> [ver 1.0.3] - *search by type function added for all games. mobile device support improved. Improved color database for the following items:* 
<details>
  <summary>Item List</summary>
+ Scaled Set  
+ Ronin's Set  
+ All Knowing Set  
+ Banished Knight Set  
+ Carian Knight Set  
+ Knight Helm / Knight Set  
+ Vagabond Knight Helm / Set  
+ Prisoner Iron Mask  
+ Exile Gauntlets  
+ Fire Prelate Armor (Altered)  
+ Gelmir Knight Set  
+ Uchigatana  
+ Veteran's Prosthesis  
+ Black Knife Set  
+ Godrick Knight Greaves  
+ Haligtree Knight Set  
+ Eleonora's Poleblade  
+ Verdigris Set  
+ Lionel's Armor (Altered)  
+ Serpent Crest Shield  
+ Ants Skull Plate  
+ Gargoyles Black Blade  
+ Death Knight Set  
+ Dancer's Dress (Altered)  
+ Whip  
+ Black Steel Greathammer  
+ Lord of Blood's Robe (Altered)  
+ Meteoric Ore Blade  
+ Gaius's Set  
+ Maternal Staff  
+ Omen Set  
+ Cerulean Scarab  
+ Ascetic Set  
+ Preceptors Big Hat  
+ Consorts Mask  
+ Aristocrat Hat  
+ Euporia  
+ Deaths Poker  
+ Commoners Simple Garb  
+ Large Leather Shield  
+ Travelers Gloves  
+ Riveted Wooden Shield  
+ Glintstone Scarab  
+ Crucible Tree Set  
+ Great Katana  
+ Royal Knight Helm/Set  
+ Ash of War Scarab  
+ Meteorite Staff  
+ Astrologer Set  
+ Great Stars  
+ Banished Knight Shield  
+ Depraved Perfumer Robe  
+ Iji’s Mirror Helm  
+ Shining Horn Headband  
+ Beast Crest Heater Shield  
+ Mushroom Set  
+ Blackflame Monk Set  
+ Bloodhound Knight Set  
+ Great Horned Headband  
+ Travelling Maiden Set  
+ Sun Realm Shield  
+ Spiked Palisade Shield  
+ Red Branch Shortbow  
+ Eye Surcoat  
+ Dirty Chainmail  
+ Lusat Staff  
+ Pike  
+ Death Ritual Spear  
+ Nightrider Glaive  
+ Nightrider Flail  
+ Velvet Sword of St Trina  
+ Bloody Helice  
+ Claws of Night  
+ Iron Greatsword  
+ Dancing Blade of Ranah  
+ Messmer Soldier Spear  
+ Zweihander  
+ Ancient Meteoric Ore Great Sword  
+ Rotten Crystal Staff  
+ Chain Leggings  
+ Finger Robe  
+ Spirit Sword  
+ Glintstone Staff  
+ Prince of Death’s Staff  
+ Spellblade’s Pointed Hat  
+ Spellblade's Gloves  
+ Beast Champion Set  
+ Black Wolf Mask  
+ Fire Knight Armour Altered  
+ Blaidd Set  
+ Warhawk’s Talon  
+ Magma Wyrm Scalesword  
+ Igon Set  
+ Fingerprint Set  
+ Leather Armour  
+ Sword of Night and Flame  
+ Fire Prelate Set  
+ Blue Festive Hood  
+ Mausoleum Surcoat  
+ Ronin Set  
+ Hoslow Petal Whip  
+ Ruler’s Robe and Mask  
+ Bandit Boots/Garb  
+ Fire Monk Set  
+ White Reed Set  
+ Longsword  
+ Winged Greathorn  
+ Scarlet Tabard  
+ Bloodhound Knight Set  
+ Perfumer Robe  
+ Marionette Soldier Armor  
+ Braided Cord Set  
+ Albinauric Bow  
+ Briar Helm  
+ Black Dumpling  
+ Lazuli Glintstone Sword  
+ Great Stars  
+ Eclipse Crest Great/Heater Shield  
+ Fallingstar Beast Jaw  
+ Pickaxe  
+ Carian Sorcery Sword  
+ Gravebird Set  
+ Troll Knight Sword  
+ Lionel Set  
+ Gravekeeper Cloak  
+ Ringed Finger  
+ Pata  
+ Errant Sorcerer Robe Altered  
+ Thiollier's Set  
+ Raptor’s Black Feathers  
+ Confessor Set  
+ Eccentric Set  
+ Inverted Hawk Heater Shield  
+ Horned Warrior Sword  
+ Greatbow  
+ Lion Greatbow  
+ Monk’s Flamemace  
+ Skeletal Mask  
+ Queens Bracelets  
+ Twinned Set  
+ Serpent Hunter  
+ Dragon Hunter Great Katana  
+ Octopus Head  
+ Lordsword’s Shield  
+ Bull Goat Set  
+ Crimson Tear Scarab  
+ Azur Glintstone Staff  
+ Rotten Battle Hammer  
+ Varre Bouquet  
+ Consort Mask  
+ Reduvia  
+ All Glintstone Crowns  
+ Raging Wolf Set  
+ Royal Remains Set  
+ Moonveil  
+ Malenia Set  
</details>

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