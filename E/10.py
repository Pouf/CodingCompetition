# Problem 10 - Summation of primes
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
def prime_sieve(limit):
    is_prime = [False] * (limit + 1)
    for x in range(1,int(limit**.5)+1):
        for y in range(1,int(limit**.5)+1):
            n = 4*x**2 + y**2
            if n<=limit and (n%12==1 or n%12==5):
                # print "1st if"
                is_prime[n] = not is_prime[n]
            n = 3*x**2+y**2
            if n<= limit and n%12==7:
                # print "Second if"
                is_prime[n] = not is_prime[n]
            n = 3*x**2 - y**2
            if x>y and n<=limit and n%12==11:
                # print "third if"
                is_prime[n] = not is_prime[n]
    for n in range(5,int(limit**.5)):
        if is_prime[n]:
            for k in range(n**2,limit+1,n**2):
                is_prime[k] = False
    return [2,3]+[i for i in range(5,limit) if is_prime[i]]
print(sum(prime_sieve(2000000)))
