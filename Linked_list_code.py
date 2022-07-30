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
        self.identifier = identifier.lower() # set the identifier for the node
    

    # method to delete the existing node
    def delete_node(self):
        del self
    
    # set the parent for an existing node
    def set_parent(self, new_parent):
        self.parent = new_parent
    
    # Continue searching through nodes in the lincked list
    def continue_search(self, target_identifier):
        #print("The current node identifier: ",self.identifier)
        #print("The target identifier: ",target_identifier)
        if self.identifier == target_identifier:
            print("Found the node.")
            print(self)
            return(self)
        elif(self.get_child() is None):
            #print("No children detected in sub levels. Returning None.")
            return("The node with identifier " + target_identifier +" does not exist.")
        else:
            child_node = self.get_child()
            child_node_result = child_node.continue_search(target_identifier)
            return(child_node_result)
        
    def search_nodes(self, target_identifier):
        target_identifier = target_identifier.lower()
        #print("The current node identifier: ",self.identifier)
        #print("The target identifier: ",target_identifier)
        if self.identifier == target_identifier:
            return(self)
        else:
            if(self.get_child() is None):
                #print("No children detected top level. Returning response.")
                return("The node with identifier " + target_identifier +" does not exist.")
            else:
                child_node = self.get_child()
                result_of_search = child_node.continue_search(target_identifier)
                print("Print result", result_of_search)
                return(result_of_search)
    
    def create_child(self, child_identifier):
        self.child = node(identifier = child_identifier.lower(), parent = self.identifier)
    
    def display_node(self):
        if(self.child != None):
            return("The node is identified as ", self.identifier," with parent ", 
                   self.parent, " and child ", self.child.identifier, ".")
        else:
            return("The node is identified as ", self.identifier," with parent ", 
                   self.parent,".")
          
               
    def get_child(self):
        return(self.child)
            
# The start_links() function is used to start running the code.
def start_links():
    new_node = node(identifier="12145_lone")
    new_node.create_child(child_identifier = "row_243")
    new_node.child.create_child(child_identifier = "bref_563_c")
    node_3 = new_node.child.child
    node_3.create_child(child_identifier = "zoz_54")
    node_4 = node_3.get_child()
    print(new_node.child.display_node())
    print(node_3.display_node())
    print(node_4.parent)
    print(node_4.display_node())
    identifier_search_value = "bref_563_c"
    result_of_search = new_node.search_nodes(identifier_search_value)
    print("The search for ",identifier_search_value," yielded: ", result_of_search, "with identifier:", result_of_search.identifier,".")
    
    
start_links()
