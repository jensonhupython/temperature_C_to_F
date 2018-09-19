#35 temparature change  oC <-> oF
# F = C*(9/5)+32

temp_C = input('請輸入攝氏溫度: ')
temp_C = float(temp_C)

temp_F = temp_C * (9/5) + 32
print('華氏溫度是: ', temp_F)
