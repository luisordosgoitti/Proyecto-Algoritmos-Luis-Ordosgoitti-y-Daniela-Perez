from db import db
from galeria import Galeria

def main():
  galeria = Galeria(db)
  galeria.start()
main()
