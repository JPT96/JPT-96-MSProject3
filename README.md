# JPT-96-MSProject3(Black Jack)

## About
For my Python project I decided to go with a very simple version of black Jack game.


WHEN PLAYING PLEASE USE CAPITALISATION ON THE FIRST LETTER TO MAKE IT WORK FOR EXAMPLE Hit or Hold NOT hit and hold



## Features
This game has cards and a simple hit or hold function and will keep going till you hit 21.
It has some fun print statements in it to give the player something more interesting to look at rather than just "Dealer wins" or "Player wins".

## Design
The design of the cards is used with print statements using | and - to for the bases of a card whilst calling f prints to print the value of said card.

### Function Purposes 
In this sub section I would like to go over my functions and give a breif run down of what they do and the objective that they achieve.
This will show my thought process and even help others that wish to do a similar project.
## Import
So first thing you need to do is import random. This is very important (get it) because you need the deck to be shuffled and distributed randomly this allows for a fair game.
## Functions & Classes
### card
This first function is called card. (no prizes for guessing what this class is for)
This is essentially comprised of a list with the values of the cards which get reassinged in the print statements. In order to create the cards
underneath this we give the __init__ within  this class, we then assign self to all neccessary variables. 
After this we then define the value of the cards with things like >= 10 for example.

### deck
We create an empty list that has the self.cards.
In here we begin with creating the actual deck by generating 52 cards and create 4 suits of each.
After this we then append it to the card using the I and J used to create the 52 cards and the different suits.
### Draw
Inside the draw function we are simply itterating and appending to the self.cards which is defined later on.
As well as appending to the card we defined earlier, when this is done at the end we return cards (not card see what I mean about naming conventions)
.
### count 
This is one line of code that reads the length of the self.cards.

### player and dealer
Within this class we essentially are assigning cards as a empty list, dealer = dealer score= 0 etc etc.
From here we create the deal and hit functions. This is essentially checking if the score equats to 21 and if the player
wants to hit, if so then we extend the hand essentially by adding another card. 
After this we do our ace alteration, by essentially saying if score is over 21 we assign it the value of 1 else it is a 11.
Once the score hit's 21 we reveal the cards of both players. We also later down the line figure out if the dealer or player has 21. 

### the game 
In here is where we essentially put in the rules. What it takes to bust what it takes to win which is having a higher score but not over 21.
I also put in a way if the dealer has under 17 the dealer should hit as it is highly unlikely it will bust making the game a bit more competitve.
We then reveal both players cards when the player is happy and the dealer is over 17. We then compare results and add appropriate print statements.
I then iniate the game by going b = the_game b.round() which is a function defined earlier in the code

This is a very basic run through of the functions and classes but gives you some idea of my thought process and approach towards this project.



## Future Features
I would like to add currency (not real) to make it feel like your gambling for more immersion in this game. I also would like to do a couple of turns in this project,  
that would allow the player to get a couple of rounds in and fully enjoy this project.
## Technologies used
[python3]<https://en.wikipedia.org/wiki/Python_(programming_language)>
## Testing
The majority of the testing is done through the terminal in VS code and gitpod.
There were a few bugs with previous itterations of this project which you will find within the comments made, using things such as classes and __init__ 
as an example. But I ran into a lot of errors that I didn't know how to fix so I reverted back to a very basic version. 
My naming convetions could of been cleaner there are some basic issues like naming functions very similarly for example price and cost are too similiar.
Which actually caused the project to not work for a day or two because I couldn't understand the errors that were occuring.

## Deployment 
### publishing
 1. Go to the GitHub website and log in.
 2. On the left-hand side, you'll see all your repositories, select the appropriate one. (Repository used for this project).
 3. Under the name of your chosen Repository you will see a ribbon of selections, click on 'Settings' located on the right hand side.
 4. Scroll down till you see 'GitHub Pages' heading. 
 5. Under the 'Source' click on the dropdown and select 'master branch' 
 6. The page will reload and you'll see the link of your published page displayed under 'GitHub' pages. 
 7. It takes a few minutes for the site to be published, wait until the background of your link changes to a green color before trying to open it.
 
