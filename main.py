import Millionaire
from Player import *

def main():
    # setup game
    # alternate turns
    # check if win or end
    # quit

    Millionaire.print_instructions()
    available_lifelines = Millionaire.all_lifelines()
    possible_answers = ['A', 'B', 'C', 'D']
    turn = 1
    players = []
    points = [0, 0, 0]
    helps = [available_lifelines, available_lifelines, available_lifelines]
    #helps = helps[0].remove('50:50')


    for i in range(1,4):
        name = input("What's your name? ")
        player = Player(name)
        players.append(player.get_name())


    while turn != 11:

        for i in range(0,3):

            print("\nWelcome ", players[i])
            # Ask the player a question and define the answer
            print("Questions #: ", turn)
            print("------------------")
            Q, choices, ans = Millionaire.ask_question(turn)

            while len(helps) != 0:

                print("The available lifelines are:")
                print(helps[i])

                try:
                    Response = str(input("Please select an answer or use a lifeline: \n"))
                    if Response in possible_answers:
                        if choices[Response] == ans:
                            print("Correct!!")
                            points[i] += 10
                            break
                        else:
                            print("Wrong answer :(")
                            break

                    elif Response in helps[i]:
                        choices = Millionaire.use_lifeline(Response, choices, ans)
                        helps[i].remove(Response)
                        print(*helps, sep='\n')

                except Exception as e:
                    print("This is not a valid choice. Please enter A, B, C, or D.")



            if(len(helps)) == 0:
                print("There are no more available lifelines.")

                while True:
                    try:
                        Response = str(input("Please select an answer or use a lifeline: "))
                        if choices[Response] == ans:
                            print("Correct!!")
                            points[i] += 10
                            break
                        else:
                            print("Wrong answer :(")
                            break
                    except Exception as e:
                        print("This is not a valid choice. Please enter A, B, C, or D.")
        turn += 1

    print("Nice try!!!")

    players_scores = {}
    for i in range(0,3):
        players_scores.update({players[i]:points[i]})

    # sorting ascent
    sorted_names = [(a,b) for b,a in sorted([b,a] for a,b in players_scores.items())]

    for k in sorted_names:
        print(k[0], 'scores ', k[1])
    print('The winner is', sorted_names[len(sorted_names)-1])
    Millionaire.exit_game()

if __name__ == "__main__":
    main()