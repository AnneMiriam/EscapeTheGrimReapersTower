# EscapeTheGrimReapersTower

## Introduction

Welcome to The Grim Reaper's Tower. You have suddenly found yourself trapped inside it on the top floor. It is your goal to escape the tower. To do so you must make your way to the ground level where there is an entryway with a door, or you can jump/repel out a window to the ground where you find a gate. Before you can exit, however, you must find the key that unlocks the entry door/front gate. 
There are other items that you can find along the way, that will help you, such as rope to help you if you choose the window option, or bread that can heal you.
In the mean time there are, also, enemies throughout the tower that can damage your health. One of which is the Grim Reaper! For an added challenge, you can create your own enemy.

Fork and clone this repo to play our cli based python game. Best of luck!

Take a look at the directory structure:

```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
├── data
│    ├── default_enemies.py
└── lib
    ├── models
    │   ├── __init__.py
    │   ├── Enemy.py
    │   ├── game.py
    │   ├── items.py
    │   ├── NonPlayChar.py
    │   ├── player.py
    │   └── rooms.py
    ├── cli.py
    ├── debug.py
    └── helpers.py
```



---

## Generating Your Environment

You might have noticed in the file structure- there's already a Pipfile!

Install any additional dependencies you know you'll need for your project by
adding them to the `Pipfile`. Then run the commands:

```console
pipenv install
pipenv shell
```

---

## Generating Your CLI

A command line interface(CLI) is, simply put, an interactive script and prompts the user and performs operations based on user input.

Enter in `python lib/cli.py` to get started!


---
### How the Game Works

The above command will display your introduction to the game. Once loaded, you will have 3 options to to proceed. 0 will exit the game, 1 will start the game, and 2 will take you to a form for creating a new enemy.
Choosing to create an enemy will allow you to access the create_enemy function of the Game class. After you create an enemy it will take you to a new menu, that allows you to again exit, start, or now you can delete the enemy(incase you changed your mind).
Starting the game, you will be prompted to create a player, by entering it's name. Then the game will start you out in the AtticRoom. From here you have two choices, the window or the door. The window asks if you'd rather go back inside, or try your luck at jumping from the unknown height.
If you choose the door, you will find yours elf on the stairs. From the stairs you have access to all the rooms, plus the exit, and a chance to see if a ghost has anything to offer you.

### What Goes into a README?

This README serves as a template. Replace the contents of this file to describe
the important files in your project and describe what they do. Each Python file
that you edit should get at least a paragraph, and each function should be
described with a sentence or two.

Describe your actual CLI script first, and with a good level of detail. The rest
should be ordered by importance to the user. (Probably functions next, then
models.)

Screenshots and links to resources that you used throughout are also useful to
users and collaborators, but a little more syntactically complicated. Only add
these in if you're feeling comfortable with Markdown.

---

## Conclusion

A lot of work goes into a good CLI, but it all relies on concepts that you've
practiced quite a bit by now. Hopefully this template and guide will get you off
to a good start with your Phase 3 Project.

Happy coding!

---

## Resources

- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
