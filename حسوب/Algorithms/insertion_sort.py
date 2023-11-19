def insertionSort(arr): 

	# التنقل عبر عناصر المصفوفة من الموقع 1 إلى نهاية المصفوفة
	for i in range(1, len(arr)): 

		key = arr[i] 

		# تحريك العناصر في المصفوفة
        # arr[0..i-1]
        # والتي تكون أكبر من المفتاح المعطى
        # بمقدار موقع واحد عن موقعها الحالي
		j = i-1
		while j >= 0 and key < arr[j] : 
				arr[j + 1] = arr[j] 
				j -= 1
		arr[j + 1] = key 


# اختبار الدالة السابقة
arr = [12, 11, 13, 5, 6] 
insertionSort(arr) 
for i in range(len(arr)): 
	print ("% d" % arr[i])