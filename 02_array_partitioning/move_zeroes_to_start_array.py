array = [2, 0, 1, 0, 3, 3, 0]

i = 0
boundary = 0
while i < len(array):
    if array[i] == 0:
        del array[i]
        array.insert(boundary, 0)
        boundary += 1
    i += 1

print(array)
# Move the zeroes to the end of the array
array = [2, 0, 1, 0, 3, 3, 0]

i = len(array) - 1
boundary = len(array) - 1
while i > 0:
    if array[i] == 0:
        array.insert(boundary + 1, 0)
        del array[i]
        boundary -= 1
    i -= 1
print(array)


# Move even numbers to the left, and odd numbers to the right:
array = [2, 1, 3, 4, 0, 5, 7, 6]

i = 0
left_b = 0
right_b = len(array) - 1
while i <= right_b:
    if array[i] % 2 == 0:
        # even number
        array.insert(left_b, array[i])
        del array[i+1]
        left_b += 1
        i += 1
    else:
        # odd number
        array.insert(right_b + 1, array[i])
        del array[i]
        right_b -= 1
print(array)

# Dutch National Flag Problem
array = [1, 4, 5, 4, 4, 6, 2, 3]
pivot = 4
left_b = 0
right_b = len(array) - 1
i = 0
while i <= right_b:
    if array[i] < pivot:
        array.insert(left_b, array[i])
        del array[i+1]
        i += 1
        left_b += 1
    elif array[i] > pivot:
        array.insert(right_b + 1, array[i])
        del array[i]
        right_b -= 1
    else:
        i += 1
print(array)

array = [2, 0, 1, 0, 3, 3, 0]

i = 0
boundary = 0
while i < len(array):
    if array[i] == 0:
        array[boundary+1:i+1] = array[boundary:i]
        array[boundary] = 0
        boundary += 1
    i += 1

print(array)

array = [1, 4, 5, 4, 4, 6, 2, 3]
pivot = 4


def smalllarge(arr, pivot):
    spointer = 0
    for i in range(len(arr)):
        if arr[i] < pivot:
            val = arr.pop(i)
            arr.insert(spointer, val)
            spointer += 1
        elif arr[i] == pivot:
            arr.pop(i)
            arr.insert(spointer, pivot)


smalllarge(array, pivot)
print(array)
