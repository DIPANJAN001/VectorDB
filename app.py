from  fastapi import FastAPI
import uvicorn
import numpy as np 
from database import Vector_Store
from text import read_pdf,tokenize_and_embed

app=FastAPI()
db=Vector_Store()

@app.get("/")
def index():
    return{"msg":"VectorDB is ready to store data"}

@app.get("/load_data")
def load_data():
    for i in range(len(sentence_embeddings)):
       db.add_vector(i,sentence_embeddings[i])
    
    return {"msg":f"Database is filled with {len(db.vectordb)} vectors"}

@app.get("/show_data/{id}")
def show_data(id:int):
    if id not in db.vectordb.keys():
      return{"msg":"vector does not exists"}
    return db.vectordb[id]


@app.post("/add_data/{id}")
def add_data(id:int):
    for ids in db.vectordb.keys():
        if id==ids:
            return {"msg":"Vector allready exists"}
    new_vector={"val":np.random.random(8)}
    db.vectordb[id]=f"{new_vector}"

@app.delete("/delete_data/{id}")
def delete_data(id:int):
    if id not in db.vectordb.keys():
      return{"msg":"vector does not exists"}
    del db.vectordb[id]


if __name__=="__main__":
    pdf_file_path = 'GOT.pdf'
    pdf_text = read_pdf(pdf_file_path)
    sentence_embeddings = tokenize_and_embed(pdf_text)
    uvicorn.run(app, host='127.0.0.1',port=8000)
