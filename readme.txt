Welcome to souls.fashion, a passion project I created to make designing outfits (specifically for Elden Ring, but adapted to other Souls games) easier. 

The tool itself primarily utilises JavaScript, particularly most of the functions can be found in search_items.js. It is, however, dependent on several python scripts in order to build JSON files and serve data to the web pages:

In each sub-directory of /pages/ you will find several scripts that can be used to generate item colors. Their uses are as follows:
getcolor3.py - 3rd iteration of my color generation script. Pulls dominant and secondary colors from images located in the /images/ folder and returns their primary and secondary colors to colors_extracted.json
generate_items.py - generates the items used by the web interface, using a combination of data from colors_extracted.json and image names + subtypes as defined within the /images/ folder. 
200px-icon-generator.py - generates the preview icons for the site so it loads faster and uses fewer resources while open. pulls images from /images/ and returns them in a 200px format to /icons/ 
generate_previews2.py - creates a new subfolder called 'processed-images' that will pull images from /images/ as well as colors from colors_extracted.json to create 500x500px images with a 120px bar showing the 3 most prominent colors from the given images, as defined in colors_extracted.json (requires running getcolor3.py beforehand) 

All images are sorted by item type. Hopefully I can find a way to implement this into the search function in future. 
-psyopgirl