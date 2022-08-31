from datetime import datetime, timedelta

d1 = datetime(2022, 8, 16, 8, 0, 0)
d2 = datetime(2022, 8, 16, 12, 0, 0)
d3 = datetime(2022, 8, 16, 13, 30, 0)
d4 = datetime(2022, 8, 16, 18, 00, 00)

ht = (d2-d1)+(d4-d3)
print(ht)
print(repr(ht))
jornada = timedelta(hours=8)

print('Faltam ', (jornada-ht).total_seconds()/3600,' horas')
td=d2-d1
print(td)
