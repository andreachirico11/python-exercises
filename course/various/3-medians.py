
# 0.0.4 4. Medians
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays.
# e.g.,
# 1
# 1. nums1 = [1, 3] nums2 = [2]
# The median is 2.0
# 2. nums1 = [1, 2] nums2 = [3, 4]
# The median is (2 + 3)/2 = 2.5


def find_median(arr1, arr2):
    merged = sorted(arr1 + arr2)
    merged_mid = int(len(merged) / 2)
    if len(merged) % 2 == 0:
        return (merged[merged_mid + 1] + merged[merged_mid]) / 2
    return merged[merged_mid]


print(find_median([1, 3], [2]))
print(find_median([1], [3, 4]))
print(find_median([1, 2], [3, 4]))


# 0.0.5 5. Medians
# Can you solve 4. by using a single loop?

arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 10
arr2 = [11, 12, 13, 14, 15, 16, 17, 18, 19]  # 9


def initialize_view(actual_view, arr):
    if not actual_view:
        return {"start": 0, "end": len(arr) - 1}
    return actual_view


def get_view_median(view):
    return ((view["end"] - view["start"]) // 2) + view["start"]


def start_is_end(arr_view):
    return arr_view["start"] == arr_view["end"]


def get_start_slice(arr, arr_view):
    return [arr[arr_view["start"]]]


def get_slice(arr, arr_view):
    return arr[arr_view["start"]: arr[arr_view["end"]]]


def get_middle_from_sorted(arr):
    return sorted(arr)[1]


def medians_recursive(arr1, arr2, arr1_view={}, arr2_view={}):
    arr1_view = initialize_view(arr1_view, arr1)
    arr2_view = initialize_view(arr2_view, arr2)
    median_1 = get_view_median(arr1_view)
    median_2 = get_view_median(arr2_view)
    if start_is_end(arr1_view) and start_is_end(arr2_view):  # stesso numero di elementi
        return (get_start_slice(arr1, arr1_view)[0] + get_start_slice(arr2, arr2_view)[0]) / 2
    # arr2 ha un elemento in piu
    elif start_is_end(arr1_view) and not start_is_end(arr2_view):
        return get_middle_from_sorted(get_start_slice(arr1, arr1_view) + get_slice(arr2, arr2_view))
    # arr1 ha un elemento in piu
    elif not start_is_end(arr1_view) and start_is_end(arr2_view):
        return get_middle_from_sorted(get_slice(arr1, arr1_view) + get_start_slice(arr2, arr2_view))
    else:  # piu di un elemento negli array
        if arr1[median_1] <= arr2[median_2]:
            arr1_view["start"] = median_1
            arr2_view["end"] = median_2
        else:
            # CASE arr1[median_1] > arr2[median_2]
            arr1_view["end"] = median_1
            arr2_view["start"] = median_2
        return medians_recursive(arr1, arr2, arr1_view, arr2_view)


print(medians_recursive(arr1, arr2))
