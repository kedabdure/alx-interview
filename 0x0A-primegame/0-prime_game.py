#!/usr/bin/python3
"""Module defining is_winner function."""

def is_winner(x, nums):
    """Function to determine the winner of the prime game."""
    maria_wins_count = 0
    ben_wins_count = 0

    for num in nums:
        available_numbers = list(range(1, num + 1))
        primes = find_primes_in_range(1, num)

        if not primes:
            ben_wins_count += 1
            continue

        is_maria_turn = True

        while True:
            if not primes:
                if is_maria_turn:
                    ben_wins_count += 1
                else:
                    maria_wins_count += 1
                break

            smallest_prime = primes.pop(0)
            available_numbers.remove(smallest_prime)

            available_numbers = [n for n in available_numbers if n % smallest_prime != 0]

            is_maria_turn = not is_maria_turn

    if maria_wins_count > ben_wins_count:
        return "Winner: Maria"

    if maria_wins_count < ben_wins_count:
        return "Winner: Ben"

    return None


def is_prime(n):
    """Returns True if n is prime, else False."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_primes_in_range(start, end):
    """Returns a list of prime numbers between start and end (inclusive)."""
    return [n for n in range(start, end + 1) if is_prime(n)]
