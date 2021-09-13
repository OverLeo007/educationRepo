# A recursive solution for subset sum
# problem

# Returns true if there is a subset
# of set[] with sun equal to given sum


def is_subset_sum(mn, n, sm):
    # Base Cases
    if sm == 0:
        return True
    if n == 0:
        return False

    # If last element is greater than
    # sum, then ignore it
    if mn[n - 1] > sm:
        return isSubsetSum(mn, n - 1, sm)

    # else, check if sum can be obtained
    # by any of the following
    # (a) including the last element
    # (b) excluding the last element
    return is_subset_sum(
        mn, n - 1, sm) or is_subset_sum(
        mn, n - 1, sm - mn[n - 1])


# Driver code
set = [3, 34, 4, 12, 5, 2]
sum = 9
n = len(set)
if isSubsetSum(set, n, sum) is True:
    print("Found a subset with given sum")
else:
    print("No subset with given sum")

# This code is contributed by Nikita Tiwari.
