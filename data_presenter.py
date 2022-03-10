open_file = open("CupcakeInvoices.csv")

# for line in open_file:
#     line = line.rstrip('\n').split(',')
    # print(line)
    # print(line[2])
total = 0
for line in open_file:
    line = line.rstrip('\n').split(',')
    # print(line)
    total_new = (int(line[3]) *(float(line[4])))
    total = total_new + total

print(total)


open_file = closed()
