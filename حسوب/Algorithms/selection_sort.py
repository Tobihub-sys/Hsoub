import sys 
A = [64, 25, 12, 22, 11] 

# التنقل عبر جميع عناصر القائمة
for i in range(len(A)): 
	
	# العثور على أصغر عنصر في المصفوفة غير المرتبة
	min_idx = i 
	for j in range(i+1, len(A)): 
		if A[min_idx] > A[j]: 
			min_idx = j 
			
	# تبديل موقع العنصر الذي عُثر عليه مع العنصر الأول
	A[i], A[min_idx] = A[min_idx], A[i] 

# اختبار الدالة السابقة
print ("Sorted array") 
for i in range(len(A)): 
	print("%d" %A[i]),