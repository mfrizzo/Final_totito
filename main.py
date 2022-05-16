'''
Main script.
'''
import utils
import time


def main():
    
    NAME = 'Angel'
    player_id = utils.register(NAME)
    # print(player_id)


    my_turn = utils.is_my_turn(player_id)

    while not my_turn:
        print('Zzz...')
        time.sleep(3)
        my_turn = utils.is_my_turn(player_id)
        
    print("It's my turn, continue in game...")


    print(my_turn)


import requests

def register(name: str) -> str: 
    response = requests.post("http://127.0.0.1:8000/register_player/"+name)
    print(response.json())
    player_id = response.json()      # TODO: implement API call
    return player_id


if __name__ == '__main__':
    main()