
ignore = ['duplex', 'alias', 'Current configuration']

def ignore_command(command, ignore):
    """
    Функция проверяет содержится ли в команде слово из списка ignore.
    command - строка. Команда, которую надо проверить
    ignore - список. Список слов
    Возвращает True, если в команде содержится слово из списка ignore, False - если нет
    """
    ignore_command = False
    for word in ignore:
        if word in command:
            return True
    return ignore_command

def config_to_dict(config):
    input_config = []
    output_dict = {}
    with open(config, 'r') as f:
        input_config = [s.rstrip() for s in f.readlines()]
    
    for s in range(0, len(input_config)):
        value_list = []
        key = ""
        if not input_config[s].startswith((' ', '!')) and not ignore_command(input_config[s], ignore):
            key = input_config[s]
            for ss in range(s+1, len(input_config)):
                if not input_config[ss].startswith(' '):
                    s = ss-1
                    break
                else:
                    value_list.append(input_config[ss].strip())
        output_dict.update({key: value_list})
        ++s
    return output_dict

for key, value in config_to_dict('config_sw1.txt').items():
    print ("{}: {}".format(key, str(value)))