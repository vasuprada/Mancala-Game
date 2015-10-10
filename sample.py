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
final_one = ""
final_two = ""



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

                                        
def greedy(player_no,board_two,board_one):
                                    global final_one
                                    global final_two
                                    
                                    dummy_one = list(board_one)
                                    dummy_two = list(board_two)
                               
                                    
                                    if player_no == '1':
                                        for start in range(0,len(dummy_one)):
                                            if dummy_one[start] == 0:
                                                continue
                                                
                                            picked_index = start
                                            picked_value = dummy_one[picked_index]
                                            start_from = start+1       #j
                                            len_one = len(dummy_one)-1 #k
                                            m = len(dummy_two)-1
                                            max_eval = dummy_one[len_one] - dummy_two[0]
                                            dummy_one[picked_index]=0

                                            while picked_value!=0:
                                                if start_from <= len_one:
                                                    picked_value-=1
                                                    #condition 1- ENDS IN MANCALA-Free turn
                                                    if (start_from == len_one) and (picked_value == 0):
                                                        dummy_one[len_one]+=1
                                                        #greedy call
                                                        greedy(player_no,dummy_two,dummy_one)
                                                        break
                                                             
                                                    #condition 2- ENDS IN EMPTY PIT ON SAME SIDE  
                                                    elif (picked_value == 0) and (dummy_one[start_from] == 0):
                                                        #mancala 1 will get beads from both player1 and opp pit
                                                        dummy_one[start_from] = 1
                                                        dummy_one[len_one] = dummy_one[len_one] + dummy_one[start_from]+ dummy_two[start_from+1]
                                                        dummy_one[start_from] = 0
                                                        dummy_two[start_from+1]= 0
                                                        
                                                        if (max_eval < (dummy_one[len_one] - dummy_two[0])):
                                                            max_eval = dummy_one[len_one] - dummy_two[0]
                                                            final_one = list(dummy_one)
                                                            final_two = list(dummy_two)
                                                    #conditon 3 - Just dropping beads one by one
                                                    else:
                                                        dummy_one[start_from] += 1
                                                        start_from += 1
                                                       
                                                else: # more beads - so adding to player 2's board
                                                    start_from=0
                                                    if m!=0:
                                                        dummy_one[start] -= 1
                                                        dummy_two[m] += 1
                                                        m -= 1
                                                        if picked_value == 0:
                                                            if (max_eval < dummy_one[len_one] - dummy_two[0]):
                                                                max_eval = dummy_one[len_one] - dummy_two[0]
                                                                final_one = list(dummy_one)
                                                                final_two = list(dummy_two)

                                                    else:
                                                        dummy_one[start_from] += 1
                                                        start_from += 1
                                            
                                            dummy_one = list(board_one)
                                            dummy_two = list(board_two)
                                        
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
    task = get_task(InputFileName)
    #print task

    input_file_handle = open(InputFileName,'r')
    output_file_handle = open(OutputFileName, 'w')

    

    read_board(input_file_handle)
    len_one = len(board_one)-1
    len_two = len(board_two)-1
    if task == '1':
            #output_file_handle.write(str(UCS()) + '\n')
            board_one.append(mancala_one) # player 1 with mancala at the end
            [mancala_two] + board_two     # player 2 with mancala in the beginning
            greedy(player_no,board_two,board_one)
            for i in final_one:
                print i,
            print
            for j in final_two:
                print j,
            print
            print final_two[0]
            print final_one[len_one]                       
            

            
        
    input_file_handle.close()
    output_file_handle.close()



if __name__ == '__main__':
    main()
