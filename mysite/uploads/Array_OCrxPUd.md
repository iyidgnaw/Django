# Array

- **Contiguous area** of memory consisting of **equal-size** elements indexed by Contiguous integers.
- **CONSTANT** time access to read and write.

### Multi Dimensional Arrays
- The address of an element:

|(0,0)| | | | | | |
|---|---|---|---|---|---|---|
|(1,0) | | | | | | |
| | | | (2,3)| | | | |

address (2,3) = address (0,0) + element_size \* ((2-0) * 7 + (3-0))

- row major as shown in the following table.

|(0,0)|
|---|
| (0,2)|
| (1,1)|
| (1,2)|

### Time for common operations
|         | Add           | Remove  |
| ------------- |:-------------:| -----:|
| Beginning     | O(n) | O(n) |
| End     | O(1)      |   O(1)  |
| Middle | O(n)     |    O(n) |
- Because for the beginning and middle element, you have to re-place the whole array to make space for the new element.
- **constants time access but not constants time change!**

### Dynamic Arrays
- Store a pointer to a dynamically allocated array, and replace it with a newly-allocated array as needed.

- In the definition of the abstract class of Dynamic Array
    - Get(i): if i<0 or i>=size, return error.
    - Set(i, val): same
    - PushBack(val): add val to the end. if size=capacity, then first twice the capacity and then use a for-loop to copy elements from older array to the new one. Finally let the pointer turn to point at new array.
    - Remove(i)
    - Size()
- **Dynamic Array Resizing: **We have a pointer pointing our array, we have size indicating the current usage of the array and capacity indicating the available size of the array. When the size is equal to the capacity, we just make a bigger array and copy elements from the past and then let our pointer to point at the new array.

### Insertion-sort of array.
- Use an outer loop to consider each element in turn, and an inner loop that moves newly considered element to its proper location relative to the sorted subarray.
```java
public static void insertionSort(char[] data){
  int n = data.length;
  for(int k=1; k<n; k++){
    char cur =data[k];
    int j = k;
    while (j>0&&data[j-1]>cur){
      data[j] = data[j-1];
      j--;
    }
    data[j] = cur;
  }
}
```
### java.util Methods for Arrays:
- 
