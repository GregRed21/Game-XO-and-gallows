import copy


def X_O():
    def get_int_n():
        while True:
            try:
                n = int(input('Введите число строк: \n'))
                return n
            except:
                print('Not a number! Try again.\n')
                continue

    n = get_int_n()

    def get_int_m():
        while True:
            try:
                m = int(input('Введите число столбцов: \n'))
                return m
            except:
                print('Not a number! Try again.\n')
                continue

    m = get_int_m()
    n = n + n - 1
    m = m + m - 1
    massiv = [[' ' for i in range(m)] for j in range(n)]
    ch1_3 = []
    for i in range(1, n):
        if i % 2 != 0:
            ch1_3.append(i)
    # print(ch1_3)

    ch1_3_m = []
    for i in range(1, m):
        if i % 2 != 0:
            ch1_3_m.append(i)
    # print(ch1_3_m)
    for i in ch1_3:
        xlen_massive_1 = 0
        while xlen_massive_1 < len(massiv[n - 1]):
            massiv[i].pop(xlen_massive_1)
            massiv[i].insert(xlen_massive_1, '-')
            xlen_massive_1 += 1

    for i in range(n):
        for j in ch1_3_m:
            massiv[i].pop(j)
            massiv[i].insert(j, '|')

    for i in range(n):
        for j in range(m):
            print(massiv[i][j], end=' ')
        print()

    def play(n=n, m=m, massiv=massiv):
        list_del_dva = []
        for i in range(n):
            if i % 2 == 0:
                list_del_dva.append(i)
        # slovar_pozicyi={i:i for i in range(1, len(list_del_dva)+1)}
        # print(slovar_pozicyi)
        count_true = list(range(int(((n + 1) / 2) * ((m + 1) / 2))))
        # print(count_true)
        count_true_zero = 0
        while count_true_zero <= len(count_true):
            def x_post_stolb_fun(m=m):
                while True:
                    try:
                        x_post_stolb = int(input('Куда хотите поставить X, столб?\n'))
                        if x_post_stolb <= 0 or x_post_stolb > ((m + 1) / 2):
                            raise ValueError
                        return x_post_stolb
                    except:
                        print('Not a number! Try again.\n')
                    continue

            def x_post_strok_fun(n=n):
                while True:
                    try:
                        x_post_strok = int(input('строка?\n'))
                        if x_post_strok <= 0 or x_post_strok > ((n + 1) / 2):
                            raise ValueError
                        return x_post_strok
                    except:
                        print('Not a number! Try again.\n')
                    continue

            while True:
                try:
                    x_post_stolb = x_post_stolb_fun()
                    x_post_strok = x_post_strok_fun()
                    for i in range(n):
                        if i == (x_post_strok + x_post_strok - 2):
                            for j in list_del_dva:
                                if j == (x_post_stolb + x_post_stolb - 2):
                                    if massiv[i][j] == "X" or massiv[i][j] == "O":
                                        raise ValueError
                    break

                except:
                    print('This field is already occupied. Choose another one.\n')
                    continue
            x_post_stolb = x_post_stolb + x_post_stolb - 2
            x_post_strok = x_post_strok + x_post_strok - 2
            for i in range(n):
                if i == x_post_strok:
                    for j in list_del_dva:
                        if j == x_post_stolb:
                            massiv[i].pop(j)
                            massiv[i].insert(j, 'X')
            for i in range(n):
                for j in range(m):
                    print(massiv[i][j], end=' ')
                print()
            ####
            count_n = 0
            count_win = 0
            while count_n <= len(massiv[n - 1]):
                win_vdol = []
                for i in list_del_dva:
                    win_vdol.append(massiv[i][count_n])
                # print(win_vdol)
                if all(i == 'X' for i in win_vdol) == True:
                    print('Player 1 win!')
                    count_win += 1
                    break
                elif all(i == 'O' for i in win_vdol) == True:
                    print('Player 2 win!')
                    count_win += 1
                    break
                else:
                    win_vdol.clear()
                count_n += 2

            count_m = 0
            while count_m <= len(massiv[m - 1]):
                win_poperek = []
                for i in list_del_dva:
                    win_poperek.append(massiv[count_m][i])
                # print(win_poperek)
                if all(i == 'X' for i in win_poperek) == True:
                    print('Player 1 win!')
                    count_win += 1
                    break
                elif all(i == 'O' for i in win_poperek) == True:
                    print('Player 2 win!')
                    count_win += 1
                    break
                else:
                    win_poperek.clear()
                count_m += 2

            count_d = 0
            while count_d <= len(massiv[m - 1]):
                win_diag = []
                for i in list_del_dva:
                    win_diag.append(massiv[i][i])
                # print(win_diag)
                if all(i == 'X' for i in win_diag) == True:
                    print('Player 1 win!')
                    count_win += 1
                    break
                elif all(i == 'O' for i in win_diag) == True:
                    print('Player 2 win!')
                    count_win += 1
                    break
                else:
                    win_diag.clear()
                count_d += 2

            count_o_d = 0
            massiv_reverse = copy.deepcopy(massiv)
            for i in list_del_dva:
                massiv_reverse[i].reverse()
            # print(massiv_reverse)

            # for i in range(n):
            #     for j in range(m):
            #         print(massiv_reverse[i][j], end=' ')
            #     print()
            ####
            while count_o_d <= len(massiv_reverse[m - 1]):
                win_o_diag = []
                for i in list_del_dva:
                    win_o_diag.append(massiv_reverse[i][i])
                # print(win_o_diag)
                if all(i == 'X' for i in win_o_diag) == True:
                    print('Player 1 win!')
                    count_win += 1
                    break
                elif all(i == 'O' for i in win_o_diag) == True:
                    print('Player 2 win!')
                    count_win += 1
                    break
                else:
                    win_o_diag.clear()
                count_o_d += 2
            massiv_reverse.clear()
            count_true_zero += 1
            if count_true_zero == len(count_true):
                print('Draw')
                break
            if count_win == 1:
                break

            ####
            def o_post_stolb_fun(m=m):
                while True:
                    try:
                        o_post_stolb = int(input('Куда хотите поставить O, столб?\n'))
                        if o_post_stolb <= 0 or o_post_stolb > ((m + 1) / 2):
                            raise ValueError
                        return o_post_stolb
                    except:
                        print('Not a number! Try again.\n')
                        continue

            def o_post_strok_fun(n=n):
                while True:
                    try:
                        o_post_strok = int(input('строка?\n'))
                        if o_post_strok <= 0 or o_post_strok > ((n + 1) / 2):
                            raise ValueError
                        return o_post_strok
                    except:
                        print('Not a number! Try again.\n')
                        continue

            while True:
                try:
                    o_post_stolb = o_post_stolb_fun()
                    o_post_strok = o_post_strok_fun()
                    for i in range(n):
                        if i == (o_post_strok + o_post_strok - 2):
                            for j in list_del_dva:
                                if j == (o_post_stolb + o_post_stolb - 2):
                                    if massiv[i][j] == "X" or massiv[i][j] == "O":
                                        raise ValueError
                    break

                except:
                    print('This field is already occupied. Choose another one.\n')
                    continue

            o_post_stolb = o_post_stolb + o_post_stolb - 2
            o_post_strok = o_post_strok + o_post_strok - 2
            for i in range(n):
                if i == o_post_strok:
                    for j in list_del_dva:
                        if j == o_post_stolb:
                            massiv[i].pop(j)
                            massiv[i].insert(j, 'O')
            for i in range(n):
                for j in range(m):
                    print(massiv[i][j], end=' ')
                print()
            count_n = 0
            count_win = 0
            while count_n <= len(massiv[n - 1]):
                win_vdol = []
                for i in list_del_dva:
                    win_vdol.append(massiv[i][count_n])
                # print(win_vdol)
                if all(i == 'X' for i in win_vdol) == True:
                    print('Player 1 win!')
                    count_win += 1
                    break
                elif all(i == 'O' for i in win_vdol) == True:
                    print('Player 2 win!')
                    count_win += 1
                    break
                else:
                    win_vdol.clear()
                count_n += 2

            count_m = 0
            while count_m <= len(massiv[m - 1]):
                win_poperek = []
                for i in list_del_dva:
                    win_poperek.append(massiv[count_m][i])
                # print(win_poperek)
                if all(i == 'X' for i in win_poperek) == True:
                    print('Player 1 win!')
                    count_win += 1
                    break
                elif all(i == 'O' for i in win_poperek) == True:
                    print('Player 2 win!')
                    count_win += 1
                    break
                else:
                    win_poperek.clear()
                count_m += 2

            count_d = 0
            while count_d <= len(massiv[m - 1]):
                win_diag = []
                for i in list_del_dva:
                    win_diag.append(massiv[i][i])
                # print(win_diag)
                if all(i == 'X' for i in win_diag) == True:
                    print('Player 1 win!')
                    count_win += 1
                    break
                elif all(i == 'O' for i in win_diag) == True:
                    print('Player 2 win!')
                    count_win += 1
                    break
                else:
                    win_diag.clear()
                count_d += 2
            ####
            count_o_d = 0
            massiv_reverse = copy.deepcopy(massiv)
            for i in list_del_dva:
                massiv_reverse[i].reverse()
            # print(massiv_reverse)

            # for i in range(n):
            #     for j in range(m):
            #         print(massiv_reverse[i][j], end=' ')
            #     print()
            ####
            while count_o_d <= len(massiv_reverse[m - 1]):
                win_o_diag = []
                for i in list_del_dva:
                    win_o_diag.append(massiv_reverse[i][i])
                # print(win_o_diag)
                if all(i == 'X' for i in win_o_diag) == True:
                    print('Player 1 win!')
                    count_win += 1
                    break
                elif all(i == 'O' for i in win_o_diag) == True:
                    print('Player 2 win!')
                    count_win += 1
                    break
                else:
                    win_o_diag.clear()
                count_o_d += 2
            massiv_reverse.clear()
            ####
            count_true_zero += 1
            # print(count_true_zero)
            # print(count_true)
            if count_true_zero == len(count_true):
                print('Draw')
                break
            if count_win == 1:
                break

    play()


X_O()
