class Node:
    def __init__(self, name, highest_final_class_label = None, subtrees = None):
        self.name = name
        if highest_final_class_label != None:
            self.highest_final_class_label = highest_final_class_label
        self.subtrees = []
        if subtrees != None:
            for node in subtrees:
                self.subtrees.append(node)