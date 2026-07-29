
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(index, current, total):
            if total == target:
                result.append(current[:])
                return

            if total > target or index == len(candidates):
                return

            # Choose the current number
            current.append(candidates[index])
            backtrack(index, current, total + candidates[index])

            # Undo the choice
            current.pop()

            # Skip the current number
            backtrack(index + 1, current, total)

        backtrack(0, [], 0)
        return result