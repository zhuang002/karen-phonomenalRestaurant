n = 0
m = 0

class Restaurant:
    def __init__(self, id):  # constructor
        self.id = id
        self.is_pho = False
        self.connected = []


def load_tree():
    n, m = map(int, input().split(" "))
    restaurants = []
    for i in range(n):
        rest = Restaurant(i)
        restaurants.append(rest)

    pho_restaurants = input().split(" ")   # input() <- "1, 3, 5".  input().split(" ") <- ["1", "3", "5"]

    a_pho_rest = None
    for i in range(n-1):
        id1, id2 = map(int, input().split(' '))
        rest1 = restaurants[id1]
        rest1.is_pho = str(id1) in pho_restaurants  # id1 <- 1, str(id1) <- "1",   "1" in ["1", "3", "5"] <- True.
        rest2 = restaurants[id2]
        rest2.is_pho = str(id2) in pho_restaurants  # id2 <- 2, str(id2) <- "2",  "2" in ["1","3","5"] <- False.
        rest1.connected.append(rest2)
        rest2.connected.append(rest1)
        if not a_pho_rest:
            if rest1.is_pho:
                a_pho_rest = rest1
            elif rest2.is_pho:
                a_pho_rest = rest2

    return a_pho_rest


def is_removable(parent, current):
    removable_subnodes = []

    for subnode in current.connected:
        if subnode==parent:
            continue
        else:
            if is_removable(current, subnode):
                removable_subnodes.append(subnode)
    for sub in removable_subnodes:
        current.connected.remove(sub)

    n -= len(removable_subnodes)
    if len(current.connected) == 1 and not current.is_pho:
        return True
    return False


def remove_unneeded(root):
    removable_subnodes = []
    for subnode in root.connected:
        if is_removable(root, subnode):
            removable_subnodes.append(subnode)
    for sub in removable_subnodes:
        root.connected.remove(sub)
    n -= len(removable_subnodes)
    return root, n-1



root = load_tree()
root, num_paths = remove_unneeded(root)
node, distance = get_furthest_node(root)
node, distance = get_furthest_node(node)

print(distance + (num_paths - distance) * 2)
