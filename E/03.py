# Problem 03 - Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

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
def trial_division(n):
    if n < 2:
        return []
    prime_factors = []
    for p in prime_sieve(int(n**.5)+1):
        if p*p > n: 
            break
        while not n % p:
            prime_factors.append(p)
            n //= p
    if n > 1:
        prime_factors.append(n)
    return prime_factors
print (trial_division(600851475143))
