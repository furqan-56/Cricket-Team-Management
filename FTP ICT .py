from time import sleep  # for delay
import os  # for clearing screen


def displayStats():

    babar_matches = 50
    babar_runs=100
    babar_highestscore = 2
    babar_century = 1
    babar_hc = 2
    babar_bbf = 0

    virat_matches = 50
    virat_runs = 100
    virat_highestscore = 2
    virat_century = 1
    virat_hc = 2
    virat_bbf = 0

    dekock_matches = 50
    dekock_runs = 100
    dekock_highestscore = 2
    dekock_century = 1
    dekock_hc = 2
    dekock_bbf = 0

    warner_matches = 50
    warner_runs = 100
    warner_highestscore = 2
    warner_century = 1
    warner_hc = 2
    warner_bbf = 0

    pietersen_matches = 50
    pietersen_runs = 100
    pietersen_highestscore = 2
    pietersen_century = 1
    pietersen_hc = 2
    pietersen_bbf = 0

    smith_matches = 50
    smith_runs = 100
    smith_highestscore = 2
    smith_century = 1
    smith_hc = 2
    smith_bbf = 0

    akmal_matches = 50
    akmal_runs = 100
    akmal_highestscore = 2
    akmal_century = 1
    akmal_hc = 2
    akmal_bbf = 0

    shadab_matches = 50
    shadab_runs = 100
    shadab_highestscore = 2
    shadab_century = 1
    shadab_hc = 2
    shadab_bbf = 0

    moeen_matches = 50
    moeen_runs = 100
    moeen_highestscore = 2
    moeen_century = 1
    moeen_hc = 2
    moeen_bbf = 0

    nawaz_matches = 50
    nawaz_runs = 100
    nawaz_highestscore = 2
    nawaz_century = 1
    nawaz_hc = 2
    nawaz_bbf = 0

    boult_matches = 50
    boult_runs = 100
    boult_highestscore = 2
    boult_century = 1
    boult_hc = 2
    boult_bbf = 0

    steyn_matches = 50
    steyn_runs = 100
    steyn_highestscore = 2
    steyn_century = 1
    steyn_hc = 2
    steyn_bbf = 0

    amir_matches = 50
    amir_runs = 100
    amir_highestscore = 2
    amir_century = 1
    amir_hc = 2
    amir_bbf = 0

    haris_matches = 50
    haris_runs = 100
    haris_highestscore = 2
    haris_century = 1
    haris_hc = 2
    haris_bbf = 0

    shaheen_matches = 50
    shaheen_runs = 100
    shaheen_highestscore = 2
    shaheen_century = 1
    shaheen_hc = 2
    shaheen_bbf = 0

    print('----------------------- Statistics of  All Players -----------------------')
    print('| Player Name          | Matches | Runs/Wkts | HSc | 100s |  HC  |  BBF  |')
    print('| Babar Azam          :|   ',babar_matches,"      ",babar_runs,"     ",babar_highestscore,"    ",babar_century,"    ",babar_hc,"    ",babar_bbf)
    print('| Virat Kohli         :|   ',virat_matches,"      ",virat_runs,"     ",virat_highestscore,"    ",virat_century,"    ",virat_hc,"    ",virat_bbf)
    print('| Q De Kock           :|   ',dekock_matches,"      ",dekock_runs,"     ",dekock_highestscore,"    ",dekock_century,"    ",dekock_hc,"    ",dekock_bbf)
    print('| David Warner        :|   ',warner_matches,"      ",warner_runs,"     ",warner_highestscore,"    ",warner_century,"    ",warner_hc,"    ",warner_bbf)
    print('| Kevin Pietersen     :|   ',pietersen_matches,"      ",pietersen_runs,"     ",pietersen_highestscore,"    ",pietersen_century,"    ",pietersen_hc,"    ",pietersen_bbf)
    print('| Steve Smith         :|   ',smith_matches,"      ",smith_runs,"     ", smith_highestscore,"    ",smith_century,"    ",smith_hc,"    ",smith_bbf)
    print('| Umar Akmal          :|   ',akmal_matches,"      ",akmal_runs,"     ",akmal_highestscore,"    ",akmal_century,"    ",akmal_hc,"    ",akmal_bbf)
    print('| Shadab Khan         :|   ',shadab_matches,"      ",shadab_runs,"     ",shadab_highestscore,"    ",shadab_century,"    ",shadab_hc,"    ",shadab_bbf)
    print('| Moeen Ali           :|   ',moeen_matches,"      ",moeen_runs,"     ",moeen_highestscore,"    ",moeen_century,"    ",moeen_hc,"    ",moeen_bbf)
    print('| Muhammad Nawaz      :|   ',nawaz_matches,"      ",nawaz_runs,"     ",nawaz_highestscore,"    ",nawaz_century, "    ",nawaz_hc,"    ",nawaz_bbf)
    print('| Trent Boult         :|   ',boult_matches,"      ",boult_runs,"     ",boult_highestscore,"    ",boult_century, "    ",boult_hc,"    ",boult_bbf)
    print('| Dale Steyn          :|   ',steyn_matches,"      ",steyn_runs,"     ",steyn_highestscore,"    ",steyn_century, "    ",steyn_hc,"    ",steyn_bbf)
    print('| Muhammad Amir       :|   ',amir_matches,"      ",amir_runs,"     ",amir_highestscore,"    ",amir_century,"    ",amir_hc,"    ",amir_bbf)
    print('| Haris Rauf          :|   ',haris_matches,"      ",haris_runs,"     ",haris_highestscore,"    ",haris_century,"    ",haris_hc,"    ",haris_bbf)
    print('| Shaheen Shah Afridi :|   ',shaheen_matches,"      ",shaheen_runs,"     ",shaheen_highestscore,"    ",shaheen_century,"    ",shaheen_hc,"    ",shaheen_bbf)

def selection():
    for i in range(0,15):
        print (i+1,"- ",Players[i])

playerSelected = []
print("Hey, This is Mirzanpur Dominators Management")

Players = ["Babar Azam", "Virat Kohli", "Q De Kock", "David Warner", "Kevin Pietersen", "Steve Smith",
           "Umar Akmal", "Shadab Khan", "Moeen Ali", "Muhammad Nawaz", "Trent Boult", "Dale Steyn",
           "Muhammad Amir", "Haris Rauf", "Shaheen Shah Afridi"]
while True:
        os.system("cls")
        print("\nEnter your Admin Username : ")
        username = input()

        print("\nEnter your Admin Password : ")
        password = input()

        if username == "MZD" and password == "221427":
            break

print("\nWelcome MZD Management")

while True :
        def menu():
            print("\nSelect any number to Manage :\n ")
            sleep(1)
            print("Press 1 to View Squad")
            print("Press 2 to Select Team for any Match")
            print("Press 3 to Remove/Add Player")
            print("Press 4 to View Stats of Players")
            print("Press 5 to Exit the Program")
            print("\n" + "Press Any Number to Select Option:")


        menu()
        number = eval(input())

        # while number !=0:
        if number == 1:  # for viewing squad
            print("Mirzanpur Team Squad : ")
            for i in Players:  # print list vertically
                print(i)

        elif number == 2:
            selection()
            count = 11
            while (count > 0):

                choice = eval(input("\nEnter Number  of Player You want to Select for Team : "))
                if choice == 1:
                    count = count - 1
                    player = "Babar Azam"
                    print('Babar Azam Selected &', "Counts left = ", count)
                    playerSelected.append(player)
                    Players.remove(player)
                elif choice == 2:
                    count = count - 1
                    player = "Virat Kohli"
                    print('Virat Kohli Selected', "Counts left = ", count)
                    playerSelected.append(player)
                    Players.remove(player)
                elif choice == 3:
                    count = count - 1
                    player = "Q De Kock"
                    print('Q De Kock Selected', "Counts left = ", count)
                    playerSelected.append(player)
                    Players.remove(player)
                elif choice == 4:
                    count = count - 1
                    player = "David Warner"
                    print('David Warner Selected', "Counts left = ", count)
                    playerSelected.append(player)
                    Players.remove(player)
                elif choice == 5:
                    count = count - 1
                    player = "Kevin Pietersen"
                    print('Kevin Pietersen Selected', "Counts left = ", count)
                    playerSelected.append(player)
                    Players.remove(player)
                elif choice == 6:
                    count = count - 1
                    player = "Steve Smith"
                    print('Steve Smith Selected', "Counts left = ", count)
                    playerSelected.append(player)
                    Players.remove(player)
                elif choice == 7:
                    count = count - 1
                    player = "Umar Akmal"
                    print('Umar Akmal Selected', "Counts left = ", count)
                    playerSelected.append(player)
                    Players.remove(player)
                elif choice == 8:
                    count = count - 1
                    player = "Shadab Khan"
                    print('Shadab Khan Selected', "Counts left = ", count)
                    playerSelected.append(player)
                    Players.remove(player)
                elif choice == 9:
                    count = count - 1
                    player = "Moeen Ali"
                    print('Moeen Ali Selected', "Counts left = ", count)
                    playerSelected.append(player)
                    Players.remove(player)
                elif choice == 10:
                    count = count - 1
                    player = "Muhammad Nawaz"
                    print('Muhammad Nawaz Selected', "Counts left = ", count)
                    playerSelected.append(player)
                    Players.remove(player)
                elif choice == 11:
                    count = count - 1
                    player = "Trent Boult"
                    print('Trent Boult Selected', "Counts left = ", count)
                    playerSelected.append(player)
                    Players.remove(player)
                elif choice == 12:
                    count = count - 1
                    player = "Dale Steyn"
                    print('Dale Steyn Selected', "Counts left = ", count)
                    playerSelected.append(player)
                    Players.remove(player)
                elif choice == 13:
                    count = count - 1
                    player = "Muhammad Amir"
                    print('Muhammad Amir Selected', "Counts left = ", count)
                    playerSelected.append(player)
                    Players.remove(player)
                elif choice == 14:
                    count = count - 1
                    player = "Haris Rauf"
                    print('Haris Rauf Selected', "Counts left = ", count)
                    playerSelected.append(player)
                    Players.remove(player)
                elif choice == 15:
                    count = count - 1
                    player = "Shaheen Shah Afridi"
                    print('Shaheen Shah Afridi Selected', "Counts left = ", count)
                    playerSelected.append(player)
                    Players.remove(player)
                else:
                    print('Invalid Number Selected')
                    break

            print('\nSelected team:\n')
            for i in playerSelected:
                print(i)
        elif number == 3:

            def menu():
                print("[1] Select any Player to Remove from Team")
                print("[2] Select any Player to Add in Team")
                print("[0] Exit the Program")


            menu()
            option = eval(input("Enter your option : "))

            if option == 1:
                while True:
                    choice2 = (input('\nEnter Y/y to Remove a Player and N/n to Exit : '))
                    if choice2 == 'n':
                        break
                    Players = ["Babar Azam", "Virat Kohli", "Q De Kock", "David Warner", "Kevin Peitersen","Steve Smith",
                               "Umar Akmal", "Shadab Khan", "Moeen Ali", "Muhamad Nawaz", "Trent Boult", "Dale Steyn",
                               "Muhammad Amir", "Haris Rauf", "Shaheen Shah Afridi"]

                    playerRemove = input("\nSelect any player to Remove : ")
                    Players.remove(playerRemove)
                    print('\nUpdated number of players : \n')
                    for i in Players:
                        print(i)

            elif option == 2:

                Players = ["Babar Azam", "Virat Kohli", "Q De Kock", "David Warner", "Kevin Peitersen", "Steve Smith",
                           "Umar Akmal", "Shadab Khan", "Moeen Ali", "Muhamad Nawaz", "Trent Boult", "Dale Steyn",
                           "Muhammad Amir", "Haris Rauf", "Shaheen Shah Afridi"]

                playersAppend = input("Select any players to Add : ")
                Players.append(playersAppend)
                print('Updated number of players : \n')
                for i in Players:
                    print(i)

            elif option == 0:
                print("Wrong Option Selected, Program Closed")
                exit(0)

        elif number == 4:
            displayStats()

        elif number == 5:
            print("\nProgram Exitted.")
            exit()

        else:
            print("\nInvalid option selected. Please try again.")