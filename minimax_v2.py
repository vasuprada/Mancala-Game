import csv
import math

global task
global player_no
global cut_off_depth
global board_two
global board_one
global mancala_two
global mancala_one
global board 


task=0
player_no=0
cut_off_depth=0
board_two=""
board_one=""
mancala_two=""
mancala_one=""
max_eval = -99999999999
board = ""
final = ""
turn = 0

                                        
def minimax(start,player_no,board,len_one,depth,cut_off_depth,state,eval_value,playing):
        global final
        global max_eval
        global turn
     
  
        dummy = list(board)

        if(player_no == 1):     
                      picked_index = start
                      
                      picked_value = dummy[picked_index]
                      
                      start_from = start+1
                 
                      m = len(dummy)-1
                      dummy[picked_index] = 0

                      while picked_value != 0:
                               
                                 
                                if start_from <= len_one:
                                        picked_value -= 1
                                        #condition 1- ENDS IN MANCALA-Free turn
                                        if (start_from == len_one) and (picked_value == 0):
                                              # Free turns so this become MAX NODE
                                              state = 1
                                              dummy[len_one]+= 1
                                              #print 'AT CONDITION 1'
                                              flag = 0
                                              flag2 = 0
                                                
                                              for u in range(0,len_one):
                                                      if dummy[u]!=0:
                                                        flag = 1
                                                        break
                                                                                                                                                                                                      
                                              for x in range(len_one+2,len(dummy)):
                                                      if dummy[x]!=0:
                                                        flag2 = 1
                                                        break
                                                                                                              
                                              if flag == 0:
                                                      for n in range(len_one+2,len(dummy)):
                                                              dummy[len_one+1] += dummy[n]
                                                              if(dummy[n]!=0):
                                                                      dummy[n]=0
                                                                                                                    
                                              if flag2 == 0:
                                                      for v in range(0,len_one):
                                                              dummy[len_one] += dummy[v]
                                                              if(dummy[v]!=0):
                                                                      dummy[v]=0
                                                         
                                               

                                                # Either or Both Boards Became empty
                                              if (flag2 == 0 or flag == 0):
                                                  if turn == 1:
                                                      temp = dummy[len_one] - dummy[len_one+1]
                                                      state = 1

                                                  else:
                                                      temp = dummy[len_one + 1] - dummy[len_one]
                                                      state = 0

  
                                                  if(playing == 1 and turn == 1):
                                                      if temp > max_eval:
                                                          max_eval = temp
                                                          final = list(dummy)
  
                                                  #print 'B' + str(start+2)+ "," + str(depth) + "," + str(temp)
                                                  output_file_handle_log.write('B' + str(start+2)+ "," + str(depth) + "," + str(temp) + '\n')
                                                  return temp
                                                      
                                              #greedy call
                                              
                                           
                                              if turn == 1:
                                                  state = 1
                                                  eval_value = float("-inf")
                                                  #print 'B'+ str(start+2)+ "," + str(depth) + "," + str("-Infinity")
                                                  output_file_handle_log.write('B' + str(start+2)+ "," + str(depth) + "," + str("-Infinity") + '\n')
                                              else:
                                                  state = 0
                                                  eval_value = float("inf")
                                                  #print 'B'+ str(start+2)+ "," + str(depth) + "," + str("Infinity")
                                                  output_file_handle_log.write('B' + str(start+2)+ "," + str(depth) + "," + str("Infinity") + '\n')
  
                                              for start_index in range(0,len_one):
  
                                                  
                                                  if dummy[start_index] == 0:
                                                      
                                                      continue
                                                  my_val = float("-inf")
                                                  
                                                  ret_val = minimax(start_index,player_no,dummy,len_one,depth,cut_off_depth,0,my_val,playing)
                                                 
                                                  
                                                  if state == 1:
                                                      eval_value = max(eval_value,ret_val)
                                                     
                                                  else:
                                                      eval_value = min(eval_value,ret_val)
                                                      
                                                  
  
                                                  #print 'B'+ str(start+2)+ "," + str(depth) + "," + str(eval_value)
                                                  output_file_handle_log.write('B' + str(start+2)+ "," + str(depth) + "," + str(eval_value) + '\n')
                                                  
  
                                              return eval_value
                                                
                     
                                        #condition 2- ENDS IN EMPTY PIT ON SAME SIDE  
                                        elif (picked_value == 0) and (dummy[start_from] == 0):
                                              #mancala 1 will get beads from both player1 and opp pit
                                              #print 'AT CONDITION 2'
                                              state = 0
                                              flag = 0
                                              flag2 = 0
                                              dummy[start_from] = 1
                                              x = start_from + len_one + 2
                                              dummy[len_one] = dummy[len_one] + dummy[start_from]+ dummy[x]
                                              dummy[start_from] = 0
                                              dummy[x]= 0
                                            
                                              for u in range(0,len_one):
                                                      if dummy[u]!=0:
                                                        flag = 1
                                                        break
                                                                                                                                                                                                      
                                              for x in range(len_one+2,len(dummy)):
                                                      if dummy[x]!=0:
                                                        flag2 = 1
                                                        break
                                                                                                                
                                              if flag == 0:
                                                      for n in range(len_one+2,len(dummy)):
                                                              dummy[len_one+1] += dummy[n]
                                                              if(dummy[n]!=0):
                                                                      dummy[n]=0
                                                                                                                    
                                              if flag2 == 0:
                                                      for v in range(0,len_one):
                                                              dummy[len_one] += dummy[v]
                                                              if(dummy[v]!=0):
                                                                      dummy[v]=0

                                      

                                              # GAME ENDS FOR PLAYER 1 - PLAYER 2 NEEDS TO PLAY
                                              if depth == cut_off_depth:
                                                  
                                                  if turn == 1:
                                                      temp = dummy[len_one] - dummy[len_one+1]
                                                      
                                                      if cut_off_depth == 1:
                                                          if temp > max_eval:
                                                              max_eval = temp
                                                              
                                                              final = list(dummy) 
                                                      
                                                  else:
                                                      temp = dummy[len_one + 1] - dummy[len_one]
                                                      

                                                  #print 'B'+ str(start+2)+ "," + str(depth) + "," + str(temp)
                                                  output_file_handle_log.write('B' + str(start+2)+ "," + str(depth) + "," + str(temp) + '\n')
                                                  
                                                  state = 1
                                                  return temp


                                              
                                              if (flag2 == 0 or flag == 0):
                                                  if turn == 1:
                                                      temp = dummy[len_one] - dummy[len_one+1]
                                                      state = 0
                                                     
                                                  else:
                                                      temp = dummy[len_one + 1] - dummy[len_one]
                                                      state = 1
                                                  
  
                                                  if(playing == 1 and turn == 1):
                                                      if temp > max_eval:
                                                          max_eval = temp
                                                          
                                                          final = list(dummy)
  
                                                  #print 'B'+ str(start+2) + "," + str(depth) + "," + str(temp)
                                                  output_file_handle_log.write('B' + str(start+2)+ "," + str(depth) + "," + str(temp) + '\n')
                                                  return temp
                                              
                                              #next player's call
                                              if turn == 1:
                                                  state = 0
                                                  eval_value = float("inf")
                                                  #print 'B' + str(start+2) + "," + str(depth) + "," + str("Infinity")
                                                  output_file_handle_log.write('B' + str(start+2)+ "," + str(depth) + "," + str("Infinity") + '\n')
                                                  
                                              else:
                                                  state = 1
                                                  eval_value = float("-inf")
                                                  #print 'B'+ str(start+2) + "," + str(depth) + "," + str("-Infinity")
                                                  output_file_handle_log.write('B' + str(start+2)+ "," + str(depth) + "," + str("-Infinity") + '\n')
                                              
                                              for start_index in range(len_one+2,len(dummy)):
                                                 
                                                  if dummy[start_index] == 0:
                                                    
                                                      continue
                                                  my_val = float("inf")
                                               
                                                  ret_val = minimax(start_index,2,dummy,len_one,depth + 1,cut_off_depth,0,my_val,0)
                                                 

                                                  if state == 1:
                                                      eval_value = max(eval_value,ret_val)
                                                     
                                                  else:
                                                      eval_value = min(eval_value,ret_val)
                                                 

                                                  #print 'B'+ str(start+2) + "," + str(depth) + "," + str(eval_value)
                                                  output_file_handle_log.write('B' + str(start+2)+ "," + str(depth) + "," + str(eval_value) + '\n')
                                                    

                                              if playing == 1 and turn == 1:
                                                  if eval_value > max_eval:
                                                      max_eval = eval_value
                                                      
                                                      final = list(dummy)
                                                  
                                              return eval_value 
    
                                        #Condition 3 - Putting Stones and ends on my side
                                        elif ((picked_value == 0) and (start_from < len_one)):
                                                    #print "AT CONDITION 3"
                                                    dummy[start_from] += 1
                                                    start_from += 1
                                                   
                                                    #GAME ENDS FOR PLAYER 1 HERE AS WELL - PLAYER 2 NEEDS TO PLAY
                                                    if depth == cut_off_depth:
                                                        if turn == 1:
                                                            temp = dummy[len_one] - dummy[len_one+1]
                                                           
                                                            if cut_off_depth == 1:
                                                                 if temp > max_eval:
                                                                    max_eval = temp
                                                                    
                                                                    final = list(dummy) 
                                                            
                                                        else:
                                                            temp = dummy[len_one + 1] - dummy[len_one]
                                                            

                                                        #print 'B'+ str(start+2) + "," + str(depth) + "," + str(temp)
                                                        output_file_handle_log.write('B' + str(start+2)+ "," + str(depth) + "," + str(temp) + '\n')
                                                        
                                                        state = 1
                                                        return temp

                                                    if turn == 1:
                                                        state = 0
                                                        eval_value = float("inf")
                                                        #print 'B'+ str(start+2)+ "," + str(depth) + "," + str("Infinity")
                                                        output_file_handle_log.write('B' + str(start+2)+ "," + str(depth) + "," + str("Infinity") + '\n')
                                                    
                                                    else:
                                                        state = 1
                                                        eval_value = float("-inf")
                                                        #print 'B'+ str(start+2)+ "," + str(depth) + "," + str("-Infinity")
                                                        output_file_handle_log.write('B' + str(start+2)+ "," + str(depth) + "," + str("-Infinity") + '\n')

                                                    for start_index in range(len_one+2,len(dummy)):
                                                       
                                                        if dummy[start_index] == 0:
                                                                continue
                                                        
                                                        my_val = float("inf")
                                                        
                                                        ret_val = minimax(start_index,2,dummy,len_one,depth + 1,cut_off_depth,0,my_val,0)
                                                      

                                                        if state == 1:
                                                            eval_value = max(eval_value,ret_val)
                                                          
                                                        else:
                                                            eval_value = min(eval_value,ret_val)
                                                     

                                                        #print 'B'+ str(start+2)+ "," + str(depth) + "," + str(eval_value)
                                                        output_file_handle_log.write('B' + str(start+2)+ "," + str(depth) + "," + str(eval_value) + '\n')

                                                    if playing == 1 and turn == 1:
                                                        #print 'I am inside here:'
                                                        if eval_value > max_eval:
                                                            max_eval = eval_value
                                                            
                                                            final = list(dummy)

                                                    return eval_value
                                                       
                                                        
                                                    
                                                
                                        #conditon 4 - Just dropping beads one by one
                                        else:
                                                #print 'AT CONDITION 4'
                                                dummy[start_from] += 1
                                                start_from += 1
                       
                                else:
                                        # more beads - so adding to player 2's board
                                        #print 'In PLayer 2 board side'

                                        m = len(dummy)-1
                                                                                                                                    
                                        while(picked_value!= 0 and m > len_one + 1):
                                                picked_value -= 1
                                                dummy[m] += 1
                                                m -= 1
                                               

                                        if(picked_value > 0):
                                                #print "SKIPPING"
                                                start_from = 0
                                                m = len(dummy)-1

                                   
                                     
                                        if picked_value == 0:
                                                flag1 = 0
                                                for u in range(0,len_one):
                                                        if dummy[u]!=0:
                                                          flag1 = 1
                                                          break
                                                if flag1 == 0:
                                                        for n in range(len_one+2,len(dummy)):
                                                                dummy[len_one+1] += dummy[n]
                                                                if dummy[n]!=0:
                                                                  dummy[n]=0

                                                

                                                if depth == cut_off_depth:
                                                    if turn == 1:
                                                        temp = dummy[len_one] - dummy[len_one+1]
                                                       
                                                        if cut_off_depth == 1:
                                                            if temp > max_eval:
                                                                max_eval = temp
                                                                                                                              
                                                                final = list(dummy) 
                                                            
                                                    else:
                                                        temp = dummy[len_one + 1] - dummy[len_one]
                                                       

                                                    #print 'B'+ str(start+2)+ "," + str(depth) + "," + str(temp)
                                                    output_file_handle_log.write('B' + str(start+2)+ "," + str(depth) + "," + str(temp) + '\n')
                                                    state = 1
                                                    return temp

                                                if (flag1 == 0):
                                                  if turn == 1:
                                                      temp = dummy[len_one] - dummy[len_one+1]
                                                      state = 1
                                                     
                                                  else:
                                                      temp = dummy[len_one + 1] - dummy[len_one]
                                                      state = 0
                                                    
  
                                                  if(playing == 1 and turn == 1):
                                                      if temp > max_eval:
                                                          max_eval = temp
                                                          
                                                          final = list(dummy)
  
                                                  #print 'B'+ str(start+2)+ "," +str(depth)+ "," + str(temp)
                                                  output_file_handle_log.write('B' + str(start+2)+ "," + str(depth) + "," + str(temp) + '\n')
                                                  return temp
                                                    
                                                if turn == 1:
                                                    state = 0
                                                    eval_value = float("inf")
                                                    #print 'B'+ str(start+2)+ "," +str(depth)+ "," +str("Infinity")
                                                    output_file_handle_log.write('B' + str(start+2)+ "," + str(depth) + "," + str("Infinity") + '\n')
                                                    
                                                else:
                                                    state = 1
                                                    eval_value = float("-inf")
                                                    #print 'B'+ str(start+2)+ "," +str(depth)+ "," +str("-Infinity")
                                                    output_file_handle_log.write('B' + str(start+2)+ "," + str(depth) + "," + str("-Infinity") + '\n')

                                                for start_index in range(len_one+2,len(dummy)):
                                                    
                                                    if dummy[start_index] == 0:
                                                        
                                                        continue    

                                                    my_val = float("inf")
                                                    ret_val = minimax(start_index,2,dummy,len_one,depth + 1,cut_off_depth,0,my_val,0)
                                                    

                                                    if state == 1:
                                                        eval_value = max(eval_value,ret_val)
                                                        
                                                    else:
                                                        eval_value = min(eval_value,ret_val)
                                                        

                                                    #print 'B'+ str(start+2)+ "," +str(depth)+ "," + str(eval_value)
                                                    output_file_handle_log.write('B' + str(start+2)+ "," + str(depth) + "," + str(eval_value) + '\n')
                                                    

                                                if playing == 1 and turn == 1:
                                                    if eval_value > max_eval:
                                                        max_eval = eval_value
                                                        final = list(dummy) 
                                                    
                                                return eval_value
                                              
                       
                        
                        
        else:#player 2
                        offset = start - len_one
                        
                        picked_index = start
                        
                        picked_value = dummy[picked_index]
                        
                        start_from = start-1 
                       
                        dummy[picked_index] = 0
                        m = 0

                        while picked_value != 0:
                               
                                 
                                if start_from >= len_one+1:
                                        picked_value -= 1
                                        #condition 1- ENDS IN MANCALA-Free turn
                                        if (start_from == len_one+1) and (picked_value == 0):
                                                dummy[len_one+1] += 1
                                                #print 'AT CONDITION 1'
                                                flag = 0
                                                flag2 = 0
                                                
                                                for u in range(0,len_one):
                                                        if dummy[u]!=0:
                                                          flag = 1
                                                          break
                                                                                                                                                                                                        
                                                for x in range(len_one+2,len(dummy)):
                                                        if dummy[x]!=0:
                                                          flag2 = 1
                                                          break
                                                                                                                
                                                if flag == 0:
                                                        for n in range(len_one+2,len(dummy)):
                                                                dummy[len_one+1] += dummy[n]
                                                                if(dummy[n]!=0):
                                                                        dummy[n]=0
                                                                                                                    
                                                if flag2 == 0:
                                                        for v in range(0,len_one):
                                                                dummy[len_one] += dummy[v]
                                                                if(dummy[v]!=0):
                                                                        dummy[v]=0
                                                
                                                                                       
                                               

                                                # Either or Both Boards Became empty
                                                if (flag2 == 0 or flag == 0):
                                                    if turn == 2:
                                                        temp = dummy[len_one + 1] - dummy[len_one]
                                                        state = 1
                                                
                                                    else:
                                                        temp = dummy[len_one] - dummy[len_one + 1]
                                                        state = 0
                                                

                                                    if(playing == 1 and turn == 2):
                                                        if temp > max_eval:
                                                            max_eval = temp
                                                            final = list(dummy)

                                                    #print 'A'+ str(offset)+ "," +str(depth)+ "," +str(temp)
                                                    output_file_handle_log.write('A'+ str(offset)+ "," +str(depth)+ "," + str(temp) + '\n')
                                                    return temp
                                                        
                                                #greedy call
                                                if turn == 2:
                                                    state = 1
                                                    eval_value = float("-inf")
                                                    #print 'A'+ str(offset)+ "," +str(depth)+ "," +str("-Infinity")
                                                    output_file_handle_log.write('A'+ str(offset)+ "," +str(depth)+ "," +str("-Infinity") + '\n')
                                                else:
                                                    state = 0
                                                    eval_value = float("inf")
                                                    #print 'A'+ str(offset)+ "," +str(depth)+ "," +str("Infinity")
                                                    output_file_handle_log.write('A'+ str(offset)+ "," +str(depth)+ "," + str("Infinity") + '\n')

                                                for start_index in range(len_one+2,len(dummy)):
                                                    
                                                    if dummy[start_index] == 0:
                                                     
                                                        continue

                                                    my_val = float("-inf")
                                                    ret_val = minimax(start_index,player_no,dummy,len_one,depth,cut_off_depth,0,my_val,playing)
                                                    
                                                    if state == 1:
                                                        eval_value = max(eval_value,ret_val)
                                                       
                                                    
                                                    else:
                                                        eval_value = min(eval_value,ret_val)
                                                      

                                                    #print 'A'+ str(offset)+ "," +str(depth)+ "," + str(eval_value)
                                                    output_file_handle_log.write('A'+ str(offset)+ "," + str(depth)+ "," + str(eval_value) + '\n')
                                                    
                                              
                                                
                                                return eval_value
                                                
                     
                                        #condition 2- ENDS IN EMPTY PIT ON SAME SIDE  
                                        elif (picked_value == 0) and (dummy[start_from] == 0):
                                                #mancala 1 will get beads from both player1 and opp pit
                                                #print 'AT CONDITION 2'
                                                flag = 0
                                                flag2 = 0
                                                dummy[start_from] = 1
                                                x = start_from - len_one - 2
                                                dummy[len_one + 1] = dummy[len_one + 1] + dummy[start_from]+ dummy[x]
                                                dummy[start_from] = 0
                                                dummy[x]= 0
                                            
                                                for u in range(0,len_one):
                                                        if dummy[u]!=0:
                                                          flag = 1
                                                          break
                                                                                                                                                                                                        
                                                for x in range(len_one+2,len(dummy)):
                                                        if dummy[x]!=0:
                                                          flag2 = 1
                                                          break
                                                                                                                
                                                if flag == 0:
                                                      for n in range(len_one+2,len(dummy)):
                                                        dummy[len_one+1] += dummy[n]
                                                        if(dummy[n]!=0):
                                                          dummy[n]=0
                                                                                                                    
                                                if flag2 == 0:
                                                      for v in range(0,len_one):
                                                        dummy[len_one] += dummy[v]
                                                        if(dummy[v]!=0):
                                                          dummy[v]=0

                                               
                                                #GAME ENDS FOR PLAYER 2 - PLAYER 1 NEEDS TO PLAY
                                                if depth == cut_off_depth:
                                                    if turn == 2:
                                                        temp = dummy[len_one + 1] - dummy[len_one]
                                                      
                                                        if cut_off_depth == 1:
                                                            if temp > max_eval:
                                                                max_eval = temp
                                                               
                                                                final = list(dummy) 
                                                        
                                                    else:
                                                        temp = dummy[len_one] - dummy[len_one + 1]
                                                      

                                                    #print 'A'+ str(offset)+ "," +str(depth)+ "," +str(temp)
                                                    output_file_handle_log.write('A'+ str(offset)+ "," + str(depth)+ "," + str(temp) + '\n')
                                                    state = 1
                                                    return temp

                                                
                                                #Boards empty
                                                if (flag2 == 0 or flag == 0):
                                                    if turn == 2:

                                                        temp = dummy[len_one + 1] - dummy[len_one]
                                                        state = 0
                                                        
                                                    else:

                                                        temp = dummy[len_one] - dummy[len_one + 1]
                                                        state = 1
                                                        

                                                    if(playing == 1 and turn == 2):
                                                        if temp > max_eval:
                                                            max_eval = temp
                                                            
                                                            final = list(dummy)

                                                    #print 'A'+ str(offset)+ "," +str(depth)+ "," + str(temp)
                                                    output_file_handle_log.write('A'+ str(offset)+ "," + str(depth)+ "," + str(temp) + '\n')
                                                    return temp

                                                #next player's call
                                                
                                                if turn == 2:
                                                    state = 0
                                                    eval_value = float("inf")
                                                    #print 'A'+ str(offset)+ "," +str(depth)+ "," +str("Infinity")
                                                    output_file_handle_log.write('A'+ str(offset)+ "," + str(depth)+ "," + str("Infinity") + '\n')
                                                    
                                                else:
                                                    state = 1
                                                    eval_value = float("-inf")
                                                    #print 'A'+ str(offset)+ "," +str(depth)+ "," +str("-Infinity")
                                                    output_file_handle_log.write('A'+ str(offset)+ "," + str(depth)+ "," + str("-Infinity") + '\n')

                                                for start_index in range(0,len_one):
                                               
                                                    if dummy[start_index] == 0:
                                                       
                                                        continue

                                                    my_val = float("inf")
                                                    ret_val = minimax(start_index,1,dummy,len_one,depth + 1,cut_off_depth,0,my_val,0)
                                                                                                 

                                                    if state == 1:
                                                        eval_value  = max(eval_value,ret_val)
                                                    
                                                    else:
                                                        eval_value = min(eval_value,ret_val)
                                                   

                                                    #print 'A'+ str(offset)+ "," +str(depth)+ "," +str(eval_value)
                                                    output_file_handle_log.write('A'+ str(offset)+ "," + str(depth)+ "," + str(eval_value) + '\n')

                                                if playing == 1 and turn == 2:
                                                    if eval_value > max_eval:
                                                        max_eval = eval_value
                                                       
                                                        final = list(dummy) 
                                                    
                                                return eval_value


                                        #Condition 3 - Putting Stones and ends on my side
                                        elif ((picked_value == 0) and (start_from > len_one + 1)):
                                            #print 'AT CONDITION 3'
                                            dummy[start_from] += 1
                                            start_from -= 1

                                    
                                            if depth == cut_off_depth:
                                                        if turn == 2:
                                                            temp = dummy[len_one + 1] - dummy[len_one]
                                                   
                                                            if cut_off_depth == 1:
                                                                if temp > max_eval:
                                                                    max_eval = temp
                                                                
                                                                    final = list(dummy) 
                                                        else:
                                                            temp = dummy[len_one] - dummy[len_one + 1]

                                                        #print 'A'+ str(offset)+ "," +str(depth)+ "," +str(temp)
                                                        output_file_handle_log.write('A'+ str(offset)+ "," + str(depth)+ "," + str(temp) + '\n')
                                                        state = 1
                                                        return temp

                                            if turn == 2:
                                                state = 0
                                                eval_value = float("inf")
                                                #print 'A'+ str(offset)+ "," +str(depth)+ "," +str("Infinity")
                                                output_file_handle_log.write('A'+ str(offset)+ "," + str(depth)+ "," + str("Infinity") + '\n')
                                                    
                                            else:
                                                state = 1
                                                eval_value = float("-inf")
                                                #print 'A'+ str(offset)+ "," +str(depth)+ "," +str("-Infinity")
                                                output_file_handle_log.write('A'+ str(offset)+ "," + str(depth)+ "," + str("-Infinity") + '\n')

                                            
                                            for start_index in range(0,len_one):
                                              
                                                if dummy[start_index] == 0:
                                                        continue

                                                my_val = float("inf")
                                                ret_val = minimax(start_index,1,dummy,len_one,depth + 1,cut_off_depth,0,my_val,0)
                                                

                                                if state == 1:
                                                    eval_value  = max(eval_value,ret_val)
        
                                                else:
                                                    eval_value = min(eval_value,ret_val)


                                                #print 'A'+ str(offset)+ "," +str(depth)+ "," +str(eval_value)
                                                output_file_handle_log.write('A'+ str(offset)+ "," + str(depth)+ "," + str(eval_value) + '\n')

                                            if playing == 1 and turn == 2:
                                                if eval_value > max_eval:
                                                    max_eval = eval_value
                                                    final = list(dummy) 
                                                    
                                            return eval_value
                                                    
                                                
                                        #conditon 4 - Just dropping beads one by one
                                        else:
                                            #print 'AT CONDITION 4'
                                            dummy[start_from] += 1
                                            start_from -= 1
                       
                                else:
                                      # more beads - so adding to player 1's board
                                      #print 'In PLayer 1 board side'
                                      #print 'Present board condition is '
                                      m = 0
                                                                  
                                      while(picked_value!= 0 and m < len_one):
                                        picked_value -= 1
                                        dummy[m] += 1
                                        m += 1
                                   

                                      if(picked_value > 0):
                                              start_from = len(dummy)-1
                                              m = 0
                                              
                                                                             
                                      if picked_value == 0:
                                        flag1 = 0
                                        for u in range(0,len_one):
                                          if dummy[u]!=0:
                                            flag1 = 1
                                            break
                                                
                                        if flag1 == 0:
                                            for n in range(len_one+2,len(dummy)):
                                              dummy[len_one+1] += dummy[n]
                                              if dummy[n]!=0:
                                                dummy[n]=0

                                     
                                        if depth == cut_off_depth:
                                                    if turn == 2:
                                                        temp = dummy[len_one + 1] - dummy[len_one]
                                                   
                                                        if cut_off_depth == 1:
                                                            if temp > max_eval:
                                                              max_eval = temp
                                                           
                                                              final = list(dummy) 
                                                            
                                                    else:
                                                        temp = dummy[len_one] - dummy[len_one + 1]
                                                       

                                                    #print 'A'+ str(offset)+ "," +str(depth)+ "," +str(temp)
                                                    output_file_handle_log.write('A'+ str(offset)+ "," + str(depth)+ "," + str(temp) + '\n')
                                                    state = 1
                                                    
                                                    return temp
                                                
                                        #Boards become empty
                                        if (flag1 == 0):
                                                    if turn == 2:
                                                        temp = dummy[len_one + 1] - dummy[len_one]
                                                        state = 1

                                                    else:
                                                        temp = dummy[len_one] - dummy[len_one + 1]
                                                        state = 0


                                                    if(playing == 1 and turn == 2):
                                                        if temp > max_eval:
                                                            max_eval = temp
                                                            final = list(dummy)

                                                    #print 'A'+ str(offset)+ "," +str(depth)+ "," + str(temp)
                                                    output_file_handle_log.write('A'+ str(offset)+ "," + str(depth)+ "," + str(temp) + '\n')
                                                    return temp
                                                
                                        #Other player's turn                                               
                                        if turn == 2:
                                            state = 0
                                            eval_value = float("inf")
                                            #print 'A'+ str(offset)+ "," +str(depth)+ "," +str("Infinity")
                                            output_file_handle_log.write('A'+ str(offset)+ "," + str(depth)+ "," + str("Infinity") + '\n')
                                                    
                                        else:
                                            state = 1
                                            eval_value = float("-inf")
                                            #print 'A'+ str(offset)+ "," +str(depth)+ "," +str("-Infinity")
                                            output_file_handle_log.write('A'+ str(offset)+ "," + str(depth)+ "," + str("-Infinity") + '\n')

                                        
                                        for start_index in range(0,len_one):
                                            
                                            if dummy[start_index] == 0:
                                                continue

                                            my_val = float("inf")
                                            ret_val = minimax(start_index,1,dummy,len_one,depth + 1,cut_off_depth,0,my_val,0)
                                        

                                            if state == 1:
                                                eval_value = max(eval_value,ret_val)
                                             
                                            else:
                                                eval_value = min(eval_value,ret_val)
                                               

                                            #print 'A'+ str(offset)+ "," +str(depth)+ "," + str(eval_value)
                                            output_file_handle_log.write('A'+ str(offset)+ "," + str(depth)+ "," + str(eval_value) + '\n')

                                        if playing == 1 and turn == 2:
                                            if eval_value > max_eval:
                                                max_eval = eval_value
                                                final = list(dummy) 
                                                    
                                        return eval_value

                                                                
                                      
    
                        
               
                                                        
    
#Main function starts here
with open("input_1.txt") as file: 
    reader = csv.reader(file, delimiter=' ')
    lis_input = []
    for row in reader:
        lis_input.append(row)

OutputFileName = "next_state.txt"
OutputFileName_log = "traverse_log.txt"
output_file_handle = open(OutputFileName, 'w')
output_file_handle_log = open(OutputFileName_log, 'w')

task = int(lis_input[0][0])
player_no = int(lis_input[1][0])
cut_off_depth = int(lis_input[2][0]) 
board_two = [ int(x) for x in lis_input[3] ]
board_one = [ int(x) for x in lis_input[4] ]
mancala_two = int(lis_input[5][0])
mancala_one = int(lis_input[6][0])

#player 1 with mancala at the end
board_one.append(mancala_one)
len_one = len(board_one)-1

board = list(board_one)
board.append(mancala_two)

#player 2 with mancala in the beginning
for i in board_two:
    board.append(i)
    
#MIN = 0 MAX = 1    
state = 1
eval_value = float("-inf")
depth = 0
max_ret_val = -9999999999
if task == 2:
        playing = 1
        #print "Node,Depth,Value"
        #print "root,0,-Infinity"
        output_file_handle_log.write('Node,Depth,Value' + '\n')
        output_file_handle_log.write('root,0,-Infinity' + '\n' )

        run_flag = 0
        
        if player_no == 1:
            turn = 1
            for start_index in range(0,len_one):
                
                if board[start_index] == 0:
                    
                    continue
                
                ret_val = minimax(start_index,player_no,board,len_one,depth + 1,cut_off_depth,0,eval_value,playing)
               
                if max_ret_val < ret_val:
                         max_ret_val = ret_val
                output_file_handle_log.write('root,0,' + str(max_ret_val)+ '\n')

                
        else:

            run_flag = 0
            turn = 2
            for start_index in range(len_one+2,len(board)):
                
                if board[start_index] == 0:
                  
                    continue

                ret_val = minimax(start_index,player_no,board,len_one,depth + 1,cut_off_depth,0,eval_value,playing)

                if max_ret_val < ret_val:
                         max_ret_val = ret_val
                output_file_handle_log.write('root,0,' + str(max_ret_val)+ '\n')

        # PRINTING FINAL STATE HERE to NEXT_STATE.TXT
        for j in range(len_one+2,len(board)):
                output_file_handle.write(str(final[j]) + ' ')
                
        output_file_handle.write('\n')

        for i in range(0,len_one):
                output_file_handle.write(str(final[i]) + ' ')
                                       
        output_file_handle.write('\n')

        output_file_handle.write(str(final[len_one+1]) + '\n')
        output_file_handle.write(str(final[len_one]) + '\n')
        
   
