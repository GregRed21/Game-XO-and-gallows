import random

class WordGame:
    def __init__(self, word_list, max_errors):
        self.word_list = word_list
        self.max_errors = max_errors
        self.secret_word = ""
        self.guessed_letters = set()
        self.errors = 0

    def generate_word(self):
        self.secret_word = random.choice(self.word_list).upper()
        self.guessed_letters.clear()
        self.errors = 0

    def guess_letter(self, letter):
        letter = letter.upper()
        if letter in self.guessed_letters:
            return "Вы уже называли эту букву."

        self.guessed_letters.add(letter)

        if letter not in self.secret_word:
            self.errors += 1
            return "Неправильно!"

        return "Правильно!"

    def get_remaining_attempts(self):
        return self.max_errors - self.errors

    def get_current_state(self):
        current_state = ''.join(
            letter if letter in self.guessed_letters else '_' for letter in self.secret_word
        )
        return current_state

    def get_sorted_guessed_letters(self):
        return sorted(self.guessed_letters)

    def is_won(self):
        return all(letter in self.guessed_letters for letter in self.secret_word)

    def is_lost(self):
        return self.errors >= self.max_errors


def play():
    # word_list = (open('9.1 WordsStockRus.txt.txt', 'r', encoding='utf-8')).readlines()
    with open('9.1 WordsStockRus.txt.txt', 'r', encoding='utf-8') as file:
        word_list=[line.rstrip('\n') for line in file.readlines()]
    max_errors = int(input(f'С каким кол-вом ошибок хотите сыграть?\n'))

    game = WordGame(word_list, max_errors)

    while True:
        game.generate_word()
        # print(list(game.secret_word))
        print("Загадано слово. Угадайте буквы!")

        while True:
            print(f"Текущее состояние: {game.get_current_state()}")
            print(f"Осталось попыток: {game.get_remaining_attempts()}")
            print(f"Уже названные буквы: {', '.join(game.get_sorted_guessed_letters())}")

            guess = input("Введите букву: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Пожалуйста, введите только одну букву.")
                continue

            result = game.guess_letter(guess)
            print(result)

            if game.is_won():
                print(f"Поздравляем! Вы угадали слово: {game.secret_word}")
                break

            if game.is_lost():
                print(f"Вы проиграли! Загаданное слово было: {game.secret_word}")
                break

        play_again = input("Хотите сыграть еще раз? (да/нет): ").strip().lower()
        if play_again != 'да':
            break



play()