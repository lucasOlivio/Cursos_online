import datetime

print(datetime.datetime.now())

print(type(datetime.datetime.now()))

otoDia=datetime.datetime(2016,5,13,11,0,0,0)

hoji=datetime.datetime.now()

print(otoDia)
print(hoji)

print(hoji-otoDia)

delta=hoji-otoDia

print(delta.days)
print(delta.seconds)
