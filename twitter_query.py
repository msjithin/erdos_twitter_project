import requests
import os
import json
from config import twitter_key as tk
# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = tk.BEARER_TOKEN

search_url = "https://api.twitter.com/2/tweets/search/recent"

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
query_params = {'query': '#memestocks', 'tweet.fields': 'author_id,created_at,public_metrics,source' ,'expansions' :'author_id', 'user.fields':'name,public_metrics', 'max_results' : 10 }
# check this for details 
# https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "twitter_data_app"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    json_response = connect_to_endpoint(search_url, query_params)
    #print(json.dumps(json_response, indent=4, sort_keys=True))
    with open('memestocks.json', 'w') as outfile:
        json.dump(json_response, outfile, indent=4, sort_keys=True)

if __name__ == "__main__":
    main()