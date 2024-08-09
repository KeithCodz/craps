import random
die1 = random.randint(1,6)
die2 = random.randint(1,6)


print( die1, die2)


total = die1 + die2
print(total)


if total == 7 or total == 11:
    print( 'Player rolled',die1,'+',die2, ' = ',total)
    print('You win!')

elif total == 2 or total == 3 or total == 12:
    print( 'Player rolled',die1,'+',die2, ' = ',total)
    print('You lose!')

else:
    print( 'Player rolled',die1,'+',die2, ' = ',total)
    print('Point to make is', total)
    
    playerPoint = total 
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    total = die1 + die2
    print( die1, die2)
    print(total)
            
#code from here is not executed  

    while not total == 7 and total == playerPoint:
        
      print( 'Player rolled',die1,'+',die2, ' = ',total)
      die1 = random.randint(1,6)
      die2 = random.randint(1,6)
      total = die1 + die2
      print( die1, die2)
      print(total)


     
    else:
      if total == 7: 
        print( 'Player rolled',die1,'+',die2, ' = ',total)
        print('You lose!')
              
      elif total == playerPoint:
        print( 'Player rolled',die1,'+',die2, ' = ',total)
        print('You win!')

  


          
        
       
   







               
    
