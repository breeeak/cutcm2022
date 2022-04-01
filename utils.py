# -*- coding: utf-8 -*-
# @Time    : 2022/4/2 0:00
# @Author  : Marshall
# @FileName: utils.py

# Get number of recording locations from patient data.
def get_num_locations(data):
    num_locations = None
    for i, l in enumerate(data.split('\n')):
        if i==0:
            try:
                num_locations = int(l.split(' ')[1])
            except:
                pass
        else:
            break
    return num_locations

# Compare normalized strings.
def compare_strings(x, y):
    try:
        return x.strip().casefold()==y.strip().casefold()
    except AttributeError: # For Python 2.x compatibility
        return x.strip().lower()==y.strip().lower()


# Get recording locations from patient data.
def get_locations(data):
    num_locations = get_num_locations(data)
    locations = list()
    for i, l in enumerate(data.split('\n')):
        entries = l.split(' ')
        if i==0:
            pass
        elif 1 <= i < num_locations+1:
        # elif 1<=i<=num_locations+1:     # 这里是不是会多一行，多算了一个location？
            locations.append(entries[0])
        else:
            break
    return locations

# Get frequency from patient data.
def get_frequency(data):
    frequency = None
    for i, l in enumerate(data.split('\n')):
        if i==0:
            try:
                # frequency = float(l.split(' ')[1])      # 这里应该是2才对
                frequency = float(l.split(' ')[2])
            except:
                pass
        else:
            break
    return frequency

# Get pregnancy status from patient data.
def get_pregnancy_status(data):
    is_pregnant = None
    for l in data.split('\n'):
        if l.startswith('#Pregnancy status:'):
            try:
                # is_pregnant = bool(l.split(': ')[1].strip())        # 这样是不能获取的，他是大写的
                is_pregnant = l.split(': ')[1].strip()  #
                if compare_strings(is_pregnant, "False"):
                    is_pregnant = 0
                elif compare_strings(is_pregnant, "True"):
                    is_pregnant = 1
            except:
                pass
    return is_pregnant