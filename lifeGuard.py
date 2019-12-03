def getTotalHours(intervals):
    """Calculate the total hours covered"""
    merged = []
    '''To find the merged interval'''
    for interval in intervals:

        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    sumHours = 0
    for mergedInterval in merged:
        sumHours += mergedInterval[1] - mergedInterval[0]
    return sumHours

def lifeGuard(file):

    with open(file, 'r') as f:
        dlList = [line for line in f]
        f.close()

        """Format to load intervals into a list of list"""
        intervals = []
        for i in range(1, len(dlList)):
            start, end = dlList[i].split(' ')
            intervals.append([int(start), int(end)])

        """Intervals sorted by start time and then end time"""
        intervals.sort(key=lambda x: (x[0], x[1]))

        """Find minimum true time"""
        minTrueTime = float('inf')
        for i in range(len(intervals)):

            """Get True start of an interval by comparing with the end of previous interval"""
            trueStart = intervals[i][0]
            if i != 0:
                if intervals[i][0] < intervals[i-1][1]:
                    trueStart = intervals[i-1][1]

            """Get True End of an interval by comparing with the start of next interval"""
            trueEnd = intervals[i][1]
            if i != len(intervals) -1:
                if intervals[i][1] > intervals[i+1][0]:
                    trueEnd = intervals[i+1][0]

            trueHours = trueEnd - trueStart
            """If complete overlap make true hours as 0"""
            if trueHours < 0:
                trueHours = 0
            minTrueTime = min(minTrueTime, trueHours)


        totHours = getTotalHours(intervals)

        """Remove the true hours of the least impactful guard to get total hours"""
        totHours = totHours - minTrueTime
        fileName = file.split('.')[0]
        fileName = fileName + '.out'
        outFile = open(fileName, 'w')
        outFile.write(str(totHours))
        outFile.close()

for i in range(1,11):
    lifeGuard(str(i)+'.in')






