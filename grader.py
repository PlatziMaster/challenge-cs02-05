"""PS05 Grader."""

import sys

from solution import Solution, Block


def parse_test_case():
    """Parse test case."""
    name, n, halts = input(), int(input()), int(input()) == 1  # pylint: disable=C0103
    s_block = Block(None)
    current = s_block
    data = [None] * n
    for i in range(n):
        tmp_block = Block(f"B{i+1:03}")
        current.next = tmp_block
        current = tmp_block
        data[i] = current
    if not halts:
        src, dest = int(input()), int(input())
        data[src].next = data[dest]
    return name, s_block.next, halts


if __name__ == '__main__':
    test_case_name, init_block, want_result = parse_test_case()
    solution = Solution()
    if solution.does_it_halt(init_block) != want_result:
        print(f"\t❌ Test case #{test_case_name} failed")
        sys.exit(1)
    print(f"\t✅ Test case accepted #{test_case_name}")
