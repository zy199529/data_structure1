def longestPalindrome(s):
        len1=len(s)
        for i in range(len1):
            for j in range(i,len1):
                len1=j+1-i
                A=s[i:j+1]
                for y in range(len(A)):
                    if A[y]!=A[len(A)-y]:
                        break
                
        return s
S = "babad"
print(longestPalindrome(S))
        