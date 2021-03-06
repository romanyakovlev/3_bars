# -*- coding: utf-8 -*-

import json
import argparse


def load_data(filepath):
    with open(filepath) as data_file:
        data = json.load(data_file)
    return data

def get_biggest_bar(bar_data):
    biggest_bar_object = max(bar_data, key=lambda x:x['Cells']['SeatsCount'])
    biggest_bar_adress = biggest_bar_object['Cells']['Address']
    return biggest_bar_adress

def get_smallest_bar(bar_data):
    smallest_bar_object = min(bar_data,key=lambda x:x['Cells']['SeatsCount'])
    smallest_bar_adress = smallest_bar_object['Cells']['Address']
    return smallest_bar_adress

def get_closest_bar(bar_data, longitude, latitude):
    closest_bar_object = min(bar_data, key=lambda x:
    (x['Cells']['geoData']['coordinates'][0]-longitude)**2 +
    (x['Cells']['geoData']['coordinates'][1]-latitude)**2)
    closest_bar_adress = closest_bar_object['Cells']['Address']
    return closest_bar_adress


if __name__ == '__main__':

    json_filepath = input('Введите путь до файла с данными или сам файл,' +
    'если он находится в этой директории:\n')
    bar_longitude= float(input('Ваш файл c данными: {}'.format(json_filepath.split('/')[-1] +
    '\nТеперь введите ваши координаты\nДолгота:')))
    bar_latitude = float(input('Широта:'))

    bar_data = load_data(json_filepath)
    print('Самый большой бар: {}'.format(get_biggest_bar(bar_data)))
    print('Самый маленький бар: {}'.format(get_smallest_bar(bar_data)))
    print('Самый близкий бар для тебя: {}'.format(get_closest_bar(
    bar_data, bar_longitude, bar_latitude)))
