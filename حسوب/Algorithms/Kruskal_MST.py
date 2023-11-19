from collections import defaultdict 

# تمثيل الرسم البياني
#Class to represent a graph 
class Graph: 

	def __init__(self,vertices): 
		self.V= vertices # عدد الرؤوس 
		self.graph = [] # قاموس افتراضي لتخزين الرسم البياني

	# دالة لإضافة ضلع إلى الرسم البياني
	def addEdge(self,u,v,w): 
		self.graph.append([u,v,w]) 

	# i دالة مساعدة للعثور على مجموعة العنصر 
	# (تستخدم طريقة ضغط المسار) 
	def find(self, parent, i): 
		if parent[i] == i: 
			return i 
		return self.find(parent, parent[i]) 

	# الدالة المسؤولة عن العثور على مجموعتين للعنصرين المعطيين 
	# (تستخدم طريقة التوحيد بالمرتبة) 
	def union(self, parent, rank, x, y): 
		xroot = self.find(parent, x) 
		yroot = self.find(parent, y) 

		# ربط الشجرة ذات الرتبة الأصغر تحت جذر 
		# ربط الشجرة ذات الرتبة الأصغر تحت جذر 
		if rank[xroot] < rank[yroot]: 
			parent[xroot] = yroot 
		elif rank[xroot] > rank[yroot]: 
			parent[yroot] = xroot 

		# إن كانت المراتب متساوية، سنجعل إحدى الشجرتين جذرًا 
		# ونرفع رتبتها بمقدار واحد 
		else : 
			parent[yroot] = xroot 
			rank[xroot] += 1

	# الدالة الرئيسية المسؤولة عن بناء الشجرة الممتدة الصغرى باستخدام خوارزمية كروسكال 
	def KruskalMST(self): 

		result =[] #هنا ستخزن الشجرة الممتدة الصغرى 

		i = 0 # متغير للموقع يستخدم مع الأضلاع المرتبة 
		e = 0 #  result[] متغير للموقع يستخدم مع المصفوفة 

		# الخطوة الأولى: ترتيب جميع الأضلاع بترتيب تصاعدي 
		# بالاعتماد على أوزانها. وإن لم يكن بالإمكان تعديل 
		# الرسم البياني المعطى، يمكن إنشاء نسخة من مصفوفة الأضلاع 
		self.graph = sorted(self.graph,key=lambda item: item[2]) 

		parent = [] ; rank = [] 

		# إنشاء مجموعة الرؤوس الفرعية مع عنصر واحد 
		for node in range(self.V): 
			parent.append(node) 
			rank.append(0) 
	
		# V-1 عدد الأضلاع التي ستعمل عليها الخوارزمية يساوي 
		while e < self.V -1 : 

			# الخطوة الثانية: اختيار الضلع الأصغر ثم زيادة 
					# متغير الموقع للدورة القادمة 
			u,v,w = self.graph[i] 
			i = i + 1
			x = self.find(parent, u) 
			y = self.find(parent ,v) 

			# إن لم تؤد إضافة هذا الضلع إلى تكوين دورة 
						# نضيف الضلع إلى النتيجة ونزيد قيمة متغير الموقع 
						#  لمصفوفة النتيجة وذلك لاستقبال الضلع التالي 
			if x != y: 
				e = e + 1	
				result.append([u,v,w]) 
				self.union(parent, rank, x, y)			 
			# وإلا سنتجاهل الضلع التالي 

		# طباعة محتويات مصفوفة النتائج وعرض الشجرة الممتدة الصغرى التي تم بناؤها 
		print ("Following are the edges in the constructed MST")
		for u,v,weight in result: 
			#print str(u) + " -- " + str(v) + " == " + str(weight) 
			print ("%d -- %d == %d" % (u,v,weight)) 

# اختبار الدوال السابقة
g = Graph(4) 
g.addEdge(0, 1, 10) 
g.addEdge(0, 2, 6) 
g.addEdge(0, 3, 5) 
g.addEdge(1, 3, 15) 
g.addEdge(2, 3, 4) 

g.KruskalMST()