# Определение финансовых резульатов работы фирмы

earnings = int(input('Введите выручку компании: '))
expenses = int(input('Введите издержки компании: '))

if earnings > expenses:
    print('Компания прибыльная.')
    profit = earnings - expenses
    profitability = profit / earnings
    print("Рентабельность выручки: %.2f" % profitability)
    staff = int(input('Введите численность сотрудников фирмы: '))
    profit_on_pearson = profit / staff
    print("Прибыль компании в рассчёте на одного сотрудника: %.2f" % profit_on_pearson)

else:
    print('Компания убыточная')
