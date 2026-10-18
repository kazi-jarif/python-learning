import time
current_time= time.strftime("%H:%M:%S")

if current_time>"05:00:00" and current_time<"12:00:00":
    print("good morning sir")
elif current_time>"12:00:00" and current_time<"15:00:00":
    print("good noon")
elif current_time>"15:00:00" and current_time<"18:00:00":
    print("good afternoon")
elif current_time>"18:00:00" and current_time<"20:00:00":
    print("good evening")
else:
    print("good night")