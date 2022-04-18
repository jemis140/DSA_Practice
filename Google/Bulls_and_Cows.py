class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        bulls = 0
        sh = defaultdict(int)
        gh = defaultdict(int)
        for s, g in zip(secret, guess):
            #bulls
            #if its in correct position then index value will be same and in map both element will be same
            if s == g:
                bulls += 1
            else:
                #Increament count of char in both map
                sh[s] += 1
                gh[g] += 1
        # take minimum counter of char between sh and gh map for counting cows
        cows = sum(min(sh[k], gh[k]) for k in sh)
        return "{}A{}B".format(bulls, cows)