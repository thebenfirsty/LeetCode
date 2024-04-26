#Problem statement
#Given a roman numeral, convert it to an integer.

#My solution (basically brute force)
class Solution(object):
    def romanToInt(self, s):
        total = 0
        s = s + ' '
        for i in range(len(s)):
            if (s[i] == "I"):
                if(s[i+1] == "V"):
                    total += 4
                    i += 2
                elif(s[i+1] == "V"):
                    total += 9
                    i += 2
                else:
                    total += 1
            elif (s[i] == "X"):
                if(s[i+1] == "L"):
                    total += 40
                    i += 2
                elif(s[i+1] == "C"):
                    total += 90
                    i += 2
                else:
                    total += 10
            elif (s[i] == "C"):
                if(s[i+1] == "D"):
                    total += 400
                    i += 2
                elif(s[i+1] == "M"):
                    total += 900
                    i += 2
                else:
                    total += 100
            elif(s[i] == "V"):
                total += 5
            elif(s[i] == "L"):
                total += 50
            elif(s[i] == "D"):
                total += 500
            elif(s[i] == "M"):
                total += 1000
        return total




# Good solution
class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number