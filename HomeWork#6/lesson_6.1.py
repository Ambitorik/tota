with open('nginx_logs.txt') as read_file:
    data = []
    for i in read_file:
        spl = i.split()
        data.append((spl[0], spl[5][1:], spl[6]))
print(data)
