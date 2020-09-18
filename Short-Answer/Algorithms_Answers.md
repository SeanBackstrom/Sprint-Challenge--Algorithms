#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)exponential O(n^2) - this is because for each addition to the input size, the work is doubled in the loop. (There is 3 * n's in the loop, and 2 in the algorithm)


b) O(n log n) - This is because there is a logarithmic formula for every one input inside the loop. this is because j*= 2 reduces the time for every input size, and doesnt have to go through every single input before the link breaks. 

c) linear O(n) - this is because it simply hits every input once, checking for a condition with each one.

## Exercise II\
>n-story building
> floor f , egg breaks

this algorithm is a quasi-Binary search the floors of the building. It cuts in half, then recurses, adding or subtracting 1 so that it can find the exact floor, characterized by a condition

function(n, midpoint= n // 2):

    if n[midpoint] == break and n[midpoint-1]  == nobreak:
        f = midpoint
        return f


    Drop egg from n[midpoint-1]:

        if it doesn't break:
            recurse function(n, midpoint=midpoint+1)
        if it does break:
            recurse function(n, midpoint=midpoint-1)
    



