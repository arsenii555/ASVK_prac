import string
import timeit

s = input()
gl = set("aeiouy")
sogl = set(string.ascii_lowercase) - gl


def func():
    global s
    s = set(s)
    glc = 0
    soglc = 0
    for i in s:
        if i in gl:
            glc += 1
        elif i in sogl:
            soglc += 1
    return glc, soglc


print(timeit.Timer(func).autorange())
