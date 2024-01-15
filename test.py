from database import Vector_Store
import numpy as np
db= Vector_Store()
for i in range(10):
    db.add_vector(i,np.random.random(8))

db.show_db()
