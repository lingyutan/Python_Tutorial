def frog_q(S, k, q):
    n = len(S)
    dp = [1] + [0] * k
    for j in xrange(1, k + 1):
        for i in xrange(n):
            if S[i] <= j:
                dp[j] = (dp[j] + dp[j - S[i]]) % q
    print(dp)
    return dp[k]

def frog(S, k):
    n = len(S)
    dp = [1] + [0] * k
    for j in xrange(1, k + 1):
        for i in xrange(n):
            if S[i] <= j:
                dp[j] += dp[j - S[i]]
    print(dp)
    return dp[k]

# print(frog_q([1,2,3], 10, 2**32-1))
print(frog([1,2,3,5,10,15], 10))
