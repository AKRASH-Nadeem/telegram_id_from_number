from pyrogram import Client
from pyrogram.types import InputPhoneContact
import asyncio
from config import session_string


async def main():
    app = Client("my_account", session_string=session_string)
    await app.start()
    contacts_to_import = [InputPhoneContact(number, str(count)) for count,number in enumerate(numbers_list,0)]
    contacts = await app.import_contacts(contacts_to_import)
    # users = await app.get_users(numbers_list)

    # print(contacts.users)
    with open("info.txt","a") as f:
        for us in contacts.users:
            if us.username:
                info = str(us.phone) + " : " + str(us.username)
                print(info)
                f.write(info + "\n")
            else:
                print(str(us.phone) + " : don't have username")
            await app.delete_contacts(us.id)
    # print(contacts)
    


if __name__ == "__main__":
    if session_string == "":
        print("No account added yet")
        exit()
    try:
        with open("numbers.txt","r") as f:
            numbers_list = f.read().split("\n")
        asyncio.run(main())
    except FileNotFoundError as error:
        print("[_] Error: File not Found")
    
