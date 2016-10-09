# -*- coding: utf-8 -*-

import json
import argparse

def load_data(filepath):
    with open(filepath) as data_file:
        data = json.load(data_file)
    return data

def get_biggest_bar(data):
    biggest_bar_object = max(data, key=lambda x:x['Cells']['SeatsCount'])
    biggest_bar_adress = biggest_bar_object['Cells']['Address']
    return u'Самый маленький бар: {}'.format(biggest_bar_adress)

def get_smallest_bar(data):
    smallest_bar_object = min(data,key=lambda x:x['Cells']['SeatsCount'])
    smallest_bar_adress = smallest_bar_object['Cells']['Address']
    return u'Самый маленький бар: {}'.format(smallest_bar_adress)

def get_closest_bar(data, longitude, latitude):
    closest_bar_object = min(data,key=lambda x:(x['Cells']['geoData']['coordinates'][0]-longitude)**2 + (x['Cells']['geoData']['coordinates'][1]-latitude)**2)
    closest_bar_adress = closest_bar_object['Cells']['Address']
    return u'Самый близкий бар для тебя: {}'.format(closest_bar_adress)

if __name__ == '__main__':
    print('Введите путь до файла с данными или сам файл, если он находится в этой директории')
    json_filepath = input()
    print('Ваш файл c данными: {}'.format(json_filepath.split('/')[-1]))
    print('Теперь введите ваши координаты')
    print('Долгота:')
    bar_longitude= float(input())
    print('Широта:')
    bar_latitude = float(input())
    bar_data = load_data(json_filepath)
    print(get_biggest_bar(bar_data))
    print(get_smallest_bar(bar_data))
    print(get_closest_bar(bar_data, bar_longitude, bar_latitude))
