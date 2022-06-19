import requests
import functools
ACCESS_TOKEN = "81d0ae3a81d0ae3a81d0ae3a6e81ab8c9c881d081d0ae3ae02b4832b856547e8cf80a6c"
def compare_function(person_a, person_b):
    if person_a[1]==person_b[1]:
        return person_a[0]-person_b[0]
    else:
        return person_b[1]-person_a[1]

def calc_age(uid):
    user_id=requests.get("https://api.vk.com/method/users.get?v=5.81&access_token="+ACCESS_TOKEN+"&user_ids="+uid).json().get("response")[0].get("id")
    friends=requests.get("https://api.vk.com/method/friends.get?v=5.81&access_token="+ACCESS_TOKEN+"&user_id="+str(user_id)+"&fields=bdate").json().get("response").get("items")
    dict_friends={}
    for i in friends:
        if(type(i.get("bdate"))==str):
            year=i.get("bdate")[-4::1]
            if "." not in year:
                dict_friends.setdefault(2022-int(year),0)
                dict_friends[2022-int(year)]+=1
    list_of_friend = list(dict_friends.items())
    list_of_friend.sort(key=functools.cmp_to_key(compare_function))
    return list_of_friend

if __name__ == '__main__':
    res = calc_age("id231416999")
    print(res)
