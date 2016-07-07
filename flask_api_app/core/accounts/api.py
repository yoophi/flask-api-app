#
# @api.route('/users/self')
# @oauth.require_oauth('email')
# def users_self():
#     """
#     현재 사용자의 정보 가져오기
#     ---
#     tags:
#       - Users
#       - 사용자
#       - 진행중
#     parameters: []
#     responses:
#       '200':
#         description: successful operation
#         schema:
#           $ref: '#/definitions/User'
#     security:
#       - oauth:
#           - email
#     """
#
#     user = request.oauth.user
#
#     return api_response(user_schema.dump(user).data)