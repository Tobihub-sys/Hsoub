# Node class 
class Node: 
   
    # دالة لتهيئة كائن العقدة
    def __init__(self, data): 
        self.data = data  # إسناد البيانات
        self.next = None  # تهيئة العقدة التالية لتكون فارغة 
   
# صنف القائمة المترابطة
class LinkedList: 
     
    # دالة لتهيئة كائن القائمة المترابطة  
    def __init__(self):  
        self.head = None

# صنف العقدة
class Node: 

	# دالة لتهيئة كائن العقدة
	def __init__(self, data): 
		self.data = data # إسناد البيانات
		self.next = None # null تهيئة العقدة اللاحقة لتكون


# صنف القائمة المترابطة الذي يحتوي على كائن عقدة
class LinkedList: 

	# تهيئة رأس القائمة
	def __init__(self): 
		self.head = None


if __name__=='__main__': 

	# نبدأ بقائمة مترابطة فارغة
	llist = LinkedList() 

	llist.head = Node(1) 
	second = Node(2) 
	third = Node(3) 

	''' 
	حجزت ثلاث كتل في الذاكرة ديناميكيًا
	ولدينا مؤشرات لهذه الكتل هي
	first, second, third

	llist.head	 second			 third 
		|			 |				 | 
		|			 |				 | 
	+----+------+	 +----+------+	 +----+------+ 
	| 1 | None |	 | 2 | None |	 | 3 | None | 
	+----+------+	 +----+------+	 +----+------+ 
	'''

	llist.head.next = second; # ربط العقدة الأولى بالثانية

	''' 
	تشير العقدة الأولى الآن إلى العقدة الثانية، وبهذا تكونان مترابطتين

	llist.head	 second			 third 
		|			 |				 | 
		|			 |				 | 
	+----+------+	 +----+------+	 +----+------+ 
	| 1 | o-------->| 2 | null |	 | 3 | null | 
	+----+------+	 +----+------+	 +----+------+ 
	'''

	second.next = third; # ربط العقدة الثانية بالثالثة

	''' 
	تشير العقدة الثانية إلى العقدة الثالثة، وبهذا تكونان مترابطتين


	llist.head	 second			 third 
		|			 |				 | 
		|			 |				 | 
	+----+------+	 +----+------+	 +----+------+ 
	| 1 | o-------->| 2 | o-------->| 3 | null | 
	+----+------+	 +----+------+	 +----+------+ 
	'''

# صنف العقدة
class Node: 
    # دالة لتهيئة كائن العقدة
    def __init__(self, data): 
        self.data = data # إسناد البيانات
        self.next = None # null تهيئة العقدة اللاحقة لتكون

# صنف قائمة مترابطة يضم كائن عقدة
class LinkedList: 
    # تهيئة رأس القائمة
    def __init__(self): 
        self.head = None

    # تطبع هذه الدالة محتويات القائمة المترابطة
    # بدءًا من العقدة المعطاة
    def printList(self): 
        temp = self.head 
        while temp: 
            print(temp.data)
            temp = temp.next

if __name__ == '__main__': 
    # البدء بقائمة مترابطة فارغة
    llist = LinkedList() 

    llist.head = Node(1) 
    second = Node(2) 
    third = Node(3) 

    llist.head.next = second # ربط العقدة الأولى بالثانية
    second.next = third # ربط العقدة الثانية بالثالثة

    llist.printList()
