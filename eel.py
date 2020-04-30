import eel

eel.init('web')
eel.start('sample-for-stegno1.html', block = False)
print("After starting")

@eel.expose()
def my_method(param1 , param2):
    print(param1 + param2)

while True:
    eel.sleep(10)