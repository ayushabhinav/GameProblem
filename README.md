# GameProblem

Problem Description:- 
  It is a treasure hunt game.
  You have been given a matrix whoes cells contain any of four value -> -1, 0, 1, 2
  
  -1 :- It is dangerous to visit the cell. You cannot visit the cell
   0 :- It is safe to visit the cell
   1 :- Your start position
   2 :  Position of Treasure
   
   Allowed moves are up, down, left, right. No diagonal movement.
   
   You have to find if it is possible to find the treasure from your current position.
   
   
   There are two solution files:-
   
   1. game_v1.py - 
        This check if the solution exists or not. 
        It tries to visit all the cell from the start position and retunrn true if target cell is reached.
        
   2. game_v2.py -
        This gives the path travered to reach the target location. The path will not necessarily be the shortest path.
        It used the brute force approach and recurssion to reach the solution.
      
   
   
