from telethon.sync import TelegramClient
from telethon import functions, types
import csv
import time
name= 'Jahirul Islam'
api_id = '2340381'
api_hash='af24eb2ad4b5b9e90699cf8deb6aeecb'
file_path='C://Users//HP//Desktop//telegram.csv'
with TelegramClient(name, api_id, api_hash) as client:
    result = client(functions.contacts.GetContactsRequest(
        hash=0
    ))
    print("Total contact list: ",len(result.contacts))
    start=int(input("Enter start position: "))
    end =int(input("Enter end position: "))
    length=0
    try:
        with open(file_path, 'w', encoding="uft-......", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Id", "Username", "Phone"])
            for i in range(start,len(result.contacts),1):
                length=i
                time.sleep(2*i)
                print("complete :",i) 
                id=result.contacts[i].user_id
                info=client.get_participants(id)
                writer.writerow([info[0].first_name, id, info[0].username, info[0].phone])
                if i==end:
                    break
    except:
        print(length)
    print("Exit")
