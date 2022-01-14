# You have an inventory of different colored balls, and there is a customer that wants orders balls of any color.

# The customer weirdly values the colored balls. Each colored ball's value is the number of balls of that color you currently have in your inventory. For example, if you own 6 yellow balls, the customer would pay 6 for the first yellow ball. After the transaction, there are only 5 yellow balls left, so the next yellow ball is then valued at 5 (i.e., the value of the balls decreases as you sell more to the customer).

# You are given an integer array, inventory, where inventory[i] represents the number of balls of the ith color that you initially own. You are also given an integer orders, which represents the total number of balls that the customer wants. You can sell the balls in any order.

# Return the maximum total value that you can attain after selling orders colored balls. As the answer may be too large, return it modulo 109 + 7.

# New Learning: divmod: https://docs.python.org/3/library/functions.html#divmod
# missed cases: equation of arithmatic progression
class Solution:
    def maxProfit(self, inventory, orders):
        inventory = sorted(inventory, reverse=True)
        inventory.append(0)
        ind, width, ans = 0, 0, 0
        while orders > 0:
            width += 1
            currentSell = min(
                orders, width * (inventory[ind] - inventory[ind + 1]))
            whole, remainder = divmod(currentSell, width)
            ans += width * \
                (whole * (inventory[ind] + inventory[ind] - whole + 1)
                 )//2 + remainder*(inventory[ind] - whole)
            orders -= currentSell
            ind += 1
        return ans % (10**9 + 7)
