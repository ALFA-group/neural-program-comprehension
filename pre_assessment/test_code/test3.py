import requests
EMAILS_FOR_ISSUES = 'https://github.com/api/v3/users/JimmyBuffet'
resource = requests.get(EMAILS_FOR_ISSUES, auth=AUTH)
if not resource.status_code == 200:
    raise Exception(resource.status_code)

'''
type(resource.json())
<type 'dict'>

resources
{
    u'site_admin': False,  
    u'hireable': None, 
    u'id': 6048,  
    u'email': u'jbuffet@xyzxyz.com'
}
'''

for x in resources:
    user_email = x['email']
    print(user_email)