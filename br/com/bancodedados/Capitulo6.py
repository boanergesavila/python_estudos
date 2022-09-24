import os
import sqlite3

os.remove("escola.db") if os.path.exists("escola.db") else None

con = sqlite3.connect('escola.db')

type(con)
