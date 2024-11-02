<p align ="center">
<img src="https://i.imgur.com/Uwno78D.png" width="680" height="150"/>
</p>

<p align ="center">Welcome to souls.fashion, a passion project created to make designing matching outfits in FromSoft's SoulsBorne game series easier.</p>

<p align ="center">The tool works by pulling the primary and secondary colors from a given set of images, then comparing them with an adjustable similarity threshold and secondary color weighting, essentially serving to enable searching through items by color.</p> 

<p align ="center">Deployed as a webpage and released as a public utility, the tool is primarily built using JavaScript; most of the filtration and search functions, as well as the color matching system, can be found in search_items.js. These javascript functions have dependencies on several JSON arrays built using included python scripts for accessibility, though rebuilding is not necessary to redeploy as all data is pulled from the existing JSON arrays.</p>



<p align ="center">
<img src="https://i.imgur.com/Jjvy4s3.png" width="680" height="100"/>
</p>

<p align="center">souls.fashion is hosted as a webapp at https://souls.fashion and therefore does not require customisation or installation to use by default. If you would like to create your own build using other files, the steps are as follows:</p>

<p align="center">There are two 7zip archives linked in the root directory, images and LegacyScripts, within which you will find several scripts that can be used to generate item colors, as well as icons, provided that the source images are placed within the appropriate /images/ folder. Their uses require previous scripts to be run in order, and are as follows:</p>

* *getcolor3.py*  - 3rd iteration of my color generation script, revised to eliminate detection of pure black and white, and to target secondary colors based on contrast. Pulls dominant and secondary colors from images located in the /images/ folder and returns their primary and secondary colors to colors_extracted.JSON. Note that this script is not perfect for the Souls series as the item icons are pre-rendered and have a tendency to show more black and white than they actually utilise in-game.
* *generate_items.py*  - generates the items shown in the search grid, using a combination of data from typed_items_for_web.JSON (dependent on items_for_web.JSON and colors_extracted.JSON) and image names + subtypes as defined within the /icons/ folder. Once colors have been generated the /images/ folders are redundant, but contain high-resolution base images labelled by item name from each game which you may use as you please.
* *200px-icon-generator.py*  - generates downscaled preview icons for the site for improved speed & resource management. Pulls source images from /images/ and returns them in a 200px format to /icons/ 
* *generate_colorimg.py*  - creates a new subfolder called 'processed-images' that will pull item icons from /images/ as well as colors from colors_extracted.JSON to create 500x500px images with a 120px bar showing the 3 most prominent colors displayed alongside eachother, as defined in colors_extracted.JSON (requires running getcolor3.py beforehand) 
* *categorise.py*  - pulls item details from items_for_web.JSON as well as their type from the subfolder of /images/, returning names, colors, icon locations and item types as a JSON array stored at typed_items_for_web.JSON.


<p align="center">
<img src="https://i.imgur.com/vT5b21S.png" width="680" height="100"/>
</p>

<p align="center">souls.fashion is leased under a Creative Commons Attribution-noncommercial license (CC BY-NC). 
You may alter, adapt, or build upon the source material, as long as attribution is given to the author (Psyopgirl) and the work is not used for profit or commercial purposes.</p>


<p align="center">
<img src="https://i.imgur.com/fAYVJlW.png" width="680" height="100"/>
</p>

> [ver 1.0.7] - Added outfit simulator to all games. Made weapons equippable in mainhand and offhand. Updated localstorage to use game-specific files so that presets and preset names, as well as outfit simulator content, do not carry over between games. 

> [ver 1.0.6] - Outfit simulator is live! Fixed an issue causing drag and drop function to break. Updated item icon names to match corrected names. 

> [ver 1.0.5] - *Optimised search function to utilise fewer resources, added versions to HTML and CSS to fix display issues with caching. Moved scripts and redundant files to off-project cloud storage to reduce build size. Merged search_items.js files into a single file to handle all games (pending Elden Ring migration due to ongoing development). Corrected duplicate and misspelt items in Elden Ring. Fixed some minor casing errors in DS1 and DS2.* 

> [ver 1.0.4] - *Added site metadata for SEO. Bloodborne supported. UI upgraded, mobile support improved. Links added for all DS1, DS2, DS3, Bloodborne, and Demon's Souls items. Color divs made individually selectable. Added "back to top" button for ease of use. Caching automatically enabled to save bandwidth.*

> [ver 1.0.3] - *Search by type function added for all games. Added feedback form. Elden Ring item links added. Mobile device support improved. Added favicons. Improved color database for the following items:* 

<details>

 <summary>Item List</summary>
  
- Albinauric Bow
- All Glintstone Crowns
- All-Knowing Set
- Ancient Meteoric Ore Great Sword
- Aristocrat Hat
- Ash Of War Scarab
- Astrologer Robe
- Azur Glintstone Staff
- Bandit Boots
- Banished Knight Set
- Banished Knight Shield
- Beast Champion Set
- Beast Crest Heater Shield
- Black Dumpling
- Black Flame Monk Armor
- Black Steel Greathammer
- Black Wolf Mask
- Black Knife Set
- Blackflame Monk Set
- Blaidd Armour
- Bloody Helice
- Blue Festive Hood
- Braided Cord Set
- Briar Helm
- Bull Goat Set
- Carian Knight Set
- Carian Sorcery Sword
- Chain Leggings
- Cerulean Scarab
- Claws Of Night
- Commoners Simple Garb
- Confessor Hood
- Consort Mask
- Consorts Mask
- Crimson Tear Scarab
- Crucible Tree Set
- Dancing Blade Of Ranah
- Dancer's Dress Altered
- Death Knight Set
- Death Ritual Spear
- Deaths Poker
- Depraved Perfumer Robe
- Dirty Chainmail
- Eclipse Great Crest Shield
- Eccentric Set
- Eleonora's Poleblade
- Exile Armor
- Exile Gauntlets
- Eye Surcoat
- Falling Star Beast Jaw
- Finger Robe
- Fingerprint Set
- Fire Knight Armour Altered
- Fire Monk Set
- Fire Prelate Armor Altered
- Fire Prelate Set
- Gelmir Knight Set
- Gargoyles Black Blade
- Gaius's Armor
- Glintstone Scarab
- Glintstone Staff
- Godrick Knight Greaves
- Grave Bird Set
- Gravekeeper Cloak
- Great Bow
- Great Horned Headband
- Great Katana
- Great Stars
- Haligtree Knight Set
- Horned Warrior Sword
- Hoslow Petal Whip
- Iji’s Mirror Helm
- Igon Set
- Inverted Hawk Heater Shield
- Iron Greatsword
- Knight Helm / Knight Set
- Large Leather Shield
- Lazuli Glintstone Sword
- Leather Armour
- Lionel Set
- Lionel's Armor Altered
- Lordsword’s Shield
- Longsword
- Lord Of Blood's Robe Altered
- Lusat Staff
- Magma Worm Scale Sword
- Malenia Set
- Marionette Soldier Armor
- Maternal Staff
- Mausoleum Surcoat
- Messmer Soldier Spear
- Meteoric Ore Blade
- Meteorite Staff
- Monk’s Flamemace
- Moonveil
- Mushroom Set
- Night Rider Flail
- Night Rider Glaive
- Octopus Head
- Omen Set
- Pata
- Perfumer Robe
- Pickaxe
- Pike
- Prince Of Death’s Staff
- Prisoner Iron Mask
- Queen's Bracelets
- Raging Wolf Armour
- Raptor’s Black Feathers
- Red Branch Shortbow
- Reduvia
- Ringed Finger
- Ronin Set
- Ronin's Set
- Rotten Battle Hammer
- Rotten Crystal Staff
- Royal Knight Helm/Set
- Royal Remains Set
- Ruler’s Robe
- Scarlet Tabard
- Scaled Set
- Serpent Crest Shield
- Serpent Hunter
- Shining Horn Headband
- Skeletal Mask
- Spellblade’s Pointed Hat
- Spirit Sword
- Spiked Palisade Shield
- Sun Realm Shield
- Sword Of Night And Flame
- Thiollier Set
- Travelling Maiden Robe
- Traveler's Gloves
- Troll Knight Sword
- Twinned Armour
- Uchigatana
- Varre Bouquet
- Velvet Sword Of St Trina
- Verdigris Set
- Veteran's Prosthesis
- Warhawk’s Talon
- White Reed Set
- Whip
- Winged Great Horn
- Zweihander

</details>

> [ver 1.0.2] - *Elden Ring, Demon's Souls, and Dark Souls 1-3 supported. Working on renaming images to enable Bloodborne support.*

> [ver 1.0.1] - *added functionality for searching items by name and color, currently only Elden Ring is supported.* 

> [ver 1.0.0] - *First public release! Color database created, pages for each game created, and index file added with links for each game.*

Upcoming changes:
- [x] Add mobile device support
- [x] Create a community discord server
- [x] Optimise images for file size
- [x] Pull data from weapons as array to use in outfit simulator
- [x] Pull talisman data to use in outfit simulator
- [ ] Integrate API to serve images and item data
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