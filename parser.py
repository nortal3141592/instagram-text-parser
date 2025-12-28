with open("sample_large.txt",encoding='utf-8') as f:
    data = f.read()

def kconvert(string):
    if ("K" in string):
        num = float(string.replace("K",""))
        return int(num*1000)
    elif("M" in string):
        num = float(string.replace("M",""))
        return int(num*1000000)
    else:
        return int(string)
print(kconvert("12.5M"))

chunks = data.split("\n\n")
chunks = [c for c in chunks if len(c)>3]

def parse_chunk(chunk):
    try:
        chunk = chunk.strip()
        sep_chunk = chunk.split('\n')
        username = sep_chunk[0]
        num_of_posts = kconvert(((sep_chunk[1].split(" "))[0]).replace(",",""))
        num_of_followers = kconvert((sep_chunk[2].split(" "))[0].replace(",",""))
        num_of_following = kconvert(sep_chunk[3].split(" ")[0].replace(",",""))
        name = sep_chunk[4]
        if(len(sep_chunk)>5):
            type_of_account = sep_chunk[5]
            bio = "\n".join(sep_chunk[6:])
        else:
            type_of_account = "Unknown"
            bio = ""
    
        # print(username,num_of_followers,num_of_following,num_of_posts,name,type_of_account,bio)
    
        return {"username":username, 
                "num_of_posts":num_of_posts, 
                "num_of_followers":num_of_followers,
                "num_of_following":num_of_following,
                "name":name,
               "type_of_account":type_of_account,
               "bio":bio}
    except Exception as e:
        print(e, chunk)    

all_chunks = []
for chunk in chunks:
    parsed_chunk = parse_chunk(chunk)
    all_chunks.append(parsed_chunk)

import json
s = json.dumps(all_chunks, indent=4)


# finding and displaying user details of user with max posts
max_posts = max(all_chunks, key = lambda x:x["num_of_posts"])
print(f"The user details of the user with the maximum posts are - \n\n{max_posts}\n\n")

# finding and displaying user details of the user with max followers
max_followers = max(all_chunks, key = lambda x:x["num_of_followers"])
print(f"The user details of the user with the maximum followers are  - \n\n{max_followers}\n\n")

# finding and displaying the user details of the user with maximum following
max_following = max(all_chunks, key=lambda x:x["num_of_following"])
print(f"The user detail of the user with the maximum following are - \n\n{max_following}\n\n")

categories = set()
for chunk in all_chunks:
    categories.add(chunk["type_of_account"])

print("There are all the categories that we have - \n")
print(categories)
print(f"\nThere are {len(categories)} categories ")





