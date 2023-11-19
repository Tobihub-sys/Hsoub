# يستخدم هذا الصنف لتمثيل الرسم البياني
class Graph: 

	def __init__(self,vertices): 
		self.V= vertices # عدد الرؤوس
		self.graph = [] # قاموس افتراضي لتخزين الرسم البياني

	# تضيف الدالة ضلعًا إلى الرسم البياني
	def addEdge(self,u,v,w): 
		self.graph.append([u, v, w]) 
		
	# دالة مساعدة لطباعة الحل
	def printArr(self, dist): 
		print("Vertex Distance from Source") 
		for i in range(self.V): 
			print("%d \t\t %d" % (i, dist[i])) 
	
	# الدالة الرئيسية والتي تعثر على المسافات الأقصر التي تفصل
	# المصدر عن جميع الرؤوس باستخدام خوارزمية بِلمان-فورد.
	# تكشف الدالة كذلك عن دورة الوزن السالب.

	def BellmanFord(self, src): 
		
		# الخطوة الأولى هي تهيئة المسافات التي تفصل بين المصدر
		# وجميع الرؤوس في الرسم البياني لتكون ما لا نهاية
		dist = [float("Inf")] * self.V 
		dist[src] = 0

		# الخطوة الثانية: إطلاق جميع الأضلاع.
		# يمكن للمسار الأقصر البسيط من المصدر إلى أي عقدة أن يمتلك
		# |V| -1 ضلعًا
		for i in range(self.V - 1): 
			# تحديث قيمة المسافة وموقع الأب للرؤوس المجاورة
			# للرأس المنتخب. سنأخذ بنظر الاعتبار الرؤوس التي لا تزال موجودة في الرتل فقط.		
			for u, v, w in self.graph: 
				if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
						dist[v] = dist[u] + w 

		# تضمن الخطوة الثانية حساب أقصر المسافات
		# إن لم يحتو الرسم البياني على دورة وزن سالب.
		# ولكن إن مررنا على جميع الأضلاع مرة أخرى وحصلنا على مسار أقصر
		# لأي رأس من الرؤوس في الرسم البياني فهذا يعني وجود دورة وزن سالب		

		for u, v, w in self.graph: 
				if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
						print( "Graph contains negative weight cycle")
						return
						
		# طباعة قيم المسافات كلها
		self.printArr(dist) 

g = Graph(5) 
g.addEdge(0, 1, -1) 
g.addEdge(0, 2, 4) 
g.addEdge(1, 2, 3) 
g.addEdge(1, 3, 2) 
g.addEdge(1, 4, 2) 
g.addEdge(3, 2, 5) 
g.addEdge(3, 1, 1) 
g.addEdge(4, 3, -3) 

# طباعة الحل
g.BellmanFord(0)