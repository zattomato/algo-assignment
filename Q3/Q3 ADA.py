#calculate probability

Countries = ["A","B","C","D","E"]
Scores = [0.08,0.2,0.04,0.04,0.06]
TotalScore = 0
Cost = [2,4,6,8,10]
TotalCost = 0
Probability = []

for ele in range (0, len(Scores)):
    TotalScore = TotalScore + Scores[ele]

for ele in range (0, len(Cost)):
    TotalCost = TotalCost + Cost[ele]

for x in range (0, len(Countries)):
    Probability.append((Scores[x]/TotalScore) + float(Cost[x]/TotalCost))

print ("Calculated Probability: ")

for x in Probability:
    print(round(x,4))

# getMax method
def getMax(array_A):
    max = array_A[0]
    for i in range(len(array_A)):
        if array_A[i] > max:
            max = array_A[i]

    return max


def shellSort(A, n):
    # set the initial gap to floor of n/2
    gap = n // 2

    # Rearrange the array elements at n/2, n/4, ..., 1 intervals
    while gap > 0:

        for i in range(gap, n):
            temp = A[i]
            j = i

            while j >= gap and A[j - gap] < temp:
                A[j] = A[j - gap]

                j -= gap

            A[j] = temp
        gap //= 2


arr = Probability.copy()
shellSort(arr, len(arr))
print('\nSorted Probability: ')

for x in arr:
    print(round(x,4))


Sorted_Sequence_of_Country = []

for x in range(0, len(arr)):
    for y in range(0, len(Probability)):
        if arr[x] == Probability[y]:
            Sorted_Sequence_of_Country.append(y)


print("\nCountries Ranking:")

for x in Sorted_Sequence_of_Country:
    print(Countries[x])






