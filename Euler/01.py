# V1
print(sum(i for i in range(1000) if not i % 3 or not i % 5))


# V2
print(sum(set(range(0,1000,3))|set(range(0,1000,5))))
