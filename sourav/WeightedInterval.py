class Interval:
    def __init__(self, start, end, profit):
        self.start = start
        self.end = end
        self.profit = profit

def compatible(i1, i2):
    if i1.start < i2.start:
        return True if i1.end <= i2.start else False
    else:
        return True if i2.end <= i1.start else False

def get_compatibility(intervals):
    n = len(intervals)
    result = [-1]

    for i in range(1, n):
        for j in range(i):
            if compatible(intervals[i], intervals[j]):
                continue
            else:
                result.append(j-1)

    return result

def schedule(intervals):
    n = len(intervals)
    compatibility = get_compatibility(intervals)
    
    intervals.sort(key= lambda x: x.end)
    results = [{
        "intervals": [intervals[0]],
        "profit": intervals[0].profit
    }]

    for i in range(1, n):
        include_profit = intervals[i].profit + results[compatibility[i]]["profit"] if compatibility[i] != -1 else 0
        exclude_profit = results[i-1]["profit"]

        if include_profit > exclude_profit:
            results.append({
                "profit": include_profit,
                "intervals": results[compatibility[i]]["intervals"] + [intervals[i]]
            })
        else:
            results.append(results[i-1])
    
    print(results[n-1])

intervals = []
n = int(input("Enter the number of intervals: "))

for i in range(n):
    intervals.append(Interval(
        int(input("Enter start: ")),
        int(input("Enter end: ")),
        int(input("Enter profit: "))
    ))

schedule(intervals)



