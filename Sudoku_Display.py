""" Task: The department you work for has received a project that displays the solved sudoku puzzles in a digital environment. 

 Write a Python code to print out the given sudoku puzzle matrix in the following format.
 Given format :
 sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 7, 0, 0]
 ]
 Desired output format :
 - - - - - - - - - - - - - - - 
 0  0  0  | 0  6  4  | 0  0  0  
 7  0  0  | 0  0  0  | 3  9  0  
 8  0  0  | 0  0  0  | 0  0  0  
 - - - - - - - - - - - - - - - 
 0  0  0  | 5  0  2  | 0  6  0  
 0  8  0  | 4  0  0  | 0  0  0  
 3  5  0  | 6  0  0  | 0  7  0  
 - - - - - - - - - - - - - - - 
 0  0  2  | 0  0  0  | 1  0  3  
 0  0  1  | 0  5  9  | 0  0  0  
 0  0  0  | 0  0  0  | 7  0  0  
 - - - - - - - - - - - - - - -

"""


def sudoku2(puzzle):
    print("- - - - - - - - - - - - - - - -")
    if len(puzzle)==9:
        for i in puzzle:
            if puzzle.index(i)==3 or puzzle.index(i)==6 :
                print("- - - - - - - - - - - - - - - -")
            if len(i)==9:
                i.insert(3,"|")
                i.insert(7,"|")
                
                print('  '.join(str(e) for e in i))
        print("- - - - - - - - - - - - - - - -")