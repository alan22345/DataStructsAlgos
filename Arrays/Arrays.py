# reorder for even first

def even_odd (A) :
    next_even, next_odd = 0, len(A) - 1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else :  
            A[next_even], A[next_odd] = A[next_odd],A[next_even]
            next_odd -= 1

    return A

# Write a program that takes an array A and an index i into A, and rearranges the elements such
# that all elements less than A[r] (the "pivot") appear first, followed by elements equal to the pivot,
# followed by elements greater than the pivot.

def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    smaller, equal, larger = 0,0,len(A)

    while equal < larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]
    return A

a = [-999,1,23,4,5,543,431,-3,-4,-531,0,12,305,97]

# Write a program which takes as input an array of digits encoding a nonnegative decimal integer
# D and updates the array to represent the integer D + 1. For example, if the input is (7,2,9) then
# you should update the array to (1,3,0). Your algorithm should work even if it is implemented in a
# language that has finite-precision arithmetic.

def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1,len(A))):
        if A[i] != 10:
            break 
        A[i] = 0
        A[i-1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(1)
    return A

# print(plus_one([2,0,0,0]))

# we can use a similar algo with a few extra steps for multiplying numbers 

# for a game where a list is a board, you can advance only as far as the number in the array that
# you land on says e.g. for an array[3,3,1,0,2,0,1] we can go A[0], A[1], A[4], A[6] and we win by 
# reaching the end
# write a program that takes an array of ints, and returns whether its possible to advance to the 
# last tile and the maxing you can advance if you cant reach the final tile

def canReachEnd(A):
    furthest_reach_so_far, last_index = 0, len(A) - 1
    i = 0
    while i <= furthest_reach_so_far and furthest_reach_so_far < last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, A[i] + i)
        print(furthest_reach_so_far)
        i += 1
    return furthest_reach_so_far >= last_index 

b = [3,3,1,0,2,0,1]
# print(canReachEnd(b))

# create a set out of a list 
def mySet(A):
    write_index = 1
    for i in range(1,len(A)):
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    A = A[:write_index]
    return A

# print(mySet([1,1,1,2,2,3,4,5,6,7,7,7]))

# buy and sell a stock at the highest price
# given an array with a bunch of stock prices find when it is most profittable to buy and sell

def buyAndSellStock(prices):
    minPriceSoFar, maxProfit = float('inf'),0.0
    for price in prices:
        maxProfitToday = price - minPriceSoFar
        maxProfit = max(maxProfit,maxProfitToday)
        minPriceSoFar = min(minPriceSoFar,price)
    return maxProfit

# same thing but buy and sell twice

def buyAndSellTwice(prices):
    maxTotalProfit, minPriceSoFar = 0.0, float('inf')
    firstBuySellProfits = [0] * len(prices)

    for i, price in enumerate(prices):
        minPriceSoFar = min(minPriceSoFar, price)
        maxTotalProfit = max(maxTotalProfit, price - minPriceSoFar)
        firstBuySellProfits[i] = maxTotalProfit
    
    maxPriceSoFar = float('-inf')
    reversedPrices = reversed(list(enumerate(prices[1:],1)))
    for i, price in reversedPrices:
        maxPriceSoFar = max(maxPriceSoFar, price)
        maxTotalProfit = max(
            maxTotalProfit,
            maxPriceSoFar - price + firstBuySellProfits[i-1]
        )

    return maxTotalProfit

prices = [12,11,13,9,12,8,14,13,15]
print(buyAndSellTwice(prices))