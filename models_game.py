from settings_game import ATTACK_STR, DEFENSE_STR, LIVES_STR, GAME_OVER_STR
from random import randint
from exceptions import EnemyDown, GameOver
from game import select_player_attack


class Enemy:
    def __init__(self, level, lives):
        self.level = level
        self.lives = lives

    if __name__ == '__main__':
        Enemy()

    @staticmethod
    def select_attack():
        return randint(1, 3)

    def decrease_lives(self):
        self.lives -= 1
        if not self.lives:
            raise EnemyDown


class Player:
    score = 0
    allowed_attacks = [1, 2, 3]

    def __init__(self, name, lives):
        self.name = name
        self.lives = lives

    @staticmethod
    def fight(attack, defense):
        if attack == defense:
            return 0
        if attack == 1 and defense == 2 or \
                attack == 2 and defense == 3 or \
                attack == 3 and defense == 1:
            return -1
        if attack == 1 and defense == 2 or \
                attack == 2 and defense == 3 or \
                attack == 1 and defense == 3:
            return 1

    def decrease_lives(self):
        self.lives -= 1
        if not self.lives:
            print(GAME_OVER_STR, self.score)
            print(LIVES_STR, self.lives)
            raise GameOver

    def attack(self, enemy_obj):
        players_choice = select_player_attack()
        result = self.fight(players_choice, enemy_obj.select_attack())
        print(ATTACK_STR[result])
        if result == 1:
            enemy_obj.decrease_lives()
            self.score += 1

    def defense(self, enemy_obj):
        players_choice = select_player_attack()
        result = self.fight(enemy_obj.select_attack(), players_choice)
        print(DEFENSE_STR[result])
        if result == 1:
            self.decrease_lives()
