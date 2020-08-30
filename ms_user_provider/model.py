import jwt


class UserModel:
    id = 0
    username = ''
    mobile = ''
    email = ''
    name = ''
    first_name = ''
    last_name = ''


def get_user_model(token):
    data = jwt.decode(token, verify=False)
    model = UserModel()
    model.id = data['sub']
    model.username = data['preferred_username']
    if 'mobile' in data:
        model.mobile = data['mobile']
    if 'email' in data:
        model.email = data['email']
    model.name = data['name']
    model.first_name = data['given_name']
    model.last_name = data['family_name']
    return model
