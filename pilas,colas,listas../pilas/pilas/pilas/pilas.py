

class Stack:#Pila 

    class Node:#Nodo
        def __init__(self,value):
            self.value=value
            self.next_node=None
    def setNextNode(self,next_node):
            self.next_node=next_node

    def __init__(self):
        self.top=None
        self.size=0

    def create_node(self,value):
        return self.Node(value)
    
    def push(self,value):#apilar
        node=self.create_node(value)    
        node.next_node=self.top
        self.top=node       
        self.size+=1

    def pop(self):#desapilar
        value = None
        if self.size>0:
            value=self.top.value#no lo etiendo
            self.top=self.top.next_node
            self.size-=1
        return value
    
    def delete(self):
        self.top=None
        self.size=0
        if self.top and self.size==0:
             return "stack is empty"
        
    def size(self):
        return self.size
    
    def peek(self):
        if self.top is not None:
            return self.top.value
        else:
            return None
        
    def list(self):
        values=[]
        pointer=self.top
        while pointer!=None:
            values.append(pointer.value)
            pointer=pointer.next_node
        return values

if __name__ == "__main__":
    stack = Stack()
    print("stack created")
    print("pushing=5")
    stack.push(5)
    print("listing="+str(stack.list())) # [8, 3, 5]
    print("pushing=3")
    stack.push(3)
    print("listing="+str(stack.list())) # [8, 3, 5]
    print("pushing=8")
    stack.push(8)
    print("listing="+str(stack.list())) # [8, 3, 5]
    print("poping="+str(stack.pop()))
    print("listing="+str(stack.list())) # [8, 3, 5] 
