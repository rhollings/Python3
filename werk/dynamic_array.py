'''
Declare a 2-dimensional array, arr, of n empty arrays. All arrays are zero indexed.
Declare an integer, lastAnswer, and initialize it to 0.

There are 2 types of queries, given as an array of strings for you to parse:

Query: 1 x y
Let idx = ((x ^ lastAnswer) % n).
Append the integer y to arr[idx].

Query: 2 x y
Let ((x ^ lastAnswer) % n).
Assign the value  to arr[idx][y % size(arr[idx])] to lastAnswer.
Store the new value of lastAnswer to an answers array.

Complete the dynamicArray function below.

dynamicArray has the following parameters:
- int n: the number of empty arrays to initialize in arr
- string queries[q]: query strings that contain 3 space-separated integers

Return int[]: the results of each type 2 query in the order they are presented
'''

def dynamicArray(n, queries):
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    ans = []
    for query in queries:
        x = query[1]
        y = query[2]
        if query[0] == 1:
            # 1 x y
            idx = ((x ^ lastAnswer) % n)
            arr[idx].append(y)
        else:
            print(query)    
            # 2 x y
            idx = ((x ^ lastAnswer) % n)
            lastAnswer = arr[idx][y% len(arr[idx])]
            ans.append(lastAnswer)
    return ans
