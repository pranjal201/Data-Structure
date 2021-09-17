'''
This is another implementation of binary search
date = 11/9/21
the testcases are the lists in decending order
'''

from jovian.pythondsa import evaluate_test_case
from testcases import tests


def locate_first_occurence(cards, query, mid):
    mid_number = cards[mid]
    if(mid_number == query):
        if mid-1 == 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'
    



def locate_cards(cards, query):
    low, high = 0, len(cards)-1

    while(low <= high):

        mid = (low + high) // 2
        result = locate_first_occurence(cards, query, mid)
        if result == 'found':
            return mid
        elif result == 'right':
            low = mid + 1
        elif result == 'left':
            high = mid - 1

    return -1


large_testcase = {'input': {
    'cards': list(range(1000000, 0, -1)),
    'query': 2
    },
    'output':999998}
evaluate_test_case(locate_cards, large_testcase)


