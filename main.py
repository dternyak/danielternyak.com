# from flask import request, jsonify, Blueprint, redirect, render_template, url_for, g
# import datetime
# from models import BlogPost
# from google.appengine.api import users
# import requests
# import requests_toolbelt.adapters.appengine
# import feedparser
#
# # Use the App Engine Requests adapter. This makes sure that Requests uses
# # URLFetch.
# requests_toolbelt.adapters.appengine.monkeypatch()
#
# api = Blueprint('api', __name__, url_prefix='/api/v1')
#
#
# @api.route('/get_single_post', methods=['POST'])
# def get_single_post():
#     loaded_message = request.get_json()
#     data_id = int(loaded_message["id"])
#     qry1 = BlogPost.get_by_id(data_id, parent=None)
#     body = qry1.body
#     author = qry1.author
#     title = qry1.title
#     the_time = qry1.time
#     id = qry1.key.id()
#     dict_to_append = {"body": body, "author": author, "title": title, "time": the_time, "id": id}
#     return jsonify(data=dict_to_append)
#
#
# from google.appengine.api import urlfetch
#
# import logging
#
# import json
# import time
#
#
# @api.route('/your_posts', methods=['GET'])
# def your_posts():
#     list_to_return = []
#     url = 'http://medium.com/@sprawsmdoo/latest?format=json'
#     print "got here"
#     try:
#         result = urlfetch.fetch(url)
#         if result.status_code == 200:
#             json_result = json.loads(result.content.replace('])}while(1);</x>', ''))
#             references = json_result["payload"]["references"]
#             if not "Post" in references:
#                 print "NO POSTS!"
#             else:
#                 posts = references["Post"]
#                 if len(posts.keys()) > 10:
#                     print "more than 10, will have to paginate."
#                 for key, value in posts.iteritems():
#                     title = value["title"].encode('ascii', 'ignore')
#                     created_at = value["createdAt"]
#                     created_at_proper = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(created_at))
#                     print created_at_proper
#                     content = value["content"]
#                     subtitle = None
#                     if content:
#                         if 'subtitle' in content:
#                             subtitle = content["subtitle"]
#                     link = value["slug"] + "-" + key
#                     full_link = 'http://medium.com/@sprawsmdoo/' + link
#                     list_to_return.append({
#                         "author": "sprawsmdoo",
#                         "title": title,
#                         "createdAt": created_at_proper,
#                         "subtitle": subtitle,
#                         "fullLink": full_link
#                     })
#
#         else:
#             print result.status_code
#     except urlfetch.Error:
#         logging.exception('Caught exception fetching url')
#
#     # qry1 = BlogPost.query()  # Retrieve all Account entitites
#     # list_to_return = []
#     #
#     # for item in qry1:
#     #     body = item.body
#     #     author = item.author
#     #     title = item.title
#     #     the_time = item.time
#     #     the_real_time = datetime.datetime.strptime(the_time, '%B %d, %Y')
#     #     item_id = item.key.id()
#     #     dict_to_append = {"body": body, "author": author, "title": title, "time": the_real_time, "id": item_id}
#     #     list_to_return.append(dict_to_append)
#     #
#     # list_to_return.sort(key=lambda r: r["time"])
#     #
#     # list_to_return.reverse()
#
#     return jsonify(data=list_to_return)
#
#
# @api.route('/create_post', methods=["POST", "GET"])
# def make_post():
#     loaded_message = request.get_json()
#
#     body = loaded_message["body"]
#     title = loaded_message["title"]
#
#     the_time = datetime.datetime.now()
#     fixed_time = the_time.strftime("%B %d, %Y")
#     author = "DTernyak@gmail.com"
#
#     insert_payload = BlogPost(
#         time=fixed_time,
#         body=body,
#         title=title,
#         author=author,
#     )
#
#     insert_payload.put()
#     return jsonify(success=True)
#
#
# @api.route('/login')
# def login():
#     login_url = users.create_login_url('/#/editor')
#     return redirect(login_url)
#
#
# @api.route('/is_admin')
# def is_admin():
#     return jsonify(result=True)
