## Summary of LeetCode

(use four # to declare the title of each problem.use two # to declare the tag)

## Array



#### 48. Rotate Image

You are given an *n* x *n* 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?



要用到两个重点知识，第一个是内建函数zip，从一个列表中依次抽取可iterate的元素，然后每次取出一个组成一个tuple，直到列表中的某一个iterate元素到尾则返回。返回的格式是和range一样的zip object，因此需要转化成list。

另一个重点是，如何把matrix里面的每一行作为一个element放进zip，

```python
zip(*matrix)
```

使用*来将一个列表中的元素作为参数表放进函数，这个技巧非常重要



#### 75. Sort Colors

Given an array with *n* objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

**Note:**
You are not suppose to use the library's sort function for this problem.

两个指针指向红色区域边界的下一个元素以及蓝色区域边界的下一个元素，（或者说，一个指向从左起第一个非红元素，另一个指向从右起第一个非蓝元素）遍历整个列表，如果是红色，那么和第一个指针的元素swap，i+1，red+1

如果是蓝色，那么和第二个指针的元素swap，blue+1但是i不动，因为我们还要继续检测这个位置上新换来的元素的属性。

当i到达蓝色边界时循环停止。



#### 167. Two Sum II - Input array is sorted

Given an array of integers that is already **sorted in ascending order**, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

**Input:** numbers={2, 7, 11, 15}, target=9
**Output:** index1=1, index2=2

由这一题要联想到二分查找，当我们看到题目中强调了sorted这个属性的时候，就要敏锐的感觉到可能与二分查找有关。

另外插一句题外话：

如果看到要求不能用额外的空间，就考虑two pointer的方法在内部完成。如果提到了线性的时间复杂度，那么就要考虑用DP的方式解决问题，另外如果限定了时间复杂度就是nlogn，那么可以基本确定需要采用binary search的方式来排序。

本题就是简单2Sum的一个变形，由于多了有序这样一个条件，我们可以不用借助额外的字典，而是直接从后面的元素中二分查找当前元素和sum的差。



#### 219. Contains Duplicate 

Given an array of integers and an integer *k*, find out whether there are two distinct indices *i* and *j* in the array such that **nums[i] = nums[j]**and the **absolute** difference between *i* and *j* is at most *k*.

使用hash table，将元素的位置作为value，如果元素不在字典中，那么就将该元素的当前位置作为value放入字典。

当发现该值已经在字典中，那么比较保存的位置和当前的位置直接的距离，如果小于k那么返回true，如果大于k那么就更新该元素的value为当前的位置。



#### 442. Find All Duplicates in an Array

Given an array of integers, 1 ≤ a[i] ≤ *n* (*n* = size of array), some elements appear **twice** and others appear **once**.

Find all the elements that appear **twice** in this array.

Could you do it without extra space and in O(*n*) runtime?

要求不使用extra space，因此就要在下标上下功夫，把出现过一次的元素的值作为下标，找到该下标的元素将其改为string，每次判断当前的元素作为下标的单元格中的元素的数据类型，如果已经变为了String，那么说明这个下标已经被改变过，说明元素作为下标出现过了，那么就是重复的元素。

#### 26. Remove Duplicates from Sorted Array

Given a sorted array, remove the duplicates in place such that each element appear only *once* and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array *nums* = `[1,1,2]`,

Your function should return length = `2`, with the first two elements of *nums* being `1` and `2` respectively. It doesn't matter what you leave beyond the new length.

这一题的重点就在于不光要统计出个数，还要把不重复的元素放到前面。因此我们需要两个指针，

一个指针用于指示当前已完成去重区域的边界，

另一个指针依次遍历整个list

```python
int i = 0;
        for (int n : nums)
            if (i == 0 || n > nums[i-1])
                nums[i++] = n;
        return i;
```

i只有在每次出现了非重复元素时才后移，因此最后i指向的位置，就是下一个非重复元素将要被放置的位置，也就是“完成整理区”的右边界，恰好也是非重复元素的个数。



#### 80. Remove Duplicates from Sorted Array II

Follow up for "Remove Duplicates":
What if duplicates are allowed at most *twice*?

For example,
Given sorted array *nums* = `[1,1,1,2,2,3]`,

Your function should return length = `5`, with the first five elements of *nums* being `1`, `1`, `2`, `2` and `3`. It doesn't matter what you leave beyond the new length.

仍然是两个指针的问题，只不过此时当前指针的对象比较的目标是在自己两个index之前的元素，如果一样则不动pointer，else将当前num的值赋给i指向的index，然后将i后移一位。



#### 27. Remove Element

Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

**Example:**
Given input array *nums* = `[3,2,2,3]`, *val* = `3`

Your function should return length = 2, with the first two elements of *nums* being 2.

题设和上面要求去重的设置基本一致，方法也是一样的思路，使用两个指针，一个指向“整理过区域”的下一个单元格，另一个用来遍历整个array



#### 283.Move Zeroes

Given an array `nums`, write a function to move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

For example, given `nums = [0, 1, 0, 3, 12]`, after calling your function, `nums` should be `[1, 3, 12, 0, 0]`.

**Note**:

1. You must do this **in-place** without making a copy of the array.
2. Minimize the total number of operations.

和上面一题思路基本类似，两个指针，一个指向整理区，另一个用来遍历整个list，整理后将所有的非零元素按顺序放到了list的最前侧，并且遍历一遍过后第一个指针指向的位置就是结果中第一个0的位置，然后再go through range(i,len(nums))并将这个范围内的元素全部置0即可。



#### 209. Minimum Size Subarray Sum

Given an array of **n** positive integers and a positive integer **s**, find the minimal length of a **contiguous** subarray of which the sum ≥ **s**. If there isn't one, return 0 instead.

For example, given the array `[2,3,1,2,4,3]` and `s = 7`,
the subarray `[4,3]` has the minimal length under the problem constraint

设置一个指针指向当前的开始点，再设置一个指针遍历整个list从第一个元素开始向后遍历一直求和，直到sum的值满足条件大于等于s，此时将begin向前移动，观察是否仍然满足sum>=s，如果不满足则停止，继续移动指针遍历list把新的值加进来直到sum再次大于s，然后重复以上过程，从已求和子数组的左侧不断推出元素观察是否仍满足sum>=s。

整个过程中使用一个变量保存截止到目前的最短子数组长度，每次改变子数组长度后更新这个变量。



#### 349. Intersection of Two Arrays

- use hashset to hash one of the array, build up a new arraylist to store the element existing in both array.
- if one element is found in another array, add it to the arraylist and then delete the key in the hashset.

  使用python的话可以简单一些，将两个list转成set。set可以采用&操作来获取交集，然后再用list()转回list。

#### 350. Intersection of Two Arrays II

- use HashMap to hash the (key,value) pair in which the key is the content and the value is the time of appearance of such content.

- In the go through process ,every time we detect whether it is in the hashmap and the appearing time is bigger than 0

- **We use the "value" in hashmap as a counter of the appearance of the key.**

- To update the time of appearance, we just put new (key,value) pair into the hashmap. the new value is updated from the value before.(we use get() method to get the past value of such key.)

  ```java
  HashMap <Integer,Integer> hs 
    = new HashMap <Integer,Integer>();
  for (int i=0;i<nums1.length;i++){
  	if (hs.containsKey(nums1[i]))
  		hs.put(nums1[i],hs.get(nums1[i])+1);
  	else
  		hs.put(nums1[i],1);
      }
  ```




#### 345. Reverse Vowels of a String

Write a function that takes a string as input and reverse only the vowels of a string.

**Example 1:**
Given s = "hello", return "holle".

**Example 2:**
Given s = "leetcode", return "leotcede".

**Note:**
The vowels does not include the letter "y".

读题，分析可以看出要将元音字符reverse，因此先要跟踪到整个字符串中的“元音字符子字符串”。记录下这个子字符串之后再顺序遍历原有字符串，将元音字符的位置依次替换为后面的值。

这里需要注意的是，因为要求完全reverse，所以需要copy出一个新的string作为替换的对象。或者在第一次遍历到元音字符时，同时记录下位置和值。

**注意大写**



#### 238. Product of Array Except Self

Given an array of *n* integers where *n* > 1, `nums`, return an array `output` such that `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

Solve it **without division** and in O(*n*).

For example, given `[1,2,3,4]`, return `[24,12,8,6]`.

**Ans**:从左右两侧分别逼近所求值

#### 268. Missing Number

Given an array containing *n* distinct numbers taken from `0, 1, 2, ..., n`, find the one that is missing from the array.

For example,
Given *nums* = `[0, 1, 3]` return `2`.

由观察可知，数组长度即为最后一项数值，因此在不缺项的情况下总和为(1+n) *n/2, 其中n即为数组长度，用此结果减去当前数组的总和就可以知道缺少的是哪一项。



#### 163. Missing Ranges

Given a sorted integer array where **the range of elements are in the inclusive range [lower, upper]**, return its missing ranges.

For example, given `[0, 1, 3, 50, 75]`, *lower* = 0 and *upper* = 99, return `["2", "4->49", "51->74", "76->99"].`

两个指针的问题，一个指针用来遍历整个输入数组，另一个指针指向当前的位置，如果当前的元素比pre大1，那么不做任何操作并使pre移动一位，如果当前元素比pre大2，那么则说明中间有一个元素missing了，此时应在结果中添这一个元素。如差值超过2，那么则以另一种格式生成string，并放入结果数组中。然后pre移动到i的值。



#### 414. Third Maximum Number

Given a **non-empty** array of integers, return the **third** maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

两种解法，第一种维护一个长度为3的队列，然后遍历列表，用每个元素依次更新队列（不一定有实际变化）。

第二种解法，如果长度小于3，那么直接返回当前列表最大值，否则删去两次max(nums)然后再返回max(nums)就是最终想要的结果。



#### 46. Permutations

Given a collection of **distinct** numbers, return all possible permutations.

For example,
`[1,2,3]` have the following permutations:

```
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

用generator实现最简洁的backtracking方法：

```python
def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]
```

本解法略显复杂但是本质非常精妙：

以[1,2,3]为例：

不符合if条件，recur call [2,3]，仍然不符合if条件，recur call[3]，符合条件，返回一个[[3]]，此时的perm是 [3],elements 是[2,3],所以就是把当前的第一个元素放到后面的结果的所有可能位置。

当前的第一个元素是2，所有的结果就是[3]所以有两个可能，放在0位置或者放在1位置，这两个位置的下标恰巧是range(2)也就是range(len(elements))也就是当前elements的长度。此步骤之后返回[[2,3],[3,2]]然后在把1放在所有的可能位置，第一个perm是[2,3]所以1有三个位置可以放，第二个perm是[3,2]同样对应三个位置。

所以最后返回结果的顺序应该是：

```python
[1,2,3]
[2,1,3]
[2,3,1]
[1,3,2]
[3,1,2]
[3,2,1]
```

一定要注意几个重点的位置：

1 使用for循环来遍历generator时返回的是list包含的结果，所以在此处是二维list。

2 使用yield，但是配合了for循环所有就是执行到所有yield结束。

3 每次的invariant实际是数组的长度，所以每次elements[0:1]实际是当前的第一个元素。



#### 15. 3Sum

Given an array *S* of *n* integers, are there elements *a*, *b*, *c* in *S* such that *a* + *b* + *c* = 0? Find all unique triplets in the array which gives the sum of zero.

**Note:** The solution set must not contain duplicate triplets.

```
For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```

首先看到返回的不是下标而是实际的组合值，本题采用two pointer思路很容易解决。

最重要的一点是**要先使数组有序**

遍历当前数组，对于每个i，设置一个left和一个right，left是i的下一个值，right是后续数组最大值。然后每次求出三者之和，如果等于0则将当前的组合值加入结果中，如果大于零，则挪动right向左移动，反之则挪动left向右移动。这样的的操作只有在原数组有序的情况下才能成立。



#### 16. 3Sum Closet

Given an array *S* of *n* integers, find three integers in *S* such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

```
    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```

本题和上一题的思路类似，仍然使用两个指针，每一次求和之后，如果等于target，那么就返回当前值。

通过一个变量来记录当前距离target最近的一个sum，每次求出新的sum之后，把新sum到target的距离和已记录的最小距离相比，如果更小则更新sum的值。然后移动指针，如果当前sum大于target则右指针左移，反之则左指针右移。



#### 18. 4Sum

Given an array *S* of *n* integers, are there elements *a*, *b*, *c*, and *d* in *S* such that *a* + *b* + *c* + *d* = target? Find all unique quadruplets in the array which gives the sum of target.

**Note:** The solution set must not contain duplicate quadruplets.

```
For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
```

这一类的题的基本方法都是类似的，就是最内层两个指针，然后外层不断增加循环的层数。

4Sum比3Sum来说，就是在最外层i的基础上再增加一个k作为外层循环，其余均不变。



#### 454. 4Sum II

Given four lists A, B, C, D of integer values, compute how many tuples `(i, j, k, l)` there are such that `A[i] + B[j] + C[k] + D[l]` is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

**Example:**

```
Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

```

本题是4Sum的一个简单变形，变形之后的复杂度可以降低很多，因为将原有的一个数组现在拆成了4个。是得我们更加方便的采用hash的方法来简化运算。

首先遍历前两个list将所有可能的求和值作为key建立一个字典，如果出现多个tuple求和为同一个值的情况，那么就在该key的value上+1.因为最终要统计一共有多少组tuple可以满足条件。

然后在遍历下面的两个list，仍然是求出每两个下标的总和，然后在ab的字典中查找-sum是否存在。



#### 259. 3Sum Smaller

Given an array of *n* integers *nums* and a *target*, find the number of index triplets `i, j, k` with `0 <= i < j < k < n` that satisfy the condition `nums[i] + nums[j] + nums[k] < target`.

For example, given *nums* = `[-2, 0, 1, 3]`, and *target* = 2.

Return 2. Because there are two triplets which sums are less than 2:

```
[-2, 0, 1]
[-2, 0, 3]

```

**Follow up:**
Could you solve it in *O*(*n*2) runtime?

本题和上一题的思路基本一样，但是注意本题的目标是找出小于target的tripple的数量，因此我们不需要遍历确定所有情况。因此，设置好left和right之后，如果大于target，也就是说当前的三个值超过了要求，此时不可能通过改变left和i来调整使得总和更小，因此我们只好调整right指针左移。当总和小于target是，right-left之间的所有点，都可以做为当前这个left和i的条件下的right值。因此我们将此时的left和right的差值加到结果中，然后移动left继续执行同样的操作。

注意：本题上述方法能够成立的一个基本条件仍然是数组有序。



## Linked List



#### 2. Add Two Numbers

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Input:** (2 -> 4 -> 3) + (5 -> 6 -> 4)
**Output:** 7 -> 0 -> 8

设置两个变量存储每一轮中的两个链表的值，重点在于，在while循环内部每次使用if判断该节点是否已经为空，如果是空的话也仍然保持使用v1和v2只不过其中已经为空的点就是赋值为0.

这一道题的重点在于保持一个相加操作的完整性，所以关键在于while循环的终止条件是

```python
while l1 or l2 or carry:
```

由此可以保证只有当三者均归零时才终止循环。

这道题的思路非常关键，也可以认为是双指针问题的一种应用。

另外还有注意一个trick：

```python
carry, val = divmod(v1+v2+carry, 10)
```

divmod语句可以同时获得结果和余数。



#### 206. Reverse Linked List

Reverse a singly linked list.

采用三个指针的方法，首先排除边界条件，如果head为空，或者head.next为空，那么直接返回head，否则的话，

令cur = head.next, temp = cur.next然后使head.next = null然后进入循环，如果temp!=null:那么:

```python
cur.next = head
head = cur 
cur= temp
temp = temp.next
```

由此一直向后推，当temp为null时，cur指向最后一个非空元素，head指向倒数第二个非空元素，因此跳出循环之后再执行一次

cur.next = head 

head= cur

然后就可以return head 了



#### 24. Swap Nodes In Pairs

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given `1->2->3->4`, you should return the list as `2->1->4->3`.

Your algorithm should use only constant space. You may **not** modify the values in the list, only nodes itself can be changed.

由于操作了head的位置，因此先设置一个dummy，然后再生成一个current，循环继续的条件就是cur.next和cur.next.next不为空。cur指向的就是处理过的区域的最后一个element，所以初始化cur在dummy。由此，如果cur后面的元素少于两个那么就可以结束了。

而后

First = cur.next

second = cur.next.next

First.next = second.next

second.next = first 

cur.next = second

Cur = first 

先把两个要换位的元素找到，然后依次交换顺序，然后把cur指向换位置后在前面的元素，在cur本身移动到换位置后在后面的元素。



#### 234. [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

- use two pointer to find out the middle point of the linked list and reverse the first or second half. Then compare.





#### 21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

新建一个链表的头节点，相当于一个dummy，然后循环两个链表，比较两个链表当前元素的值，然后将dummy依次指向每次较小的一个节点，并在相应链表上向后走：

```python
 while(l1!=null&&l2!=null){
            if (l1.val<=l2.val){
                cur.next = l1;
                l1 = l1.next;
            }
            else{
                cur.next =l2;
                l2 = l2.next;
            }
            cur = cur.next;
        }
```



#### 141. Linked List Cycle

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

方法就是使用两个指针，其中一个每次移动单位1，另外一个每次走两步，如果存在环的话，那么第二个早晚会在某一个时间点追上第一个。



#### 142. Linked List Cycle II

Given a linked list, return the node where the cycle begins. If there is no cycle, return `null`.

**Note:** Do not modify the linked list.

本题仍然如上一题一样采用两个指针，一个快一个慢。重点在于一个数学性质：

我们假设，从head到循环的开始位置距离为A，循环的长度为B。当二倍速的指针追上一倍速的指针时，一倍速指针距离循环开始位置的距离为N，那么有：

2*（A+N） = A+B+N

左侧为2倍的一倍速指针行进的距离，右侧为2倍速指针行进的距离。

由此我们可以得到：

A+N = B

那么我们就可以知道，当前的一倍速指针已经从循环开始的位置行进了N，接下来只要再走一个A就可以回到循环开始的位置。

因为如果这时我们从head再出发一个一倍速指针，那么这两个一倍速指针将在行进A这个距离后汇合，且汇合的位置就是距离head为A的循环起始位置。



#### 160. Intersection of Two Linked Lists

Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

```
A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3

```

begin to intersect at node c1.

**Notes:**

- If the two linked lists have no intersection at all, return `null`.
- The linked lists must retain their original structure after the function returns.
- You may assume there are no cycles anywhere in the entire linked structure.
- Your code should preferably run in O(n) time and use only O(1) memory.

本题的重点其实就是，让两个链表同步到达一个节点，那么就可以找到这个节点。因为链表重叠部分的长度肯定是一样的，所以解题的思路就是：首先取得两个链表的长度，然后设置两个指针遍历两个链表，将两个链表的长度始终向相同靠拢：

如果a长，那么a先向后走，反之b向后走。如果len已经一样，那么就每次一起向后走并判断是否相等

解法二：

不用求len，如果a到了尽头就将headA的next指向b的头，同理b到了尽头就将b的next指向a，这样退出时，两个指针都恰好遍历了a+b长度的链表，如果有重叠，那就在二者第一次转头回来的时候碰到。



#### 237. Delete Node in a linked list

只允许访问当前节点的情况下，删除当前的节点。（属于链表的基本操作）

！！！把当前节点的val置为下一个节点的val，再把当前节点的next指向next.next！！！



#### 203. Remove Linked List Elements

Remove all elements from a linked list of integers that have value **val**.

**Example**
**\*Given:*** 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, **val** = 6
**\*Return:*** 1 --> 2 --> 3 --> 4 --> 5

和27题一样的设置，但是处理对象变成了链表。从操作来看，链表执行这样的操作其实更加方便一些。

遍历整个链表，每次检查当前元素的下一个元素的val，如果是目标值就改变指针跨过下一个元素。



#### 19. Remove Nth Node From End of List

Given a linked list, remove the *n*th node from the end of list and return its head.

For example,

```
   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
```

两个指针，拉开距离为n的间隔，然后依次向后走，当后面一个到达null时，前面一个的位置就是所需要的位置。

有两个难点，一个是边界条件有可能有问题，第二个问题是，因为我们要删除这个节点，因此实际上我们需要在第二个指针指向空的时候，让第一个指针指向所需节点的上一个节点，这样才能够完成删除操作。



#### 86. Partition List

Given a linked list and a value *x*, partition it such that all nodes less than *x* come before nodes greater than or equal to *x*.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given `1->4->3->2->5->2` and *x* = 3,
return `1->2->2->4->3->5`.

有一定难度的一道链表处理的题。

因为涉及到比较大规模且位置不定的重组我们需要dummy，本题适合采用两个dummy，分别指向小于x和大于x的部分的head。

两个dummy自然就对应两个cur，两个cur不断移动指向大于x和小于x部分的tail，当整个遍历原链表的过程结束时，让cur1.next指向dummy2的next，也就是将两个子链表链接起来，然后再使得cur2.next指向空，因为我们需要自行构造链表的结尾。最后返回dummy1.next

有时间要总结一下现在已经出现的链表操作，从中找一些规律，two-pointer问题似乎更加适用与形容array一类的问题。

要给链表这类问题也找到一个应用比较广泛有一定共性的方法，目前看来，dummy的设置是有一定规律可循的。



#### 147. Insertion Sort List

Sort a linked list using insertion sort.

三个指针：

pre每次都从dummy出发，最终指向比当前元素小的最大位置。

cur指向当前遍历的元素

temp用来存储cur的下一个元素，因为要把cur插入到已排序列中，所以要存储cur的下一个节点

算法可以非常简洁：

```python
dummy = ListNode(0)
        cur = head
        pre = dummy
        while(cur!=None):
            temp = cur.next
            while pre.next!=None and pre.next.val<cur.val:
                pre = pre.next
            cur.next = pre.next
            pre.next = cur
            cur = temp 
            pre = dummy
        return dummy.next
```

第一个要注意本题中生成的dummy一开始要指向None才能满足循环条件，因为每一轮的pre移动后，我们要是得cur指向pre的next，那么第一轮的移动后，cur的next就要指向dummy的next。对于第一个元素来说，我们需要它指向None，所以我们要把dummy的初始化指向None。

第二个要注意本题的内层循环条件是pre的next不是None，并且pre的next比当前的元素小。

第三就是要注意确定插入位置之后的赋值语句的顺序。





## Dynamic Programming



#### 264. Ugly Number II

Write a program to find the `n`-th ugly number.

Ugly numbers are positive numbers whose prime factors only include `2, 3, 5`. For example, `1, 2, 3, 4, 5, 6, 8, 9, 10, 12` is the sequence of the first `10` ugly numbers.

Note that `1` is typically treated as an ugly number, and *n* **does not exceed 1690**.

动态规划问题，或者也可以成为3指针问题，2，3，5各对应一个指针。ugly number的队列实际上是2，3，5三个倍数队列的并集。所以其实我们的目标就是找到下一个元素应该从哪一个队列中选取，这个选择的条件就是比较大小。如果被选中了，那么就要把指针后移，下一轮用当前队列的下一个元素作为候选。问题迎刃而解。



#### 70. Climbing Stairs

You are climbing a stair case. It takes *n* steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

**Note:** Given *n* will be a positive integer.

本质就是一个fibonacci问题，0，1，2，3，5，8，13....



#### 121. Best Time to Buy and Sell Stock

Say you have an array for which the *i*th element is the price of a given stock on day *i*.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

**Answer**:The logic to solve this problem is same as "max subarray problem" using `Kadane's Algorithm`. Since no body has mentioned this so far, I thought it's a good thing for everybody to know.

All the straight forward solution should work, but if the interviewer twists the question slightly by giving the **difference array of prices**, Ex: for `{1, 7, 4, 11}`, if he gives `{0, 6, -3, 7}`, you might end up being confused.

Here, the logic is to calculate the difference (`maxCur += prices[i] - prices[i-1]`) of the original array, and find a contiguous subarray giving maximum profit. If the difference falls below 0, reset it to zero.

```
    public int maxProfit(int[] prices) {
        int maxCur = 0, maxSoFar = 0;
        for(int i = 1; i < prices.length; i++) {
            maxCur = Math.max(0, maxCur += prices[i] - prices[i-1]);
            maxSoFar = Math.max(maxCur, maxSoFar);
        }
        return maxSoFar;
    }
```

本质上也是两个值，重点在于，maxCur每次要累加之后和0做比较。



#### 122. Best Time to Buy and Sell Stock II

Say you have an array for which the *i*th element is the price of a given stock on day *i*.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

本题的解法比较脑残，从题目的设置中我们可以看出，当前这种购买和卖出的规则使得我们可以获取所有利润，因此能够获取的最大利润其实就是所有差值之和。

因此我们只需遍历整个list，找到差值为正的情况，也就是后一个时刻的price高于前一时刻的情况，对所有正差值求和即可。



#### 198. House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight **without alerting the police**.

两条线，一条存如果抢了可以得到的最大值，一条存如果不抢可以得到的最大值。抢了的最大值是上一家的不抢+当前家的money，不抢的最大值，是上一家的两个值中更大的一个。

```python
for money in nums:
            temp = skip
            skip = max(rob,skip)
            rob = money+temp
```

最后返回rob和skip中最大的一个就可以了。



#### 243. Shortest Word Distance

Given a list of words and two words *word1* and *word2*, return the shortest distance between these two words in the list.

For example,
Assume that words = `["practice", "makes", "perfect", "coding", "makes"]`.

Given *word1* = `“coding”`, *word2* = `“practice”`, return 3.
Given *word1* = `"makes"`, *word2* = `"coding"`, return 1.

本题使用stack思想，遍历列表，每次找到一个等于两个单词其中一个的元素，就和栈中的元素对比，如果相同则再次入栈，如果不同，则求一个差并保存到结果列表中，然后再将元素入栈（为了避免遗漏，在此处不能返回）



#### 255. Paint house

There are a row of *n* houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n*3 cost matrix. For example, `costs[0][0]` is the cost of painting house 0 with color red; `costs[1][2]` is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

**Note:**
All costs are positive integers.

典型的memoize问题，转移方程为：

```python
f[n] = cost + min(f[n+1:]+f[:n])
```

其中min是对整个数组中，出去当前元素的所有其他元素的上一轮备份值去min，然后加上本轮的cost。

需要注意的是，每一轮备份的值需要先备份在一个temp中，这样就能保证本轮的min的操作的对象是上一轮的各个值，不过很神奇的是

```python
prev = [now[i] + min(prev[:i]+prev[i+1:]) for i in range(3)]

#prev is the backup value for last iter.
#prev[:i]+prev[i+1:] is the list of value except the cost of current i.
```

这样也可以保证每一轮应用的都是上一轮的值。



#### 276. Paint Fence

There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

**Note:**
n and k are non-negative integers.

使用两个变量保存上一轮的备份值，分别是上一轮diff和上一轮same的情况

```python
same ,diff= k,k*(k-1)
        while(n>2):
            temp = same
            same = diff
            diff = (temp+same)*(k-1)
            n-=1
```

新的一轮循环时，本轮的same是上一轮diff，而本轮的diff意即，本轮的颜色和上一轮不一样，因此对上一轮的颜色没有限制，也就是说上一轮的diff和same都可以作为选项，因此diff的结果就是上一轮的temp+same再乘上当前轮的可能性，因为一定和上一轮不一样，因为本轮只有k-1种可能的颜色可供选择。



#### 55. Maximum Subarray

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array `[-2,1,-3,4,-1,2,1,-5,4]`,
the contiguous subarray `[4,-1,2,1]` has the largest sum = `6`.

思路就是，从小到大依次遍历，如果之前的和为负，则i这个点的备份值为自身值，一直向后更新

```
for(int i = 1; i < n; i++){
            dp[i] = A[i] + (dp[i - 1] > 0 ? dp[i - 1] : 0);
            max = Math.max(max, dp[i]);
        }
```

每一轮都更新max_value = max（max_value,dp[i]).



#### 152. Maximum Product Subarray

Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array `[2,3,-2,4]`,
the contiguous subarray `[2,3]` has the largest product = `6`.

和上面一题的思路类似，从小到大遍历，第i个点，备份可能的最大值和最小值，

```Python
for i in nums[1:]:
            temp = max_value
            max_value = max(i*max_value,i*min_value,i)
            min_value = min(i*temp,i*min_value,i)
            pre_max = max(max_value,pre_max)
#g中存储最小值，f中存储最大值，res中存储当前的最大结果
#另外要注意，每一轮的第一项更新之前要先用temp备份好。
```



#### 416. [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)

Given a **non-empty** array containing **only positive integers**, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

**Note:**

1. Each of the array element will not exceed 100.
2. The array size will not exceed 200.

**Example 1:**

```
Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
```

首先进行判断，如果sum是奇数则直接返回False，如果是偶数则求出总和的一半作为target，问题转化为在列表中找若干项总和为target，遍历一遍列表，如果有元素比target大，返回False，否则把问题转化为0-1背包问题，

构造一个二维数组:

```python
f[N][target]
#每一个单元格中的值为放入前N个元素是否能够达到target的值，初始化为一个True和target个False
```

比如【2，2，3，5】的target=6则初始化为

​	0    1    2    3   4    5    6 

init  T    F    F    F    F    F    F

而后对于每一个列表中的元素，从左至右遍历一次，

```python
f[n] = (f[n] or f[n-i])
```

2      T    F    T    F    F    F    F

2      T    F    T    F    T    F    F

3      T    F    T    T    T    F    F

5      T    F    T    T    T    T    F

每一轮遍历f之后，检查最后一位是否为True，如果是则返回True，如果至外层循环结束仍未返回，则返回False

#### 338. Counting Bits

Given a non negative integer number **num**. For every numbers **i** in the range **0 ≤ i ≤ num** calculate the number of 1's in their binary representation and return them as an array.

**Example:**
For `num = 5` you should return `[0,1,1,2,1,2]`.

观察可知：

dp[0] = 0;

dp[1] = dp[1-1] + 1;

dp[2] = dp[2-2] + 1;

dp[3] = dp[3-2] +1;

dp[4] = dp[4-4] + 1;

dp[5] = dp[5-4] + 1;

dp[6] = dp[6-4] + 1;

dp[7] = dp[7-4] + 1;

dp[8] = dp[8-8] + 1;
..

由此发现每隔一定周期就更新被减数即可

#### 139. Word Break
Given a **non-empty** string *s* and a dictionary *wordDict* containing a list of **non-empty** words, determine if *s* can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
*s* = `"leetcode"`,
*dict* = `["leet", "code"]`.

Return true because `"leetcode"` can be segmented as `"leet code"`.

**UPDATE (2017/1/4):**
The *wordDict* parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.

因为可能在任意位置插入空格，所以要转化为ＤＰ问题，思路是，在每个位置遍历所有的列表中的单词，如果能在ｉ这个位置之前的len(w)长度匹配到一个单词，并且ｆ[i-len(w)] 也是Ｔｒｕｅ，那么则赋值为Ｔｒｕｅ，整个循环结束之后，返回最后一个单元格中的布尔类型值即为最终答案。

比如在所给字符串的７这个位置，现在我们遍历整个列表，从７向前找len(ｗｏｒｄ)这么长的一段字符串，和这个ｗｏｒｄ进行比较。如果现在的这个ｗｏｒｄ的长度为４，则拿ｓ[7-4:7]和ｗｏｒｄ进行比较，如果相等说明匹配成功，再看f[7-4]的值是否是Ｔｒｕｅ，如果是Ｔｒｕｅ则意味着前面部分的字符串也能够由一个或多个列表中元素进行匹配，那么我们就把７这个位置对应的ｆ数组中的单元格里面存入一个Ｔｒｕｅ。

生成一个长度len(s)的全false列表f，将原问题转化为背包问题，列表中的第i个元素的bool类型表示，截止到该位置以前的字符串s[:i]是否可以用dictionary中的元素拼接而成。从头至尾遍历s，在每个位置内嵌一个遍历字典的循环，遍历到i位置时：

          for w in wordDict:
               if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
                    d[i] = True
在i位置遍历整个字典，对于每个字典中的单词w，从i向前找len（w）个字符，看是否匹配，如果发生了匹配，再看i-len（w）这个位置的布尔类型是否为True，或者到了整个字符串的头部。如果满足上述两个条件，则将该i位置的布尔值置为True然后继续向后遍历。

#### 279. Perfect Squares

Given a positive integer *n*, find the least number of perfect square numbers (for example, `1, 4, 9, 16, ...`) which sum to *n*.

For example, given *n* = `12`, return `3` because `12 = 4 + 4 + 4`; given *n* = `13`, return `2` because `13 = 4 + 9`.

解决边界条件，小于4时不需要进行计算直接返回

大于4的情况下，找到第一个超出范围的平方值的底数max_index。初始化dp各个位置的值为下标（假设全部square都是1的平方）

从2至max_index依次作为i，遍历dp（小技巧：不用从0开始遍历，因为每一轮中小于i*i的位置是不可能出现变化的）

```python
for j in range(i*i,len(dp)):
               dp[j] = min(dp[j],dp[j-i*i]+1)
```

现在的问题转化成了一个完全背包问题，每次可以取1，4，9，16，25....这些物品放入包中，可以无限次选取，求最终装满背包时，最少的物品个数。或者可以具体转化为，占体积为1，4，9，16，25...等一系列物品，其价值均为1，求能够恰好装满背包的最小价值。此时就是一个“恰好”条件下的“完全”（无限次拿取）背包问题

#### 120. Triangle

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

```
triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
```

The minimum path sum from top to bottom is `11` (i.e., 2 + 3 + 5 + 1 = 11).

观察问题可以发现，由于本层选取的元素位置可能影响到下一层的元素选取，所以使用DP来自上而下计算截止到每个点的最小可能和。构造：

```python
f= [
     [0],
    [0,0],
   [0,0,0],
  [0,0,0,0]
]
```

从第一个元素开始，备份当前可能的最小和，到达当前的最小和，就是当前节点的值加上上一层可能到达节点的备份值，转移方程即：

```python
f[i][j] = triangle[i][j] + min(f[i-1][j-1],f[i-1][j])
```

要注意对于每一层最左侧和最右侧的节点，后一部分的备份值只有一个选择，解决好边界条件，问题解决。

#### 62. Unique Paths

A robot is located at the top-left corner of a *m* x *n* grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

从左上角出发，只能向下走或向右走，很典型是一个recur+memoize问题，转移方程可以写成：

```python
f[i][j] = f[i-1][j]+f[i][j-1]
```

初始化之后最上面一层和最右侧一层均为1，因为这两条路径上的节点都只有一种到达方式（以3*7为例）：

```python
f = [
  	[1,1,1,1,1,1,1]
    [1,0,0,0,0,0,0]
    [1,0,0,0,0,0,0]
]
```

从小到大依次推，最后返回右下角的值即可。

#### 64. Minimum Path Sum

Given a *m* x *n* grid filled with non-negative numbers, find a path from top left to bottom right which *minimizes* the sum of all numbers along its path.

与上面的问题类似，同样只能向下或向右走，转移方程为：

```python
f[i][j] = grid[i][j]+min(f[i-1][j],f[i][j-1])
```

初始化和上一题基本一样的风格：在最上面一行和最左侧一行分别从左到右和从上至下求和到相应元素并放入f(值是虚构的)

```python
f = [
  	[1,2,8,15,24,45]
    [3,0,0,0,0,0]
    [8,0,0,0,0,0]
]
```

从小到大一次递推，最后返回右下角的值。

#### 322. Coin Change

You are given coins of different denominations and a total amount of money *amount*. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

**Example 1:**
coins = `[1, 2, 5]`, amount = `11`
return `3` (11 = 5 + 5 + 1)

**Example 2:**
coins = `[2]`, amount = `3`
return `-1`.

一样是一个“恰好”的“完全”背包问题，每个硬币的出现次数不限。可以转化为，每个物品的体积就是硬币的面额，每个物品的价值是1，要求放入一个总容积为amount的背包，求恰好放入的情况下最小的价值。



#### 343.  Integer Break

Given a positive integer *n*, break it into the sum of **at least** two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given *n* = 2, return 1 (2 = 1 + 1); given *n* = 10, return 36 (10 = 3 + 3 + 4).

**Note**: You may assume that *n* is not less than 2 and not larger than 58.

比较简单的memoize问题，转移方程可以写为：

```python
f(n) = max(k*(n-k),k*f(n-k)| 1<=k<=n/2)
```

每个节点的备份值有两种可能，一种是当前数值直接相乘，另一种是一个作为倍数，另一个以备份值的形式拆解并相乘出备份值。

依次遍历即可解决问题。（本问题可以从数学证明上得到一个更简单的方法，但是我觉得意义不大）



#### 221. Maximal Square

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

For example, given the following matrix:

```
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

```

Return 4.

本题设置子问题有一些难度，目前看到的最好的设置子问题的方式是，生成一个初始化全为0的二维数组，每个点上的值是以该点为右下角的正方形的边长。转移公式是，如果

```python
dp[i][j] == 1
```

那么：

```python
dp[i][j] = min(dp[i][j-1],dp[i-1][j-1],dp[i-1][j])+1
```

以周围上个角的值中最小的一个作为base，在这个base的基础上加1.

最后记得要把变长平方得到面积。



#### 300. Longest  Increasing Subsequence

Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given `[10, 9, 2, 5, 3, 7, 101, 18]`,
The longest increasing subsequence is `[2, 3, 7, 101]`, therefore the length is `4`. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(*n2*) complexity.

生成一个比原有序列长1的全零序列dp，然后从左至右遍历原有序列。dp中储存的就是原有序列截止到该位置上时的最长递增子序列长度。对于每一个原有序列中的元素，向左找到所有比当前元素小的元素的位置，然后将这些位置在dp中对应的值全都添加到一个list中，然后取出list中的max元素，就是截止当前节点之前的最长递增子序列的长度，然后在此基础上加一，就是截止到这个节点的最长递增子序列长度。



## Hash

#### 1. Two Sum

Given an array of integers, return **indices** of the two numbers such that they add up to a specific target.

You may assume that each input would have **exactly** one solution.

**Example:**

```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

```

**UPDATE (2016/2/13):**
The return format had been changed to **zero-based** indices. Please read the above updated description carefully.

典型的一道hash题，记录每个经过的点的下标，若target减去当前遍历值的差值也在字典中则返回两个下标。



#### 49. Group Anagrams

Given an array of strings, group anagrams together.

For example, given: `["eat", "tea", "tan", "ate", "nat", "bat"]`, 
Return:

```
[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
```

**Note:** All inputs will be in lower-case.

写一个子函数用来判断当前元素的组成，返回一个长度为26的列表，每一位是这个字幕在当前字符中出现的次数。

然后把这个返回的list转化为tuple作为字典的key，如果出现同样的key，那么就把新的字符串也加到value的列表中。

Trick，设置一个index指针指向新的二元列表中的一个新元素，然后将key对应的value设置为这个index，由此通过字典的映射，就可以知道这个元素将被添加到哪一个list中。

最后返回整个二元列表。



#### 202. Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

**Example: **19 is a happy number

- 12 + 92 = 82
- 82 + 22 = 68
- 62 + 82 = 100
- 12 + 02 + 02 = 1

本题的难度不高，写一个子函数用来拆分integer，返回一个list。再写一个子函数用于将list中的元素全部平方求和。然后判断结果是否在hashset中，如果不在则添加该元素。

直到该元素为1，则返回True。

若出现了重复元素，则返回False。



#### 136. Single Number

Given an array of integers, every element appears *twice* except for one. Find that single one.

**Note:**
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

原题是一道比较典型的Hash题目，建立一个hashtable存储每个元素出现的次数，最后将出现次数为1的元素返回。

但是可以使用一个Trick

```python
result^=i
```

这个操作可以去重

1^2^2 = 1

连续两次操作同一个数会抵消掉实际效果。



#### 325. Maximum Size Subarray Sum Equals K

Given an array *nums* and a target value *k*, find the maximum length of a subarray that sums to *k*. If there isn't one, return 0 instead.

**Note:**
The sum of the entire *nums* array is guaranteed to fit within the 32-bit signed integer range.

**Example 1:**

Given *nums* = `[1, -1, 5, -2, 3]`, *k* = `3`,
return `4`. (because the subarray `[1, -1, 5, -2]` sums to 3 and is the longest)

**Example 2:**

Given *nums* = `[-2, -1, 2, 1]`, *k* = `1`,
return `2`. (because the subarray `[-1, 2]` sums to 1 and is the longest)

**Follow Up:**
Can you do it in O(*n*) time?

使用两个变量来存储信息，acc存储截止到当前节点的总和，ans存储当前出现的总和等于k的最长子串的长度。

使用一个hash mp来存储已经出现过的数值，以到此节点的acc为key，value是当前节点的index，然后在每个节点上检查acc-k是否在mp中，如果已经出现在map中，说明mp[acc-k]这个index和当前的index之间的和就是k，所以这两个节点的差值就是一个可能的answer。

每次更新answer取max保证ans变量存储的一直都是最大值。初始化为0，如果从头到尾没有更新过ans说明没有总和为k的子串于是返回其初始化值0.



## String



#### 5. Longest Palindromic Substring

Given a string **s**, find the longest palindromic substring in **s**. You may assume that the maximum length of **s** is 1000.

**Example:**

```
Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.

```

**Example:**

```
Input: "cbbd"

Output: "bb"
```

遍历整个字符串，每一次指针，对于最长的palindromic来说只有两种情况，加1或加2

aab+b=aabb 2->4

aa+a = aaa 2->3

所以只需要记住当前最长的回文长度，每次从第i个节点向前找maxlen或maxlen-1两种情况看这个范围内的字符串是否是回文。

注意，每次找到回文之后，要移动指向回文substring起点的字符串，因为最后我们需要返回的不只是一个长度，所以我们遍历之后不能只记录一个长度。



#### 12. Integer To Roman

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

不要把问题想的太难，要找到问题背后的突破点。因为最大值就是3999，所以在最高位上只有四种可能：

M = ["", "M", "MM", "MMM"]

同理剩下的几位也都只有几种可能性，

所以我们用四个列表把4位上的各种可能性都包含在里面，并且是得num/1000的值正好就是列表的下标，由此就能极为简便的通过一个组合的方式将integer变为罗马字符。



#### 14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

边界条件，如果list中只有一个元素那么直接返回这个元素的长度。

否则从第一个元素和第二个元素中找到common prefix，然后以此为基准遍历整个列表，一旦发现不相等的情况就剪短comon的长度继续查找。

最后返回common



#### 67. Add Binary

Given two binary strings, return their sum (also a binary string).

For example,
a = `"11"`
b = `"1"`
Return `"100"`.

两个重点的用法：

- 使用int将字符串转化为整形数时，可以附加一个转换的进制参数。

  如果附加的参数为2的话，那么也就是按照二进制将字符串转化为实际数值，所以会返回一个2

  ```python
  int("10",2) = 2
  int("10") = 10
  ```

- 二进制加法：

  ```python
  "{0:b}".format(i1+i2)
  # https://docs.python.org/3.6/library/stdtypes.html#str.format
  ```



#### 344. Reverse String

- toCharArray convert the String into char[], and then use StringBuilder to append each char from the end. Then use toString() to convert back to String.



#### 383. Ronsom Note

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

**Note:**
You may assume that both strings contain only lowercase letters.

```
canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
```

先统计第二个字符串中各个元素出现的次数，然后遍历第一个字符串，将字典中每个出现过的字符的值减1，如果出现了0或者字典中没有这个字符的话，返回False



#### 13. Roman to Integer

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

首先建立一个字典，把每个罗马字母对应的阿拉伯数字的值建立映射关系。

遍历整个字符串，如果当前的字符的值小于下一个字符的值，那么在sum上加当前字符所代表值的负数

“CM” = -100+1000 = 900

#### 151. Reverse word in a string

Given an input string, reverse the string word by word.

For example,
Given s = "`the sky is blue`",
return "`blue is sky the`".

本题的一个难点在于单词之间的空格数可能不止一个，但是python中的String类提供了split函数。这一函数在没有接受参数的情况下默认参数即为空格分隔符，在默认数量未指明的条件下，默认所有数量的空格均为分隔符，所以只需要一行：

```python
return " ".join(s.split()[::-1])
```

注意.join函数的使用



## Others

#### 155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

- push(x) -- Push element x onto stack.
- pop() -- Removes the element on top of the stack.
- top() -- Get the top element.
- getMin() -- Retrieve the minimum element in the stack.

**Ans:** 在stack的基础上，每次push的时候判断是否出现了更小的元素，如果出现，那么先将现在的min备份（push）然后再push当前传入的元素。同理在pop的时候，如果当前元素就是最小的元素,那么要将self.min设置为再一次pop出的元素(因为刚才的次最小值已经备份在了这个元素的前一个位置)



#### 20. Valid Parentheses

Given a string containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

The brackets must close in the correct order, `"()"` and `"()[]{}"` are all valid but `"(]"` and `"([)]"` are not.

典型的使用stack的问题，每次遍历到左括号就入栈，如果遇到右括号就将栈顶元素推出匹配，如果匹配成功则继续遍历，如果失败则返回False

全部遍历结束后，如果栈空间为空则说明全部完美匹配，返回True。否则说明有元素没有匹配成功，返回False。



#### 22. Generate Parentheses

Given *n* pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given *n* = 3, a solution set is:

```
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
```

采用recursion 的方式解题，设定invariant为left paren的数量，每次迭代各种添加左和右两种情况，当剩余可以添加的左等于0并且此时没有右可以添加时结束。

这个题目的重点是从后向前的recur思想，其实也就是所谓的backtracking思想。我们在程序中写两个recur入口，分别是left和right，如果沿着程序的执行路径来看，会一直添加到没有左可以用，然后开始一直添加右，也就是返回

（（（）））

然后回到倒数第二层的调用，也就是（（，执行一个右，到达：

（（）然后继续执行（，到达

（（）（））然后再返回添加右

周而复始。

值得注意的就是，backtracking其实也是recursion，recursion只是这种回环调用的一种结构，但是backtracking其实说明的就是一种可以返回到上一层然后继续执行“兄弟选项”的能力。

我之前理解的recur都是一条路走到黑的recur，也就是不断在一条路径上一直走下去。或者单写一个分叉程序，那样的结构就非常冗余。



#### 60. Permutation Sequence

The set `[1,2,3,…,*n*]` contains a total of *n*! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for *n* = 3):

1. `"123"`
2. `"132"`
3. `"213"`
4. `"231"`
5. `"312"`
6. `"321"`

Given *n* and *k*, return the *k*th permutation sequence.

**Note:** Given *n* will be between 1 and 9 inclusive

本题其实是一个数学问题，最重要的性质是：

k／(n-1)!的除数就是起始的数字

比如n=3时，k=4，4/2 = 2所以一定是以range(1,10)的第二项作为起始。

由此可以recur求得答案，每次的k等于k/(n-1)!的余数。也就是确定了某一位之后的偏移量。





## Backtracking

#### 79. Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given **board** =

```
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
```

典型的dfs解题，使用dfs方法遍历所有可能。

nested function传入i j k.

k是一个指针，指向当前需要的word中字符

如果ij越界，返回false，如果当前节点不等于word中的对应元素，返回false，如果当前的ij位置的字符和k位置的字符串中的字符一致则进行dfs，首先判断k时候已经到达末尾，如果到达末尾说明最后一个字符已经完成了匹配，那么返回True，否则分别对上下左右四个方向进行DFS，注意两点：

recur DFS时k指针的位置要向后移动，因为当前的k位置的字符已经得到了匹配。

要有explored集合，本题中可以采用将每个遍历过的元素的值用temp储存起来然后将本位置的值置为inf或者其他不可能出现的重复值。注意在当前节点回溯时要将temp值放回去。



#### 39. Combination Sum

Given a **set** of candidate numbers (**C**) **(without duplicates)** and a target number (**T**), find all unique combinations in **C** where the candidate numbers sums to **T**.

The **same** repeated number may be chosen from **C** unlimited number of times.

**Note:**

- All numbers (including target) will be positive integers.
- The solution set must not contain duplicate combinations.

For example, given candidate set `[2, 3, 6, 7]` and target `7`, 
A solution set is: 

```
[
  [7],
  [2, 2, 3]
]
```

本题也属于典型的backtrack类题目，首先进行排序，来简化后续运算。

然后从第一个元素开始recur，维护两个变量，一个保存当前的队列，一个保存当前队列的总和，如果总和等于k，那么把当前队列中的元素作为一个结果添加到results中，否则如果小于k那么就继续recur到后续的队列中，如果大于k那么则pop出当前队列中的最后一个元素，然后返回到上一层。

 

#### Combinations

Given two integers *n* and *k*, return all possible combinations of *k* numbers out of 1 ... *n*.

For example,
If *n* = 4 and *k* = 2, a solution is:

```
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
```

典型的回溯问题，设置一个length，一个cur，当length==k，cur加入results，然后回溯。



#### 93. Restore IP Addresses

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given `"25525511135"`,

return `["255.255.11.135", "255.255.111.35"]`. (Order does not matter)

设置四个指针，分别存储四部分的长度，每部分的长度可能是1，2，3 然后考虑所有组合，

如果abcd四个值相加不等于当前length，那么跳过。

否则按照当前abcd进行切分，检查四个切分后的值是否在255以内，否则跳过

最后检查当前的切分方式下，是否存在001这样的情况，检查的方式就是把值转换回string，对比两个string的长度。

如果以上均满足说明找到了一种切分方式。



第二种解法采用回溯，设置两个invariant，length和count，如果count=0时length正好也等于字符串长度，那么当前的结果就是可用的。否则返回空，while循环1到3，从当前length向后切割j长度，首先判断子字符串值是否溢出，然后判断字符串是否包含无意义0，如果都Ok那么就count-1然后传入length+j继续recur。



注意有可能出现条件是切割完的子字符串是空，此事说明提早到达了末尾，应该返回空。



#### 78. Subsets

Given a set of **distinct** integers, *nums*, return all possible subsets.

**Note:** The solution set must not contain duplicate subsets.

For example,
If **nums** = `[1,2,3]`, a solution is:

```
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
```

方法比较简朴，初始化一个[[]]，每次把新的元素加到所有现有的result中的list里面作为新的list加入到result当中。

```python
res += [item+[num] for item in res]
```



#### 131. Palindrome Partitioning

Given a string *s*, partition *s* such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of *s*.

For example, given *s* = `"aab"`,
Return

```
[
  ["aa","b"],
  ["a","a","b"]
]
```

仍然是比较典型的回溯问题，用一个helper来判断当前字符串是不是回文，recur函数使用一个cur保存当前分割结果，使用一个指针指向下一个元素。当指针溢出字符串长度时cur中的内容就是一个可能结果。while循环从当前i开始向后不断加1，while循环内部首先判断当前的l到i之间的部分是否形成了回文。



