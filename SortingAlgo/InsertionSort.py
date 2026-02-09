def insertionSort(arr):
    n = len(arr)

    for i in range(n):
        currentCard = arr[i]
        correctPosition = i - 1

        while correctPosition >= 0:
            if arr[correctPosition] < currentCard:
                break
            else:
                arr[correctPosition + 1] = arr[correctPosition]
                correctPosition -= 1
        arr[correctPosition + 1] = currentCard
    return arr

# Example usage
arr = [12, 11, 13, 5, 6]
sorted_arr = insertionSort(arr)
print("Sorted array is:", sorted_arr)