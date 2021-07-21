temperature = input('請輸入體溫:')
temperature = float(temperature)
if temperature >= 37.5:
    print('體溫過高，請儘速就醫')
elif temperature < 35:
    print('體溫異常')
else:
    print('體溫正常')