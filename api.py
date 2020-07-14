from src.app import app
from src.config import PORT
import src.controllers.chatsystem

app.run("0.0.0.0", PORT, debug=True)