from read_data import read_data

def find_all_users_name(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    users_name = []
    for user in data["messages"]:
        
        if "actor" in user:
            a = user["actor"]
            # b = user["actor_id"]
            if a not in users_name: # and b.startswith("user"):
                users_name.append(a)
        elif "from" in user:
            a = user["from"]
            # b = user["from_id"]
            if a not in users_name and: # b.startswith("user"):
                users_name.append(a)
                
    return users_name

data = read_data('data/result.json')
# print(find_all_users_name(data))
