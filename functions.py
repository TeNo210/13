def hello_who(name):
    return f'Hello,{name}'


def salary(hours,salary_by_hour):
    '''
    :param hours: Расчет зп сотрудника
    :param salary_by_hour: зарплата за час
    :return: итоговая сумма
    '''
    k=2
    return hours * salary_by_hour * k