def histogr(arr):
    for i in range(len(arr)):
        print(arr[i]*'*')
    
histogr(list(map(int, input().split())))