# Complexity of Algorithms

### Selection Sort

Best case: $O(n^2)$

Average case: $O(n^2)$

Worst case: $O(n^2)$



### Insertion Sort

Best case: $O(n)$

Average case: $O(n^2)$

Worst case: $O(n^2)$



### Merge Sort

Best case: $O(n*log_2(n))$

Average case: $O(n*log_2(n))$

Worst case: $O(n*log_2(n))$

De hoeveelheid vergelijkingen dat mergesort maximaal nodig heeft om n elementen te sorteren kunnen we berekenen met de volgende formule:

$n^*log_2(n)-n+1$

Dus voor 6 element:

$6^*2.585-6+1 = 10.51$

Wat ongeveer 11 vergelijkingen is.



### Quick Sort

$\sim 1.39*n*log_2(n)$

Best case: $O(n*log_2(n))$

Average case: $O(n*log_2(n))$

Worst case: $O(n^2)$

All the variants are about as fast but **Hoare's** variant is way better because it does 3x as less swaps as **Lomunto**. Normal 



### Bucket Sort

Average/Best case: $O(n*log_2(\frac{n}k))$

If k is proportional to n, $\frac{n}k$ will be a constant which means the log will go away -> $O(n)$

if k is not - > $O(n*log_2(n)$

Worst case: Hard to say because our worst case would be everything in the same bucket but because we might use insertion sort in that our complexity might still be $O(n)$ or it might go to $O(n^2)$ because of best and worst case of insertion sort.



### Counting Sort

Counting sort is for all cases $O(n+k)$ where n is the size of the array and k is the range of the numbers in our array.

Array accesses: $\sim8N + 3R+1$ -> Running Time

Where R = size of your alphabet

### LSD

Since LSD will use Counting sort most of the time it will be as above but multiplicated by the amount of digits in the largest number.



Array accesses: $\sim7WN + 3WR$ -> Running time

Where R = largest number of array

​			W = width of largest number



### MSD

Could be anything but worse case it is going to be like LSD

### 

### 3-Way String Quicksort

$\sim1.39*n*log_2(n)$

Best case:

Average case:

Worst case:



### Priority Queue

Insert: $n$

del max: $1$

max: $1$

### Binary Tree

Best case:

Average case:

Worst case:



### Binary Heap

Insert: $log_2(n)$

del max: $log_2(n)$

max: $1$



### Heap Sort

$\sim2*n*log_2(n)$

Best case: $O(n*log_2(n))$

Average case: $O(n*log_2(n))$

Worst case :$O(n*log_2(n))$



### Binary Search Trees

Search:

- Average Case: $\sim 1.39*log(n)$
- Worse Case: $\sim N$
  - If the BST is unbalanced and looks like a linked list

Insert:

- Average Case: $\sim 1.39*log(n)$ 
- Worse Case:  $\sim N$

Delete:

- Average Case: $\sim \sqrt{N}$
- Worst Case: $\sim N$ 

### 2-3 Trees

Search:

- Average Case: $\sim c*log(n)$
- Worse Case: $\sim c*log(n)$

Insert:

- Average Case: $\sim c*log(n)$
- Worse Case:  $\sim c*log(n)$

Delete:

- Average Case: $\sim c*log(n)$
- Worst Case: $\sim c*log(n)$

Exact value of c unknown but close to 1

Worst Case: $O(log_2(n))$

Best Case: $O(log_3(n))$

### Red-Black Trees

Search:

- Average Case: $\sim 2*log(n)$
- Worse Case: $\sim 1.0*log(n)$

Insert:

- Average Case: $\sim 2*log(n)$
- Worse Case:  $\sim 1.0*log(n)$

Delete:

- Average Case: $\sim 2*log(n)$
- Worst Case: $\sim 1.0*log(n)$



