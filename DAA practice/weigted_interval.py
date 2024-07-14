def input_jobs():
    jobs = [] 
    n = int(input('Enter number of jobs: '))
    for _ in range(n):
        s = int(input('Start: '))
        e = int(input('End: '))
        d = int(input('Profit: '))
        jobs.append([s,e,d])
    return (n, jobs)

def opt(jobs, j):
    start_time = jobs[j][0]
    low = 0 
    high = j-1 
    while low <= high:
        mid = (low+high)//2
        end_time = jobs[mid][1]
        if end_time > start_time:
            high = mid-1
        else:
            if jobs[mid+1][1] <= start_time:
                low = mid+1
            else:
                return mid 
    return -1 

def schedule(jobs):
    jobs.sort(key = lambda x : x[1])
    print(jobs)
    dp = [0 for _ in range(len(jobs))]
    dp[0] = jobs[0][2]
    n = len(jobs)
    jobs_selected = []

    for i in range(1, n):
        not_choose = choose = -float('inf')
        p_i = opt(jobs, i)
        
        not_choose = dp[i-1]
        if p_i != -1:
            choose = jobs[i][2] + dp[p_i]
        
        dp[i] = max(choose, not_choose)

    print(dp)

    def find_solution(i):
        if i < 0:
            return 
        p_i = opt(jobs, i)
        if jobs[i][2] + (dp[p_i] if p_i != -1 else 0) >= (dp[i-1] if i != 0 else 0):
            jobs_selected.append(i)
            find_solution(p_i)
        else:
            find_solution(i-1)
    find_solution(n-1)
    print(jobs_selected)

n, jobs = input_jobs()
schedule(jobs)