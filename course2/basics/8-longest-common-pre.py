'''
Longest Common Prefix
Write a function lpc() to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:lpc(["flower","flow","flight"])
Output: "fl"
Example 2:lpc(["dog","racecar","car"])
Output: ""
Explanation: There is no common prefix among the input strings.

'''


def lpc(ls):
    pref = ''
    position = 1
    while True:
        filtered_list = set([pref[0: position] for pref in ls])
        if len(filtered_list) > 1:
            break
        pref = list(filtered_list)[0]
        position += 1
    return pref


print(lpc(["flower", "flow", "flight"]))
print(lpc(["dog", "racecar", "car"]))
