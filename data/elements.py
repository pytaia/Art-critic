from math import gcd
import numpy as np
from connect import information, statistics, rooms

# все данные передаем в функции строками!

def create_art(hall_number, author, name, style, width, year_of_creation):
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
    information.update_item(Key={'individual_number': individual_number},
                            UpdateExpression='SET hall_number = :val1',
                            ExpressionAttributeValues={':val1': new_hall_number})


def create_room(size, paintings):
    number = str(len(rooms.scan()['Items']) + 1)
    for i in paintings:
        hang_art(i[0], number)
    rooms.put_item(Item={
        'number': number,
        'size': size,
        'paintings': list_in_str(paintings)
    })


def edit_room(number, new_paintings):
    res = return_room_data(number)['paintings']
    for i in filter(lambda x: x[0] not in [j[0] for j in res], new_paintings):
        hang_art(i[0], number)
    for i in filter(lambda x: x[0] not in [j[0] for j in new_paintings], res):
        hang_art(i[0], '0')
    rooms.update_item(Key={'number': number},
                      UpdateExpression='SET paintings = :val1',
                      ExpressionAttributeValues={':val1': list_in_str(new_paintings)})


def delete_room(number):
    res = rooms.get_item(Key={'number': number})['Item']['paintings']
    for i in res.split(';'):
        hang_art(i.split(',')[0], '0')
    rooms.delete_item(Key={'number': number})


def delete_art(individual_number):
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
    res = statistics.get_item(Key={'individual_number': individual_number})['Item']
    emotions = np.array(new_emotions.split(), int) + np.array(res['emotions'].split(','), int)
    c = gcd(*emotions, int(res['views']) + 1)
    emotions = ','.join(np.array(emotions // c, str))
    statistics.update_item(Key={'individual_number': individual_number},
                           UpdateExpression='SET emotions = :val1',
                           ExpressionAttributeValues={':val1': emotions})
    statistics.update_item(Key={'individual_number': individual_number},
                           UpdateExpression='SET views = :val1',
                           ExpressionAttributeValues={':val1': str((int(res['views']) + 1) // c)})


def list_in_str(paintings):
    return ';'.join([','.join(i) for i in paintings])


def return_information(individual_number):
    return information.get_item(Key={'individual_number': individual_number})['Item']



def return_statistics(individual_number):
    res = statistics.get_item(Key={'individual_number': individual_number})['Item']['emotions'].split(',')
    return {'angry': int(res[0]), 'disgust': int(res[1]), 'fear': int(res[2]),
            'happy': int(res[3]), 'sad': int(res[4]), 'surprise': int(res[5]),
            'neutral': int(res[6])}


def return_room_data(number):
    res = rooms.get_item(Key={'number': number})['Item']
    paintings = [i.split(',') for i in res['paintings'].split(';')]
    return {'size': [int(i) for i in res['size'].split(',')], 'paintings': paintings}


create_art(hall_number='0', author='.', name='.', style='.', width='.', year_of_creation='9')
create_room(size='10,10', paintings=['0', '0', '5'])
edit_room('2', new_paintings=[])
edit_room('2', new_paintings=['0', '0', '5'])
print(return_room_data('2'))
delete_room('2')
#edit_stat(individual_number='0', new_emotions='0,1,0,34,0,0,0')
#return_statistics('0')
return_information('0')
#delete_art('0')
information.scan()
