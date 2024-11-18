# Напишите программу, которая принимает две строки
# вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму дробей.
# Ввод:
# 1/2
# 2/3
# Вывод:
# 7/6  (будет еще круче если упростите до 1+1/6)

frac1 = "1/2"
frac2 = "2/3"

num1, denum1 = map(int, frac1.split("/"))
num2, denum2 = map(int, frac2.split("/"))

frac_sum_chisl = num1*denum2 + num2*denum1
frac_sum_znam = denum2*denum1

print(f"{frac_sum_chisl}/{frac_sum_znam}")