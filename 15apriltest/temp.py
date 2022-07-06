dict = {'Data': '[922, 799, 572, 1000, 673, 119, 460, 120, 130, 255, 983, 194, 673, 175, 945, 480, 745, 786, 451, 772]', 'Secret': 'Q7GRUV'}

data = dict['Data']
print(type(data))

data = list(data)



import statistics

count = len(data)
maxi = max(data)
mini = min(data)
mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)


print(count, maxi, mini, mean , median, mode)