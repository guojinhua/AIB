# 1
def chirab(head,leg):
    for i in range(1,head+1):
        if leg == (i*2+(head-i)*4):
            return ("chicken:"+str(i),"rabbit:"+str(head-i))
    else:
        return ("no solutions!")

# print(chirab(35,94))
# print (chirab(2,1))

# 2
graph = {}
graph["you"] = ["alice","bob","claire"]
graph["bob"] = ["anuj","peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom","jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def findout(name):
    return (name[-1] == "m")

def main():
    searching = []
    searched = []
    searching += graph["you"]
    while searching:
        nextPeople = searching.pop()
        if findout(nextPeople):
            print(nextPeople + " is the buyer!")
        else:
            searched.append(nextPeople)
            searching += graph[nextPeople]

if __name__ == '__main__':
    main()

# 3 dfs
import os
import fnmatch
def dfstranverse(path):
    tranversing = []
    # tranversed = []
    tranversing.append(path)
    while tranversing:
        nextFile = tranversing.pop()
        try:
            list = os.listdir(nextFile)
        except WindowsError as e:
            pass

        for filename in list:
            next = os.path.join(nextFile,filename)
            if os.path.isfile(next):
                if fnmatch.fnmatch(filename,'*.dll'):
                    print (filename)
            elif os.path.isdir(next):
                tranversing.append(next)

# dfstranverse('C:\\')

# 4 bfs
class Queue:
    "A container with a first-in-first-out (FIFO) queuing policy."
    def __init__(self):
        self.list = []

    def push(self,item):
        "Enqueue the 'item' into the queue"
        self.list.insert(0,item)

    def pop(self):
        """
          Dequeue the earliest enqueued item still in the queue. This
          operation removes the item from the queue.
        """
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the queue is empty"
        return len(self.list) == 0

def bfstranverse(path):
    tranversing = Queue()
    tranversing.push(path)
    while not tranversing.isEmpty():
        nextFile = tranversing.pop()
        try:
            list = os.listdir(nextFile)
        except WindowsError as e:
            pass
        for filename in list:
            next = os.path.join(nextFile, filename)
            if os.path.isfile(next):
                if fnmatch.fnmatch(filename, '*dll'):
                    print(filename)
            elif os.path.isdir(next):
                tranversing.push(next)

# bfstranverse('C:\\')

# 5 uniform-cost-search
import math
goal = 85
# the length of the state list.
state = [0] * (goal+2)

start = 2
state[start] = 0
end = (int)((85+1)/2)

for k in range(start,end):
    for pos,cost in [(k*2, k),
        (k*2 + 1, math.floor(k/2)),
        (k*2+2, k+2)]:
        state[pos] = state[k] + cost

print(state[goal])

# 6 A* ## The answer is from teacher;
import math
AB_MAP = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
]
POS_UP = 1
POS_LEFT = 2
POS_DOWN = 3
POS_RIGHT = 4

def mod_map(map,pos_x,pos_y,val):
    map[pos_x][pos_y] = val

def print_map(map):
    rows = len(map)
    for i in range(0,rows):
        cols = len(map[i])
        for j in range(0,cols):
            print(str(map[i][j]),end='\n')


class Node(object):
    def __init__(self,x,y,h_n=0,g_n=0):
        self.pos_x = x
        self.pos_y = y
        self.parent = None
        self.h_n = h_n
        self.g_n = g_n
        self.f_n = self.h_n + self.g_n

    def update_h_n(self,target):
        self.h_n = int(math.sqrt((target.pos_x - self.pos_x)**2 + (target.pos_y - self.pos_y)**2))
        return self.h_n
    def update_g_n(self,source):
        self.h_n = int(math.sqrt((source.pos_x - self.pos_x)**2 + (source.pos_y - self.pos_y)**2))
        return self.g_n
    def update_f_n(self,source,target):
        self.f_n = self.update_g_n(source) + self.update_h_n(target)
        return self.f_n
    def update_parent(self,par):
        self.parent = par
        return self.parent

    def get_adj_node(self,flag,source,target):
        if flag == POS_UP:
            cur_node = Node(self.pos_x,self.pos_y-1)
            cur_node.update_f_n(source,target)
            cur_node.parent = self
            return cur_node
        elif flag == POS_LEFT:
            cur_node = Node(self.pos_x-1,self.pos_y)
            cur_node.update_f_n(source,target)
            cur_node.parent = self
            return cur_node
        elif flag == POS_DOWN:
            cur_node = Node(self.pos_x, self.pos_y+1)
            cur_node.update_f_n(source, target)
            cur_node.parent = self
            return cur_node
        elif flag == POS_RIGHT:
            cur_node = Node(self.pos_x+1, self.pos_y)
            cur_node.update_f_n(source, target)
            cur_node.parent = self
            return cur_node
        else: return None

def node_addible(node,open_list,close_list):
    index = str(node.pos_x) + '_' + str(node.pos_y)
    if index not in open_list and index not in close_list:
        open_list[index] = node

def reach_end(node,target):
    if node and target and node.pos_x == target.pos_x and node.pos_y == target.pos_y:
        return True
    else:
        return False

def handle_reach_end(node,map,modval,print_path=False):
    if node and map:
        while node:
            if print_path:
                print("x:%s,y%s"%(node.pos_x,node.pos_y))
            mod_map(map,node.pos_x,node.pos_y,modval)
            node = node.parent

def main(source,target,open_list,close_list,map):
    open_list[str(source.pos_x) +'_'+str(source.pos_y)] = source
    while open_list:
        tem_dict = sorted(open_list.items(),key=lambda d:d[1].f_n)
        first_key = tem_dict[0][0]
        first_node = open_list[first_key]
        del open_list[first_key]

        up_node = first_node.get_adj_node(POS_UP,source,target)
        if reach_end(up_node,target):
            handle_reach_end(up_node,map,2)
            break

        left_node = first_node.get_adj_node(POS_LEFT,source,target)
        if reach_end(left_node,target):
            handle_reach_end(left_node,map,2)
            break

        down_node = first_node.get_adj_node(POS_DOWN,source,target)
        if reach_end(down_node,target):
            handle_reach_end(down_node,map,2)
            break

        right_node = first_node.get_adj_node(POS_RIGHT,source,target)
        if reach_end(right_node,target):
            handle_reach_end(right_node,map,2)
            break

        if first_key not in close_list:
            close_list[first_key] = first_node

        node_addible(up_node,open_list,close_list)
        node_addible(left_node,open_list,close_list)
        node_addible(down_node,open_list,close_list)
        node_addible(right_node,open_list,close_list)

if __name__ == '__main__':
    print ("******************************* before *******************************")
    print(AB_MAP)
    OPEN_LIST = {}
    CLOSE_LIST = {}

    SOURCE = Node(3,4)
    TARGET = Node(13,9)
    main(SOURCE,TARGET,OPEN_LIST,CLOSE_LIST,AB_MAP)

    print ("******************************** after *******************************")
    mod_map(AB_MAP,SOURCE.pos_x,SOURCE.pos_y,0)
    mod_map(AB_MAP,TARGET.pos_x,TARGET.pos_y,0)
    print(AB_MAP)

