# Write your code here
import random


class RPS:
    options = ['rock', 'paper', 'scissors']

    def __init__(self):
        self.options = ['rock', 'paper', 'scissors']
        self.lose = {'scissors': 'rock', 'paper': 'scissors', 'rock': 'paper'}
        self.wins = {'scissors': 'paper', 'paper': 'rock', 'rock': 'scissors'}
        self.player_rating = 0
        self.player_name = None
        self.choice = random.choice(self.options)
        self.users = {}
        with open('rating.txt', 'r') as f:
            users_data = f.readlines()
            for line in users_data:
                name, score = line.split()
                self.users[name] = int(score)
                # print(f'user {name} highscore: {score}')
        pass

    def play(self):
        if self.player_name is None:
            self.get_user()
        user_choice = input()
        self.choice = random.choice(self.options)

        if user_choice not in self.options + ['!exit', '!rating']:
            print('Invalid input')
        elif user_choice == '!exit':
            print('Bye!')
            exit()
        elif user_choice == '!rating':
            print(f'Your rating: {self.player_rating}')
        elif self.choice == user_choice:
            print(f'There is a draw ({self.choice})')
            self.player_rating += 50
        elif self.choice in self.lose[user_choice]:
            print(f'Sorry, but the computer chose {self.choice}')
        elif self.choice in self.wins[user_choice]:
            print(f'Well done. The computer chose {self.choice} and failed')
            self.player_rating += 100
        else:
            print(f'u: {user_choice} cp:{self.choice}')

    def get_user(self):
        self.player_name = input('Enter your name: ')
        print(f'Hello, {self.player_name}')
        user_input = input().split(',')
        if len(user_input) > 3:
            self.options = user_input
            for i, item in enumerate(self.options, 1):
                self.lose[item] = [self.options[move % len(self.options)] for move in
                                   range(i, i + len(self.options) // 2)]
            for i, item in enumerate(self.options):
                self.wins[item] = [self.options[move % len(self.options)] for move in
                                   range(i - len(self.options) // 2, i)]
        print("Okay, let's start")
        # print(self.options)
        # print(self.lose)
        if self.player_name in self.users:
            self.player_rating = self.users[self.player_name]
            # print(f'Your rating is {self.player_rating}')
        pass


game = RPS()
while True:
    game.play()
