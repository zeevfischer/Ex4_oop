
# Ex4_OOP  

## **Cours info**  
Prof. Boaz Ben-Moshe  
Submitted by: Liav Levi , Eden mor , zeev fisher  

---

## **Explanation**
This repository contains an implementation of Pokemon game!!  
The game is being played on a directed weighted graph that is implemented in Python
this is also based on the last assignment Ex3_oop wich can be found in this github account  

---

### How to play the game

This is an non interactiv game while running the game a pre given server will suply the program with the folowing infurmation  
* a graph to work on 
* a number of agents and there infurmation 
* a number of pokemons and there infurmation  
The pokemons are located on the graph’s (directed) edges, therefore, the agent needs to take the proper edge to “grab” the pokemon while each pokemon contains a value of points.
The goal is to maximize the overall sum of points of the “grabbed” pokemons at a given limited time.

---

### How to run the game
There are tew main ways to start the game 
#### option 1 
step 1: downlode the folowing content of this reposetor to your laptop  
step 2: place all the fille in a progect folder ass is note changnig any fill or order can couses problems  
make shore to locate the server and the data folder in the same folder  
step 3: open the terminal in your work space (pycharm for exampel)  
step 4: run the folowing: python Ex4.py 11   

#### option 2
folow step 1,2 above  
make shore to locate the server and the data folder in the same folder  
step 3: run cmd in your folder  
step 4: enter python Ex4.py 11

NOTE: in step: 4 "11" is the stage number and can alsow be 0-15  
NOTE: the terminal path way shold match your curent worck space location  
NOTE: The folowing picture a fix to a comeon problem (ModuleNotFoundError: No module named 'pygame')  
![how to ](https://user-images.githubusercontent.com/92921822/148664097-ba1eb39c-abf7-48ff-9049-4faac231f522.jpg)
### how to fix:
step 1: pip install pygame  
step 2: a update command may be sugjested (optinal)  
step 3: run python Ex4.py 11 and enjoy  

---

### for more information about our implementation of the game check out our wiki at:
https://github.com/zeevfischer/Ex4_oop/wiki
