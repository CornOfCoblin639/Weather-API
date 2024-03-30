import requests 

def get_weather(city="London", units='metric', api_key='1a58e6e953db263991ef793d77acb7b3'):

    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units={units}&appid={api_key}"

    r = requests.get(url)
    content = r.json()
    print(content)
    #open text file to write, with 'a' as apphend 
    with open('data.txt', 'a') as file: 
        
    #JSON format is read as a dictionary by python, so you must access object as such. 
    #content var is saved as a list of dictionaries, so we have to iterate over the items under the 'list' list 
    #NOTE: as the weather obj returns a list when viewing the json contents, we must specificy the index of the list before parsing the json data
    #EG: weather is returned from json file as "weather": [ {**array of key/values**} ] - [] denotes list within json
        for dicty in content['list']:
            #this prints the dt_txt key value pair from the json file, under the dictionary location
            file.write(f"{dicty['dt_txt']}, {dicty['main']['temp']}, {dicty['weather'][0]['description']}\n")



    #return conten


print(get_weather())
