N = int(input("Plese Enter a Number: "))
high = 1000
low = 0
num_guesses = 0
guess = (low + high) / 2.0
while guess >= N:
    if guess < N:
        low = guess
    else:
        high = guess
    num_guesses += 1
    guess = (low + high) / 2.0
print(f'count = {num_guesses}')
print(f'N = {N}')
