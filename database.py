import numpy as np 




class Vector_Store:
    def __init__(self):
        self.vectordb={}
    
    def add_vector(self,id,vector):
        vec={"val":vector}
        self.vectordb[id]=f"{vec}"

    def show_db(self):
        print(self.vectordb)

