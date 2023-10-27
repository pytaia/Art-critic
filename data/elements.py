from math import gcd
import numpy as np
from connect import information, statistics, rooms

def create_art(hall_number, author, name, style, width, year_of_creation):
    #создание картины. передать необходимые данные строками
    individual_number = str(len(information.scan()['Items']))
    information.put_item(Item={
        'individual_number': individual_number,
        'hall_number': hall_number,
        'author': author,
        'name': name,
        'style': style,
        'width': width,
        'year_of_creation': str(year_of_creation)
    })
    statistics.put_item(Item={
        'individual_number': individual_number,
        'views': '0',
        'emotions': '0,0,0,0,0,0,0'
    })


def hang_art(individual_number, new_hall_number):
    # изменить зал картины. передать необходимые данные строками. используется в других функциях
    information.update_item(Key={'individual_number': individual_number},
                            UpdateExpression='SET hall_number = :val1',
                            ExpressionAttributeValues={':val1': new_hall_number})


def create_room(size, paintings):
    # создать комнату. передать размер строкой вида 'x,y' и данные о картинах СПИСКОМ
    number = str(len(rooms.scan()['Items']) + 1)
    for i in paintings:
        hang_art(i[0], number)
    rooms.put_item(Item={
        'number': number,
        'size': size,
        'paintings': list_in_str(paintings)
    })


def edit_room(number, new_paintings):
    # редактирование комнаты. номер комнаты строкой, данные картин СПИСКОМ
    res = return_room_data(number)['paintings']
    for i in filter(lambda x: x[0] not in [j[0] for j in res], new_paintings):
        hang_art(i[0], number)
    for i in filter(lambda x: x[0] not in [j[0] for j in new_paintings], res):
        hang_art(i[0], new_hall_number='0')
    rooms.update_item(Key={'number': number},
                      UpdateExpression='SET paintings = :val1',
                      ExpressionAttributeValues={':val1': list_in_str(new_paintings)})


def delete_room(number):
    # удаление комнаты. номер строкой
    res = rooms.get_item(Key={'number': number})['Item']['paintings']
    for i in res.split(';'):
        hang_art(i.split(',')[0], new_hall_number='0')
    rooms.delete_item(Key={'number': number})


def delete_art(individual_number):
    # удаление картины. номер строкой
    res = information.get_item(Key={'individual_number': individual_number})['Item']['hall_number']
    if res != '0':
        res = rooms.get_item(Key={'number': res})['Item']['paintings']
        s = []
        for i in res.split(';'):
            if i.split(',')[0] != individual_number:
                s.append(i)
        rooms.update_item(Key={'number': res},
                          UpdateExpression='SET paintings = :val1',
                          ExpressionAttributeValues={':val1': ';'.join(s)})
    information.delete_item(Key={'individual_number': individual_number})
    statistics.delete_item(Key={'individual_number': individual_number})


def edit_stat(individual_number, new_emotions):
    # изменение статистики. все передается строками
    res = statistics.get_item(Key={'individual_number': individual_number})['Item']
    emotions = np.array(new_emotions.split(','), int) + np.array(res['emotions'].split(','), int)
    c = gcd(*emotions, int(res['views']) + 1)
    emotions = ','.join(np.array(emotions // c, str))
    statistics.update_item(Key={'individual_number': individual_number},
                           UpdateExpression='SET emotions = :val1',
                           ExpressionAttributeValues={':val1': emotions})
    statistics.update_item(Key={'individual_number': individual_number},
                           UpdateExpression='SET views = :val1',
                           ExpressionAttributeValues={':val1': str((int(res['views']) + 1) // c)})


def list_in_str(paintings):
    # реоброазование в строку. используется в других функциях
    return ';'.join([','.join(i) for i in paintings])


def return_information(individual_number):
    # возвращает информацию о картине. номер строкой
    return information.get_item(Key={'individual_number': individual_number})['Item']



def return_statistics(individual_number):
    # возвращает статистику картины. номер строкой
    res = statistics.get_item(Key={'individual_number': individual_number})['Item']['emotions'].split(',')
    return {'angry': int(res[0]), 'disgust': int(res[1]), 'fear': int(res[2]),
            'happy': int(res[3]), 'sad': int(res[4]), 'surprise': int(res[5]),
            'neutral': int(res[6])}


def return_room_data(number):
    # возвращает данные комнаты. номер строкой
    res = rooms.get_item(Key={'number': number})['Item']
    paintings = [i.split(',') for i in res['paintings'].split(';')]
    return {'size': [int(i) for i in res['size'].split(',')], 'paintings': paintings}


def get_individual_number(name):
    # получение номера картины по названию
    return information.get_item(Key={'name': name})['Item']['individual_number']


def get_names():
    # получение всех названий
    names = []
    res = information.scan()['Items']
    for i in res:
        names.append(i['name'])
    return names