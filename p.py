import requests
from pprint import pprint
from danger import *

# url = "http://apis.mapmyindia.com/advancedmaps/v1/8dzezyssdbkn9ufq48kin8z7xu36f9en/route?start=28.7164,77.1546&destination=28.4917,77.0949&alternatives=true&with_advices=1"
# res = requests.get(url)

# d = res.json()
# print(d['results'].keys())
# all_advices = [ d['results']['trips'][0]['advices'], d['results']['alternatives']['advices'] ] 
all_paths = []
# source = "28.7164,77.1546"
# destination = "28.4917,77.0949"
# vtype = "0"
def get_response(source, destination, rtype, vtype):
    url = f"http://apis.mapmyindia.com/advancedmaps/v1/8dzezyssdbkn9ufq48kin8z7xu36f9en/route?start={source}&destination={destination}&alternatives=true&with_advices=1&vtype={vtype}&rtype={rtype}"
    res = requests.get(url)
    d = res.json()
    # pprint(d['results'])
    return(d)

rtype = [0, 1]

def assign_safest(all_paths):
    l = [path['danger_index'] for path in all_paths]
    # print(l.index(min(l)))

    return (l.index(min(l)))


            

def get_path(source, destination, vtype):
    for r in rtype:
        d = get_response(source, destination, r, vtype)
        advices = d['results']['trips'][0]['advices']
        all_duration = [d['results']['trips'][0]['duration']]
        all_advices = [advices]
        all_distances = [d['results']['trips'][0]['length']]
    
        # print(len(d['results']['alternatives']))
        if len(d['results']['alternatives']) > 0:
            all_advices.append(d['results']['alternatives'][0]['advices'])
            all_duration.append(d['results']['alternatives'][0]['duration'])
            all_distances.append(d['results']['alternatives'][0]['length'])
        
        for advices,duration,distance in zip(all_advices, all_duration, all_distances):
            path = []
            # pprint(duration)
            for advice in advices:
                pt = list(advice['pt'].values())
                # print(advice['pt'])
                path.append(pt)
            index = final_index(path)
            output = {'path': path, 'danger_index' : index, 'duration': duration//60, 'distance': distance//1000}


            if r == 0:
                output['type'] = ['quickest']
            elif r== 1: 
                output['type'] = ['shortest']
            all_paths.append(output)
    safe_index = assign_safest(all_paths)
    all_paths[safe_index]['type'].append("safest")

        # pprint(len(all_paths))
        # print(len(all_paths))


    # for path in all_paths:
        # pprint(path)
    return(all_paths)


# pprint(d['results']['alternatives'])
# get_path()

if __name__ == '__main__':
    source = "28.7164,77.1546"
    destination = "28.4917,77.0949"
    vtype = "0"
    all_paths = get_path(source, destination, vtype)
    pprint(all_paths)


# pprint(pts)
# [28.647492469553, 77.199372053146]