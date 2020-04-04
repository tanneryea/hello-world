import random

def diceRoll(amount):
    results = []
    for x in range(amount):
        results.append(random.randint(1,6))
    return results

def main():
    rollAgain = 'Y'
    while rollAgain.upper() == 'Y':
        actionDie = int(input('How many action die do you want to roll? '))
        dangerDie = int(input('How many danger die do you want to roll? '))
        actionResult = diceRoll(actionDie)
        actionResult.sort()
        dangerResult = diceRoll(dangerDie)
        dangerResult.sort()
        finalResult = []
        print('Your action die results are:', *actionResult)
        print('Your danger die results are:', *dangerResult)
        for x in actionResult:
            if x not in dangerResult:
                finalResult.append(x)
            if x in dangerResult:
                dangerResult.remove(x)
        print('Your final result is:', *finalResult)
        rollAgain = input('Would you like to roll again? Y/N: ')

main()