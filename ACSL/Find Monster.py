def find_Dwight(input_1, input_2, input_3):
    # This function takes three locations and the distance between them and triangulates Dwight
    input_1 = input_1.split(' ')

    location_1 = input_1[0]
    location_1 = [int(location_1[:2], 16), int(location_1[2:], 16)]

    distance_1 = input_1[1]
    distance_1 = [int(distance_1[:2], 16), int(distance_1[2:], 16)]


    # Second input
    input_2 = input_2.split(' ')

    location_2 = input_2[0]
    location_2 = [int(location_2[:2], 16), int(location_2[2:], 16)]

    distance_2 = input_2[1]
    distance_2 = [int(distance_2[:2], 16), int(distance_2[2:], 16)]


    input_3 = input_3.split(' ')

    location_3 = input_3[0]
    location_3 = [int(location_3[:2], 16), int(location_3[2:], 16)]

    distance_3 = input_3[1]
    distance_3 = [int(distance_3[:2], 16), int(distance_3[2:], 16)]

    list_1 = find_input_list(location_1, distance_1)
    list_2 = find_input_list(location_2, distance_2)
    list_3 = find_input_list(location_3, distance_3)

    for i in list_1:
        if i in list_2 and i in list_3:
            print(i)

            final = (',').join(list(map(hex, i)))
            if i[0] < 16:
                final = '0' + final

            final = ((('('+final+')')).replace(' ', ',')).replace('0x', '').upper()

            return final
            



def find_input_list(location, distance):
     # First location
    list = []
    # forward values
    v = [location[0] + distance[0], location[1] + distance[1]]
    list.append(v)
    v = [location[0] + distance[0], location[1] - distance[1]]
    list.append(v)
    v = [location[0] - distance[0], location[1] + distance[1]]
    list.append(v)
    v = [location[0] - distance[0], location[1] - distance[1]]
    list.append(v)
    # backward values
    v = [location[0] + distance[1], location[1] + distance[0]]
    list.append(v)
    v = [location[0] + distance[1], location[1] - distance[0]]
    list.append(v)
    v = [location[0] - distance[1], location[1] + distance[0]]
    list.append(v)
    v = [location[0] - distance[1], location[1] - distance[0]]
    list.append(v)
    return list



print(find_Dwight("4D93 414D", "A566 997A", "F633 EAAD"))