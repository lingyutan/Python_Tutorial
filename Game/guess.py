import random, time
start = 0
end = 100
num = random.randint(start,end)
current = None
while current is None or current != num:
    print("Please input a number from", start, "to", end, ":")
    try:
        current = int(input())
    except:
        print("Error: Not a number! Please re-input your number.")
        continue
    if current < start or current > end:
        print("Error: Number out of range! Please re-input your number.")
    elif current == num:
        print("Pili!")
        time.sleep(0.7)
        print("Pala!!!")
        time.sleep(0.7)
        print("Boom!!!")
        time.sleep(0.7)
        print("Blast!!!!")
        time.sleep(0.7)
        print("You lost!!!!!!")
    else:
        if current > num:
            end = current - 1
        if current < num:
            start = current + 1
