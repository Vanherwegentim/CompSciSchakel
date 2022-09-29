# Handy functions

## no import

**replicate n m:** copy m n times, **example**: replicate 4 x = [x,x,x,x] 

**replicateM**__: Same as replicate but used in **IO**

**length**: returns the size of the list

**lookup**: lookup key assocs looks up a key in an association list

![image-20220808184524519](img/image-20220808184524519.png)

**map**: Take a function and a list and applies that function to every element in the list.

**filter**: Takes a predicate a list and filters out all elements that to do not pass the predicate

**pred**: Returns preceding item in an enumeration (integers and characters in the following examples).

![image-20220827161118908](img/image-20220827161118908.png)

**succ**: Returns following item in an enumeration (integers and characters in the following examples).

![image-20220827161214578](img/image-20220827161214578.png)

![image-20220828175107941](img/image-20220828175107941.png)

## import Data.List (nub,intersperse)

**nub:** removes duplicates from a list

**intersperse y xs**: intersperse function takes an element and a list and puts that element between the elements of the list, **example**: intersperse ',' "abcde" = "a,b,c,d,e"

**delete**: removes the first occurrence of the specified element from its list argument

**filter:** returns the minimum value from the list



