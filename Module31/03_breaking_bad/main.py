import requests
import json
from typing import Dict

if __name__ == '__main__':
    response = requests.get('https://www.breakingbadapi.com/api/episodes?series=Breaking+Bad')
    response_deaths = requests.get('https://www.breakingbadapi.com/api/deaths')


    def info_for_serial_deaths(data_serial: list, result={}) -> Dict:

        for i in range(len(data_serial)):
            if data_serial[i]['number_of_deaths'] > result.get('number_of_deaths', 0):
                result = {'episode_id': None, 'season': data_serial[i]['season'], 'episode': data_serial[i]['episode'],
                          'number_of_deaths': data_serial[i]['number_of_deaths'], 'death': data_serial[i]['death']}

        return result


    def info_for_serial(data_serial: list, result={}) -> Dict:

        for i in range(len(data_serial)):
            episode = result['episode']
            season = result['season']
            if int(data_serial[i]['season']) == season and int(data_serial[i]['episode']) == episode:
                result['episode_id'] = data_serial[i]['episode_id']

        return result


    info_depths = info_for_serial_deaths(response_deaths.json())
    info_serial = info_for_serial(response.json(), info_depths)
    print(json.dumps(info_serial, indent=4))

    with open('death_dict.json', 'w') as file:
        json.dump(info_serial, file, indent=4)
