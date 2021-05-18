
class Tree:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children


    def __str__(self, level=0):
        ret = ' ' * level + str(self.data + '\n')
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret


    def add_child(self, Tree):
        self.children.append(Tree)


tree = Tree('Drinks', [])
cold = Tree('Cold', [])
hot = Tree('Hot', [])

tree.add_child(cold)
tree.add_child(hot)

tea = Tree('Tea', [])
coffee = Tree('Coffee', [])
hot.add_child(tea)
hot.add_child(coffee)

cola = Tree('Cola', [])
fanta = Tree('Fanta', [])
cold.add_child(cola)
cold.add_child(fanta)
print(tree)