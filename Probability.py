# ------------------------------------------------------------------------------
# Probability.py
# Programming Assignment 5
# Computer attempts to guess a number you choose between given integers,
# ------------------------------------------------------------------------------
import random
frequency = []
numberOfTrials = []

def throwDice(m, k):
    """
   throws two independent dice and returns the result in a 2-tuple
    """
    rolls = [0] * m
    for r in range(0, m + 1):
        rolls[r] = rng.randrange(1, k + 1)
    return rolls
    # end throwDice()

    # -- main ---------------------------------------------------------------

print('\n')

rollAgain = "Yes" or "yes" or "y"

while rollAgain == "Yes" or "yes" or "y":

    m = input('Enter the number of dice: ')  # input
    k = input('Enter the number of sides on each die: ')
    numberOfTrials = input('Enter the number of trials to perform: ')

    if m < 1:
        m = input('Enter the number of dice: ').m()

    if k < 2:
        k = input("Enter the number of sides on each die: , ").k()

    if numberOfTrials > 1:
        numberOfTrials = input("Enter the number of trials to perform: , ")

    rng = random.Random()  # Create a random number generator

    while (m > 1) and (k > 2) and (numberOfTrials > 1):
        print("Caclulating...")
        print("------------------------------------------------------------------------------")
        print(throwDice(m, k))

    for i in range(numberOfTrials):
        t = throwDice(m, k)
        frequency = 13 * [0]  # same as [0,0,0,0,0,0,0,0,0,0,0,0,0]
        frequency[t[0] + t[1]] += 1
    # end for
        print()
        print("Frequencies:")
        print(frequency)
# perform simulation, record and print frequencies
# calculate relative frequencies, probabilities and errors
relativeFrequency = [0, 0]
probability = [0, 0]
error = [0, 0]
for i in range(2, len(frequency)):
    relativeFrequency.append(frequency[i] / numberOfTrials)
    probability.append(min(i - 1, 13 - i) / 36)
    error.append(abs(probability[i] - relativeFrequency[i]))
    # end for


# print(relativeFrequency)
# print(probability)
# print(error)
print()

# print results
f1 = "{0:<10}{1:<22}{2:<22}{3:<22}"
f2 = 71 * "-"
f3 = "{0:>3}       {1:<22.15f}{2:<22.15f}{3:<.15f}"
print(f1.format("Sum", "Relative Frequency", "Probability", "Error"))
print(f2)
for i in range(2, len(frequency)):
    print(f3.format(i, relativeFrequency[i], probability[i], error[i]))
# end for
print()
