def build_profile(first, middle, last, **user_info):
    profile={}
    profile["first_name"]= first
    profile["middle_name"]= middle
    profile["last_name"]=last
    for key, value in user_info.items():
        profile[key]=value
    return profile

user_profile= build_profile("lee", "sung", "jang", location="Busan", field="computer", age=20, email="lee@gmail.com")
print(user_profile)