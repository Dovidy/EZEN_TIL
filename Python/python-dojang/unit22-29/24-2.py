input_str = '51900;83000;158000;367500;250000;59200;128500;1304000'
money_list = [int(i) for i in input().split(';')]
money_list.sort(reverse=True)

for money in money_list:
    print('%9s' % format(money, ','))