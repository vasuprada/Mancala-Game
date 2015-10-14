import copy
import fileinput
import sys

task=0
player_no=0
cut_off_depth=0
board_two=""
board_one=""
mancala_two=""
mancala_one=""
final_one =""
final_two =""
max_eval=-1
flagger = 0

           
def read_board(file_handle):
                      global task
                      global player_no
                      global cut_off_depth 
                      global board_two
                      global board_one
                      global mancala_two
                      global mancala_one
       
    
                      task = int(file_handle.readline().rstrip('\n'))
                        
                      player_no = int(file_handle.readline().rstrip('\n'))
                      cut_off_depth = int(file_handle.readline().rstrip('\n'))
                      test_two = (file_handle.readline().rstrip('\n').split(' '))
                      test_one = (file_handle.readline().rstrip('\n').split(' '))
                      board_two = map(int,test_two)
                      board_one = map(int,test_one)
                      mancala_two = int(file_handle.readline().rstrip('\n'));
                      mancala_one = int(file_handle.readline().rstrip('\n'));

                                        
def greedy(player_no,board_two,board_one):
                                 global final_one
                                 global final_two
                                 global max_eval
                                 global flagger
                                 dummy_one = list(board_one)
                                 dummy_two = list(board_two)

                                 for y in dummy_two:
                                            print y,
                                 print
                                 for x in dummy_one:
                                            print x,
                                 print
                                 print
                                 
                                    
                                 
                                 for start in range(0,len(dummy_one)-1):
                                                       print 'start is',start
                                                       if dummy_one[start] == 0:
                                                           print 'start is:',start
                                                           continue
                                                
                                                       picked_index = start
                                                       print 'picked index',picked_index
                                                       picked_value = dummy_one[picked_index]
                                                       print 'picked value:',picked_value
                                                       start_from = start+1 #j
                                                       print 'starting from:',start_from
                                                       len_one = len(dummy_one)-1 #k
                                                       print 'length of board 1:',len_one
                                                       m = len(dummy_two)-1
                                                       print 'length of board 2:',m
                                                       #max_eval = dummy_one[len_one] - dummy_two[0]
                                                       #print 'max_eval is:',max_eval
                                                       dummy_one[picked_index]= 0

                                                       while picked_value != 0:
                                                                  print 'picked_value is:',picked_value              
                                                                  print 'Outside start_from is :',start_from
                                                                 
                                                                  if start_from <= len_one:
                                                                             picked_value -= 1
                                                                             #condition 1- ENDS IN MANCALA-Free turn
                                                                             if (start_from == len_one) and (picked_value == 0):
                                                                                        dummy_one[len_one]+= 1
                                                                                        print 'AT CONDITION 1'
                                                                                        flag = 0
                                                                                        flag2 = 0
                                                                                        
                                                                                        for u in range(0,len(dummy_one)-1):
                                                                                            if dummy_one[u]!=0:
                                                                                                flag = 1
                                                                                                break
                                                                                                                                                                                                                                                
                                                                                        for x in range(1,len(dummy_two)):
                                                                                            if dummy_two[x]!=0:
                                                                                                flag2 = 1
                                                                                                break
                                                                                                                                                        
                                                                                        if flag == 0:
                                                                                            for n in range(1,len(dummy_two)):
                                                                                                dummy_two[0] += dummy_two[n]
                                                                                                if(dummy_two[n]!=0):
                                                                                                    dummy_two[n]=0
                                                                                                                                                            
                                                                                        if flag2 == 0:
                                                                                            for v in range(0,len(dummy_one)-1):
                                                                                                dummy_one[len_one] +=dummy_one[v]
                                                                                                if(dummy_one[v]!=0):
                                                                                                    dummy_one[v]=0
                                                                                        
                                                                                        print 'flag 2 and flag',flag2,flag
                                                                                        print '******************'
                                                                                        for y in dummy_two:
                                                                                            print y,
                                                                                        print
                                                                                                                                                    
                                                                                        for x in dummy_one:
                                                                                            print x,
                                                                                        print
                                                                                        print '******************'
                                                                                        # Either or Both Boards Became empty
                                                                                        if (flag2 == 0 or flag == 0):
                                                                                                final_one = list(dummy_one)
                                                                                                final_two = list(dummy_two)
                                                                                                break
                                                                                        #greedy call
                                                                                        greedy(player_no,dummy_two,dummy_one)
                                                                                        #break
                                                             
                                                                             #condition 2- ENDS IN EMPTY PIT ON SAME SIDE  
                                                                             elif (picked_value == 0) and (dummy_one[start_from] == 0):
                                                                                        #mancala 1 will get beads from both player1 and opp pit
                                                                                        print 'AT CONDITION 2'
                                                                                        flag = 0
                                                                                        flag2 = 0
                                                                                        dummy_one[start_from] = 1
                                                                                        dummy_one[len_one] = dummy_one[len_one] + dummy_one[start_from]+ dummy_two[start_from+1]
                                                                                        dummy_one[start_from] = 0
                                                                                        dummy_two[start_from+1]= 0
                                                                                    
                                                                                        for u in range(0,len(dummy_one)-1):
                                                                                            if dummy_one[u]!=0:
                                                                                                flag = 1
                                                                                                break
                                                                                                                                                                                                                                            
                                                                                        for x in range(1,len(dummy_two)):
                                                                                            if dummy_two[x]!=0:
                                                                                                flag2 = 1
                                                                                                break
                                                                                                                                                        
                                                                                        if flag == 0:
                                                                                            for n in range(1,len(dummy_two)):
                                                                                                dummy_two[0] += dummy_two[n]
                                                                                                if(dummy_two[n]!=0):
                                                                                                    dummy_two[n]=0
                                                                                                                                                            
                                                                                        if flag2 == 0:
                                                                                            for v in range(0,len(dummy_one)-1):
                                                                                                dummy_one[len_one] +=dummy_one[v]
                                                                                                if(dummy_one[v]!=0):
                                                                                                    dummy_one[v]=0
                                                                                        
                                                                                        
                                                                                        print '******************'
                                                                                        for y in dummy_two:
                                                                                                   print y,
                                                                                        print
                                                                                        for x in dummy_one:
                                                                                                   print x,
                                                                                        print
                                                                                        print '******************'

                                                                                                                                                                                                                                          
                                                                                        if (max_eval < (dummy_one[len_one] - dummy_two[0])):
                                                                                                    max_eval = dummy_one[len_one] - dummy_two[0]
                                                                                                    final_one = list(dummy_one)
                                                                                                    final_two = list(dummy_two)

                                                                             elif ((picked_value == 0) and (start_from < len_one)):
                                                                                        break
                                                                                
                                                                             #conditon 3 - Just dropping beads one by one

                                                                             else:
                                                                                        print 'AT CONDITION 3'
                                                                                        dummy_one[start_from] += 1
                                                                                        start_from += 1
                                                       
                                                                  else: # more beads - so adding to player 2's board
                                                                             print 'In PLayer 2 board side'
                                                                             print 'Present board condition is '
                                                                             for y in dummy_two:
                                                                                print y,
                                                                             print
                                                                             for x in dummy_one:
                                                                                print x,
                                                                             print

                                                                             if(picked_value > 0 and m == 0):
                                                                                    print "SKIPPING"
                                                                                    start_from = 0
                                                                                                                                     
                                                                             while(picked_value!= 0 and m > 0):
                                                                                       
                                                                                                   #dummy_one[start] = 0
                                                                                                   picked_value -= 1
                                                                                                   print 'm is :',m
                                                                                                   dummy_two[m] += 1
                                                                                                   m -= 1
                                                                                                   print 'm is:',m
                                                                                                   print 'picked_value is',picked_value
                                                                                        
                                                                             
                                                                             if picked_value == 0:
                                                                                        flag1 = 0
                                                                                        for u in range(0,len(dummy_one)-1):
                                                                                            if dummy_one[u]!=0:
                                                                                                flag1 = 1
                                                                                                break
                                                                                        if flag1 == 0:
                                                                                                   for n in range(1,len(dummy_two)):
                                                                                                              dummy_two[0] += dummy_two[n]
                                                                                                              if dummy_two[n]!=0:
                                                                                                                  dummy_two[n]=0
                                                                                                                
                                                                                        if flagger == 1:
                                                                                            if (max_eval <= dummy_one[len_one] - dummy_two[0]):
                                                                                                   max_eval = dummy_one[len_one] - dummy_two[0]
                                                                                                   final_one = list(dummy_one)
                                                                                                   final_two = list(dummy_two)
                                                                                        else:
                                                                                            
                                                                                            if (max_eval < dummy_one[len_one] - dummy_two[0]):
                                                                                                    max_eval = dummy_one[len_one] - dummy_two[0]
                                                                                                    final_one = list(dummy_one)
                                                                                                    final_two = list(dummy_two)
                                                                                        for y in final_two:
                                                                                                   print y,
                                                                                        print
                                                                                        for x in final_one:
                                                                                                   print x,
                                                                                        print
                                                                                        print 'Last start from is : ',start_from
                                                                                        print 'Last picked value',picked_value                                                                             
                                            

                                                                             
                                            
                                                       dummy_one = list(board_one)
                                                       dummy_two = list(board_two)
                                                       for y in dummy_two:
                                                                  print y,
                                                       print
                                                       for x in dummy_one:
                                                                  print x,
                                                       print
                                                       #start = 0
                                                    
                                        
                             
                                            

                                    
                                                            

    
def main():
    global task
    global player_no
    global cut_off_depth
    global board_two
    global board_one
    global mancala_two
    global mancala_one
    global final_one
    global final_two
    global flagger
    
    #InputFileName = str(sys.argv[2])
    InputFileName = "input_1.txt"
    OutputFileName = "output.txt"
    #task = get_task(InputFileName)
   

    input_file_handle = open(InputFileName,'r')
    output_file_handle = open(OutputFileName, 'w')

    

    read_board(input_file_handle)
    #print task
    board_one.append(mancala_one) # player 1 with mancala at the end
    board_two = [mancala_two] + board_two     # player 2 with mancala in the beginning
    if task == 1:
           #output_file_handle.write(str(UCS()) + '\n')
           if player_no == 1:
               greedy(player_no,board_two,board_one)
               len_one = len(board_one)-1
               len_two = len(board_two)-1
               for i in range(1,len_two+1):
                    print final_two[i],
               print
               for j in range(0,len_one):
                    print final_one[j],
               print
               print final_two[0]
               print final_one[len_one]
           else:
               board_two_p2 = list(reversed(board_one))
               board_one_p1 = list(reversed(board_two))
               flagger = 1
               greedy(player_no,board_two_p2,board_one_p1)
               len_one = len(board_one_p1)-1
               len_two = len(board_two_p2)-1
               #final_two = list(reversed(final_one))
               final_one_p1 = list(reversed(final_two))
               final_two_p2 = list(reversed(final_one))
               
               for i in range(1,len_two+1):
                    print final_two_p2[i],
               print
               for j in range(0,len_one):
                    print final_one_p1[j],
               print
               print final_two_p2[0]
               print final_one_p1[len_one]
                                
            

            
        
    input_file_handle.close()
    output_file_handle.close()



if __name__ == '__main__':
    main()
