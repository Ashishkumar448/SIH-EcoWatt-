import csv

file = open("dataset.csv", "r")

reader = csv.reader(file)

header = next(reader)

data = [i for i in reader if i]

for i in data:
    i[1] = int(i[1])

def get_m_avg():
    last30 = data[-30:-1] 
    kWh = [i[1] for i in last30]
    avg = format(sum(kWh)/len(kWh), '.2f')
    return avg

def get_m_sum():
    last30 = data[-30:-1] 
    avg = sum([i[1] for i in last30])
    return avg
    


if "__main__" == __name__:
    print(get_m_sum())
