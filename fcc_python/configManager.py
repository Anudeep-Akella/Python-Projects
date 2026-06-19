"""Takes all the user settings in the form of Key-Value pairs. All the functions accept only the key-value pair tupple (key,value) for any configuration of the settings except the delete_setting()"""

def add_setting(all_settings,settings):
    """Takes the user settings and adds new setting if the setting is not present"""

    key,value = settings[0].lower(),settings[1].lower()
    if key in all_settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    all_settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"
    

def update_setting(all_settings,settings):
    """Takes user settings and updates the setting if the given setting is present"""
    
    key,value = settings[0].lower(),settings[1].lower()
    if key in all_settings:
        all_settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(all_settings,settings):
    """Takes the user setting and deletes the selected setting from the user settings"""
    
    key,value = settings[0].lowere(),settings[1].lower()
    if key in all_settings:
        del all_settings[key]
        return f"Setting '{key}' deleted successfully!"
    return "Setting not found!"


def view_settings(all_settings):
    """Function listing the user configured settings"""

    if not all_settings:
        return "No settings available"

    return "Current User Settings:\n" + "\n".join(f"{k.capitalize()}: {v}" for k,v in all_settings.items())

def main():

    test_settings = {'theme': 'dark', 'notifications': 'enabled'}
    print(update_setting(test_settings,('theme','white')))
    print(view_settings(test_settings))

if __name__ == "__main__":
    main()
