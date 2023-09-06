# # messenger_integration/controllers.py

# from odoo import http
# from odoo.http import request , Response
# import json
# from odoo.exceptions import UserError
# import os,sys
# import logging
# _logger = logging.getLogger(__name__)
# verify_token = 'hello'

# class MessengerIntegrationController(http.Controller):

#     # @http.route('/', type='http', auth='public', website=True, csrf=False)
#     # @http.route('/messenger_integration', type='http', auth='public',methods=['GET'], website=True, csrf=False)
#     @http.route('/messenger_integration', type='http', auth='public', website=True, csrf=False)
#     def verify(self, **kw):
#         # # webhook verification
#         # if kwargs.get("hub.mode") == "subscribe" and kwargs.get("hub.challenge"):
#         #     if not kwargs.get("hub.verify_token") == "hello":
#         #         return "Verification token mismatch", 403
#         #     return kwargs["hub.challenge"], 200
#         # return "Hello World", 200
#         # # response_data = {"message": "Hello World"}

#         # # return http.Response(json.dumps(response_data), status=200, content_type='application/json')
#         # Parse the query params
#         mode = kw.get('hub.mode')
#         token = kw.get('hub.verify_token')
#         challenge = kw.get('hub.challenge')
#         # raise UserError(token)
#         # _logger.info(str(kw.get('hub.verify_token')))
#         # Replace 'config.verifyToken' with your actual verify token value
#         verify_token = 'hello'

#         # Check if a token and mode is in the query string of the request
#         if mode and token:
#             # Check the mode and token sent is correct
#             if mode == 'subscribe' and token == verify_token:
#                 # Respond with the challenge token from the request
#                 print("WEBHOOK_VERIFIED")
#                 return Response(challenge, status=200)
#             else:
#                 # Respond with '403 Forbidden' if verify tokens do not match
#                 return Response('Forbidden', status=403)
#         else:
#             # Respond with '400 Bad Request' if mode or token is missing
#             return Response('Bad Request', status=400)



#     # @http.route('/', type='json', auth='public', methods=['POST'], csrf=False)
#     # @http.route('/messenger_integration', type='json', auth='public', methods=['POST'], csrf=False)
#     @http.route('/messenger_integration', type='json', auth='public', methods=['POST'], csrf=False)
#     def webhook(self, **kwargs):
#         # data = json.loads(request.httprequest.data)
        
#         # self.log(data)
#         # return Response('Ok', status=200)
#         # data = request.httprequest.data
#         data = request.httprequest.data
#         body = json.loads(data.decode('utf-8'))
#         if 'object' in body and body['object'] == 'page':
#             entries = body['entry']
#             for entry in entries:
#                 webhookEvent = entry['messaging'][0]
#                 print(webhookEvent)
#                 senderPsid = webhookEvent['sender']['id']
#                 print('sender PSID: {}'.format(senderPsid))
#                 if 'message' in webhookEvent:
#                     # raise UserError(str(webhookEvent))
#                     _logger.info(str(webhookEvent))
#                     # _logger.info(str(webhookEvent['message']))
#                     # _logger.info(str(webhookEvent['sender']))
#                     # handleMessage(senderPsid, webhookEvent['message'])
#                     # profile_url = f"https://graph.facebook.com/{senderPsid}?fields=first_name,last_name,profile_pic,gender,locale,email,phone&access_token={verify_token}"
#                     # profile_response = kwargs.get(profile_url)
                    
#                     # # profile_response = request.httprequest.data(profile_url)
#                     # profile_data = profile_response.json()
#                     # _logger.info(str(profile_data))

#                     # # Extract sender's information
#                     # sender_name = profile_data.get('first_name', '') + ' ' + profile_data.get('last_name', '')
#                     # sender_email = profile_data.get('email', '')
#                     # sender_phone = profile_data.get('phone', '')
#                     # return request.make_response(webhookEvent)
#                 return Response('Ok', status=200)
#         else:
#             return Response('Error', status=404)
#         # _logger.info(f"Raw Request Data: {data}")
#         # return Response('Ok', status=200)

#     def log(self, message):
#         # raise UserError(str(message))
#         _logger.info(str(message))
#         sys.stdout.flush()


from odoo import http
from odoo.http import request
from werkzeug.wrappers import Response
import json
import logging, requests
_logger = logging.getLogger(__name__)


class WebhookController(http.Controller):

    @http.route('/webhook', type='http', auth='public', methods=['GET'], csrf=False)
    def handle_webhook(self, **post):
        print("Get")
        # Handle the webhook verification
        verify_token = post.get('hub.verify_token')
        # return Response(verify_token, content_type='text/plain', status=200)
        # _logger.info(str(webhookEvent))
        # return Response(post.get('hub.verify_token'), content_type='text/plain', status=200)
        hub_challenge = post.get('hub.challenge')
        _logger.info(str(hub_challenge))
        if verify_token == 'hello':
        # if verify_token == verify_token:
            return Response(hub_challenge, content_type='text/plain', status=200)
        
        else:
            return Response("Invalid verify token", content_type='text/plain', status=403)
            
    @http.route('/webhook', type='http', auth='public', methods=['POST'], csrf=False)
    def webhook(self, **kwargs):
        print('Post')
        data = request.httprequest.data
        body = data.decode('utf-8')
        new = eval(body)
        # _logger.info(str(eval(body)))
        # _logger.info(str(new))
        # print(body)
        # body = json.loads(data.decode('utf-8'))
        # if 'object' in body and body['object'] == 'page':
        if 'object' in new and new['object'] == 'page':
            entries = new['entry']
            for entry in entries:
                webhookEvent = entry['messaging'][0]
                # return str(webhookEvent)
                # return request.make_response(webhookEvent)
                senderPsid = webhookEvent['sender']['id']
                # print('sender PSID: {}'.format(senderPsid))
                if 'message' in webhookEvent:
                    # return Response(webhookEvent, status=200)

                    _logger.info(str(webhookEvent))
                    url = "https://graph.facebook.com/{}?fields=id,name,email,picture&access_token={}".format(senderPsid, "EAA0GF4cZCxPkBOwDZBDm92wHtUCgVVuXYTM6NbtkXMzEeQ5wyzeEqhCGsMdeqSeoDjDAH07GZBkWSoCBKPqTZBr6XEbcPb04Lrr4KkbHafeC7rzhqMiZCIKHG0fYSyU6XZA3jgMsQNOqJlu4dm5O9RN3R9qsT009oZAE3yeXu6svFVfOJMmG7bAH5kZCMU2FqGve")
                    profile_data = requests.get(url)
                    sender_data = profile_data.json()
                    _logger.info(str(sender_data))

                    # _logger.info(str(webhookEvent['message']))
                    # _logger.info(str(webhookEvent['sender']))
                    # handleMessage(senderPsid, webhookEvent['message'])
                # return Response('Ok', status=200)

                return Response(webhookEvent, status=200)
        else:
            return Response('Error', status=404)
