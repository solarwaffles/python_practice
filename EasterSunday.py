import math

class EasterSunday:
    def findEasterSunday(y):
        a = y % 19
        b = math.floor(y / 100)
        c = y % 100
        d = math.floor(b / 4)
        e = b % 4
        g = math.floor((8 * b + 13) / 25)
        h = (19 * a + b - d - g + 15) % 30
        j = math.floor(c / 4)
        k = c % 4
        m = math.floor((a + 11 * h) / 319)
        r = (2 * e + 2 * j - k - h + m + 32) % 7
        n = math.floor((h - m + r + 90) / 25)
        p = ( h - m + r + n + 19) % 32
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
        print(g)
        print(h)
        print(j)
        print(k)
        print(m)
        print(r)
        print(m)
        print(p)
        

test = EasterSunday
test.findEasterSunday(2001)