from Maze import *
from GUI import *

def main():
    maze = Maze(10)
    mat,num = maze.randomMap()
    matans = maze.mazeAnswer()
    inter = gui(mat,num)
    inter.run(matans)

if __name__ == "__main__":
    main()
