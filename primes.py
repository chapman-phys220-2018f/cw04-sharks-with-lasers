#!/usr/bin/env python3

###
# Name: Morgan Holve
# Student ID: 2281337
# Email: holve100@mail.chapman.edu
# Course: MATH220 FALL 2018
# Assignment: CW4
###

def integers():
    """Generates positive integers greater than 2"""
    a = 2
    while True:
        yield a
        a += 1

def gen_eratosthenes():
    "Generates prime numbers based on the Sieve of Eratosthenes"""
    primes=[2]
    yield 2
    for i in integers():
        prime = True
        for p in primes:
            if i % p == 0:
                prime = False 
        if prime:
            primes.append(i)
            yield i

def eratosthenes(n):
    ps = gen_eratosthenes()
    out = []
    for p in ps:
        if p<n:
            out.append(p)
        else:
            break
    return out

def main(argv):
   print (eratosthenes(argv))


if __name__ == "__main__":
    import sys
    main(sys.argv)
