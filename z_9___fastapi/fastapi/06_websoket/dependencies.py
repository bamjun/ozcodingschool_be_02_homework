# 인증 관련 추가 -> 토근 기반으로 유저 네임값을 가져올 수 있도록 한다.

users = {
    1: {'username': 'test1@example.com'},
    2: {'username': 'test2@example.com'},
    3: {'username': 'test3@example.com'},
    4: {'username': 'test4@example.com'},
    5: {'username': 'test5@example.com'},
    6: {'username': 'test6@example.com'}
}


def get_username(token: str):
    # 토큰을 유저 id로 간주
    user_id = int(token)

    user = users.get(user_id)

    return user['username']