 # Создайте программу для игры с конфетами человек против человека.
 # Подумайте? как наделить бота "интеллектом"

from random import randint
# M % (N + 1) Last player wins
# (M % (N + 1)) - 1 Last player lose
def last_wins(heap_value: int, step_value: int)-> None: 
    count = 0
    curr_player_turn = 0
    flag = True
    print(f"Remained {heap_value} candies")
    while True:
        count += 1
        if heap_value <= step_value:
           print(f"Computer takes {heap_value} candies. Computer Wins!")
           break

        turn = heap_value % (step_value + 1)
        if turn == 0:
            turn = randint(1, step_value)
            flag = False
        
        heap_value -= turn
        print(f"Computer takes {turn} candies. Remained {heap_value} candies")

        # на доработке
        # if heap_value % (step_value + 1) != 0:
        #     flag = True
        #     print("Computer changes its strategy")

        #turn = step_value + 1 - curr_player_turn if flag else randint(1, step_value)
        #heap_value -= turn
        #print(f"Computer take {turn} candies. Remained {heap_value} candies")
        count += 1
        
        print("Enter candies quantity")
        curr_player_turn = int(input())
        heap_value -= curr_player_turn

        if heap_value == 0:
            print("You are Winner!!!")
            break
        else:
            print(f"Player takes {curr_player_turn} candies. Remained {heap_value} candies\n")
        
        
        

last_wins(20, 3)