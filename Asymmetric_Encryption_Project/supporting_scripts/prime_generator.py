# Chris Zavik 
# Basic Encryption program project
# This file is for generating large prandom primes, following the example and guidance from https://www.geeksforgeeks.org/how-to-generate-large-prime-numbers-for-rsa-algorithm/

"""
The security of the RSA algorithm is based on the difficulty of factorizing very large numbers.  The setup of an RSA cryptosystem involves the generation of two large primes, say p and q, from which, the RSA modulus is calculated as n = p * q.  The greater the modulus size, the higher is the security level of the RSA system. The recommended RSA modulus size for most settings is 2048 bits to 4096 bits. Thus, the primes to be generated need to be 1024 bit to 2048 bit long. For the synthesis of such large primes, instead of depending on deterministic methods, 
we rely on finding numbers that are prime with a satisfactorily high level of probability.

Large Prime Generation Procedure:
The goal is to efficiently compute very large random prime numbers with a specified bit-size. The standard method of manually implementing a random prime number generator which can generate prime values with a satisfactory level of accuracy is given as follows: 
1 - Preselect a random number with the desired bit-size.
2 - Ensure the chosen number is not divisible by the first few hundred primes (these are pre-generated)
3- Apply a certain number of Rabin Miller Primality Test iterations, based on acceptable error rate, to get a number which is probably a prime"""


import random
from supporting_scripts.initial_primes_list import inital_primes_list


###
###   STEP 1 --- Generate Random Prime Candidate
###

'''Generating an n-bit number means that the number will be between 0 and (2^n-1).
Some considerations when generating the random number are: 
Small primes are not good for RSA because they are easily guessable, so we will make sure to not have leading zeroes in our generted numbers, by making the highest order bit of our generated number always 1.
All prime numbers >2 are odd, so we won't pick even numbers.
We pick any random number in the range (2^{n-1} + 1, 2^n - 1)
The above line ensures  that the first largest bit will be 1.'''

def nBitRandom(n): 
    # Returns a random number 
    # between 2**(n-1)+1 and 2**n-1''' 
    return(random.SystemRandom().randrange(2**(n-1)+1, 2**n-1)) # random.SystemRandom() uses the system's TRNG



###
###   STEP 2 --- Low-Level Primality Test
###

'''Here we simply have a list of the first 300 prime numbers in a list using the Sieve of Eratosthenes. We check to see if our candidate is coprime with these priems. If not, we generate a new one - if yes, we move the the high level test'''

def getLowLevelPrime(n):
    '''Generate a prime candidate divisible 
    by first primes'''
    while True:
        # Obtain a random number
        pc = nBitRandom(n)

        # Test divisibility by pre-generated
        # primes
        for divisor in inital_primes_list:
            if pc % divisor == 0 and divisor**2 <= pc:
                break
        else:
            return pc
        

###
###   STEP 3 --- High-Level Primality Test
###

'''Here we use the Rabin Miller Primality Test. The Maths of this is detailed, but essentially: to see if n is prime, we check for -- a^(n-1)-1 ≡ 0(mod n) -- for various values of a, where -- 1 < a < (n-1) -- . Each time the test passes for a given value of a, there is a 3/4th chance that n is prime, and 1/4th chance that n is composite. So if the test passes for m different values of a, then there is a -- (1/4)^m = (1/2)^2m -- chance that n is prime. Here we aim for a certainty of at most (2^-128) that n is composite.'''

def isMillerRabinPassed(mrc):
    '''Run 20 iterations of Rabin Miller Primality test'''
    maxDivisionsByTwo = 0
    ec = mrc-1
    while ec % 2 == 0:
        ec >>= 1
        maxDivisionsByTwo += 1
    assert(2**maxDivisionsByTwo * ec == mrc-1)

    def trialComposite(round_tester):
        if pow(round_tester, ec, mrc) == 1:
            return False
        for i in range(maxDivisionsByTwo):
            if pow(round_tester, 2**i * ec, mrc) == mrc-1:
                return False
        return True

    # Set number of trials here
    numberOfRabinTrials = 64
    for i in range(numberOfRabinTrials):
        round_tester = random.SystemRandom().randrange(2, mrc)
        if trialComposite(round_tester):
            return False
    return True


###
###   Running the Script
###

#if __name__ == '__main__':
def generatePrime():
    while True:
        n = 1024
        prime_candidate = getLowLevelPrime(n)
        if not isMillerRabinPassed(prime_candidate):
            continue
        else:
            break
    return prime_candidate
