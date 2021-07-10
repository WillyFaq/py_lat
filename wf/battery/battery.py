import psutil

baterry = psutil.sensors_battery()
percent = str(baterry.percent)
print(baterry)
# print("Battery running on "+percent+" %")

use = psutil.users()
print(use)

# tem = psutil.sensors_temperatures()
# print(tem)

# fans = psutil.sensors_fans()
# print(fans)


count = psutil.cpu_count()
print(f"cpu count {count}")
logi_count = psutil.cpu_count(logical=False)
print(f"cpu count {logi_count}")
for x in range(3):
	cpu = psutil.cpu_percent(interval=1, percpu=True)
	print(cpu)