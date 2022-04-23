with open("files/nginx_logs.txt", "r", encoding="UTF-8") as f:
    g = []
    result = []
    for i in f:
        g.append(i)
        for o in g:
            a = o.split(" ")
            pre_result = a[0], a[6], a[7]
            result.append(pre_result)
    spamer = max(set(result), key = result.count)
    count_spam = result.count(spamer)
    print(f'IP-адрес спамера: {"".join(list(spamer[:1]))}, кол-во запросов: {count_spam}')
    print(*result, sep="\n")