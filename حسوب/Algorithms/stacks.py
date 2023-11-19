from sys import maxsize 

# دالة لإنشاء المكدس وتهيئته ليكون بحجم 0
def createStack(): 
	stack = [] 
	return stack 

# يكون المكدس فارغًا عندما يكون حجمه صفرًا
def isEmpty(stack): 
	return len(stack) == 0

# دالة لإضافة عنصر إلى المكدس، وزيادة حجم المكدس بمقدار 1
def push(stack, item): 
	stack.append(item) 
	print(item + " pushed to stack ") 
	
# دالة لحذف عنصر من المكدس، وإنقاص حجم المكدس بمقدار 1
def pop(stack): 
	if (isEmpty(stack)): 
		return str(-maxsize -1) #تعيد القيمة سالب ما لا نهاية
	
	return stack.pop() 

# اختبار الدوال السابقة
stack = createStack() 
push(stack, str(10)) 
push(stack, str(20)) 
push(stack, str(30)) 
print(pop(stack) + " popped from stack")

# صنف لتمثيل العقدة
class StackNode: 

	# دالة بانية لتهيئة العقدة
	def __init__(self, data): 
		self.data = data 
		self.next = None

class Stack: 
	
	# دالة بانية لتهيئة الجذر الخاص بالقائمة المترابطة 
	def __init__(self): 
		self.root = None

	def isEmpty(self): 
		return True if self.root is None else False

	def push(self, data): 
		newNode = StackNode(data) 
		newNode.next = self.root 
		self.root = newNode 
		print("%d pushed to stack" %(data)) 
	
	def pop(self): 
		if (self.isEmpty()): 
			return float("-inf") 
		temp = self.root 
		self.root = self.root.next
		popped = temp.data 
		return popped 
	
	def peek(self): 
		if self.isEmpty(): 
			return float("-inf") 
		return self.root.data 

# اختبار الدوال السابقة
stack = Stack() 
stack.push(10)		 
stack.push(20) 
stack.push(30) 

print ("%d popped from stack" %(stack.pop())) 
print ("Top element is %d " %(stack.peek()))