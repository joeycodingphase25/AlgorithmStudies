# Difficulty: Medium
# O(nlog(n)) time, O(n) space

def mergeOverlappingIntervals(intervals):
    # use lambda to sort by first value in interval
    sortedIntervals = sorted(intervals, key=lambda x: x[0])
    # create a variable to append values 
    mergedIntervals = []
    # identify the current interval 
    currentInterval = sortedIntervals[0]
    mergedIntervals.append(currentInterval)

    for nextInterval in sortedIntervals:
        # decouple the current inverval and nextinterval for comaprison
        _, currentIntervalEnd = currentInterval
        nextIntervalStart, nextIntervalEnd = nextInterval

        # simple logic statements
        if currentIntervalEnd >= nextIntervalStart:
            currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd)
        else:
            currentInterval = nextInterval
            mergedIntervals.append(currentInterval)
    return mergedIntervals