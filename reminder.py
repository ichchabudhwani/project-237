import time
print("welcome to reminder!!!")
print("what should I remind you about?")
text = str(input("type here:"))
print("In how many hours?")
local_time = float(input("type here:"))
local_time = local_time * 3600
time.sleep(local_time)
print(text)
