# Project Title

Help MacGyver to escape: in this little game, Macgyver is supposed to pick up all the objects in the labyrinth before reaching the guardian if he wants to win.

## Code style

I follow the [PEP8 style guide for Python](http://www.python.org/dev/peps/pep-0008/).

## Screenshots

Textual version:
![alt text]()

Pygame version:
![alt text]()


## Library used
[Pygame](https://www.pygame.org/news).

## Installation

To be able to play that game you need to:
    
1. create a virtualenv to receive the program by entering in your command prompt: virtualenv name_of_your_directory
          then move inside the virtualenv with: cd name_of_your_repository and activate it with: Scripts\activate
1. enter in your command prompt: git clone https://github.com/Nivose44/projet_trois.git
    
1. move inside that directory by entering in your command prompt: cd projet_trois
    
1. install the dependencies by entering in the command prompt: pip install -r requirements.txt
    
1. Then still in the command prompt, you can choose if you want to play the textual version or the pygame version of the game:

	for macos/linux:
                    
		python3 game_macgyver.py -e text   (to use the textual version)
                    
		python3 game_macgyver.py -e pygame (to use the pygame version)
                
	for windows:
                    
		py -3 game_macgyver.py -e text   (to use the textual version)
                    
		py -3 game_macgyver.py -e pygame   (to use the pygame version)
