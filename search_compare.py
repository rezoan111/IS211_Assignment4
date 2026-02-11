import random
import time

# Week 4 - Part I
# Here I compare 4 search algorithms and see which one is faster (worst case).
# Worst case = searching for something that is NOT in the list.
# Lists are only positive ints, so 99999999 should never be in the list.

TARGET = 99999999
NUM_LISTS = 100
SIZES = [500, 1000, 5000]
RANDOM_MAX = 1_000_000


def sequential_search(a_list, item):
    # normal sequential search (not sorted)
    start = time.perf_counter()

    for x in a_list:
        if x == item:
            end = time.perf_counter()
            return True, end - start

    end = time.perf_counter()
    return False, end - start


def ordered_sequential_search(a_list, item):
    # ordered sequential search (list must be sorted)
    start = time.perf_counter()

    for x in a_list:
        if x == item:
            end = time.perf_counter()
            return True, end - start

        # early stop because list is sorted
        if x > item:
            break

    end = time.perf_counter()
    return False, end - start


def binary_search_iterative(a_list, item):
    # iterative binary search (list must be sorted)
    start = time.perf_counter()

    low = 0
    high = len(a_list) - 1

    while low <= high:
        mid = (low + high) // 2

        if a_list[mid] == item:
            end = time.perf_counter()
            return True, end - start
        elif item < a_list[mid]:
            high = mid - 1
        else:
            low = mid + 1

    end = time.perf_counter()
    return False, end - start


def binary_search_recursive(a_list, item):
    # recursive binary search (list must be sorted)

    def _helper(lst, item_, low, high):
        if low > high:
            return False

        mid = (low + high) // 2

        if lst[mid] == item_:
            return True
        elif item_ < lst[mid]:
            return _helper(lst, item_, low, mid - 1)
        else:
            return _helper(lst, item_, mid + 1, high)

    start = time.perf_counter()
    result = _helper(a_list, item, 0, len(a_list) - 1)
    end = time.perf_counter()

    return result, end - start


def _avg_time(times):
    return sum(times) / len(times)


def main():
    # For each size: 500, 1000, 5000
    # make 100 lists and run each algorithm, then print average time.
    for n in SIZES:
        lists = [
            [random.randint(1, RANDOM_MAX) for _ in range(n)]
            for _ in range(NUM_LISTS)
        ]

        # 1) Sequential Search (no sort needed)
        seq_times = []
        for lst in lists:
            _, t = sequential_search(lst, TARGET)
            seq_times.append(t)
        print(f"Sequential Search took {_avg_time(seq_times):10.7f} seconds to run, on average")

        # For the rest, list must be sorted.
        # IMPORTANT: sort before calling search so sort time is not included.

        # 2) Ordered Sequential Search
        ord_times = []
        for lst in lists:
            sorted_lst = sorted(lst)
            _, t = ordered_sequential_search(sorted_lst, TARGET)
            ord_times.append(t)
        print(f"Ordered Sequential Search took {_avg_time(ord_times):10.7f} seconds to run, on average")

        # 3) Binary Search Iterative
        bin_iter_times = []
        for lst in lists:
            sorted_lst = sorted(lst)
            _, t = binary_search_iterative(sorted_lst, TARGET)
            bin_iter_times.append(t)
        print(f"Binary Search (Iterative) took {_avg_time(bin_iter_times):10.7f} seconds to run, on average")

        # 4) Binary Search Recursive
        bin_rec_times = []
        for lst in lists:
            sorted_lst = sorted(lst)
            _, t = binary_search_recursive(sorted_lst, TARGET)
            bin_rec_times.append(t)
        print(f"Binary Search (Recursive) took {_avg_time(bin_rec_times):10.7f} seconds to run, on average")


if __name__ == "__main__":
    main()
