# Pygame Runner Game

#### Video Demo: <https://youtu.be/KuEvi-bw0Do>
#### Description:

The Game:

The game is a two dimensional running game, where you dodge an incoming blue ball with spawns at different Y coordinates on the right side of the screen.
The blue ball, round after round increases its speed endlessly, I used a limit equation for this so that it doesn’t become unplayable but every round is technically more difficult than the last.


The Controls:

W: up
A: left
S: down
D: right

Why I Chose Pygame:

Since I was a young chap I have always been enthralled by game creation, and many times in the past I had attempted to learn how to use Unity game engine, but I was never focused enough so I always became overwhelmed and gave up.
After taking an interest into programming itself, and taking cs50 I realized that if i create a final project in pygame, I could break the seal on my game development career, and get some more advanced programming practice with python, I say this because engines like unity require less general programming as far as I know.

The Art:

I decided to use rather plain art as I mainly wanted to practice my programming skills, so I used gimp to make simplay drawings, I went a bit harder on the character model, which has an animation which I think it pretty cleverly implemented.

The functions:

scoreboard()
scoreboard is called every tick because I believe in pygame fonts are immutable so in order to update the scoreboard a new text surface has to be created.

collisions()
collisions is used to check if the player's rectangle has collided with the obstacle's rectangle, if so it will activate the end screen.

obstacle_movement()
obstacle movement checks if the obstacle has started moving or not, if not it chooses a random y value for the obstacle to start at then it moves it by a certain number of pixels to the left each tick. This number is Difficulty and Difficulty() is a limit meaning it can get infinitely close to but never at 25.

player_animation()
player animation creates an index that goes back and forth from 0 to 1. player_walk is a list of two images, and player animation uses its value to index to which image should be chosen for that frame.

player_move()

this function gets a list of events from pygame and then checks if they are happening and in this case it has to do with WASD for the movements keys.

The Loop:

this game loop runs at 60fps, inside it first check if the window has been close then it check which what the game state is, I used a dictionary {start, main, end} only one where the values are 1 if thats the state and 0 if they are not, start presents the start screen, main is the actualy game, and end is the end screen.
