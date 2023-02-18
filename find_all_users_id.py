from read_data import read_data

def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    users_id = []
    for user in data["messages"]:
        
        if "actor_id" in user:
            a = user["actor_id"]
            if a not in users_id and a.startswith("user"):
                users_id.append(a)
        elif "from_id" in user:
            a = user["from_id"]
            if a not in users_id and a.startswith("user"):
                users_id.append(a) 
                
    return users_id

data = read_data('data/result.json')
print(find_all_users_id(data))