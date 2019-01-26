from user.serializers import UserSerializer


def jwt_response_payload_handler(token, user=None, request=None):
    """
    自定义jwt的返回，将用户信息与token一起返回
    """
    return {
        'token': token,
        'user': UserSerializer(user).data
    }
