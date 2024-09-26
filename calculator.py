num1 = int(input("첫 번째 정수를 입력하세요: "))
num2 = int(input("두 번째 정수를 입력하세요: "))

sum_result = num1 + num2
sub_result = num1 - num2
mul_result = num1 * num2

if num2 != 0:
    div_result = num1 / num2
    print(f"{num1} / {num2} = {div_result}")
else:
    print("0으로 나눌 수 없습니다.")

print(f"{num1} + {num2} = {sum_result}")
print(f"{num1} - {num2} = {sub_result}")
print(f"{num1} * {num2} = {mul_result}")
