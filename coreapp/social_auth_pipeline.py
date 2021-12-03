from coreapp.models import Customer, Driver

# create_user_by_type
def create_user_by_type(backend, user, response, *args, **kwargs):
    request = backend.strategy.request_data()

    if backend.name == 'facebook':
        avatar = 'http://graph.facebook.com/%s/picture?type=large' % response['id']

        if request['user_type']=="driver":
            Driver.objects.get_or_create(user_id=user.id, avatar=avatar)
        elif request['user_type']=="customer":
            Customer.objects.get_or_create(user_id=user.id, avatar=avatar)
        
        

"""
Usual Facebook-like response
{
    'username': 'foobar',
    'access_token': 'CAAD...',
    'first_name': 'Foo',
    'last_name': 'Bar',
    'verified': True,
    'name': 'Foo Bar',
    'locale': 'en_US',
    'gender': 'male',
    'expires': '5183999',
    'email': 'foo@bar.com',
    'updated_time': '2014-01-14T15:58:35+0000',
    'link': 'https://www.facebook.com/foobar',
    'timezone': -3,
    'id': '100000126636010',
}
"""
