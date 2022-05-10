# Oefenzittingen



## Oefenzitting 2

### Vraag 1

**(warmup) Show, in the style of the trace given with partition (p. 291), how that method partitions the array E A S Y Q U E S T I O N. (For the purpose of this exercise, ignore the initial shuffle.) (2.3.1)**

ik ga dit met getallen doen want letters maakt het gewoon een stuk moeilijker dan het moet zijn.

8,3,7,2,12,6,5,1,9,10,2,4,11



First we choose the pivot, we will use the median of the first, middle and last elements. [5,6,8,11]. We take 6 as our pivot

| initial values                     | 8,3,7,2,12,6,5,1,9,10,4,11                                   |
| ---------------------------------- | ------------------------------------------------------------ |
| 6 as pivot                         | 4,3,7,2,12,6,5,1,9,12,8,11<br />4,3,1,2,12,6,5,7,9,12,8,11<br />4,3,1,2,5,6,12,7,9,12,8,11 |
| 3 as pivot for our first partition | 4,3,1,2,5<br />2,3,1,4,5<br />                               |
|                                    |                                                              |
|                                    |                                                              |

