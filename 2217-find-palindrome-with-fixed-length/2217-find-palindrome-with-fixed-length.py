class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        answer = []

        halfLength = (intLength + 1) // 2

        start = 10 ** (halfLength - 1)
        end = 10 ** halfLength - 1

        for query in queries:
            firstHalf = start + query - 1

            if firstHalf > end:
                answer.append(-1)
                continue

            left = str(firstHalf)

            if intLength % 2 == 0:
                palindrome = left + left[::-1]
            else:
                palindrome = left + left[:-1][::-1]

            answer.append(int(palindrome))

        return answer