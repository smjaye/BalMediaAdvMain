import datetime

from faker import Faker
fake = Faker(locale='en_CA')


#____________________Balle Media Funnel DATA PARAMETERS________________________________________
adv = 'Balle Media'
bmfunnel_url = 'https://seomarketingvancouverbc.ca/physiotherapy/get-started/?source_id=FB'


first_name = fake.first_name()
last_name = fake.last_name()
phone_number = fake.phone_number()
email = fake.email()
website = fake.domain_name()
area = fake.province_abbr()
subject = fake.sentence(10)
text = fake.text()
revenue = 20000
# problem = 'Continuous inflow of Patients'
# obstacle = 'Marketing Strategy'
start = 'In about a month'
subject1 = fake.sentence(nb_words=30)