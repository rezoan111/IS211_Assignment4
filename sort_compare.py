import random
import time

# Week 4 - Part II
# Here I compare 3 sorting algorithms and see which one is faster (average case).
# I use random lists of size 500, 1000, 5000 and run each sort on 100 lists.
# I time each sort and print the average time.

NUM_LISTS = 100
SIZES = [500, 1000, 5000]
RANDOM_MAX = 1_000_000


def insertion_sort(a_list):
    # insertion sort from the reading
    start = time.perf_counter()

    for i in range(1, len(a_list)):
        current_value = a_list[i]
        position = i

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position -= 1

        a_list[position] = current_value

    end = time.perf_counter()
    return a_list, end - start


def shell_sort(a_list):
    # shell sort from the reading (gap insertion sort)

    def gap_insertion_sort(lst, start_pos, gap):
        for i in range(start_pos + gap, len(lst), gap):
            current_value = lst[i]
            position = i

            while position >= gap and lst[position - gap] > current_value:
                lst[position] = lst[position - gap]
                position -= gap

            lst[position] = current_value

    start = time.perf_counter()

    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_pos in range(sublist_count):
            gap_insertion_sort(a_list, start_pos, sublist_count)
        sublist_count //= 2

    end = time.perf_counter()
    return a_list, end - start


def python_sort(a_list):
    # wrapper for Python built-in sort()
    start = time.perf_counter()
    a_list.sort()
    end = time.perf_counter()
    return a_list, end - start


def _avg_time(times):
    return sum(times) / len(times)


def main():
    for n in SIZES:
        # make 100 random lists of size n
        lists = [
            [random.randint(1, RANDOM_MAX) for _ in range(n)]
            for _ in range(NUM_LISTS)
        ]

        ins_times = []
        shell_times = []
        py_times = []

        # run each sort on a copy of the list so they all get same input
        for lst in lists:
            _, t1 = insertion_sort(lst[:])
            ins_times.append(t1)

            _, t2 = shell_sort(lst[:])
            shell_times.append(t2)

            _, t3 = python_sort(lst[:])
            py_times.append(t3)

        print(f"Insertion Sort took {_avg_time(ins_times):10.7f} seconds to run, on average")
        print(f"Shell Sort took {_avg_time(shell_times):10.7f} seconds to run, on average")
        print(f"Python Sort took {_avg_time(py_times):10.7f} seconds to run, on average")


if __name__ == "__main__":
    main()
