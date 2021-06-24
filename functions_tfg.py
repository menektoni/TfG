def contributions_separation(string):
    return [int(i) for i in re.findall('[0-9]+', string)]

# THE ULTIMATE MUTUAL INFOMRATION (FOR 3 VALUES) FUNCTION.

def mutual_information(dataframe):
    side = dataframe.count()['c1'] + 1
    i = 0
    smi_ver_vila = np.zeros(shape=(side,side))
    for index_1, user_1 in dataframe.iterrows():
        i += 1
        j = 0
        for index_2, user_2 in dataframe.iterrows():
            j += 1
            index_1 = contributions_separation(str(index_1))[0]
            index_2 = contributions_separation(str(index_2))[0]
            x_array = np.asarray(user_1[['c1', 'c2', 'c3','c4', 'c5', 'c6','c7', 'c8', 'c9', 'c10']])
            y_array = np.asarray(user_2[['c1', 'c2', 'c3','c4', 'c5', 'c6','c7', 'c8', 'c9', 'c10']])


            y_prob = []  
            cont_0y = 0
            cont_2y = 0
            cont_4y = 0

            x_prob = []
            cont_0 = 0
            cont_2 = 0
            cont_4 = 0

            # Y PROBABILITIES
            for index, num in enumerate(y_array):
                # Pair of Study Catched


                # Separate Probabilities:


                if num == 0:
                    cont_0y += 1
                elif num == 2:
                    cont_2y += 1
                else:
                    cont_4y += 1
            y_prob.append(cont_0y/10)
            y_prob.append(cont_2y/10)
            y_prob.append(cont_4y/10)




            # X PROBABILITIES
            for index, num in enumerate(x_array):
                # Pair of Study Catched
                pair = [num, y_array[index]]

                # Separate Probabilities:


                if num == 0:
                    cont_0 += 1
                elif num == 2:
                    cont_2 += 1
                else:
                    cont_4 += 1
            x_prob.append(cont_0/10)
            x_prob.append(cont_2/10)
            x_prob.append(cont_4/10)


            # CONDITIONATED PROBABILITY AND MUTUAL INFORMATION    
            mi = 0        # INITIATING THE MUTUAL INFORMATION FOR EACH VALUE
            for index, num in enumerate(x_array):
                # PROBABILITIES
                px = x_prob[int(num)//2]
                py = y_prob[int(y_array[index])//2]



                # Condicionated Probability:
                # It looks that what we have here works. 
                pos_x = []
                for index_x, num_x in enumerate(x_array):

                    if num == num_x:
                        pos_x.append(index_x)
                cont_y = 0
                for pos in pos_x:
                    if y_array[index] == y_array[pos]:
                        cont_y += 1

                p_x_given_y = cont_y/len(pos_x)

                mi = mi + (p_x_given_y*px*math.log(p_x_given_y*px/(px*py),3))

            if mi != None:
                smi_ver_vila[i, j] = mi/10
            else:
                smi_ver_vila[i, j] = 0
    return smi_ver_vila

# THE ULTIMATE SHUFFLED MUTUAL INFOMRATION (FOR 3 VALUES) FUNCTION.

def mutual_information_shuffled(dataframe):
    side = dataframe.count()['c1'] + 1
    i = 0
    smi_ver_vila = np.zeros(shape=(side,side))
    for index_1, user_1 in dataframe.iterrows():
        i += 1
        j = 0
        for index_2, user_2 in dataframe.iterrows():
            j += 1
            index_1 = contributions_separation(str(index_1))[0]
            index_2 = contributions_separation(str(index_2))[0]
            x_array = shuffle(np.asarray(user_1[['c1', 'c2', 'c3','c4', 'c5', 'c6','c7', 'c8', 'c9', 'c10']]))
            y_array = shuffle(np.asarray(user_2[['c1', 'c2', 'c3','c4', 'c5', 'c6','c7', 'c8', 'c9', 'c10']]))


            y_prob = []  
            cont_0y = 0
            cont_2y = 0
            cont_4y = 0

            x_prob = []
            cont_0 = 0
            cont_2 = 0
            cont_4 = 0

            # Y PROBABILITIES
            for index, num in enumerate(y_array):
                # Pair of Study Catched


                # Separate Probabilities:


                if num == 0:
                    cont_0y += 1
                elif num == 2:
                    cont_2y += 1
                else:
                    cont_4y += 1
            y_prob.append(cont_0y/10)
            y_prob.append(cont_2y/10)
            y_prob.append(cont_4y/10)




            # X PROBABILITIES
            for index, num in enumerate(x_array):
                # Pair of Study Catched
                pair = [num, y_array[index]]

                # Separate Probabilities:


                if num == 0:
                    cont_0 += 1
                elif num == 2:
                    cont_2 += 1
                else:
                    cont_4 += 1
            x_prob.append(cont_0/10)
            x_prob.append(cont_2/10)
            x_prob.append(cont_4/10)


            # CONDITIONATED PROBABILITY AND MUTUAL INFORMATION    
            mi = 0        # INITIATING THE MUTUAL INFORMATION FOR EACH VALUE
            for index, num in enumerate(x_array):
                # PROBABILITIES
                px = x_prob[int(num)//2]
                py = y_prob[int(y_array[index])//2]



                # Condicionated Probability:
                # It looks that what we have here works. 
                pos_x = []
                for index_x, num_x in enumerate(x_array):

                    if num == num_x:
                        pos_x.append(index_x)
                cont_y = 0
                for pos in pos_x:
                    if y_array[index] == y_array[pos]:
                        cont_y += 1

                p_x_given_y = cont_y/len(pos_x)

                mi = mi + (p_x_given_y*px*math.log(p_x_given_y*px/(px*py),3))

            if mi != None:
                smi_ver_vila[i, j] = mi/10
            else:
                smi_ver_vila[i, j] = 0
    return smi_ver_vila

def mi_masked(natural, shuffled):
    mask = np.zeros(natural.shape)
    
    for i in range(0, natural.shape[0]):
        for j in range(0, natural.shape[1]):
            if((natural[i,j]-shuffled[i,j]) > 0):
                mask[i, j] = 1
    return mask*natural       