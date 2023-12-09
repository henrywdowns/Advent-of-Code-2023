with open('Dec 5/input.txt','r',newline='') as doc:
    lines = doc.readlines()

sample_input = lines

# print(sample_input)
data = []
supplies = ['seeds','seed-to-soil map','soil-to-fertilizer map','fertilizer-to-water map','water-to-light map','light-to-temperature map','temperature-to-humidity map','humidity-to-location map']
supply_dict = {}
for line in sample_input:
    data.append(line.strip())

print(f'Data length: {len(data)}; supplies length: {len(supplies)}')

for item in data:
    print('==========new item==========')
    print(item)

# for dataBlock, data in enumerate(data):
#     if supplies[dataBlock] in data:
#         supply_dict[supplies[dataBlock]] = data

#print(supply_dict)