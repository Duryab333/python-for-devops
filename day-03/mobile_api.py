import requests
import json

def save_data_in_file(data, file_name):
    with open(file_name,"w") as f:
        #json.dump(data,f)
        for key in data:
            f.write( "\n" + repr(key))
    print("Successfully saved in file")

def api_data(api_url):
    headers = {"content-type": "application/json"}
    try: 
        response = requests.get(url=api_url , headers=headers)
        mobile_data= response.json()
    except Exception as e:
        print(f"API Data is not accessable due to {e}")
    return mobile_data

def show_info(mobile_data):
    for mobile in mobile_data:
        print(f"\nMobile Name : {mobile['name']}   ")
        #print(type(mobile['data']))
        if mobile['data'] is None:
            print("No additional Informaion Found")
        else:
            for key, val in  mobile['data'].items():
                print(f"{key}: {val}")


if __name__=="__main__":
    api_url = "https://api.restful-api.dev/objects"
    data = api_data(api_url)
    show_info(data)
    save_data_in_file(data,"file.txt")
