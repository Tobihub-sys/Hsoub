def mergeSort(arr): 
	if len(arr) >1: 
		mid = len(arr)//2 #إيجاد منتصف المصفوفة
		L = arr[:mid] # تقسيم محتويات المصفوفة
		R = arr[mid:] # إلى نصفين

		mergeSort(L) # ترتيب النصف الأول
		mergeSort(R) # ترتيب النصف الثاني

		i = j = k = 0
		
		# نسخ البيانات إلى مصفوفتين مؤقتتين
		while i < len(L) and j < len(R): 
			if L[i] < R[j]: 
				arr[k] = L[i] 
				i+=1
			else: 
				arr[k] = R[j] 
				j+=1
			k+=1
		
		# التأكد من بقاء أي عنصر في المصفوفتين المؤقتتين
		while i < len(L): 
			arr[k] = L[i] 
			i+=1
			k+=1
		
		while j < len(R): 
			arr[k] = R[j] 
			j+=1
			k+=1

# طباعة المصفوفة
def printList(arr): 
	for i in range(len(arr)):		 
		print(arr[i],end=" ") 
	print() 

# اختبار الدوال السابقة
if __name__ == '__main__': 
	arr = [12, 11, 13, 5, 6, 7] 
	print ("Given array is", end="\n") 
	printList(arr) 
	mergeSort(arr) 
	print("Sorted array is: ", end="\n") 
	printList(arr)