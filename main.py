# Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, node):
        node.parent = self
        self.children.append(node)

    def get_level(self):
        level = 0
        p = self.parent
        while p is not None:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = 3 * " " * self.get_level()
        prefix = spaces + "|-->"
        print(prefix + self.data)
        for child in self.children:
            child.print_tree()
            # use of recursion


def build_product_tree():
    electronics = Node("Electronics")
    mobile = Node("mobile")
    electronics.add_child(mobile)
    tv = Node("TV")
    electronics.add_child(tv)

    iphone = Node("IPhone")
    oneplus = Node("Oneplus")
    oppo = Node("Oppo")
    vivo = Node("Vivo")
    mobile.add_child(iphone)
    mobile.add_child(oneplus)
    mobile.add_child(oppo)
    mobile.add_child(vivo)

    samsungTV = Node("Samsung TV")
    miTV = Node("Xiaomi TV")

    tv.add_child(samsungTV)
    tv.add_child(miTV)
    return electronics


if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()
