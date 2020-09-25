import tsp
import math
import requests

def get_api(source, dest):
    url ='https://maps.googleapis.com/maps/api/distancematrix/json?'
    r = requests.get(url + 'origins=' + source +
                     '&destinations=' + dest +
                     '&key=' + gmaps_key)
    x = r.json()
    x = dict(x)
    distance = str(x['rows'][0]['elements'][0]['distance']['text']).replace(" km", "").replace(",", "")
    return float(distance)


def distance_calculation(list,API):
    #determine the ending of a loop.
    #geolist
    # get the starting point


    print("the places you wanna go are ",list," , and you wanna go back to ",list[0]," after this busy day..")

    #construct a source-destination pair
    source_dest_pair = []
    for i in range(0,len(list)):
        #source;
        source = list[i]
        for j in range(i+1,len(list)):
            #destination
            temp = []
            temp.append(source)
            dest = list[j]
            temp.append(dest)
            source_dest_pair.append(temp)


    distance_list=[]
    loops = int(math.factorial(len(list)) / (2*math.factorial(len(list)-2)))
    #as if we've got the distance;
    for i in range(loops):
        distance_list.append(get_api(source_dest_pair[i][0],source_dest_pair[i][1]))

    #print(distance_list)


    distance_matrix=[]
    for i in range(0,len(list)):
        temp_matrix = [0] * len(list)
        distance_matrix.append(temp_matrix)

    temp_list_row = distance_list.copy()

    for i in range(0,distance_matrix.__len__()):
        # for each source
        for j in range(i+1,distance_matrix.__len__()):
            distance_matrix[i][j] = temp_list_row.pop(0)

    temp_list_col = distance_list.copy()

    for i in range(0,distance_matrix.__len__()):
        # for each source
        for j in range(i+1,distance_matrix.__len__()):
            distance_matrix[j][i] = temp_list_col.pop(0)


    print(distance_matrix)
    # print(distance_list)



    r = range(len(distance_matrix))
    #
    #construct a path matrix and put it into a dictionary
    shortestpath = {(i,j): distance_matrix[i][j] for i in r for j in r}

    #print(tsp.tsp(r,shortestpath)[1])
    print("----------------------------------------------")
    print("\nyour travel routine is ")
    total_list = ''
    for i in range(len(tsp.tsp(r,shortestpath)[1])):
        total_list += str(list[tsp.tsp(r,shortestpath)[1][i]])+" -> "
    total_list += list[0]
    total_list += ", and the total distance of travel is: "+str(tsp.tsp(r,shortestpath)[0]) +" km."
    return total_list
