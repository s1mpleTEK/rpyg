##
## FLIK STUDIO PROJECT, 2021
## rpyg
## File description:
## main
##

from Player import Player

def main():
    try:
        player = Player()
        player.setName()
        player.setJob()
        player.getInfo()
        exit
    except (EnvironmentError, KeyboardInterrupt):
        exit


if __name__ == "__main__":
    main()