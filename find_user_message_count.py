from read_data import read_data
from find_all_users_id import find_all_users_id

def find_user_message_count(data: dict, users_id: str)->dict:
    """
    This function will find the user's message count.
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
        user_id (list): User id of the user
    Returns:
        dict: Number of messages of the users
    """
    users_id = []
    for user in data["messages"]:
        
        if "from_id" in user:
            a = user["from_id"]
            if a not in users_id:
                users_id.append(a)
    # print(users_id) 
                
    massege_user: dict= {}
   
    for userId in users_id:
        # print(userId)
        massage_count: int = 0
        for user in data["messages"]:
            if user["type"] == "message" and user["from_id"] == userId:
                massage_count += 1
        if massage_count != 0:
            massege_user.update({userId: massage_count})
    return massege_user
                

    
data = read_data('data/result.json')
user_id = find_all_users_id(data)
# print(find_user_message_count(data, user_id))
