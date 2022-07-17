# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 10:05:06 2022

@author: Thomas Johnson III
"""

"""
Practice using linked lists.
"""

class node: # initializing the node class
    def __init__(self,  identifier, parent = None, child = None,):
        self.parent = parent # Set the parent for the node
        self.child = child #set the child for the node
        self.identifier = identifier # set the identifier for the node
    

    # method to delete the existing node
    def delete_node(self):
        del self
    
    # set the parent for an existing node
    def set_parent(self, new_parent):
        self.parent = new_parent
    
    # Continue searching through nodes in the lincked list
    def continue_search(self, target_identifier,base_node):
        if base_node.identifier == target_identifier:
            del base_node
        else: 
            base_node.continue_search(target_identifier, base_node.child)
        
    def search_nodes(self, target_identifier,root_node):
        if root_node.identifier == target_identifier:
            del(root_node)
        else:
            root_node.continue_search(target_identifier, root_node)
    
    def create_child(self, child_identifier):
        self.child = node(identifier = child_identifier, parent = self.identifier)
    
    def display_node(self):
        return("The node is identified as ", self.identifier," with parent ", 
               self.parent, " and child ", self.child, ".")
            
# The start_links() function is used to start running the code.
def start_links():
    new_node = node(identifier="12145_lone")
    new_node.create_child(child_identifier = "row_243")
    print(new_node.child.display_node())
    
    
start_links()