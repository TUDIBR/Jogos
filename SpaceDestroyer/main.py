import sys
from ui.menu import MenuStart


def start_game():
    import core.game
    core.game.Main()

if __name__ == '__main__':
    menu = MenuStart()
    should_start_game = menu.start()

    if should_start_game:
        start_game()
    else:
        sys.exit()