array = [5, 2, 10, 8, 7, 1, 3, 6, 9, 4]

# Selection Sort
def selection_sort(arr):
  
  length = len(arr)

  for i in range (length - 1):
    minor = i

    for j in range(i + 1, length):
      if(arr[j] < arr[minor]):
        minor = j

    aux = arr[minor]
    arr[minor] = arr[i]
    arr[i] = aux

  return arr

"""
Explanation: 

1) In a function, which receives an array as argument, we use a 'For Loop' to iterate through the array. The first loop iterates from the first element to the penultimate. 
2) In order to be able to compare the elements, we will store the first element's position in a variable called 'minor' (because until we find an element less than it, the first one is the minor)
3) Then, we hav to iterate the array again but this time we it goes from the 'i + 1' position (always one more than the first iteration) to the last element of the list. 
4) Now that we have an element and the next one, we can compare each other. We do this using an 'If else' statement where we check if the elements in the 'j' position (second iteration) are less than the element in the 'i' position (the first iteration).
5) In each iteration (the second one) we make the conditional statement. If that check is True, we will make change between the elements. We will want to move the arr[j] element to the 'i' position, and the arr[i] element to the 'j' position. That's what we do in line 13º, where the 'minor' variable is 'j' now.
6) Now that we change the minor position value, the last step is to exchange the values. In order to do this, we need an aux/temporary variable to store one of the two values (this is because once we replace its value, we lose it. But we want to use that value later, so we have to store it). 
"""

# Bubble Sort

def bubble_sort(arr):

  for i in range(len(arr) - 1):
    
    for j in range(len(arr) - 1):
      if(arr[j] > arr[j + 1]):        
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
      
  return arr
    
"""
Explanation:

1) For this sort algorithm we have to use a 'For Loop' to indicate how many times we want to make the main operation (compare each element with its next one).
2) Once we have the first loop, we need another 'For Loop' to make this comparison operations we said. Inside of it, we will check if the first element is greater than the next one. 
3) If that is true we exchange the values (this time, we use multiple assignment but the idea is the same; we need to store a value in a temporary variable so we don't lose it after we change the values)
4) Finally we return the ordered array
5) As we could see, this method is not the most efficient because it needs a lot of iterations, comparisons (the length of the array - 1 ^ 2), position's changes in each iteration, etc.
"""

# Bubble Sort 2.0

def bubble_sort_2(arr):

  for i in range(len(arr) - 1):
    
    for j in range(len(arr) - 1 - i):
      if(arr[j] > arr[j + 1]):        
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
      
  return arr

"""
1) An improvement to the Bubble Sort algorithm can be reducing the number of iterations. How can we do it? Well, if we see what the algorithm does, we can see that each iteration push the greater number of the list to the end. So... in the first iteration we have one ordered element at the end, in the second one we have two, in the third one three, and so on and so on. See? We have 'i' ordered elements after each iteration
2) Knowing this, we could exclude that elements that are 'already ordered' of the iteration and comparisons. In order to do this, we would have something like 'Bubble Sort 2.0' (code below)
3) Check line 63, we modify the range. Now, after each iteration, we reduce by 'i' the range of the loop so we exclude the last element (already ordered) and we don't make unnecessary comparisons.
"""
# Bubble Sort 3.0

def bubble_sort_3(arr):

  hasChanged = True

  i = 0

  while(hasChanged and i < len(arr)):

    for i in range(len(arr) - 1 - i):
      
      hasChanged = False

      for j in range(len(arr) - 1 - i):
        if(arr[j] > arr[j + 1]):        
          arr[j], arr[j + 1] = arr[j + 1], arr[j]
          hasChanged = True

    i += 1

  return arr
  
print(bubble_sort_3(array))

"""
1) Another improvement also can be to stop iterating once we ordered all the list. But, how can we know when it is completely ordered? Well, we can detect values' and positions' changes.
2) In order to do this, we will make a validation to enter to the main loop. The condition is that there were changes in the last iteration.
3) We do this conditional statement with a 'While', so the loop will start if and only if the array changed during the last iteration. With this two changes, we have a Bubble Sort algorithm a little bit more efficient :)
"""

# Insertion Sort




