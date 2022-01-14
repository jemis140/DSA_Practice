# You are given two string arrays username and website and an integer array timestamp.
# All the given arrays are of the same length and the tuple [username[i], website[i], timestamp[i]] indicates that the user username[i] visited the website website[i] at time timestamp[i].

# A pattern is a list of three websites (not necessarily distinct).

# For example, ["home", "away", "love"], ["leetcode", "love", "leetcode"], and ["luffy", "luffy", "luffy"] are all patterns.
# The score of a pattern is the number of users that visited all the websites in the pattern in the same order they appeared in the pattern.

# For example, if the pattern is ["home", "away", "love"], the score is the number of users x such that x visited "home" then visited "away" and visited "love" after that.
# Similarly, if the pattern is ["leetcode", "love", "leetcode"], the score is the number of users x such that x visited "leetcode" then visited "love" and visited "leetcode" one more time after that.
# Also, if the pattern is ["luffy", "luffy", "luffy"], the score is the number of users x such that x visited "luffy" three different times at different timestamps.
# Return the pattern with the largest score. If there is more than one pattern with the same largest score, return the lexicographically smallest such pattern.

# Missed Edge Cases
# 1: Timestamp is not always in sorted order
# 2: Missed only 3 item combination is answer

# New Learning
# Counter Function
# Combinations
# zip

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        users = defaultdict(list)
        for user, time, site in sorted(zip(username, timestamp, website), key=lambda x: (x[0], x[1])):
            users[user].append(site)

        combinationsOfSite = Counter()

        for user, sites in users.items():
            combinationsOfSite.update(set(combinations(sites, 3)))

        return max(sorted(combinationsOfSite), key=lambda x: combinationsOfSite[x])
