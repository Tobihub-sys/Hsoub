# الدالة الرئيسية التي ترتّب السلسلة النصية المعطاة ترتيبًا أبجديًّا
def countSort(arr): 

	# مصفوفة المخرجات التي ستتضمّن الحروف مرتّبةً
	output = [0 for i in range(256)] 

	
	# إنشاء مصفوفة للعد وذلك لتخزين تعداد كل حرفٍ 
	#  في المصفوفة وتهيئة القيمة الأولية للتعداد لتكون صفرًا 
	count = [0 for i in range(256)] 

	# تستخدم هذه القائمة لتخزين النتيجة
	# وذلك لأنّ السلاسل النصية غير قابلة للتغيير في بايثون
	ans = ["" for _ in arr] 

	# تخزين تعداد كل عنصر
	for i in arr: 
		count[ord(i)] += 1

	
	# تغيير قيمة العنصر لتكون الموقع الحقيقي
	# للحرف الحالي في مصفوفة المخرجات 
	for i in range(256): 
		count[i] += count[i-1] 

	# بناء مصفوفة المخرجات
	for i in range(len(arr)): 
		output[count[ord(arr[i])]-1] = arr[i] 
		count[ord(arr[i])] -= 1

	# arr نسخ مصفوفة المخرجات إلى القائمة
	# لتتضمّن هذه القائمة الحروف المرتّبة
	for i in range(len(arr)): 
		ans[i] = output[i] 
	return ans 

# اختبار الدوال السابقة
arr = "geeksforgeeks"
ans = countSort(arr) 
print ("Sorted character array is %s" %("".join(ans)))