def calculate(start_bet_amount=1,max_streak=15,increase_bet_every_streak=1,increase_multiplier=2,multiplier=2):
    #multiplier değeri ile gelecek kar'ı hesaplamak

    multiplier_list = []
    betting_amount_list = []


    #Calculating Template
    for i in range(0,max_streak):
        if i ==0:
            multiplier_list.append(1)
        if i !=0:
            increase_this_value_is_int = divmod(i,increase_bet_every_streak)
            overplus= increase_this_value_is_int[1]


            if overplus==0:
                a=i-1
                multiplier_list.append(multiplier_list[a]*increase_multiplier)

            else:
                a=i
                multiplier_list.append(multiplier_list[a-1])

    print("Template: " ,multiplier_list)

    # Calculating Real
    for i in range(0,max_streak):

            if i == 0:
                betting_amount_list.append(start_bet_amount)

            if i != 0:
                increase_this_value_is_int = divmod(i, increase_bet_every_streak)
                overplus = increase_this_value_is_int[1]

            if overplus == 0:
                start_bet_amount = start_bet_amount * increase_multiplier
                betting_amount_list.append(start_bet_amount)

            else:
                betting_amount_list.append(start_bet_amount)
    print("Betting amounts: ",betting_amount_list)

    #Calculating How much money we need?
    all_money=0
    for i in range(0,len(betting_amount_list)):
        all_money+=betting_amount_list[i]
    print("You need this money for start martingale : " ,"$",all_money)

    #When we win ,how much profit will be?
    print("When it comes green ,how much profit it took?")
    when_come_green=[0,(max_streak/2)-1,max_streak-1]


    for a in when_come_green:
        minus_that_money = 0
        for i in range(0,int(a)):
            minus_that_money+=betting_amount_list[i+1]
        profit= betting_amount_list[int(a)] * multiplier
        profit -=minus_that_money
        print(int(a+1),":",profit)









#Calculate( FIRST BET AMOUNT?, MAX STREAKS YOU WANT?, AFTER HOW MUCH RED YOUR BET WILL INCREASE?, HOW MUCH WILL IT INCREASE? (X2), YOUR MULTIPLY (X2) )
#Calculate(start bet amount,max streak, increase streak, increase multiplier ,multiplier )


calculate(start_bet_amount=5,max_streak=10,increase_bet_every_streak=1,increase_multiplier=2,multiplier=2)
