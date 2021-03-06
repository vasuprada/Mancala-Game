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


task = 0
player_no = 0
cut_off_depth = 0
board_two = ""
board_one = ""
mancala_two = ""
mancala_one = ""
max_eval= -9999999999
flagger = 0
board = ""
final = ""


def greedy(player_no,board,len_one):
        global final
        global max_eval
        global flagger
        


        dummy = list(board)

        for start in range(0,len_one):
                if dummy[start] == 0:
                        continue

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
                                                        if dummy[n]!=0 :
                                                                dummy[n] = 0

                                        if flag2 == 0:
                                                for v in range(0,len_one):
                                                        dummy[len_one] += dummy[v]
                                                        if(dummy[v]!=0):
                                                                dummy[v] = 0

                                        # Either or Both Boards Became empty
                                        if (flag2 == 0 or flag == 0):
                                                final = list(dummy)
                                                break

                                        #greedy call
                                        greedy(player_no,dummy,len_one)


                                #condition 2- ENDS IN EMPTY PIT ON SAME SIDE
                                elif (picked_value == 0) and (dummy[start_from] == 0):
                                        #mancala will get beads from both player1 and opp pit
                                        #print 'AT CONDITION 2'
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
                                                                dummy[n] = 0

                                        if flag2 == 0:
                                                for v in range(0, len_one):
                                                        dummy[len_one] += dummy[v]
                                                        if dummy[v] != 0:
                                                                dummy[v] = 0
                                        if flagger == 1:
                                                # If evals are same, tie breaking on order
                                                if (max_eval <= dummy[len_one] - dummy[len_one+1]):
                                                        max_eval = dummy[len_one] - dummy[len_one+1]
                                                        final = list(dummy)

                                        else:
                                                if max_eval < dummy[len_one]- dummy[len_one+1]:
                                                        max_eval = dummy[len_one] - dummy[len_one+1]
                                                        final = list(dummy)

                                elif ((picked_value == 0) and (start_from < len_one)):
                                        dummy[start_from] += 1
                                        if flagger == 1:
                                                # If evals are same, tie breaking on order
                                                if (max_eval <= dummy[len_one] - dummy[len_one+1]):
                                                        max_eval = dummy[len_one] - dummy[len_one+1]
                                                        final = list(dummy)
                                        else :
                                                if max_eval < dummy[len_one]- dummy[len_one+1]:
                                                        max_eval = dummy[len_one] - dummy[len_one+1]
                                                        final = list(dummy)
                                        break

                                else:
                                        dummy[start_from] += 1
                                        start_from += 1

                        else:
                                m = len(dummy)-1
                                while(picked_value != 0 and m > len_one + 1):
                                        picked_value -= 1
                                        dummy[m] += 1
                                        m -= 1
                                       
                                if(picked_value > 0 and m == len_one + 1):
                                        #SKIPPING OTHER PLAYER'S MANCALA
                                        start_from = 0
                                        m = len(dummy) - 1
                                

                                if picked_value == 0:
                                        flag1 = 0
                                        for u in range(0,len_one):
                                                if dummy[u]!=0:
                                                  flag1 = 1
                                                  break

                                        if flag1 == 0:
                                                for n in range(len_one+2,len(dummy)):
                                                        dummy[len_one+1] += dummy[n]
                                                        if dummy[n]!= 0:
                                                          dummy[n] = 0

                                        if flagger == 1:
                                                # If evals are same, tie breaking on order
                                                if (max_eval <= dummy[len_one] - dummy[len_one+1]):
                                                    max_eval = dummy[len_one] - dummy[len_one+1]
                                                    final = list(dummy)

                                        else:
                                                if max_eval < dummy[len_one] - dummy[len_one+1]:
                                                    max_eval = dummy[len_one] - dummy[len_one+1]
                                                    final = list(dummy)





                dummy = list(board)
             
#Main function starts here
with open("input_1.txt") as file:
    reader = csv.reader(file, delimiter=' ')
    lis_input = []
    for row in reader:
        lis_input.append(row)

OutputFileName = "next_state.txt"
output_file_handle = open(OutputFileName, 'w')

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

if task == 1:
        if player_no == 1:
                greedy(player_no,board,len_one)
                
                for j in range(len_one+2,len(board)):
                        output_file_handle.write(str(final[j]) + ' ')
                
                output_file_handle.write('\n')

                for i in range(0,len_one):
                    output_file_handle.write(str(final[i]) + ' ')
                                       
                output_file_handle.write('\n')

                output_file_handle.write(str(final[len_one+1]) + '\n')
                output_file_handle.write(str(final[len_one]) + '\n')


        else:   # Reversing the Board for Player 2
                board_p2 = list(reversed(board))

                # Tie Breaking based on order
                flagger = 1

                greedy(player_no,board_p2,len_one)
                final_p2 = list(reversed(final))
                
                for j in range(len_one+2,len(board)):
                        output_file_handle.write(str(final_p2[j]) + ' ')

                output_file_handle.write('\n')

                for i in range(0,len_one):
                   output_file_handle.write(str(final_p2[i]) + ' ')

                output_file_handle.write('\n')
            
                output_file_handle.write(str(final_p2[len_one+1]) + '\n')
                output_file_handle.write(str(final_p2[len_one]) + '\n')

