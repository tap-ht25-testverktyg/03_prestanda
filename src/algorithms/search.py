from math import floor


# Linjärsökning: kolla varje element
# Tidskomplexitet: O(n)   (längden på listan)
def find_in_list(needle, haystack):
    for straw in haystack:
        # print("find in list", straw)
        if straw == needle:
            return True
    return False


# Binärsökning: kolla mitten, släng bort den halva som elementet garanterat inte finns i
# Tidskomplexitet: ?
def find_in_list_binary(needle, haystack):
    left = 0
    right = len(haystack) - 1

    while left <= right:
        mid = floor((left + right) / 2)
        if haystack[mid] == needle:
            return True
        elif haystack[mid] < needle:
            left = mid + 1
        else:
            right = mid - 1

    return False