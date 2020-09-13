from exceptions import GameOver, EnemyDown
import models_game
from settings_game import WELCOME_STR, BYE_STR, ERROR_SELECT_STR, START_STR, START_EXIT, \
    LIVES, SCORE, ENENY_DOWN_STR, LIVES_STR


def player_name_input(string=WELCOME_STR):
    return input(string)


def start_input(string=START_STR):
    q = " "
    while q.lower() not in [z.lower() for z in START_EXIT.values()]:
        q = input(string).strip()
        if q == START_EXIT["exit"]:
            print(BYE_STR)
            exit()


def select_player_attack():
    stringer = "Для выбора Разбойника введите 1, для Воина 2, для Волшебника 3 "
    while True:
        q = int(input(stringer))
        if q == 1 or q == 2 or q == 3:
            break
        else:
            print(ERROR_SELECT_STR)
            continue


def play():
    level = 1
    player = models_game.Player(player_name_input(), LIVES)
    enemy = models_game.Enemy(level)
    while True:
        try:
            player.attack(enemy)
            player.defense(enemy)
        except EnemyDown:
            level += 1
            enemy = models_game.Enemy(level)
            player.score += SCORE
            print(ENENY_DOWN_STR, player.score)
            print(LIVES_STR, player.lives)

            continue
        except GameOver:
            with open("scores.txt", "a") as f:
                f.writelines("{}:  {}".format(player.name, player.score))
    raise GameOver


if __name__ == '__main__':
    try:
        play()
    except GameOver:
        pass
    except KeyboardInterrupt:
        pass
    finally:
        print("Досвидания ")
