# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.



# Restate: 
## Find the two positions whose number add up to target
# Example:
## [2, 7, 11, 15], target 9 -> at 2, I need 7 (9-2). 7 comes next so [0, 1]
# Plan:
## Walk through th elist once, for each number, work out the partner needed (target - number)
## If I've already seen that partner, I'm done, if not, remenber te number and its index in a dictionnary and move on. 
def two_sum(nums, target):
    # Outline (write your plan here first):
    #   ...
    # TODO: return the indices [i, j] (i < j) of the two numbers in `nums` that add up
    #   to `target`. Assume there is exactly one answer.
    seen = {}
    for j in range(len(nums)):
        need = target - nums[j]
        if need in seen:
            return [seen[need], j]
        seen[nums[j]] = j
    return []


# Restate: 
## Buy one day, sell on a later day, make the biggest gain (or 0)
# Example:
## [7, 1, 5, 3, 6, 4] -> cheapest so far is 1, selling at 6 later gives 5/
# Plan:
## Walk through the prices once. Keep the loswest price seen so far. For each 
## price, the best profit if I sold today is (today - lowest so far). Keep the best
def max_profit(prices):
    # Outline:
    #   ...
    # TODO: `prices[i]` is a stock price on day i. Return the most profit obtainable by
    #   buying on one day and selling on a LATER day. If no profit is possible, return 0.
    lowest = None
    best = 0
    for price in prices:
        if lowest is None or price < lowest:
            lowest = price
        elif price - lowest > best:
            best = price - lowest
    return best

# Restate: 
## Find the in-a-row block with the biggest sum
# Example:
## [-2, 1, -3, 4, -1, 2, 1, -5, 4], -> 4 + -1 + 2 + 1 = 6
# Plan:
## At each member, decide: extend the block I was building, or start fresh her? 
## If the running block is negative, starting fresh is better. Keep the biggest running sum I ever saw. 
def max_subarray(nums):
    # Outline:
    #   ...
    # TODO: return the largest sum of any contiguous (in-a-row) block of numbers in
    #   `nums`. The list has at least one number.
    current = nums[0]
    best = nums[0]
    for i in range(1, len(nums)):
        current = max(nums[i], current + nums[i])
        best = max(best, current)
    return best

# Restate: 
## Every bracket must close, in the right order
# Example:
## "([)]" -> ')' arrives but the last open bracket is '[', so false
# Plan:
## Use a list as a stack. Opening bracket -> push it. Closing bracket -> the top ot the stack must 
## be its matching opener, otherwise False. At the end the stack must be empty.
def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in pairs:
            if len(stack) == 0:
                return False
            if stack[-1] != pairs[ch]:
                return False
            del stack[-1]
    return len(stack) == 0


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    print(two_sum([2, 7, 11, 15], 9))                       # [0, 1]
    print(max_profit([7, 1, 5, 3, 6, 4]))                   # 5
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))    # 6
    print(is_balanced("{[]}"))                              # True
    


if __name__ == "__main__":
    main()
