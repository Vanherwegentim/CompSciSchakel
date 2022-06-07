# Gegevensstructuren en Algoritmen

## Les 1: analyse en algoritmen

### Asymptotische analyse

| Notation  | provides                  | example       | shorthand for                                | used to                   |
| --------- | ------------------------- | ------------- | -------------------------------------------- | ------------------------- |
| Tilde     | leading term              | ~ 10N^2^      | 10N^2^<br />10N^2^+22NlogN                   | provide approximate model |
| Big Theta | Asymptotic growth rate    | $\theta(N^2)$ | (1/2)N^2^<br />10N^2^<br />5N^2^ +22NlogN+3N | classify algorithms       |
| Big Oh    | $\Theta(N^2)$ and smaller | O(N^2^)       | 10N^2^<br />100N                             | develop upper bounds      |
| Big Omega | $\Theta(N^2)$ and larger  | $\Omega(N^2)$ | (1/2)N^2^<br />N^5^<br />N^3^+22NlogN + 3N   | develop lower bounds      |

![image-20220607161326933](C:\Users\timva\AppData\Roaming\Typora\typora-user-images\image-20220607161326933.png)

### Grafiek complexiteit

![image-20220607161400837](C:\Users\timva\AppData\Roaming\Typora\typora-user-images\image-20220607161400837.png)





## Les 2: Sorting Algorithms

### Selection Sort

#### **How does it work?**

The selection sort algorithm sorts an array by repeatedly finding the minimum element from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

	1.	The subarray which is already sorted
	1.	Remaining subarray which is unsorted. 

In every iteration of selection sort, the minimum element from the unsorted subarray is picked and moved to the sorted subarray. 



#### **Performance**

- Comparisons:

  - (n-1)+(n-2)+... + 1 = n(n-1)/2  **~ n^2^/2**

- Exchanges:

  - 1+1+...+1 = n-1 **~ n**

  



### Insertion sort

#### How does it work?

Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.

- Good for partially sorted arrays and small arrays.



#### Performance

- Best case
  - All elements to the left of i are smaller: 
    - Comparisons :**~n**
    - Exchanges: 0
- Worst case
  - All elements to the left of i are larger: 
    - Comparisons: **~n^2^/2**
    - Exchanges: **~n^2^/2**
- Average case
  - Half of the elements to the left of i are larger: 
    - Comparisons: **~n^2^/4**
    - Exchanges: **~n^2^/4**
    - 

### Partially sorted arrays

What happens when most elements are near their final positions?

- Selection sort: No effect, still **~ n^2^/2**
- Insertion sort: elements move only a few places: **~c.n**

On the basis of this mergesort was created.



### Merge Sort

#### **How does it work**

Quicksort is a divide and conquer algorithm. It divides the input array into two halves, calls itself for the two halves, then it merges the two sorted halves. 



#### Performance

~2k data moves and ~k compares to merge 2 arrays of length k/2

- Comparisons: **\~n.log~2~n**
- Exchanges: **\~n.log~2~n**
- But **~n** extra space required

Average/worst cases are asymptotically faster than insertion sort

Best case is asymptotically slower than insertion sort.



### How fast can sorting algorithms go

**Comparison sorts:**

**Any comparison sort needs at least ~n.logn comparisons**

Thus merge sort is asymptotically optimal!



**Non-comparison sorts, in linear (~n) time:**

- Counting sort
- Radix sort
- Bucket sort



### Lower bound for comparison sorting

All possible permutations of n elements can be made into a tree. For example, here is a compare tree for N = 3:

![image-20220607175509854](img/image-20220607175509854.png)

As you can see all the possible permutations is atleast equal to **N!** because there are N! different permutation of N distinct keys.

The max amount of leaves a tree can have is 2^h^ with h being it's height. Which means:

​								$N!\leq$ **number of leaves** $\leq 2^h$

![image-20220607180430714](img/image-20220607180430714.png)

The value of h is precisely the worst-case numbers of compares, so we can take the logarithm (base 2) of both sides of this equation and conclude that the number of compares used by any algorithm must be at least **log(N!)**. The approximation 

**The worst-case number of comparisons is the height of the tree.**

TODO

1. Toon aan dat een sorteeralgoritme, dat gebruik maakt van onderlinge vergelijkingen van elementen, steeds minstens log2(n!) vergelijkingen zal nodig hebben om algemeen een rij van n elementen te sorteren.

### Search problems (similar problem)

Minimal log(n+1)comparisons needed

-> Best search algorithms **~log(n)**





### Benadering van Stirling

**Bewijs:**

Omzetten naar natuurlijk logaritme maakt benaderen van som naar integraal mogelijk

$log_2(n!)=log_2(e)ln(n!)$

​				$=log_2(e)[ln(n) + ln(n-1)+...+ln(2)+ln(1)]$

Som van natuurlijk logaritme benaderen we door een integraal

$[ln(n) + ln(n-1)+...+ln(2)+ln(1)] \approx \int^n_1ln(x)dx$

$\int^n_1ln(x)dx = [xln(x)-x]^n_1$

​					  $= n.ln(n)-n+1$

En dus:

​	$log_2(n!) =log_2(e)ln(n!)$

​					$\approx log_2(e)[n.ln(n)-n+1]$

​					$=nlog_2(n) - nlog_2(e)+log_2(e)$

​					$=nlog_2(n) - 1.443n + 1.443$

=> $log_2(n!)~n.log_2(n)$



### Quick Sort

Most widely used sorting algorithm:

- \~1.39nlog~2~(n) comparisons on average 



Mergesort:

- ​	Recurse first (trivial), then merge (do real work)

Quicksort:

- Partition first (do real work), then recurse (trivial)



#### How it does work?

Like MergeSort, QuickSort is a Divide and conquer algorithm. It picks an element as pivot and partitions the given array around the picket pivot. Elements less than or equal go to the left of the pivot and elements greater than go to the right. When that is done it picks a new pivot in left partition and does the same thing again untill there is only one element left in each partition.



#### **Performance**

**Best Case:**

- Split is always balanced
- Partitioning takes n comparisons

=> **\~nlog~2~n**

**Worst Case:**

- 0 elements in one subarray and (n-1) elements in the other subarray
- E.g. array already sorted and first or last element is chosen as pivot.

=> **n^2^/2**

**Average Case:**

As long as Quicksort splits in proportions of n, behavior is \~𝑐nlog~2~.
c is determined by splitting fraction

=> \~1.39nlog~2~n element compares



**Quicksort can recover from bad splits**

![image-20220607222451138](img/image-20220607222451138.png)

After bad split, nlog~2~n behavior is resumed

- Extra cost ~n (lower order term)
- one bad split is ok, perhaps a few bad splits are ok as well





#### Quicksort optimizations

- Cuttoff to insertion sort for small number of elements
- Median of 3 values for pivot
  - Better probability of splitting roughly in half
- Many similar values in array
  - 3-way partitioning (less, equal, greater)



#### Summary of performance

**Average case**

- \~1.39nlog~2~n
- More compares than mergesort but often faster than mergesort in practice because of less exchanges

**Random shuffle**

- Probabilistic guarantee against worst case

**Worst case**

- \~n^2^/2 but this is so unlikely that you'll win the lottery first : )

**Many textbook implementations go quadratic if array …**

- is sorted or reverse sorted
- has many duplicates



#### Quicksort Complexiteit Bewijs

=>**\~1.39nlog~2~n**

**Aanpak 1:**

**Veronderstelling 1:** partitionering voor n elementen vraagt n+1 vergelijkingen



