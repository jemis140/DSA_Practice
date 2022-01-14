# Convert a non-negative integer num to its English words representation.
class Solution:
    def numberToWords(self, num):
        units = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                 "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["Twenty", "Thirty", "Forty", "Fifty",
                "Sixty", "Seventy", "Eighty", "Ninety"]
        bigs = {1000: "Thousand", 1000000: "Million", 1000000000: "Billion"}

        if num == 0:
            return "Zero"

        def words(n, idx=0):
            if n == 0:
                return []
            if n < 20:
                return [units[n - 1]]
            if n < 100:
                return [tens[n//10 - 2]] + words(n % 10)
            if n < 1000:
                return [units[n//100 - 1]] + ['Hundred'] + words(n % 100)
            else:
                for i in [1000000000, 1000000, 1000]:
                    if n // i > 0:
                        return words(n//i) + [bigs[i]] + words(n % i)

        return ' '.join(words(num))
