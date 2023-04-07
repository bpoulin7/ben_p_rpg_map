# Changelog

**v1.0**  
Name: RPGmap  
added - map (nested lists)  
added - global variables row and col  
added - contiuous play  
added - movement and quit game options  
added - movement() function  
added - cardinal direction options for movement()  
fixed - movement so player can not walk off "map"  

**v2.0**  
Name: Dawn of Civilization  
added - dictionary for map tiles with descriptions  
added - dictionary of civilizations  
added - dictionary of map objects  
added - dictionary of inventory items  
added - inventory as null list  
added - list of actions printed before input  
added - weighted chance of finding map objects after moving  
  
*v2.1*  
added - simple starting message  
added - line spaces between text in console  
added - placeholder text for enemy/ally interaction  
  
**v3.0**  
added - external map file  
added - game option to open map  
moved - map tile, object, and item dictionaries to individual modules  

**v4.0**  
fixed - account for invalid input when asking to quit  
added - function for requesting to add item to inventory, accounting for invalid user input  
added - temporary win condition closing the game when reaching egypt  
added - redundant try/except/else/finally statement for assignment  
added - formatting to changelog  

## To Do:  
 - remove brackets and quotation marks from objects and items
 - have interactions with allies and enemies
 - make traversing wasteland more difficult
 - proper victory screen