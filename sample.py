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
                                 dummy_one = list(board_one)
                                 dummy_two = list(board_two)

                                 for y in dummy_two:
                                            print y,
                                 print
                                 for x in dummy_one:
                                            print x,
                                 print
                                 print
                                 
                                    
                                 if player_no == 1:
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
                                                                  picked_value -= 1
                                                                  print 'start_from is :',start_from
                                                                  if start_from <= len_one:
                                                                             #picked_value -= 1
                                                                             #condition 1- ENDS IN MANCALA-Free turn
                                                                             if (start_from == len_one) and (picked_value == 0):
                                                                                        dummy_one[len_one]+= 1
                                                                                        print 'AT CONDITION 1'
                                                                                        #greedy call
                                                                                        greedy(player_no,dummy_two,dummy_one)
                                                                                        break
                                                             
                                                                             #condition 2- ENDS IN EMPTY PIT ON SAME SIDE  
                                                                             elif (picked_value == 0) and (dummy_one[start_from] == 0):
                                                                             #mancala 1 will get beads from both player1 and opp pit
                                                                                        print 'AT CONDITION 2'
                                                                                        dummy_one[start_from] = 1
                                                                                        dummy_one[len_one] = dummy_one[len_one] + dummy_one[start_from]+ dummy_two[start_from+1]
                                                                                        dummy_one[start_from] = 0
                                                                                        dummy_two[start_from+1]= 0
                                                                                        for n in range(1,len(dummy_two)):
                                                                                            dummy_two[0] += dummy_two[n]
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
                                                    
                                                                             #conditon 3 - Just dropping beads one by one
                                                                             else:
                                                                                        print 'AT CONDITION 3'
                                                                                        dummy_one[start_from] += 1
                                                                                        start_from += 1
                                                       
                                                                  else: # more beads - so adding to player 2's board
                                                                             print 'IN PLAYER 2 side'
                                                                             if m!=0:
                                                                                 #dummy_one[start] = 0
                                                                                 print 'm is :',m
                                                                                 dummy_two[m] += 1
                                                                                 m -= 1
                                                                                 print 'm is:',m
                                                                                 print 'picked_value is',picked_value
                                                                                 if picked_value == 0:
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

                                                                                        else:
                                                                                                   #dummy_one[start_from] += 1
                                                                                                   start_from = start + 1
                                            
                                                       dummy_one = list(board_one)
                                                       dummy_two = list(board_two)
                                                       for y in dummy_two:
                                                                  print y,
                                                       print
                                                       for x in dummy_one:
                                                                  print x,
                                                       print
                                                       #start = 0
                                                    
                                        
                                    #Else if player 2 
                                            

                                    
                                                            

    
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
    
    
    #InputFileName = str(sys.argv[2])
    InputFileName = "input_1.txt"
    OutputFileName = "output.txt"
    #task = get_task(InputFileName)
   

    input_file_handle = open(InputFileName,'r')
    output_file_handle = open(OutputFileName, 'w')

    

    read_board(input_file_handle)
    #print task
    len_one = len(board_one)-1
    len_two = len(board_two)-1
    if task == 1:
           #output_file_handle.write(str(UCS()) + '\n')
           board_one.append(mancala_one) # player 1 with mancala at the end
           board_two = [mancala_two] + board_two     # player 2 with mancala in the beginning
           greedy(player_no,board_two,board_one)
           for i in final_two:
                      print i,
           print
           for j in final_one:
                      print j,
           print
           print final_two[0]
           print final_one[len_one]                       
            

            
        
    input_file_handle.close()
    output_file_handle.close()



if __name__ == '__main__':
    main()
