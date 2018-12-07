#Oscar Tobanche
#Prof. Diego Aguirre
#manoj saha
#CS 2302
#this code implements a binary search tree of words.
# Main program to test Binary search tree.
from BinarySearchTree import Node
from BinarySearchTree import BinarySearchTree
from lab_3_new import Node, AVLTree
from lab_3_new import RBTNode,RedBlackTree

mytree = BinarySearchTree()



text = open("glove.6B.50d.txt")
input_list = text.readlines()

for i in range(len(input_list)):
    input_list[i] = input_list[i][:-2]
myTree = None
tree_type = input('what type of tree do you want to use?, AVL or RBT \n')

if tree_type == 'AVL':
    myTree = AVLTree()
elif tree_type == 'RBT':
    myTree = RedBlackTree()

counter = 0
tree = AVLTree()
for ln in input_list:
    if counter == 50:
        break
    ln = ln.replace('\n', '')
    ln = Node(ln)
    tree.insert(ln)
    counter += 1


if tree_type == 'AVL':
    tree_AVL = AVLTree()
    for ln in input_list:
        ln = ln.replace('\n', '')
        words = Node(ln)
        tree_AVL.insert(words)
    print(tree_AVL)

if tree_type == 'RBT':
    tree_RBT = RedBlackTree()
    for ln in input_list:
        tree_RBT.insert(ln)
    print('tree has height ' + str(tree_RBT.get_height()))

user_values = input('Enter insert values with spaces between: ')
print()

for value in user_values.split():
    new_node = Node(int(value))
    tree.insert(new_node)

print('Initial tree:')
print(tree)
print()

remove_value = int(input('Enter value to remove: '))
print()

print('Tree after removing %d:' % remove_value)
tree.remove(remove_value)
print(tree)


