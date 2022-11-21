import json
from pprint import pprint

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


user_data = {"user_info": {"user_full_name": {"name": "Oldrich", "surname": "Rezek"},
                           "user_bio": {"dob": "02051984", "age": "38", "nationality": "czech",
                                        "place_of_birth": "trinec",
                                        "country": "czechia", "marital_status": "single"},
                           "user_address": {"street": "quai au foin", "house_no": "41", "city": "brussels",
                                            "postal_code": "1000",
                                            "country": "belgium"},
                           "user_contacts": {"email": "orezek@seznam.cz", "phone_no": "+420608840502",
                                             "linkedin": "data", "github": "data"}},
             "profile_info": {"profile_summary": "data"},
             "work_experience": {"job_obj1": {"job_title": "data", "job_company": "data", "job_description": "data"}},
             "skills": {"skill": "data", "skill1": "data"},
             "certification": {"cert1": "data", "cert2": "data"},
             "education": {"institution": "data"},
             "interests": ["data"]
             }

print(type(user_data))
print(user_data["work_experience"]["job_obj1"])
