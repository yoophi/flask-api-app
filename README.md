# FlaskApiApp

회원 로그인 및 API 인증 기능 및 관리자페이지를 제공하는 Flask App 을 쉽게 만들 수 있도록 합니다.

현재 Flask-Security 를 이용한 회원인증과 OAuth2.0 의 token 방식 인증을 제공합니다.

```python
from flask import jsonify

from flask_rest_app import FlaskApiApp
from flask_rest_app.core.api import api
from flask_rest_app.extensions import oauth

app = FlaskApiApp(__name__)

@api.route('/sample')
@oauth.require_oauth('email')
def handle_sample():
    return jsonify(hello='world')
    
    
app.register_core_blueprint(api=api, api_url_prefix='/api/v1.0', )

if __name__ == '__main__':
    app.run()
```

간단한 사용 예제가 `/example` 에 들어있으니 확인해보세요.

