# يستخدم هذا الصنف لتمثيل الرتل
class Queue:
    # الدالة البانية
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.Q = [None] * capacity
        self.capacity = capacity

    # يصبح الرتل ممتلئًا عندما
    # يصبح حجمه مساويًا لسعته
    def isFull(self):
        return self.size == self.capacity

    # يكون الرتل فارغًا عندما يساوي حجمه الصفر
    def isEmpty(self):
        return self.size == 0

    # تضيف الدالة عنصرًا إلى الرتل
    # وتعدل الفهرس الأخير وحجم الرتل
    def EnQueue(self, item):
        if self.isFull():
            print("Full")
            return
        self.rear = (self.rear + 1) % (self.capacity)
        self.Q[self.rear] = item
        self.size = self.size + 1
        print("%s enqueued to queue" % str(item))

    # تحذف الدالة عنصرًا من الرتل
    # وتعدل الفهرس الأول وحجم الرتل
    def DeQueue(self):
        if self.isEmpty():
            print("Empty")
            return

        print("%s dequeued from queue" % str(self.Q[self.front]))
        self.front = (self.front + 1) % (self.capacity)
        self.size = self.size - 1

    # تجلب الدالة العنصر الأول في الرتل
    def que_front(self):
        if self.isEmpty():
            print("Queue is empty")

        print("Front item is", self.Q[self.front])

    # تجلب الدالة العنصر الأخير في الرتل
    def que_rear(self):
        if self.isEmpty():
            print("Queue is empty")
        print("Rear item is", self.Q[self.rear])


# اختبار الدوال السابقة
if __name__ == '__main__':
    queue = Queue(30)
    queue.EnQueue(10)
    queue.EnQueue(20)
    queue.EnQueue(30)
    queue.EnQueue(40)
    queue.DeQueue()
    queue.que_front()
    queue.que_rear()
