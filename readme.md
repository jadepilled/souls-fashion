![souls.fashion header](https://i.imgur.com/Uwno78D.png)

Welcome to souls.fashion, a passion project created to make designing outfits in FromSoft's SoulsBorne game series easier.

The tool itself primarily utilises JavaScript, particularly most of the functions can be found in search_items.js. It is, however, dependent on several python scripts in order to build JSON files and serve data to the web pages.

![installation](https://i.imgur.com/Jjvy4s3.png)

souls.fashion is hosted as a web-app at https://souls.fashion and therefore does not require customisation or installation to use by default. If you would like to create your own build using other files, the steps are as follows:

In each sub-directory of /pages/ you will find several scripts that can be used to generate item colors. Their uses are as follows:
getcolor3.py - 3rd iteration of my color generation script. Pulls dominant and secondary colors from images located in the /images/ folder and returns their primary and secondary colors to colors_extracted.json
generate_items.py - generates the items used by the web interface, using a combination of data from colors_extracted.json and image names + subtypes as defined within the /images/ folder. 
200px-icon-generator.py - generates the preview icons for the site so it loads faster and uses fewer resources while open. pulls images from /images/ and returns them in a 200px format to /icons/ 
generate_previews2.py - creates a new subfolder called 'processed-images' that will pull images from /images/ as well as colors from colors_extracted.json to create 500x500px images with a 120px bar showing the 3 most prominent colors from the given images, as defined in colors_extracted.json (requires running getcolor3.py beforehand) 

![license](https://i.imgur.com/vT5b21S.png)
souls.fashion is leased under a Creative Commons Attribution-noncommercial license (CC BY-NC). 
You may alter, adapt, or build upon the source material, as long as attribution is given to the author (Psyopgirl) and the work is not used for profit or commercial purposes.

![changelog](https://i.imgur.com/606munG.png)

![special thanks](https://i.imgur.com/606munG.png)
@hoycid, for providing search by type functionality, UI improvements and mobile device support as well as ongoing bugfixes for my terrible code.
FromSoftware, for developing the amazing games these tools are used for.

-psyopgirl