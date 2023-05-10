
import sys
import os

# Add the parent directory of 'starklu' to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def city_count(sal_data):
    city_dict = {}
    for location in sal_data.keys():
        if sal_data.get(location).get('gcc')[1] != 'r':
            city_dict[location] = sal_data.get(location).get('gcc')
    return city_dict



