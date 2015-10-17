import csv

global task
global player_no
global cut_off_depth
global board_two
global board_one
global mancala_two
global mancala_one
global flagger
global board 


task=0
player_no=0
cut_off_depth=0
board_two=""
board_one=""
mancala_two=""
mancala_one=""
max_eval=-1
flagger = 0
board = ""
final = ""

                                        
def greedy(player_no,board,len_one):
        global final
        global max_eval
        global flagger
        
      
        dummy = list(board)

        for y in dummy:
                print y,
        print
               
            
  if(player_no == 1):     
        for start in range(0,len_one):
                print 'start is',start
                if dummy[start] == 0:
                    dummy[start] == 0
                    print 'start is:',start
                    continue
        
                picked_index = start
                print 'picked index',picked_index
                #picked_value = dummy_one[picked_index]
                picked_value = dummy[picked_index]
                print 'picked value:',picked_value
                start_from = start+1 #j
                print 'starting from:',start_from
                #len_one = len(dummy_one)-1 #k
                print 'length of board 1:',len_one
                m = len(dummy)-1
                #print 'length of board 2:',m
                #max_eval = dummy_one[len_one] - dummy_two[0]
                #print 'max_eval is:',max_eval
                #dummy_one[picked_index]= 0
                dummy[picked_index] = 0

                while picked_value != 0:
                        print 'picked_value is:',picked_value              
                        print 'Outside start_from is :',start_from
                         
                        if start_from <= len_one:
                                picked_value -= 1
                                #condition 1- ENDS IN MANCALA-Free turn
                                if (start_from == len_one) and (picked_value == 0):
                                        dummy[len_one]+= 1
                                        print 'AT CONDITION 1'
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
                                        
                                        print 'flag 2 and flag',flag2,flag
                                        print '******************'

                                        for y in dummy:
                                                print y,
                                        print
                                        print '******************'                                                            
                                       

                                        # Either or Both Boards Became empty
                                        if (flag2 == 0 or flag == 0):
                                                final = list(dummy)
                                                #final_two = list(dummy_two)
                                                break
                                        #greedy call
                                        greedy(player_no,dummy,len_one)
                                        
             
                                #condition 2- ENDS IN EMPTY PIT ON SAME SIDE  
                                elif (picked_value == 0) and (dummy[start_from] == 0):
                                        #mancala 1 will get beads from both player1 and opp pit
                                        print 'AT CONDITION 2'
                                        flag = 0
                                        flag2 = 0
                                        dummy[start_from] = 1
                                        x = start_from + len_one + 2
                                        #print x
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
                                        print '******************'
                                        for y in dummy:
                                                print y,
                                        print
                                        print '******************'
                                        
                                        

                                                                                                                                                                                          
                                        if (max_eval < (dummy[len_one] - dummy[len_one+1])):
                                                max_eval = dummy[len_one] - dummy[len_one+1]
                                                final = list(dummy)
                                                #final_two = list(dummy_two)

                                        elif ((picked_value == 0) and (start_from < len_one)):
                                                break
                                        
                                #conditon 3 - Just dropping beads one by one

                                else:
                                        print 'AT CONDITION 3'
                                        dummy[start_from] += 1
                                        start_from += 1
               
                        else: # more beads - so adding to player 2's board
                                print 'In PLayer 2 board side'
                                print 'Present board condition is '
                                for y in dummy:
                                        print y,
                                print
                              

                                if(picked_value > 0 and m == len_one + 1):
                                        print "SKIPPING"
                                        start_from = 0
                                                                                     
                                while(picked_value!= 0 and m > len_one + 1):
                                        picked_value -= 1
                                        print 'm is :',m
                                        dummy[m] += 1
                                        m -= 1
                                        print 'm is:',m
                                        print 'picked_value is',picked_value
                        
                             
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
                                                        
                                        if flagger == 1:# If evals are same, tie breaking on order
                                                if (max_eval <= dummy[len_one] - dummy[len_one+1]):
                                                    max_eval = dummy[len_one] - dummy[len_one+1]
                                                    final = list(dummy)
                                                    #final_two = list(dummy_two)
                                        else: 
                                                if max_eval < dummy[len_one] - dummy[len_one+1]:
                                                    max_eval = dummy[len_one] - dummy[len_one+1]
                                                    final = list(dummy)
                                                    #final_two = list(dummy_two)

                                        for y in final:
                                            print y,
                                        print
                                       
                                        print 'Last start from is : ',start_from
                                        print 'Last picked value',picked_value                                                                             
  #player 2 plays                           
  else:
    for start in range(len_one+2,len(dummy)):
                print 'start is',start
                if dummy[start] == 0:
                    dummy[start] == 0
                    print 'start is:',start
                    continue
        
                picked_index = start
                print 'picked index',picked_index
                #picked_value = dummy_one[picked_index]
                picked_value = dummy[picked_index]
                print 'picked value:',picked_value
                start_from = start-1 #j
                print 'starting from:',start_from
                #len_one = len(dummy_one)-1 #k
                print 'length of board 2:',len_one
                #m = len(dummy)-1
                dummy[picked_index] = 0

                while picked_value != 0:
                        print 'picked_value is:',picked_value              
                        print 'Outside start_from is :',start_from
                         
                        if start_from >= len_one+1:
                                picked_value -= 1
                                #condition 1- ENDS IN MANCALA-Free turn
                                if (start_from == len_one+1) and (picked_value == 0):
                                        dummy[len_one+1] += 1
                                        print 'AT CONDITION 1'
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
                                        
                                        print 'flag 2 and flag',flag2,flag
                                        print '******************'

                                        for y in dummy:
                                                print y,
                                        print
                                        print '******************'                                                            
                                       

                                        # Either or Both Boards Became empty
                                        if (flag2 == 0 or flag == 0):
                                                final = list(dummy)
                                                #final_two = list(dummy_two)
                                                break
                                        #greedy call
                                        greedy(player_no,dummy,len_one)
                                        
             
                                #condition 2- ENDS IN EMPTY PIT ON SAME SIDE  
                                elif (picked_value == 0) and (dummy[start_from] == 0):
                                        #mancala 1 will get beads from both player1 and opp pit
                                        print 'AT CONDITION 2'
                                        flag = 0
                                        flag2 = 0
                                        dummy[start_from] = 1
                                        x = start_from - len_one - 2
                                        #print x
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
                                        print '******************'
                                        for y in dummy:
                                                print y,
                                        print
                                        print '******************'
                                        
                                        
                                        if (max_eval < (dummy[len_one+1] - dummy[len_one])):
                                                max_eval = dummy[len_one+1] - dummy[len_one]
                                                final = list(dummy)
                                                #final_two = list(dummy_two)

                                        elif ((picked_value == 0) and (start_from > len_one + 1)):
                                                break
                                        
                                #conditon 3 - Just dropping beads one by one
                                else:
                                        print 'AT CONDITION 3'
                                        dummy[start_from] += 1
                                        start_from -= 1
               
                        else: # more beads - so adding to player 1's board
                                print 'In PLayer 1 board side'
                                print 'Present board condition is '
                                for y in dummy:
                                        print y,
                                print
                              ` #start_from = 0
                                if(picked_value > 0 and start_from == len_one):
                                        print "SKIPPING"
                                        start_from = 0
                                                          
                                while(picked_value!= 0 and start_from < len_one ):
                                        picked_value -= 1
                                        #print 'm is :',m
                                        dummy[start_from] += 1
                                        start_from += 1
                                        #print 'm is:',m
                                        print 'picked_value is',picked_value
                                
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
                                                        
                                        if max_eval < dummy[len_one + 1] - dummy[len_one]:
                                                    max_eval = dummy[len_one+1] - dummy[len_one]
                                                    final = list(dummy)
                                                    #final_two = list(dummy_two)

                                        for y in final:
                                            print y,
                                        print
                                       
                                        print 'Last start from is : ',start_from
                                        print 'Last picked value',picked_value    
    
  
                dummy = list(board)
                #dummy_two = list(board_two)
                for y in dummy:
                  print y,
                print
               
                                                        
    
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
    

if task == 1:
        #if player_no == 1:
                greedy(player_no,board,len_one)
                
                for i in range(0,len_one):
                    print final[i],
                print
                               
                for j in range(len_one+2,len(board)):
                        print final[j],
                print
                print final[len_one]
                print final[len_one+1]
                
        '''else:   # Reversing the Board for Player 2
                board_p2 = list(reversed(board))
                flagger = 1 # Tie Breaking based on order
                greedy(player_no,board_p2,len_one)
                final_p2 = list(reversed(final))
               
                              
                for i in range(0,len_one):
                    print final_p2[i],
                print
                               
                for j in range(len_one+2,len(board)):
                        print final_p2[j],
                print
                print final_p2[len_one]
                print final_p2[len_one+1]
        '''
