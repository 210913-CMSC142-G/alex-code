# Subset Sum
Weighted Set Problems

CMSC 142 G  
Alexis Cacayuran


## Problem
Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum. 

**Input**: set[] = {3, 34, 4, 12, 5, 2}, sum = 9  
**Output**: True  
_There is a subset (4, 5) with sum 9._

## Subset
**Example.**  
A = {1, 2, 3}  
The following subsets are:  
1. { } (empty set)
2. {1}
3. {2}
4. {3}
5. {1,2}
6. {1,3}
7. {2,3}
8. {1,2,3}

Array size: 3  
Number of subset: `2^n = 2^3 = 8` subsets  
Time Complexity (Brute force method): `O(2^n)`  


## Brute Force Method (Recursion)
Approach: For the recursive approach we will consider two cases. 

1. Include the last element and now the required sum = target sum – value of ‘last’ element and number of elements = total elements – 1
2. Exclude the ‘last’ element and now the required sum = target sum and number of elements = total elements – 1

Following is the recursive formula for isSubsetSum() problem.

`isSubsetSum(set, n, sum) = isSubsetSum(set, n-1, sum) || isSubsetSum(set, n-1, sum-set[n-1])`

Base Cases:

1. `isSubsetSum(set, n, sum) = false, if sum > 0 and n == 0`  
2. `isSubsetSum(set, n, sum) = true, if sum == 0 `

Simulation of above approach:

```
set[] = {3, 4, 5, 2}  
sum = 9
(x, y) = 'x' is the left number of elements,
'y' is the required sum
  
              (4, 9)
             {True}
           /        \  
        (3, 6)       (3, 9)
               
        /    \        /   \ 
     (2, 2)  (2, 6)   (2, 5)  (2, 9)
     {True}  
     /   \ 
  (1, -3) (1, 2)  
{False}  {True} 
         /    \
       (0, 0)  (0, 2)
       {True} {False}
```
![Subset-Sum-Problem1](https://user-images.githubusercontent.com/69415093/146544492-2f6ec6b2-d5d1-483b-be4d-d0f001fe4864.jpg)

#### Code Implementation (Java)
```
// A Dynamic Programming solution for subset
// sum problem
class SubsetSum{
 
    // Returns true if there is a subset of
    // set[] with sum equal to given sum
    static boolean isSubsetSum(int set[],
                               int n, int sum)
    {
        // The value of subset[i][j] will be
        // true if there is a subset of
        // set[0..j-1] with sum equal to i
        boolean subset[][] = new boolean[sum + 1][n + 1];
 
        // If sum is 0, then answer is true
        for (int i = 0; i <= n; i++)
            subset[0][i] = true;
 
        // If sum is not 0 and set is empty,
        // then answer is false
        for (int i = 1; i <= sum; i++)
            subset[i][0] = false;
 
        // Fill the subset table in bottom
        // up manner
        for (int i = 1; i <= sum; i++) {
            for (int j = 1; j <= n; j++) {
                subset[i][j] = subset[i][j - 1];
                if (i >= set[j - 1])
                    subset[i][j] = subset[i][j] || subset[i - set[j - 1]][j - 1];
            }
        }
 
        for (int i = 0; i <= sum; i++){
            for (int j = 0; j <= n; j++){
                if(subset[i][j] == true){
                System.out.print("T" + "\t");
                }else{
                    System.out.print("F" + "\t");
                }
            }
            System.out.println();
        }

 
        return subset[sum][n];
    }
 
    /* Driver code*/
    public static void main(String args[])
    {
        int set[] = { 2, 3, 7, 8, 10};
        int sum = 11;
        int n = set.length;
        if (isSubsetSum(set, n, sum) == true)
            System.out.println("Found a subset with given sum");
        else
            System.out.println("No subset with given sum");
    }
}
 
/* This code is contributed by Rajat Mishra */
```

Output:  
```
T       T       T       T       T       T
F       F       F       F       F       F
F       T       T       T       T       T
F       F       T       T       T       T
F       F       F       F       F       F
F       F       T       T       T       T
F       F       F       F       F       F
F       F       F       T       T       T
F       F       F       F       T       T
F       F       F       T       T       T
F       F       F       T       T       T
F       F       F       F       T       T
Found a subset with given sum
```
## References

\[1\] [Subset Sum Problem. https://www.geeksforgeeks.org/subset-sum-problem-dp-25/?ref=lbp](https://www.geeksforgeeks.org/subset-sum-problem-dp-25/?ref=lbp "Reference 1")  
\[2\] [Visual Explanation for the Subset Sum Problem. https://www.youtube.com/watch?v=PdQIG0Qe_a8&t=602s](https://www.youtube.com/watch?v=PdQIG0Qe_a8&t=602s "Reference 2")  
\[3\] [Dynamic Programmming Approach. https://www.youtube.com/watch?v=s6FhG--P7z0&t=482s](https://www.youtube.com/watch?v=s6FhG--P7z0&t=482s "Reference 3")  
