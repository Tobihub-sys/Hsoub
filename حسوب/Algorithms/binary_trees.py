class Node: 
	def __init__(self,key): 
		self.left = None
		self.right = None
		self.val = key

# يمثل هذا الصنف عقدة مفردة في شجرة البيانات الثنائية
class Node: 
	def __init__(self,key): 
		self.left = None
		self.right = None
		self.val = key 


# إنشاء الجذر
root = Node(1) 
''' أصبحت الشجرة بعد تنفيذ العبارة السابقة بالشكل التالي 
		1 
	/ \ 
	None None'''

root.left	 = Node(2); 
root.right	 = Node(3); 
	
''' أصبحت العقدتان 2 و 3 الابنين الأيسر والأيمن للعقدة 1 
		1 
		/ \ 
		2	 3 
	/ \ / \ 
None None None None'''


root.left.left = Node(4); 
'''أصبحت العقدة 4 الابن الأيسر للعقدة 2 
		1 
	/	 \ 
	2		 3 
	/ \	 / \ 
4 None None None 
/ \ 
None None'''

class newNode(): 

	def __init__(self, data): 
		self.key = data 
		self.left = None
		self.right = None
		
# التنقل عبر مستويات الشجرة الثنائية

def inorder(temp): 

	if (not temp): 
		return

	inorder(temp.left) 
	print(temp.key,end = " ") 
	inorder(temp.right) 


# دالة لإدراج عنصر في الشجرة الثنائية

def insert(temp,key): 

	q = [] 
	q.append(temp) 
	
    # التنقل عبر مستويات الشجرة الثنائية بحثاً عن مكان فارغ
	while (len(q)): 
		temp = q[0] 
		q.pop(0) 

		if (not temp.left): 
			temp.left = newNode(key) 
			break
		else: 
			q.append(temp.left) 

		if (not temp.right): 
			temp.right = newNode(key) 
			break
		else: 
			q.append(temp.right) 
	
# اختبار الدوال السابقة
if __name__ == '__main__': 
	root = newNode(10) 
	root.left = newNode(11) 
	root.left.left = newNode(7) 
	root.right = newNode(9) 
	root.right.left = newNode(15) 
	root.right.right = newNode(8) 

	print("Inorder traversal before insertion:", end = " ") 
	inorder(root) 

	key = 12
	insert(root, key) 

	print() 
	print("Inorder traversal after insertion:", end = " ") 
	inorder(root)