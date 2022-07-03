money = int(input("Введите сумму:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
L = (per_cent.values())
i = list(L)
raschet = (money/100)
deposit = [(int(float(raschet*i[0]))), (int(float(raschet*i[1]))), (int(float(raschet*i[2]))), (int(float(raschet*i[3])))]
print(deposit)
print("Максимальный депозит:"),print(max(deposit))
