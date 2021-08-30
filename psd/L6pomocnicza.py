import time

# to co klient kupił
customer_LSK_za_ile = []
customer_LSK_w_jakiej_ilosci = []

customer_ETH_za_ile = []
customer_ETH_w_jakiej_ilosci = []

customer_LTC_za_ile = []
customer_LTC_w_jakiej_ilosci = []

srednia_LSK = []
srednia_ETH = []
srednia_LTC = []

# to co klient sprzedał
customer_LSK_za_ile_sprzedal = []
customer_LSK_w_jakiej_ilosci_sprzedal = []

customer_ETH_za_ile_sprzedal = []
customer_ETH_w_jakiej_ilosci_sprzedal = []

customer_LTC_za_ile_sprzedal = []
customer_LTC_w_jakiej_ilosci_sprzedal = []

srednia_LSK_sprzedal = []
srednia_ETH_sprzedal = []
srednia_LTC_sprzedal = []


def average(customer_za_ile, customer_w_jakiej_ilosci):
    suma_kosztow = 0
    if customer_za_ile  == [] or customer_w_jakiej_ilosci == []:
        return # 'nie ma z czego policzyć sredniej'
    else:
        for i in range(len(customer_za_ile)):
            for j in range(len(customer_w_jakiej_ilosci)):
                if i == j:
                    suma_kosztow += customer_za_ile[i]*customer_w_jakiej_ilosci[j]
        suma_ilosci = sum(customer_w_jakiej_ilosci)
        average1 = suma_kosztow / suma_ilosci
        return average1


flag = True
while flag:
    LSK_zysk_strata11 = 0
    ETH_zysk_strata22 = 0
    LTC_zysk_strata33 = 0

    czy_kupiles_cos = input('czy kupiles cos t/n: ')
    if czy_kupiles_cos == 't':
        co_kupil = (input('Co kupiles: '))
        za_ile_kupil = int(input('Za ile kupiles: '))
        w_jakiej_ilosci_kupil = int(input('W jakiej ilosci kupiles: '))

        if co_kupil == 'LSK':
            customer_LSK_za_ile.append(za_ile_kupil)
            customer_LSK_w_jakiej_ilosci.append(w_jakiej_ilosci_kupil)

        if co_kupil == 'ETH':
            customer_ETH_za_ile.append(za_ile_kupil)
            customer_ETH_w_jakiej_ilosci.append(w_jakiej_ilosci_kupil)

        if co_kupil == 'LTC':
            customer_LTC_za_ile.append(za_ile_kupil)
            customer_LTC_w_jakiej_ilosci.append(w_jakiej_ilosci_kupil)

    czy_sprzedales_cos = input('czy sprzedales cos t/n: ')
    if czy_sprzedales_cos == 't':
        co_sprzedal = (input('Co sprzedales: '))
        za_ile_sprzedal = int(input('Za ile sprzedales: '))
        w_jakiej_ilosci_sprzedal = int(input('W jakiej ilosci sprzedales: '))

    # tu trzeba wepchac cos takiego żeby usuwało to co sprzedaliśmy z listy do ktorej dawalismy to co kupilismy
        if co_sprzedal == 'LSK':
            customer_LSK_za_ile_sprzedal.append(za_ile_sprzedal)
            customer_LSK_w_jakiej_ilosci_sprzedal.append(w_jakiej_ilosci_sprzedal)

            licznik1 = 0
            i1 = 0
            zysk_strata1 = 0
            flag1 = True
            while flag1:
                # for i in cust_LSK_number_buy:
                licznik1 += customer_LSK_w_jakiej_ilosci[i1]

                # tu zaczynam liczyc zysk lub strate
                zysk_strata1 += customer_LSK_za_ile[i1] * customer_LSK_w_jakiej_ilosci[i1]
                # tu koncze z zyskiem strata
                customer_LSK_w_jakiej_ilosci[i1] = 0
                if licznik1 > w_jakiej_ilosci_sprzedal:
                    customer_LSK_w_jakiej_ilosci[i1] = licznik1 - w_jakiej_ilosci_sprzedal # 17 -12
                    #
                    zysk_strata11 = zysk_strata1 - customer_LSK_w_jakiej_ilosci[i1] * customer_LSK_za_ile[i1]  # 5 * 20
                    if zysk_strata11 > 0:
                        LSK_zysk_strata = "zysk"
                    if zysk_strata11 < 0:
                        LSK_zysk_strata = "strata"
                    if zysk_strata11 == 0:
                        LSK_zysk_strata = "nie ma ani zysku ani straty"
                    #
                    flag1 = False
                i1 += 1


        if co_sprzedal == 'ETH':
            customer_ETH_za_ile_sprzedal.append(za_ile_sprzedal)
            customer_ETH_w_jakiej_ilosci_sprzedal.append(w_jakiej_ilosci_sprzedal)

            licznik2 = 0
            i2 = 0
            zysk_strata2 = 0
            flag2 = True
            while flag2:
                #
                licznik2 += customer_ETH_w_jakiej_ilosci[i2]
                #
                licznik2 += customer_ETH_w_jakiej_ilosci[i2]
                customer_ETH_w_jakiej_ilosci[i2] = 0
                if licznik2 > w_jakiej_ilosci_sprzedal:
                    customer_ETH_w_jakiej_ilosci[i2] = licznik2 - w_jakiej_ilosci_sprzedal
                    #
                    zysk_strata22 = zysk_strata2 - customer_ETH_w_jakiej_ilosci[i2] * customer_ETH_za_ile[i2]  # 5 * 20
                    if zysk_strata22 > 0:
                        ETh_zysk_strata = "zysk"
                    if zysk_strata22 < 0:
                        ETH_zysk_strata = "strata"
                    if zysk_strata22 == 0:
                        ETH_zysk_strata = "nie ma ani zysku ani straty"
                    #
                    flag2 = False
                i2 += 1


        if co_sprzedal == 'LTC':
            customer_LTC_za_ile_sprzedal.append(za_ile_sprzedal)
            customer_LTC_w_jakiej_ilosci_sprzedal.append(w_jakiej_ilosci_sprzedal)

            licznik3 = 0
            i3 = 0
            zysk_strata3 = 0
            flag3 = True
            while flag3:
                #
                licznik3 += customer_LTC_w_jakiej_ilosci[i3]
                #
                licznik3 += customer_LTC_w_jakiej_ilosci[i3]
                customer_LTC_w_jakiej_ilosci[i3] = 0
                if licznik3 > w_jakiej_ilosci_sprzedal:
                    customer_LTC_w_jakiej_ilosci[i3] = licznik3 - w_jakiej_ilosci_sprzedal
                    #
                    zysk_strata33 = zysk_strata3 - customer_LTC_w_jakiej_ilosci[i3] * customer_LTC_za_ile[i3]  # 5 * 20
                    if zysk_strata33 > 0:
                        LTC_zysk_strata = "zysk"
                    if zysk_strata33 < 0:
                        LTC_zysk_strata = "strata"
                    if zysk_strata33 == 0:
                        LTC_zysk_strata = "nie ma ani zysku ani straty"
                    #
                    flag3 = False
                i3 += 1


    srednia_LSK_sprzedal.append(average(customer_LSK_za_ile_sprzedal, customer_LSK_w_jakiej_ilosci_sprzedal))
    srednia_ETH_sprzedal.append(average(customer_ETH_za_ile_sprzedal, customer_ETH_w_jakiej_ilosci_sprzedal))
    srednia_LTC_sprzedal.append(average(customer_LTC_za_ile_sprzedal, customer_LTC_w_jakiej_ilosci_sprzedal))

    srednia_LSK.append(average(customer_LSK_za_ile, customer_LSK_w_jakiej_ilosci))
    srednia_ETH.append(average(customer_ETH_za_ile, customer_ETH_w_jakiej_ilosci))
    srednia_LTC.append(average(customer_LTC_za_ile, customer_LTC_w_jakiej_ilosci))


    odpowiedz = input('Czy chcesz zakonczyc: t/n: ')
    print('LSK')
    print(customer_LSK_za_ile)
    print(customer_LSK_w_jakiej_ilosci)
    print('srednia za kupione akcje', srednia_LSK)
    print('srednia za sprzedane akcje', srednia_LSK_sprzedal)
    print(LSK_zysk_strata11)

    print('ETH')
    print(customer_ETH_za_ile)
    print(customer_ETH_w_jakiej_ilosci)
    print('srednia za kupione akcje', srednia_ETH)
    print('srednia za sprzedane akcje', srednia_ETH_sprzedal)
    print(ETH_zysk_strata22)

    print('LTC')
    print(customer_LTC_za_ile)
    print(customer_LTC_w_jakiej_ilosci)
    print('srednia za sprzedane akcje', srednia_LTC_sprzedal)
    print(LTC_zysk_strata33)


    time.sleep(3)
    if odpowiedz == 't':
        flag = False

#chyba działa git więc jeszcze dodać możliwość zapisywania pliku