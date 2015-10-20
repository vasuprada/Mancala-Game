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
max_eval=-1
board = ""
final = ""
turn = 0

                                        
def minimax(start,player_no,board,len_one,depth,cut_off_depth,state,eval_value,playing):
        global final
        global max_eval
        global turn
     
  
        dummy = list(board)

        for y in dummy:
                print y,
        print
               
            
        if(player_no == 1):     
                        picked_index = start
                        #print 'picked index',picked_index
                        picked_value = dummy[picked_index]
                        #print 'picked value:',picked_value
                        start_from = start+1
                        #print 'starting from:',start_from
                        #print 'length of board 1:',len_one
                        m = len(dummy)-1
                        dummy[picked_index] = 0

                        while picked_value != 0:
                                #print 'picked_value is:',picked_value              
                                #print 'Outside start_from is :',start_from
                                 
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
                                                                                                                                                                                                        
                                                for x in range(len_one+2,len(dummy)-1):
                                                        if dummy[x]!=0:
                                                          flag2 = 1
                                                          break
                                                                                                                
                                                if flag == 0:
                                                        for n in range(len_one+2,len(dummy)):
                                                                dummy_two[len_one+1] += dummy_two[n]
                                                                if(dummy[n]!=0):
                                                                        dummy[n]=0
                                                                                                                    
                                                if flag2 == 0:
                                                        for v in range(0,len_one):
                                                                dummy[len_one] += dummy[v]
                                                                if(dummy[v]!=0):
                                                                        dummy[v]=0
                                                
                                                '''print 'flag 2 and flag',flag2,flag
                                                print '******************'

                                                for y in dummy:
                                                        print y,
                                                print
                                                print '******************' '''                                                           
                                               

                                                # Either or Both Boards Became empty
                                                if (flag2 == 0 or flag == 0):
                                                    if turn == 1:
                                                        temp = dummy[len_one] - dummy[len_one+1]
                                                        #print "turn is: in C1",turn
                                                        #print "value of temp in C1",temp
                                                    else:
                                                        temp = dummy[len_one + 1] - dummy[len_one]
                                                        #print "turn is: IN C1",turn
                                                        #print "value of temp IN C1",temp

                                                    if(playing == 1 and turn == 1):
                                                        if temp > max_eval:
                                                            max_eval = temp
                                                            #print "max_eval is: IN C1",max_eval
                                                            final = list(dummy)

                                                    print 'B'+ str(start+2),depth,temp
                                                    return temp
                                                        
                                                #greedy call
                                                
                                                #eval_value = float(-inf)
                                                #state = 1
                                                if turn == 1:
                                                    state = 1
                                                    print 'B'+ str(start+2),depth,str("-Infinity")
                                                else:
                                                    state = 0
                                                    print 'B'+ str(start+2),depth,str("Infinity")

                                                for start_index in range(0,len_one):

                                                    #print 'start is',start_index
                                                    if dummy[start_index] == 0:
                                                        #print 'start is:',start_index
                                                        continue
                                                    my_val = float("-inf")
                                                    ret_val = minimax(start_index,player_no,dummy,len_one,depth,cut_off_depth,0,my_val,playing)

                                                    if state == 1:
                                                        temp = min(eval_value,ret_val)
                                                        #print "turn is: IN C1",turn
                                                        #print "value of temp IN C1",temp
                                                    else:
                                                        temp = max(eval_value,ret_val)
                                                        #print "turn is: IN C1",turn
                                                        #print "value of temp IN C1",temp

                                                    print 'B'+ str(start+2),depth,temp

                                                return temp
                                                
                     
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

                                                '''print '******************'
                                                for y in dummy:
                                                        print y,
                                                print
                                                print '******************'''

                                                #print 'depth is now:',depth

                                                # GAME ENDS FOR PLAYER 1 - PLAYER 2 NEEDS TO PLAY
                                                if depth == cut_off_depth:
                                                    if turn == 1:
                                                        temp = dummy[len_one] - dummy[len_one+1]
                                                        #print "turn is: IN C2",turn
                                                        #print "value of temp IN C2",temp
                                                        if cut_off_depth == 1:
                                                            if temp > max_eval:
                                                                max_eval = temp
                                                                #print "max_eval is: IN C2",max_eval
                                                                final = list(dummy) 
                                                        
                                                    else:
                                                        temp = dummy[len_one + 1] - dummy[len_one]
                                                        #print "turn is: IN C2",turn
                                                        #print "value of temp IN C2",temp

                                                    print 'B'+ str(start+2),depth,temp
                                                    state = 1
                                                    return temp

                                                #next player's call
                                                
                                                if turn == 1:
                                                    state = 0
                                                    print 'B'+ str(start+2),depth,str("Infinity")
                                                    
                                                else:
                                                    state = 1
                                                    print 'B'+ str(start+2),depth,str("-Infinity")
                                                
                                                for start_index in range(len_one+2,len(dummy)):
                                                    #print 'start is',start_index
                                                    if dummy[start_index] == 0:
                                                        #print 'start is:',start_index
                                                        continue
                                                    my_val = float("inf")
                                                    ret_val = minimax(start_index,2,dummy,len_one,depth + 1,cut_off_depth,0,my_val,0)
                                                

                                                    if state == 1:
                                                        temp = min(eval_value,ret_val)
                                                        #print "turn is: IN C2",turn
                                                        #print "value of temp IN C2",temp
                                                    else:
                                                        temp = max(eval_value,ret_val)
                                                        #print "turn is: IN C2",turn
                                                        #print "value of temp IN C2",temp

                                                    print 'B'+ str(start+2),depth,temp
                                                    

                                                if playing == 1 and turn == 1:
                                                    if temp > max_eval:
                                                        max_eval = temp
                                                        #print "max_eval is: IN C2",max_eval
                                                        final = list(dummy)
                                                    
                                                return temp  
                                                
                                                                  
                                                
                                                      
                                        #Condition 3 - Putting Stones and ends on my side
                                        elif ((picked_value == 0) and (start_from < len_one)):
                                                    #print "AT CONDITION 3"
                                                    dummy[start_from] += 1
                                                    start_from += 1
                                                    #print 'depth is now:',depth
                                                    #GAME ENDS FOR PLAYER 1 HERE AS WELL - PLAYER 2 NEEDS TO PLAY
                                                    if depth == cut_off_depth:
                                                        if turn == 1:
                                                            temp = dummy[len_one] - dummy[len_one+1]
                                                            #print "turn is: IN C3",turn
                                                            #print "value of temp IN C3",temp
                                                            if cut_off_depth == 1:
                                                                 if temp > max_eval:
                                                                    max_eval = temp
                                                                    #print "max_eval is: IN C3",max_eval
                                                                    final = list(dummy) 
                                                            
                                                        else:
                                                            temp = dummy[len_one + 1] - dummy[len_one]
                                                            #print "turn is: IN C3",turn
                                                            #print "value of temp IN C3",temp

                                                        print 'B'+ str(start+2),depth,temp
                                                        state = 1
                                                        return temp

                                                    if turn == 1:
                                                        state = 0
                                                        print 'B'+ str(start+2),depth,str("Infinity")
                                                    
                                                    else:
                                                        state = 1
                                                        print 'B'+ str(start+2),depth,str("-Infinity")

                                                    for start_index in range(len_one+2,len(dummy)):
                                                        #print 'start is',start_index
                                                        if dummy[start_index] == 0:
                                                            #print 'start is:',start_index
                                                            continue
                                                        my_val = float("inf")
                                                        ret_val = minimax(start_index,2,dummy,len_one,depth + 1,cut_off_depth,0,my_val,0)

                                                        if state == 1:
                                                            temp = min(eval_value,ret_val)
                                                            #print "turn is: IN C3",turn
                                                            #print "value of temp IN C3",temp
                                                        else:
                                                            temp = max(eval_value,ret_val)
                                                            #print "turn is: IN C3",turn
                                                            #print "value of temp IN C3",temp

                                                        #print 'new B value'

                                                        print 'B'+ str(start+2),depth,temp

                                                    if playing == 1 and turn == 1:
                                                        #print 'I am inside here:'
                                                        if temp > max_eval:
                                                            max_eval = temp
                                                            #print "max_eval is: IN C3",max_eval
                                                            final = list(dummy)
                                                    return temp
                                                       
                                                        
                                                    
                                                
                                        #conditon 4 - Just dropping beads one by one
                                        else:
                                                #print 'AT CONDITION 4'
                                                dummy[start_from] += 1
                                                start_from += 1
                       
                                else: # more beads - so adding to player 2's board
                                        #print 'In PLayer 2 board side'
                                        #print 'Present board condition is '
                                        '''for y in dummy:
                                                print y,
                                        print'''
                                      

                                        if(picked_value > 0 and m == len_one + 1):
                                                #print "SKIPPING"
                                                start_from = 0
                                                                                             
                                        while(picked_value!= 0 and m > len_one + 1):
                                                picked_value -= 1
                                                #print 'm is :',m
                                                dummy[m] += 1
                                                m -= 1
                                                #print 'm is:',m
                                                #print 'picked_value is',picked_value

                                        for y in dummy:
                                                print y,
                                        print
                                
                                     
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

                                                #print 'depth is now:',depth

                                                if depth == cut_off_depth:
                                                    if turn == 1:
                                                        temp = dummy[len_one] - dummy[len_one+1]
                                                        #print "turn is: IN OTHER BOARD SIDE",turn
                                                        #print "value of temp IN OTHER BOARD SIDE",temp
                                                        if cut_off_depth == 1:
                                                            if temp > max_eval:
                                                                max_eval = temp
                                                                #print "max_eval: IN OTHER BOARD SIDE",max_eval
                                                                
                                                                final = list(dummy) 
                                                            
                                                    else:
                                                        temp = dummy[len_one + 1] - dummy[len_one]
                                                        #print "turn is: IN OTHER BOARD SIDE",turn
                                                        #print "value of temp IN OTHER BOARD SIDE",temp

                                                    print 'B'+ str(start+2),depth,temp
                                                    state = 1
                                                    return temp
                                                    
                                                if turn == 1:
                                                    state = 0
                                                    print 'B'+ str(start+2),depth,str("Infinity")
                                                    
                                                else:
                                                    state = 1
                                                    print 'B'+ str(start+2),depth,str("-Infinity")

                                                for start_index in range(len_one+2,len(dummy)):
                                                    #print 'start is',start_index
                                                    if dummy[start_index] == 0:
                                                        #print 'start is:',start_index
                                                        continue    

                                                    my_val = float("inf")
                                                    ret_val = minimax(start_index,2,dummy,len_one,depth + 1,cut_off_depth,0,my_val,0)

                                                    if state == 1:
                                                        temp = min(eval_value,ret_val)
                                                        #print "turn is: IN OTHER BOARD SIDE",turn
                                                        #print "value of temp IN OTHER BOARD SIDE",temp
                                                    else:
                                                        temp = max(eval_value,ret_val)
                                                        #print "turn is: IN OTHER BOARD SIDE",turn
                                                        #print "value of temp IN OTHER BOARD SIDE",temp

                                                    print 'B'+ str(start+2),depth,temp

                                                if playing == 1 and turn == 1:
                                                    if temp > max_eval:
                                                        max_eval = temp
                                                        #print "max_eval: IN OTHER BOARD SIDE",max_eval
                                                        final = list(dummy) 
                                                    
                                                return temp
                                                #print 'Last start from is : ',start_from
                                                #print 'Last picked value',picked_value
                       
                        
                        
        else:#player 2
                        offset = start - len_one
                        #print "the offset is:",offset
                        picked_index = start
                        #print 'picked index',picked_index
                        picked_value = dummy[picked_index]
                        #print 'picked value:',picked_value
                        start_from = start-1 
                        #print 'starting from:',start_from
                        #print 'length of board 2:',len_one
                        dummy[picked_index] = 0

                        while picked_value != 0:
                                #print 'picked_value is:',picked_value              
                                #print 'Outside start_from is :',start_from
                                 
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
                                                
                                                '''print 'flag 2 and flag',flag2,flag
                                                print '******************'

                                                for y in dummy:
                                                        print y,
                                                print
                                                print '******************''''

                                                
                                               

                                                # Either or Both Boards Became empty
                                                if (flag2 == 0 or flag == 0):
                                                    if turn == 2:
                                                        temp = dummy[len_one + 1] - dummy[len_one]
                                                        #print "turn is: IN C1",turn
                                                        #print "value of temp IN C1",temp
                                                    else:
                                                        temp = dummy[len_one] - dummy[len_one + 1]
                                                        #print "turn is: IN C1",turn
                                                        #print "value of temp IN C1",temp

                                                    if(playing == 1 and turn == 2):
                                                        if temp > max_eval:
                                                            max_eval = temp
                                                            #print "max_eval is: IN C1",max_eval
                                                            final = list(dummy)

                                                    print 'A'+ str(offset),depth,temp
                                                    return temp
                                                        
                                                #greedy call
                                                if turn == 2:
                                                    state = 1
                                                    print 'A'+ str(offset),depth,str("-Infinity")
                                                else:
                                                    state = 0
                                                    print 'A'+ str(offset),depth,str("Infinity")

                                                for start_index in range(len_one+2,len(dummy)):
                                                    #print 'start2 is',start_index
                                                    if dummy[start_index] == 0:
                                                        #print 'start2 is:',start_index
                                                        continue

                                                    my_val = float("-inf")
                                               
                                                    ret_val = minimax(start_index,player_no,dummy,len_one,depth,cut_off_depth,0,my_val,playing)

                                                    if state == 1:
                                                        temp = min(eval_value,ret_val)
                                                        #print "turn is: IN C1",turn
                                                        #print "value of temp IN C1",temp
                                                    
                                                    else:
                                                        temp = max(eval_value,ret_val)
                                                        #print "turn is: IN C1",turn
                                                        #print "value of temp IN C1",temp

                                                    print 'A'+ str(offset),depth,temp

                                                return temp
                                                
                     
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
                                                '''print '******************'
                                                for y in dummy:
                                                        print y,
                                                print
                                                print '******************'

                                                print 'depth is now:',depth'''
                                                #GAME ENDS FOR PLAYER 2 - PLAYER 1 NEEDS TO PLAY
                                                if depth == cut_off_depth:
                                                    if turn == 2:
                                                        temp = dummy[len_one + 1] - dummy[len_one]
                                                        #print "turn is: IN C2",turn
                                                        #print "value of temp IN C2",temp
                                                        if cut_off_depth == 1:
                                                            if temp > max_eval:
                                                                max_eval = temp
                                                                #print "max_eval is: IN C2",max_eval
                                                                final = list(dummy) 
                                                        
                                                    else:
                                                        temp = dummy[len_one] - dummy[len_one + 1]
                                                        #print "turn is: IN C2",turn
                                                        #print "value of temp IN C2",temp

                                                    print 'A'+ str(offset),depth,temp
                                                    state = 1
                                                    return temp

                                                #next player's call
                                                
                                                if turn == 2:
                                                    state = 0
                                                    print 'A'+ str(offset),depth,str("Infinity")
                                                    
                                                else:
                                                    state = 1
                                                    print 'A'+ str(offset),depth,str("-Infinity")

                                                for start_index in range(0,len_one):
                                                    #print 'start2 is',start_index
                                                    if dummy[start_index] == 0:
                                                        #print 'start2 is:',start_index
                                                        continue

                                                    my_val = float("inf")
                                                    ret_val = minimax(start_index,1,dummy,len_one,depth + 1,cut_off_depth,0,my_val,0)
                                                

                                                    if state == 1:
                                                        temp = min(eval_value,ret_val)
                                                        #print "turn is: IN C2",turn
                                                        #print "value of temp IN C2",temp
                                                    else:
                                                        temp = max(eval_value,ret_val)
                                                        #print "turn is: IN C2",turn
                                                        #print "value of temp IN C2",temp

                                                    print 'A'+ str(offset),depth,temp

                                                if playing == 1 and turn == 2:
                                                    if temp > max_eval:
                                                        max_eval = temp
                                                        #print "max_eval is: IN C2",max_eval
                                                        final = list(dummy) 
                                                    
                                                return temp


                                        #Condition 3 - Putting Stones and ends on my side
                                        elif ((picked_value == 0) and (start_from > len_one + 1)):
                                            #print 'AT CONDITION 3'
                                            dummy[start_from] += 1
                                            start_from -= 1

                                            #print 'depth is now:',depth
                                            if depth == cut_off_depth:
                                                        if turn == 2:
                                                            temp = dummy[len_one + 1] - dummy[len_one]
                                                            #print "turn is: IN C3",turn
                                                            #print "value of temp IN C3",temp
                                                            if cut_off_depth == 1:
                                                                if temp > max_eval:
                                                                    max_eval = temp
                                                                    #print "max_eval is: IN C3",max_eval
                                                                    final = list(dummy) 
                                                        else:
                                                            temp = dummy[len_one] - dummy[len_one + 1]
                                                            #print "turn is: IN C3",turn
                                                            #print "value of temp IN C3",temp

                                                        print 'A'+ str(offset),depth,temp
                                                        state = 1
                                                        return temp

                                            if turn == 2:
                                                state = 0
                                                print 'A'+ str(offset),depth,str("Infinity")
                                                    
                                            else:
                                                state = 1
                                                print 'A'+ str(offset),depth,str("-Infinity")

                                            
                                            for start_index in range(0,len_one):
                                                #print 'start2 is',start_index
                                                if dummy[start_index] == 0:
                                                        #print 'start2 is:',start_index
                                                        continue

                                                my_val = float("inf")
                                                ret_val = minimax(start_index,1,dummy,len_one,depth + 1,cut_off_depth,0,my_val,0)

                                                if state == 1:
                                                    temp = min(eval_value,ret_val)
                                                    #print "turn is: IN C3",turn
                                                    #print "value of temp IN C3",temp
                                                else:
                                                    temp = max(eval_value,ret_val)
                                                    #print "turn is: IN C3",turn
                                                    #print "value of temp IN C3",temp

                                                print 'A'+ str(offset),depth,temp

                                            if playing == 1 and turn == 2:
                                                if temp > max_eval:
                                                    max_eval = temp
                                                    #print "max_eval is: IN C3",max_eval
                                                    final = list(dummy) 
                                                    
                                            return temp
                                                    
                                                
                                        #conditon 4 - Just dropping beads one by one
                                        else:
                                            #print 'AT CONDITION 4'
                                            dummy[start_from] += 1
                                            start_from -= 1
                       
                                else: # more beads - so adding to player 1's board
                                      #print 'In PLayer 1 board side'
                                      #print 'Present board condition is '
                                      '''for y in dummy:
                                        print y,
                                      print'''
                                      if(picked_value > 0 and start_from == len_one):
                                        #print "SKIPPING"
                                        start_from = 0
                                                                  
                                      while(picked_value!= 0 and start_from < len_one ):
                                        picked_value -= 1
                                        dummy[start_from] += 1
                                        start_from += 1
                                        #print 'picked_value is',picked_value

                                      #print 'Present board condition is '
                                      '''for y in dummy:
                                        print y,
                                      print'''
                                        
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

                                        #print 'depth is now:',depth

                                        if depth == cut_off_depth:
                                                    if turn == 2:
                                                        temp = dummy[len_one + 1] - dummy[len_one]
                                                        #print "turn is: IN OTHER BOARD SIDE",turn
                                                        #print "value of temp IN OTHER BOARD SIDE",temp
                                                        if cut_off_depth == 1:
                                                            if temp > max_eval:
                                                                max_eval = temp
                                                                #print "max_eval is: IN BOARD SIDE",max_eval
                                                                final = list(dummy) 
                                                            
                                                    else:
                                                        temp = dummy[len_one] - dummy[len_one + 1]
                                                        #print "turn is: IN OTHER BOARD SIDE",turn
                                                        #print "value of temp IN OTHER BOARD SIDE",temp

                                                    print 'A'+ str(offset),depth,temp
                                                    state = 1
                                                    return temp
                                                    
                                        if turn == 2:
                                            state = 0
                                            print 'A'+ str(offset),depth,str("Infinity")
                                                    
                                        else:
                                            state = 1
                                            print 'A'+ str(offset),depth,str("-Infinity")

                                        
                                        for start_index in range(0,len_one):
                                            #print 'start2 is',start_index
                                            if dummy[start_index] == 0:
                                                #print 'start2 is:',start_index
                                                continue

                                            my_val = float("inf")
                                            ret_val = minimax(start_index,1,dummy,len_one,depth + 1,cut_off_depth,0,my_val,0)

                                            if state == 1:
                                                temp = min(eval_value,ret_val)
                                                #print "turn is: IN OTHER BOARD SIDE",turn
                                                #print "value of temp IN OTHER BOARD SIDE",temp
                                            else:
                                                temp = max(eval_value,ret_val)
                                                #print "turn is: IN OTHER BOARD SIDE",turn
                                                #print "value of temp IN OTHER BOARD SIDE",temp

                                            print 'A'+ str(offset),depth,temp

                                        if playing == 1 and turn == 2:
                                            if temp > max_eval:
                                                max_eval = temp
                                                #print "max_eval is: IN BOARD SIDE",max_eval
                                                final = list(dummy) 
                                                    
                                        return temp

                                        #print 'Last start from is : ',start_from
                                        #print 'Last picked value',picked_value
                                                                
                                      
    
                        
               
                                                        
    
#Main function starts here
with open("input_1.txt") as file: 
    reader = csv.reader(file, delimiter=' ')
    lis_input = []
    for row in reader:
        lis_input.append(row)

task = int(lis_input[0][0])
player_no = int(lis_input[1][0])
cut_off_depth = int(lis_input[2][0]) 
board_two = [ int(x) for x in lis_input[3] ]
board_one = [ int(x) for x in lis_input[4] ]
mancala_two = int(lis_input[5][0])
mancala_one = int(lis_input[6][0])

# player 1 with mancala at the end
board_one.append(mancala_one)
len_one = len(board_one)-1

board = list(board_one)
board.append(mancala_two)

# player 2 with mancala in the beginning
for i in board_two:
    board.append(i)
    
# MIN = 0 MAX = 1    
state = 0
eval_value = float("-inf")
depth = 0
max_ret_val = 0
if task == 2:
        playing = 1
        print "Node,Depth,Value"
        print "root,0,-Infinity"
        if player_no == 1:
            turn = 1
            for start_index in range(0,len_one):
                #print 'start is',start_index
                if board[start_index] == 0:
                    #print 'start is:',start_index
                    continue
                
                ret_val = minimax(start_index,player_no,board,len_one,depth + 1,cut_off_depth,state,eval_value,playing)

                if max_ret_val < ret_val:
                    max_ret_val = ret_val

            print "root,0," + str(max_ret_val)
                
        else:
            turn = 2
            for start_index in range(len_one+2,len(board)):
                #print 'start2 is',start_index
                if board[start_index] == 0:
                    #print 'start2 is:',start_index
                    continue

                ret_val = minimax(start_index,player_no,board,len_one,depth + 1,cut_off_depth,state,eval_value,playing)

                if max_ret_val < ret_val:
                    max_ret_val = ret_val

            print "root,0," + str(max_ret_val)
        
       

        for j in range(len_one+2,len(board)):
                print final[j],
        print
        for i in range(0,len_one):
            print final[i],
        print
                       
        print final[len_one+1]
        print final[len_one]
        
   
