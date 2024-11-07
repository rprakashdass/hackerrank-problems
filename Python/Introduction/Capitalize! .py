# Complete the solve function below.
def solve(s):
    a = []
    for i in s.split(" "):
        i = i.capitalize()
        a.append(i)
    return ' '.join(a)
