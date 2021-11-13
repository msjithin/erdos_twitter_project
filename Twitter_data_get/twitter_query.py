"""
This set up gives full-archive Tweet search
"""

import requests
import json
from twitter_api import bearer_oauth

search_url = "https://api.twitter.com/2/tweets/search/all"
# check the following for details
#  https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-all

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    # Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
    # expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
    query_params = {'query': 'snp500 lang:en', 
                    'tweet.fields': 'author_id,created_at,public_metrics,source',
                    'expansions' :'author_id', 
                    'user.fields':'name,public_metrics', 
                    'max_results' : 10 ,
                    'start_time': '2019-01-01T00:00:00Z',
                    }  # max allowed is 100
    # json_response = connect_to_endpoint(search_url, query_params)
    # print(json.dumps(json_response, indent=4, sort_keys=True))
    # with open('finance.json', 'w', encoding="utf-8") as outfile:
    #     json.dump(json_response, outfile, indent=4, sort_keys=True)


    json_response = connect_to_endpoint(search_url, params=query_params)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
