# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    laiks = [0] * n
    for i in range (m):
        thread = 0

        for j in range(n):
            if laiks[thread] > laiks[j]:
                thread = j

        output.append((thread,laiks[thread]))
        laiks[thread] = laiks[thread] + data[i]
        thread = 0
    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = 0
    m = 0
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job

    # TODO: create the function
    result = parallel_processing(n,m,data)
    for i in result:
        print(i[0],i[1])
    
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
