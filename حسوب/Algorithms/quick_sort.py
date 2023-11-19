''' 
تنفّذ هذه الدالة عملية الترتيب السريع
arr: - المصفوفة المراد ترتيبها
start: - موق البداية
stop: موقع النهاية
'''
def quicksort(arr, start , stop): 
	if(start < stop): 
		
		# موقع العنصر المحوري ضمن المصفوفة
		pivotindex = partition(arr, start, stop) 
		
		# ليست المصفوفة مرتبة بالكامل حول العنصر المحوري في هذه المرحلة
		# ترتيب النصفين الأيمن والأيسر من المصفوفة كلًّا على حدة
		quicksort(arr , start , pivotindex - 1) 
		quicksort(arr, pivotindex + 1, stop) 
		
''' 
تأخذ هذه الدالة العنصر الأول كعنصر محوري
وتضعه في موقعه المصحيح ضمن المصفوفة المرتبة
يعاد ترتيب جميع العناصر نسبة إلى العنصر المحوري
توضع العناصر التي تكون أصغر من العنصر المحوري إلى يساره
والعناصر التي تكون أكبر من العنصر المحوري إلى يمينه
'''
def partition(arr,start,stop): 
	pivot = arr[start] # pivot 
	i = start - 1 # a variable to memorize where the 
				# partition in the array starts from. 
	for j in range(start, stop - 1): 
		
		# يزاح العنصر الحالي إلى الجهة اليسرى من المصفوفة المجزئة
		# إذا كان أصغر من العنصر المحوري أو مساويًا له
		if arr[j] <= pivot: 
			arr[i] , arr[j] = arr[j] , arr[i] 
			i = i + 1
	arr[stop] , arr[i + 1] = arr[i + 1] , arr[stop] 
	return (i + 1) 

# اختبار الدالتين السابقتين
if __name__ == "__main__": 
	array = [10, 7, 8, 9, 1, 5] 
	quicksort(array, 0, len(array) - 1) 
	print(array)