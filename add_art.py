from data.elements import create_art, delete_art, create_room, delete_room, edit_stat


delete_art('1')

create_art(hall_number='0', author='РЕМБРАНДТ', name='НОЧНОЙ ДОЗОР', style='', width='100', year_of_creation='1')
create_art(hall_number='0', author='ЛЕОНАРДО ДА ВИНЧИ', name='ДЖОКОНДА', style='', width='100', year_of_creation='1')
create_art(hall_number='0', author='КАЗИМИР МАЛЕВИЧ', name='ЧЕРНЫЙ КВАДРАТ', style='', width='100', year_of_creation='1')
create_art(hall_number='0', author='ВИНСЕНТ ВАН ГОГ', name='ЗВЕЗДНАЯ НОЧЬ', style='', width='100', year_of_creation='1')

delete_room('1')
delete_room('2')
delete_room('3')

create_room(number='1', size='100,200', paintings='1,50,50')
create_room(number='1', size='200,175', paintings='2,50,50')
create_room(number='1', size='300,150', paintings='3,50,50')

edit_stat('1', '1,45,65,2,34,2,45')