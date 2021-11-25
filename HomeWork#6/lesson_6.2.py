with open('nginx_logs.txt') as read_file:
    spammers = {}
    for i in read_file:
        spl = i.split()
        spammers.setdefault(spl[0], 0)
        spammers[spl[0]] += 1
spam = sorted(spammers.items(), key=lambda x: x[1], reverse=True)
print(spam[:10])
