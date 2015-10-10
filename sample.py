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



def get_task(FileName):
    with open(FileName,"r") as file_handle:
        try:
            return int(file_handle.readline().rstrip('\n'))
        except ValueError:
            print "Please check if you have added the task no at the top of the test case set"
            
def read_board(file_handle):
                        global task
                        global player_no
                        global cut_off_depth
                        global board_two
                        global board_one
                        global mancala_two
                        global mancala_one
       
    
                        task = file_handle.readline().rstrip('\n')
                        player_no = file_handle.readline().rstrip('\n')
                        cut_off_depth = file_handle.readline().rstrip('\n')
                        board_two = (file_handle.readline().rstrip('\n').split(' '))
                        board_one = (file_handle.readline().rstrip('\n').split(' '))
                        mancala_two = file_handle.readline().rstrip('\n');
                        mancala_one = file_handle.readline().rstrip('\n');

'''def check(player_no,board_two,board_one):
    global player_no
    global board_two
    global board_one
    l = len(board_one)-1
    max_eval = board_one[l] - board_two[0]
    for start in range(0,len(board_one)):
            if board_one[start]== 0:
                continue
            
            greedy(start,player_no,board_two,board_one)'''
                                        
def greedy(player_no,board_two,board_one):
                                    global player_no
                                    global board_two
                                    global board_one
                                   
                                    if player_no == '1':
                                            #if board_one[start] > 0:
                                            for start in range(0,len(board_one)):
                                                if board_one[start] == 0:
                                                    continue
                                                
                                                picked_index = start
                                                picked_value = board_one[start]
                                                start_from = start+1       #j
                                                len_one = len(board_one)-1 #k
                                                m = len(board_two)-1 

                                                while picked_value!=0:
                                                    if start_from <= len_one:
                                                        picked_value-=1
                                                        #condition 1- ENDS IN MANCALA-Free turn
                                                        if (start_from == len_one) and (picked_value == 0):
                                                             board_one[len_one]+=1
                                                             break
                                                        #condition 2- ENDS IN EMPTY PIT ON SAME SIDE  
                                                        elif (picked_value == 0) and (board_one[start_from] == 0):
                                                            #mancala 1 will get beads from both player1 and opp pit
                                                            board_one[start_from] = 1
                                                            board_one[len_one] = board_one[len_one] + board_one[start_from]+ board_two[start_from+1]
                                                            board_one[start_from] = 0
                                                            board_two[start_from+1]= 0
                                                            break
                                                        else:
                                                                board_one[start_from]+=1
                                                                start_from++
                                                       
                                                    else: # more beads - so adding to player 2's board
                                                            start_from=0
                                                            if m!=0:
                                                                board_one[start]-=1
                                                                board_two[m]+=1
                                                                m--
                                                            else:
                                                                    board_one[start_from]+=1
                                                                    start_from++
                                            
                                                    
                                        
                                        #Else if player 2 
                                            

                                    
                                                            

    
def main():
    global task
    global player_no
    global cut_off_depth
    global board_two
    global board_one
    global mancala_two
    global mancala_one
    
    
    
    #InputFileName = str(sys.argv[2])
    InputFileName = "input_1.txt"
    OutputFileName = "output.txt"
    task = get_task(InputFileName)
    print task

    input_file_handle = open(InputFileName,'r')
    output_file_handle = open(OutputFileName, 'w')

    

    read_board(input_file_handle)

    if task == '1':
            #output_file_handle.write(str(UCS()) + '\n')
            board_one.append(mancala_one) # player 1 with mancala at the end
            [mancala_two] + board_two     # player 2 with mancala in the beginning
            #check(player_no,board_two,board_one)
            greedy(player_no,board_two,board_one)
            print player_no
            print cut_off_depth 
            for i in board_two:
                print i,
            print
            for j in board_two:
                print j,
            print
            print mancala_two
            print mancala_one                          
            

            
        
    input_file_handle.close()
    output_file_handle.close()



if __name__ == '__main__':
    main()

