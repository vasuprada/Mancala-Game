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

def check(player_no,board_two,board_one):
    global player_no
    global board_two
    global board_one
    l = len(board_one)-1
    max_eval = board_one[l] - board_two[0]
    for start in range(0,len(board_one)):
            greedy(start,player_no,board_two,board_one)
            if max_eval < board_one[l] - board_two[0]: #eval function
                    max_eval = board_one[l] - board_two[0]   
            else:
                continue
            
                                            

def greedy(start,player_no,board_two,board_one):
                                    global player_no
                                    global board_two
                                    global board_one
                                   
                                    if player_no == '1':
                                            if board_one[start] > 0:
                                                j = start+1
                                                k = len(board_one)-1
                                                m = len(board_two)-1
                                                while board_one[start]!=0:
                                                    if j <= k:
                                                        board_one[start]-=1
                                                        #condition 1- ENDS IN MANCALA-Free turn
                                                        if (j == k) and ( board_one[start]== 0):
                                                             board_one[j]+=1
                                                             break
                                                        #condition 2- ENDS IN EMPTY PIT ON SAME SIDE  
                                                        elif (board_one[start] == 0) and (board_one[j] == 0):
                                                            board_one[j] = 0
                                                            #mancala 1 will get beads from both player1 and opp pit
                                                            board_one[k] = board_one[k] + board_two[j+1]
                                                            board_two[j+1]=0
                                                        else:
                                                                board_one[j]+=1
                                                                j++
                                                       
                                                    else: # more beads - so adding to player 2's board
                                                            if m!=0:
                                                                board_one[start]-=1
                                                                board_two[m]+=1
                                                                m--
                                                            else:
                                                                    j=0
                                                                    board_one[j]+=1
                                                                    j++
                                            
                                                    
                                        # ---else part --
                                        #same thing for when Player_no = '2'
                                            

                                    
                                                            

    
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
            check(player_no,board_two,board_one)
            #greedy(player_no,board_two,board_one)
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

