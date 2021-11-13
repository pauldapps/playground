import itertools

a = ["a1", "a2", "a3", "a4", "a5"]
b = ["b1", "b2", "b3", "b4", "b5", "b6"]
c = ["c1", "c2", "c3", "c4", "c5", "b7", "b8"]

for x, y, z in itertools.zip_longest(a, b, c):
    print(x, y, z)

data = {"list_a": a, "list_b": b, "list_c": c}
for x, y, z in itertools.zip_longest(data["list_a"], data["list_b"], data["list_c"]):
    print(x, y, z)
