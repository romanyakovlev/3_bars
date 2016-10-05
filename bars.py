import json


def load_data(filepath):
    data = []
    with open(filepath) as data_file:
        data = json.load(data_file)
    return data

def get_biggest_bar(data):
    mx = max(x['Cells']['SeatsCount'] for x in data)
    for x in data:
        if x['Cells']['SeatsCount']==mx:
            return x['Cells']['Address']
            break


def get_smallest_bar(data):
    mn = min(x['Cells']['SeatsCount'] for x in data)
    for x in data:
        if x['Cells']['SeatsCount']==mn:
            return x['Cells']['Address']
            break

def get_closest_bar(data, longitude, latitude):
    mn = min((x['Cells']['geoData']['coordinates'][0]-longitude)**2 +(x['Cells']['geoData']['coordinates'][1]-latitude)**2 for x in data)
    for x in data:
        var = (x['Cells']['geoData']['coordinates'][0]-longitude)**2 + (x['Cells']['geoData']['coordinates'][1]-latitude)**2
        if mn == var:
            return x['Cells']['Address']
            break


if __name__ == '__main__':
    data = load_data('data.json')
    print(get_biggest_bar(data))
    print(get_smallest_bar(data))
    print(get_closest_bar(data,float(input()),float(input())))
