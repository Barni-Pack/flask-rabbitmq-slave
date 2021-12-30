
import os
print(os.listdir())
from app import app
if __name__ == "__main__":
    
    app.run(
        debug=True,
        host='localhost',
    )
