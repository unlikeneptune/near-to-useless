import json

def compare_followers_following():
    with open('followers_1.json', 'r', encoding='utf-8') as f:
        followers_data = json.load(f)
    
    with open('following.json', 'r', encoding='utf-8') as f:
        following_data = json.load(f)
    
    followers = set()
    for follower in followers_data: 
        if 'string_list_data' in follower and len(follower['string_list_data']) > 0:
            username = follower['string_list_data'][0].get('value', '')
            if username:
                followers.add(username)
    
    following = set()
    if isinstance(following_data, list):
        following_list = following_data
    else:
        following_list = following_data.get('relationships_following', [])
    
    for followed in following_list:
        if 'string_list_data' in followed and len(followed['string_list_data']) > 0:
            username = followed['string_list_data'][0].get('value', '')
            if username:
                following.add(username)
    
    not_following_back = following - followers
    
    print(f"Followers: {len(followers)}")
    print(f"Following: {len(following)}")
    print(f"Don't follow back: {len(not_following_back)}")
    
    print("\nAccounts that don't follow you back:")
    for username in sorted(not_following_back):
        print(f"- {username}")

if __name__ == "__main__":
    compare_followers_following()
