from art import logo, vs
from game_data import data
import random
score = 0

def generate_random_choice(data_list):
    random_index = random.randint(0, len(data_list)-1)
    return data_list[random_index]

def check_answer(option, followers_A, followers_B):
    if followers_A > followers_B and option == 'A':
        return True
    elif followers_A > followers_B and option == 'B':
        return False
    elif followers_A < followers_B and option == 'B':
        return True
    else:
        return False


print(logo)
should_continue = True;
choice_dict_B = generate_random_choice(data)
while should_continue:
    choice_dict_A = choice_dict_B
    print(f"Compare A: {choice_dict_A['name']}, {choice_dict_A['description']}, from {choice_dict_A['country']}")
    print(vs)
    choice_dict_B = generate_random_choice(data)
    print(f"Against B: {choice_dict_B['name']}, {choice_dict_B['description']}, from {choice_dict_B['country']}")
    answer = input("Who has more followers? Type 'A' or 'B': ")
    if check_answer(answer, choice_dict_A['follower_count'], choice_dict_B['follower_count']) == True:
        should_continue = True
        score = score+1
        print("\n")
        print(f"You're right! Current score: {score}.")
    else:
        should_continue = False
        print("\n")
        print(f"Sorry, that's wrong. Final score: {score}")
