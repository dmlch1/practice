a = [1, 4, 6]
b = [11, 33, 22]
mapping = dict(zip(b, a))
sorted_a = [mapping[key] for key in sorted(b)]
print(sorted_a)