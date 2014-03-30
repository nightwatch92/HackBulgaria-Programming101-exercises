def slope_style(scores):
	scores.sort()
	scores.pop(0)
	scores.pop()
	f = 0
	count = 0
	for item in scores:
		# print(item)
		f += item	
		count +=1

	result = "%.2f" % (f/count)
	return float(result)
	# print(slope_style([95,100,31,52]))
	# print(slope_style([94, 95, 95, 95, 90]))
	# print(slope_style([60, 70, 80, 90, 100]))
	# print(slope_style([96, 95.5, 93, 89, 92]))
