import json

# data_model = {
#     "principal": {{"principal_name": {"name": "data", "surname": "data"},
#                    "principal_bio": {"dob": "data", "address": "data", "status": "data"},
#                    "contacts": {"phone_number": ["data"], "email": ["data"],
#                                 "social_nets": [{"social_net": "data"}]}}},
#     "profile_info": {"profile_summary": "data"},
#     "work_experience": [{"job_obj1": {"job_title": "data", "job_company": "data", "job_description": "data"}},
#                         {"job_obj2": {"job_title": "data", "job_company": "data", "job_description": "data"}}],
#     "skills": [{"skill1": "data"}, {"skill2": "data"}],
#     "certifications": [{"cert1": "data"}, {"cert2": "data"}],
#     "education": {"institution": "data"},
#     "interests": ["data"]
# }


dc = {"user": {"user_full_name": {"name": "Oldrich", "surname": "Rezek"},
               "user_bio": {"dob": "02051984", "nationality": "czech", "place_of_birth": "trinec",
                            "country_of-birth": "czechia", "marital_status": "single"},

               }}

print(type(dc))
print(dc["user"]["user_bio"])
