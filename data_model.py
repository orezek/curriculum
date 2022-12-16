import json
from pprint import pprint

# PAGE DATA and METADATA
# headers - metadata
website_metadata = {"contacts": "Contacts", "skills": "Skills", "certifications": "Certifications",
                    "education": "Education", "interests": "Interests", "profile_summary": "Profile Summary",
                    "work_experience": "Work Experience", "linkedin": "LinkedIn", "github": "Github",
                    "about_me": "About Me", "page_title": "Rezek Oldrich CV"}

# info about the page as a project
footer_about_info = """The page is made up of standard HTML, CSS, some Javascript 
code. However, it is a Flask application and runs fully on AWS Elastic Beansltalk. The components used are; simple 
EC2 instance along with ELB in front of it, DynamoDB as its backend, S3 for media storage, Route53 for DNS and domain 
name registration. I am also utilising AWS CodePipeline to automate deployment when the repo in GitHub gets updated. """

footer_data = {"footer_about_info": footer_about_info}

# text for the navbar
aws_logo_link = "https://d0.awsstatic.com/logos/powered-by-aws-white.png"
aws_link = "https://aws.amazon.com/what-is-cloud-computing"
navbar_metadata = {"aws_logo": aws_logo_link, "aws_link": aws_link}

# USER DATA SECTION

personal_mini_header = "Cloud Engineer, Developer and Technology Enthusiast"

# interests section
interests = ["Technology",
             "Blockchain",
             "Finance",
             "Sport",
             "Photography",
             "History",
             "Philosophy",
             "Travelling",
             "Exploring"]

# skills section along with competency score
skills = {"AWS Cloud": 80,
          "Windows Server": 82,
          "MS Sharepoint": 60,
          "Networking": 75,
          "Linux": 45,
          "VM Ware": 70,
          "Veeam": 60,
          "Python": 50,
          "HTML": 55,
          "Problem Solving": 90, }

# job titles
job_titles = {"sys_admin": "System Administrator", "it_man": "IT Manager", "net_admin": "Network Administrator"}

# profile_summary_and_basic_info
profile_summary_data_prod = """I have been in the IT industry for more than a decade and I have spent time in various 
roles. I started in a support role back in 2008 and progressively moved on to more technically advanced roles before 
eventually landing in a more managerial position. Over the years, I have acquired "industry standard" skills as I 
have been exposed to various products from industry household names and infrastructure environments, such as VMware, 
Veeam, Microsoft, Cisco, Aruba, Ubiquity, Ruckus, Oracle, and other software or hardware products. However, 
as technology and the approach to IT are evolving, so is my current interest. I have lately been focused on cloud 
technologies and the modern DevOps and SysOps approach to the IT discipline, particularly with AWS offerings. I am 
aware that the current trend in IT operations is moving quickly towards automation, and therefore knowing how to work 
with code is a necessity. Serverless, containers, cloud, CI/CD, and git are not foreign buzzwords to me. That being 
said, during the last 5 years, I was fortunate to work and live in interesting places and experience firsthand what 
others might read about in adventure books. On the less bright side, I have been absent from real-life exposure to 
the DevOps and SysOps world as I was in environments that embraced the "older way of doing" IT. In order to keep my 
career in touch with current trends and ensure that I have some minimal knowledge, I have recently passed a number of 
cloud certifications and am working on a few more to solidify my skill set. Recently, I have returned to the EU and I 
am looking for an opportunity to work on an interesting project, either in a full-time position or as a freelancer. 
The ideal situation, which I am most interested in, is a company that has already embraced or is in the process of 
moving towards cloud, automation, DevOps, and SysOps operations and creates an interesting product that I can 
associate with."""

# profile summary and basic info
profile_summary_data_prod_v0 = """I have been in the IT industry for more than a decade and I had spent time in various 
roles. I started in a support role back in 2008 and progressively moved on to more technically advanced roles and 
subsequently landing into more managerial position. During the years, I have acquired “industry standard” skills as I 
was exposed to various products from the industry household names and infrastructure environments. <kbd>VM 
Ware</kbd>, <kbd>Veeam</kbd>, <kbd>Microsoft</kbd>, <kbd>Cisco</kbd>, <kbd>Aruba</kbd>, <kbd>Ubiquity</kbd>, 
<kbd>Ruckus</kbd>, <kbd>Oracle</kbd> and other software or hardware products to name a few. However, as technology 
and approach to the IT is evolving so is my current interest. I have lately been focused on cloud technologies and 
modern <kbd>DevOps</kbd> and <kbd>SysOps</kbd> approach to the IT discipline, especially from the <kbd>AWS</kbd> 
offerings. I am aware that the current trend in IT operations is moving fast into automation and therefore knowing 
how to work with a code is a necessity. <kbd>Serverless</kbd>, <kbd>containers</kbd>, <kbd>cloud</kbd>, 
<kbd>CI/CD</kbd> and <kbd>git</kbd> are not foreign buzzwords for me. Having said that, during the last 5 years, 
I was fortunate to had worked and lived in interesting places and experience firsthand what others might read in 
adventure books. On the less bright side, I have been absent from real-life exposure into the <kbd>DevOps</kbd> and 
<kbd>SysOps</kbd> world as I was in environments that embraced the "older way of doing” IT. In order to keep my 
career in touch with the current trends and ensure that I have some minimal knowledge, I have recently passed, 
number of cloud certifications and working on few more to solidify my skill set. Recently I have returned to the EU 
and I am looking for an opportunity to work on an interesting project either in a full-time position or as a 
freelancer. The ideal, that I am most interested in, is a company that already have embraced or is in the process of 
moving into cloud, automation, DevOps and SysOps operations and creates an interesting product that I can associate 
with. """

profile_summary_data_v1 = """I am an experienced system and network administrator who is passionate about technology in 
general. The last several years I have been living and working abroad. Either managing a whole IT department or 
ensuring servers and networks are running smoothly and users/clients are happy. I am currently living in Brussels, 
Belgium and planning to relocate back to Czech or Slovak republic during the springtime. My recent focus and aim is 
to find an employment in cloud-oriented company where I can further develop my skills, knowledge and gain experience 
in participating in related projects. Recently, I have been working on to validate my skills by taking several AWS 
certifications exams to increase my chances to land on a cloud related job. My future employer should be or have 
exposition into cloud technologies preferably in AWS cloud offerings. I am open to work both as a freelancer or as a 
full-time employee."""

profile_summary_data_v2 = """I have been in the IT industry for more than a decade and I had spent time in various 
roles. I started in a support role back in 2008 and progressively moved on to more technically advanced roles and 
subsequently landing into more managerial position. I am an experienced system and network administrator who is 
passionate about technology in general. During the years, I have acquired “industry standard” skills as I was exposed 
to various products from the industry household names and infrastructure environments. For example, VM Ware, Veeam, 
Microsoft & Linux, Cisco, Aruba Ubiquity, Ruckus, Oracle and other software or hardware products to name a few. 
However, as technology and approach to the IT in general is evolving so is my current interest. I have been lately 
personally focused on cloud technologies and modern DevOps and SysOps approach to the discipline, especially from the 
AWS offerings. I am aware that the current trends in IT operations are moving fast into the cloud, automation and as 
the consequence for an individual in the industry, knowing how to handle a code in a repository or write a script is 
a necessity. Serverless, containers, CI/CD and IaC is present and the future. In the last 5 years, I was fortunate to 
had worked and lived in interesting places and experience firsthand what others might read in adventure books. On the 
less bright side, I missed the real-life exposure into the DevOps and SysOps world as I was in environments that 
embraced the older way of “doing” IT. To keep my career in touch with the current trends and ensure that I have some 
minimal knowledge, I have recently passed number of cloud certifications and working on few more to solidify my skill 
set. In June 2022, I returned back to the EU and I am looking for an opportunity to work on an interesting project 
either in a full-time position or in a freelance role. The ideal that I am most interested in is a company that have 
already embraced or is in the process of moving into the cloud, DevOps and SysOps world and creates an interesting 
product. """

soitron_job_description_data = """Maintaining and supporting IT infrastructure along with other office hardware and fleet of 
client computers across several offices in Brussels Belgium. I am part of a two-man team that is hired to completely 
outsource IT operations for a large international customer. We provide complete service from areas such as 
consultancy, server and network management and extensive client support."""

zuri_job_description_data_v1 = """I was responsible for managing the IT department of a luxurious hotel in Zanzibar, 
Tanzania. My main duties were to ensure smooth 24/7 IT operations for both internal and external customers, 
with a strong emphasis on maintaining a tight budget, especially during the pandemic. I led a small team of local 
personnel and we performed most tasks with excellent results. Due to the nature of the place, 24/7 attention, 
high speed, and quality in execution were expected at all times. The workload was very varied and rich. I was 
expected to handle tasks ranging from financial planning, hiring, and attendance to negotiating with vendors, 
communicating with government agencies, sourcing and purchasing hardware, and completely managing the campus-like 
server, network, and application infrastructure. The property was 14 acres in size, with around 220 active access 
points, over 11km of optical cabling, and over 350 employees, or over 100 high-profile paying clients, just to give 
you an idea. I am happy to provide references upon request."""

zuri_job_description_data = """I was in charge of managing the IT department at a luxurious hotel located in 
Zanzibar, Tanzania. My primary responsibilities included ensuring that the IT operations ran smoothly around the 
clock for both internal and external customers, with a particular focus on sticking to a strict budget during the 
pandemic. I led a small team of local staff and together, we achieved excellent results in our tasks. Given the 
nature of the hotel, it was essential to maintain constant vigilance and to execute tasks with a high level of speed 
and quality. The job was quite varied and required me to handle a range of duties, such as financial planning, 
hiring, negotiations with vendors, communication with government agencies, sourcing and purchasing hardware, 
and overseeing the server, network, and application infrastructure of the property, which covered 14 acres and had 
around 220 active access points, over 11km of optical cabling, and more than 350 employees or 100 high-profile paying 
clients. I am happy to provide references upon request."""

velaa_job_description_data_v1 = """I maintained and supported a large network, server infrastructure, applications, 
and end-client devices on a secluded private island in the Maldives for top 1% net worth individuals. It was a very 
demanding working environment with various tasks and projects that usually required fast resolution times. I am happy 
to provide references upon request."""

velaa_job_description_data = """I was responsible for maintaining and supporting the large network, 
server infrastructure, applications, and end-client devices on a secluded private island in the Maldives, 
which was used by top 1% net worth individuals. The environment was extremely demanding, requiring me to handle a 
wide range of tasks and projects with fast resolution times. These duties included monitoring and managing the 
network and server infrastructure, troubleshooting and resolving issues with applications and end-client devices, 
implementing security measures to protect against cyber threats, and collaborating with team members to ensure the 
smooth operation of the IT systems. Despite the challenges, I was able to consistently deliver high-quality work and 
meet the expectations of our clients. If you require further information about my experience and skills, I am happy 
to provide references upon request."""

olympus_job_description_data_v1 = """Responsible for maintaining Microsoft Sharepoint 2013 and 2016 server farm and 
building business applications and workflows for internal clients."""

olympus_job_description_data = """I was responsible for maintaining a Microsoft Sharepoint 2013 and 2016 server farm 
and building business applications and workflows for internal clients using Nintex workflow software. This position 
required me to have a strong understanding of Sharepoint and the ability to troubleshoot and resolve issues as they 
arose. I worked closely with the internal IT team and our clients to ensure that the server farm was running 
efficiently and that the business applications and workflows, developed using Nintex software, were meeting the needs 
of the organization. In addition to my technical responsibilities, I also contributed to the development of policies 
and procedures related to Sharepoint and participated in regular training and professional development activities to 
stay up-to-date on the latest technology trends and best practices in the field. Overall, my experience at Olympus 
helped me to build valuable skills in system administration and further my career in the IT industry. """

# links to social media and aws certifications
linkedin_link = "https://www.linkedin.com/in/oldrich-rezek-175503229/"
github_link = "https://github.com/orezek/curriculum"

aws_dev_link = "https://www.credly.com/badges/56210d28-1b2e-4835-acbd-a71978577fb9/public_url"
aws_arch_link = "https://www.credly.com/badges/e247032c-7f99-45a1-84b4-0a0760de2808/public_url"
aws_fond_link = "https://www.credly.com/badges/9c64e8d6-4632-41b6-aa12-29c521802fb6/public_url"

user_data = {"user_info": {"user_full_name": {"name": "Oldrich", "surname": "Rezek"},
                           "user_bio": {"dob": "02051984", "age": "38", "nationality": "czech",
                                        "place_of_birth": "trinec",
                                        "country": "czechia", "marital_status": "single"},
                           "user_address": {"street": "quai au foin", "house_no": "41", "city": "brussels",
                                            "postal_code": "1000",
                                            "country": "belgium"},
                           "user_contacts": {"email": "orezek@seznam.cz", "phone_no_cz": "+420 608 840 502",
                                             "phone_no_be": "+320 497 127 267",
                                             "linkedin": linkedin_link, "github": github_link}},
             "user_miscellaneous": {"languages": {"czech": "Czech", "english": "English"},
                                    "whoami": personal_mini_header,
                                    "greeting": "Hey, I'm"},
             "profile_info": {"profile_summary": profile_summary_data_prod},
             "work_experience": {"soitron": {"job_title": job_titles["sys_admin"],
                                             "job_company": "Soitron s.r.o - Brussels, Belgium - June 2022 - present",
                                             "job_description": soitron_job_description_data},
                                 "zuri": {"job_title": job_titles["it_man"],
                                          "job_company": "Zuri Zanzibar hotel and resort - Zanzibar - June 2019 - May "
                                                         "2022", "job_description": zuri_job_description_data},
                                 "velaa": {"job_title": job_titles["net_admin"],
                                           "job_company": "Velaa Private Island - Maldives - October 2018 - May 2019",
                                           "job_description": velaa_job_description_data},
                                 "olympus": {"job_title": job_titles["sys_admin"],
                                             "job_company": "Olympus sro - Prague Czech "
                                                            "Republic - April 2016 - "
                                                            "September 2018",
                                             "job_description": olympus_job_description_data}},
             "skills": skills,
             "certification": {"aws_dev": aws_dev_link, "aws_arch": aws_arch_link, "aws_fond": aws_fond_link},
             "education": {"institution": "Technical colleague Kolin, Czech Republic",
                           "field": "Mechanical engineering"},
             "interests": interests
             }
