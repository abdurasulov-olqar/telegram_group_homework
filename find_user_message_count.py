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
    massege_user: dict= {}
   
    for userId in user_id:
        # print(userId)
        massage_count: int = 0
        for user in data["messages"]:
            if user["type"] == "message" and user["from_id"] == userId:
                massage_count += 1
        massege_user.update({userId: massage_count})
    return massege_user
                

    
data = read_data('data/result.json')
user_id = find_all_users_id(data)
# print(find_user_message_count(data, user_id))
