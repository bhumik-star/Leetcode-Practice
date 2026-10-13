
"""
Problem: 3Sum
Approach: Sorting + Two Pointers
Time Complexity: O(n^2)
Auxiliary Space: O(1), excluding sorting and output
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()
        n = len(nums)

        for x in range(n - 2):
            # Skip duplicate first elements
            if x > 0 and nums[x] == nums[x - 1]:
                continue

            left, right = x + 1, n - 1

            while left < right:
                total = nums[x] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[x], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate right values
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    # Increase the sum
                    left += 1

                else:
                    # Decrease the sum
                    right -= 1

        return result


if __name__ == "__main__":
    solution = Solution()

    nums = [-1, 0, 1, 2, -1, -4]
    print(solution.threeSum(nums))
    # Expected: [[-1, -1, 2], [-1, 0, 1]]
