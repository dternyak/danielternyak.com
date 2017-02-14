from flask import Flask, render_template, redirect, request
import FlaskDeferredHandler
from flask.ext.cors import CORS
from google.appengine.api import urlfetch
import logging
import json
import datetime

app = Flask(__name__, template_folder="templates")
app.url_map.strict_slashes = False

FlaskDeferredHandler.register(app)
CORS(app)


@app.before_request
def clear_trailing():
    rp = request.path
    if rp != '/' and rp.endswith('/'):
        return redirect(rp[:-1])


@app.route('/blog', methods=['GET'])
def blog():
    list_to_return = []
    author = 'dternyak'
    json_url = 'http://medium.com/@{}/latest?format=json'.format(author)
    url = 'http://medium.com/@{}'.format(author)
    try:
        result = urlfetch.fetch(json_url)
        if result.status_code == 200:
            json_result = json.loads(result.content.replace('])}while(1);</x>', ''))
            references = json_result["payload"]["references"]
            if "Post" not in references:
                print "NO POSTS!"
            else:
                posts = references["Post"]
                for key, value in posts.iteritems():
                    title = value["title"].encode('ascii', 'ignore')
                    updated_at = value["updatedAt"]
                    updated_at_proper = datetime.datetime.fromtimestamp(updated_at / 1000.0).strftime(
                        '%Y-%m-%d %H:%M:%S')
                    content = value["content"]
                    subtitle = None
                    if content:
                        if 'subtitle' in content:
                            subtitle = content["subtitle"]
                    link = value["slug"] + "-" + key
                    full_link = 'http://medium.com/@dternyak/' + link
                    list_to_return.append({
                        "author": "dternyak",
                        "title": title,
                        "updatedAt": updated_at_proper,
                        "subtitle": subtitle,
                        "fullLink": full_link
                    })
                list_to_return.sort(key=lambda e: e['updatedAt'], reverse=True)
                additional_posts = len(list_to_return) < (json_result['payload']['userMeta']["numberOfPostsPublished"])
                if additional_posts:
                    additional_posts = url
                else:
                    additional_posts = False
                print url
                return render_template('blog.html', posts=list_to_return,
                                       additional={
                                           "additional": bool(additional_posts),
                                           "link": additional_posts
                                       })

        else:
            print result.status_code
    except urlfetch.Error:
        logging.exception('Caught exception fetching url')


@app.route('/', methods=['GET'])
def totally_home():
    return render_template('home.html')


@app.route('/portfolio', methods=['GET'])
def portfolio():
    return render_template('portfolio.html')


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def page_not_found(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
