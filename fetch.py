
import requests

base_url = "https://www.demonslayer-api.com/api/v1/characters?"

def get_demon_slayer_info(name):
    url = f"{base_url}/demon_slayer/{name}"
    response = requests.get(url)
    print(response)    

    if response.status_code == 200:
       demon_slayer_data = response.json()
       return demon_slayer_data
    else:
        print(f"failed to retrieve data{response.status_code}")

    demon_slayer_name ="nezuko kamado"
    demon_slayer_info =get_demon_slayer_info(demon_slayer_name)

    if demon_slayer_info:
        print(f"Name: {demon_slayer_info["Name"]}")
        print(f"Id:   {demon_slayer_info["Id"]}") 
        print(f"Height:{demon_slayer_info["Height"]}")
        print(f"Weight:{demon_slayer_info["weight"]}")

