def length_of_longest_substring(s):
    chars = set()
    left = 0
    result = 0
    for right in range(len(s)):
        while s[right] in chars:
            chars.remove(s[left])
            left += 1
        chars.add(s[right])
        result = max(result, right - left + 1)
    return result

# Example usage
print(length_of_longest_substring("abcabcbb"))  # Output: 3
