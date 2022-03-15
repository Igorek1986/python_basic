import requests
import json
from typing import Dict

if __name__ == '__main__':
    response = requests.get('https://www.breakingbadapi.com/api/episodes?series=Breaking+Bad')
    response_deaths = requests.get('https://www.breakingbadapi.com/api/deaths')


    def info_for_serial_deaths(data_serial: list) -> Dict:
        result = max(data_serial, key=lambda x: x['number_of_deaths'])
        result = {'episode_id': None, 'season': result['season'], 'episode': result['episode'],
                  'number_of_deaths': result['number_of_deaths'], 'death': result['death']}

        return result


    def info_for_serial(data_serial: list, result={}) -> Dict:

        for i, v in enumerate(data_serial):
            episode = result['episode']
            season = result['season']
            if int(v['season']) == season and int(v['episode']) == episode:
                result['episode_id'] = data_serial[i]['episode_id']

        return result


    info_depths = info_for_serial_deaths(response_deaths.json())
    info_serial = info_for_serial(response.json(), info_depths)
    print(json.dumps(info_serial, indent=4))

    with open('death_dict.json', 'w') as file:
        json.dump(info_serial, file, indent=4)
