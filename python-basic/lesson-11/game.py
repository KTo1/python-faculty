import random
import os
import platform


class LottoInit:
    def __init__(self):
        self._MAX_NUMBERS = 90
        self._MAX_NUMBERS_IN_CARD = 15
        self._NEED_SPACES = 4
        self._NEED_NUMBERS = 5


class LottoCard(LottoInit):
    def __init__(self, name, ai):
        super().__init__()
        self.name = name
        self._ai = ai
        self._card = [[], [], []]
        self._in_game = True
        self._init_card()

    def get_card(self):
        return self._card

    def is_ai(self):
        return self._ai

    def in_game(self):
        return self._in_game

    def game_over(self):
        self._in_game = False

    def card_fill(self, dropped_numbers):
        count = 0
        for line in self.get_card():
            for num in line:
                if num in dropped_numbers:
                    count += 1

        return count == self._MAX_NUMBERS_IN_CARD

    def print_card(self, dropped_numbers):
        result = '---------------------------\n'
        for line in self.get_card():
            for num in line:
                result += 'X'.rjust(3, ' ') if num in dropped_numbers else f'{str(num)}'.rjust(3, ' ')
            result += '\n'

        result += '---------------------------\n'

        print(result)

    def num_in_card(self, num):
        for line in self._card:
            if num in line:
                return True
        return False

    def _init_card(self):
        numbers = random.sample(range(1, self._MAX_NUMBERS + 1), self._MAX_NUMBERS_IN_CARD)
        for line in self._card:
            for _ in range(self._NEED_SPACES):
                line.append(' ')

            for _ in range(self._NEED_NUMBERS):
                line.append(numbers.pop())

        def check_sort_item(item):
            if isinstance(item, int):
                return item
            else:
                return random.randint(1, self._MAX_NUMBERS)

        for index, line in enumerate(self._card):
            self._card[index] = sorted(line, key=check_sort_item)


class LottoGame(LottoInit):
    def __init__(self, *players):
        super().__init__()
        self._numbers = random.sample(range(1, self._MAX_NUMBERS + 1), self._MAX_NUMBERS)
        self._dropped_numbers = []
        self._command_cls = 'cls' if platform.system() == 'Windows' else 'clear'
        self.players = players

    def start(self):
        count = 1
        yes_or_no = ('y', 'Y', 'n', 'N')
        for num in self._numbers:
            os.system(self._command_cls)
            print(f'Новый бочонок: {num}, осталось: {len(self._numbers) - count}')
            for player in self.players:
                if not player.in_game():
                    continue
                print(f'Карточка игрока: {player.name}')
                player.print_card(self._dropped_numbers)

            self._dropped_numbers.append(num)

            for player in self.players:
                if not player.in_game():
                    continue

                print(f'Ход игрока: {player.name}')

                if not player.is_ai():
                    while True:
                        choice = input('Зачеркнуть цифру? (y/n)')
                        if choice in yes_or_no:
                            break

                    if choice == 'y' or choice == 'Y':
                        if not player.num_in_card(num):
                            print(f'Игрок {player.name} проиграл!')
                            player.game_over()
                            continue

                    if choice == 'n' or choice == 'N':
                        if player.num_in_card(num):
                            print(f'Игрок {player.name} проиграл!')
                            player.game_over()
                            continue

                if player.card_fill(self._dropped_numbers):
                    print(f'Игрок: {player.name}, победил!')
                    exit()

            count += 1
            print()

        print('Гейм, как говорится, овер...')


player_one = LottoCard('Игрок 1', False)
player_two = LottoCard('Игрок 2', False)
player_three = LottoCard('Компьютер', True)

game = LottoGame(player_one, player_two, player_three)
game.start()
