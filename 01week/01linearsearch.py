# This is a program for linear search algorithim
#date 11/9/21
from jovian.pythondsa import evaluate_test_case
from testcases import tests
def find_cards(cards, query):
    position = 0

    while (position < len(cards)):
        if(cards[position] == query):
            return position

        position = position + 1

    return -1

large_testcase = {'input': {
    'cards': list(range(1000000, 0, -1)),
    'query': 2
    },
    'output':999998}
print(evaluate_test_case(find_cards, large_testcase ))
