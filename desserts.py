#!/usr/bin/python

desserts = ["ice cream", "cookies"]
desserts.sort()
print desserts

print desserts.index("ice cream")


food = []
food = desserts[:]
print food

food.append("broccoli")
food.append("turnips")

print food
print desserts
food.remove("cookies")
print food

cookies = "cookies, cookies, cookies"
breakfast = []
cookies.split(',')
print cookies

breakfast.extend([cookies])
print breakfast

values = [2, 4, 8, 16, 32, 64]
def list_of_numbers(values):
	for i in values:
		if i >=1 and i < 20:
			print i

list_of_numbers(values)
