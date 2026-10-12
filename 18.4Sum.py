class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        result = []

        for x in range(n - 3):
            # Skip duplicate first numbers
            if x > 0 and nums[x] == nums[x - 1]:
                continue

            for y in range(x + 1, n - 2):
                # Skip duplicate second numbers
                if y > x + 1 and nums[y] == nums[y - 1]:
                    continue

                # Calculate the sum required from the remaining pair
                rem_target = target - (nums[x] + nums[y])

                left, right = y + 1, n - 1

                while left < right:
                    total = nums[left] + nums[right]

                    if total == rem_target:
                        result.append([
                            nums[x],
                            nums[y],
                            nums[left],
                            nums[right]
                        ])

                        # Move both pointers after finding a match
                        left += 1
                        right -= 1

                        # Skip duplicate third numbers
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        # Skip duplicate fourth numbers
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif total < rem_target:
                        # Increase the sum
                        left += 1

                    else:
                        # Decrease the sum
                        right -= 1

        return result


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (
            [1, 0, -1, 0, -2, 2],
            0,
            [
                [-2, -1, 1, 2],
                [-2, 0, 0, 2],
                [-1, 0, 0, 1]
            ]
        ),
        (
            [2, 2, 2, 2, 2],
            8,
            [
                [2, 2, 2, 2]
            ]
        ),
        (
            [-2, -1, -1, 1, 1, 2, 2],
            0,
            [
                [-2, -1, 1, 2],
                [-1, -1, 1, 1]
            ]
        )
    ]

    for index, (nums, target, expected) in enumerate(test_cases, start=1):
        actual = solution.fourSum(nums, target)

        # Compare results regardless of quadruplet ordering
        assert sorted(actual) == sorted(expected), (
            f"Test {index} failed: expected {expected}, got {actual}"
        )

        print(f"Test {index} passed!")
        print(f"Input: nums={nums}, target={target}")
        print(f"Output: {actual}\n")

    print("All test cases passed!")
