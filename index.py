import datetime
import json
import logging
from google.appengine.api import urlfetch

import FlaskDeferredHandler
from flask import Flask, render_template, jsonify, redirect, request
from flask.ext.cors import CORS

app = Flask(__name__, template_folder="templates")
app.url_map.strict_slashes = False

FlaskDeferredHandler.register(app)
CORS(app)
import textwrap


def my_dedent(string):
    if string and string[0] == '\n':
        string = string[1:]
    return textwrap.dedent(string)


@app.before_request
def clear_trailing():
    rp = request.path
    if rp != '/' and rp.endswith('/'):
        return redirect(rp[:-1])

@app.route('/', methods=['GET'])
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
                    # print value
                    # print ""
                    title = value["title"].encode('ascii', 'ignore')
                    updated_at = value["firstPublishedAt"]
                    updated_at_proper = datetime.datetime.fromtimestamp(updated_at / 1000.0).strftime(
                        '%Y-%m-%d %H:%M:%S')
                    content = value["content"]
                    firstPublishedAt = value["firstPublishedAt"]
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
                        "fullLink": full_link,
                        "firstPublishedAt": firstPublishedAt
                    })
                list_to_return.sort(key=lambda e: e['firstPublishedAt'], reverse=True)
                additional_posts = len(list_to_return) < (json_result['payload']['userMeta']["numberOfPostsPublished"])
                if additional_posts:
                    additional_posts = url
                else:
                    additional_posts = False

                return render_template('blog.html', posts=list_to_return,
                                       additional={
                                           "additional": bool(additional_posts),
                                           "link": additional_posts
                                       })

        else:
            print result.status_code
    except urlfetch.Error:
        logging.exception('Caught exception fetching url')


# @app.route('/', methods=['GET'])
# def totally_home():
#     return render_template('home.html')

@app.route('/projects', methods=['GET'])
@app.route('/portfolio', methods=['GET'])
def portfolio():
    portfolio_items = [
        {
            "title": "React-Redux-Flask",
            "image": "/assets/react-redux-flask.png",
            "link": "http://github.com/dternyak/react-redux-flask",
            "description": my_dedent(
                """React-Redux-Flask is a boilerplate with a Python/Flask JWT Backend and a Javascript/React/Redux
                        Front-End
                        packaged with Material UI.
                        While I am the official maintainer and original creator,
                        React-Redux-Flask has 8 contributors, and over 1000 public forks."""
            )
        },
        {
            "title": "MoneroWallet",
            "image": "/assets/monerowallet.png",
            "link": "http://monerowallet.com",
            "description": my_dedent(
                """MoneroWallet is an AngularJS
                        based CryptoCurrency Web Wallet for storing and sending Monero. It uses
                        Firebase for its backend and Google App Engine for hosting. After generating a unique seed on the client, it is encrypted and then persisted in Firebase. 
                        After authentication,
                        the encrypted seed is retrieved and is used to rebuild the Monero Private Key. The private key is then used
                        to sign transactions which are later broadcast to the Monero Network. An
                        Android app was also built leveraging the codebase."""
            )
        },
        {
            "title": "MoneroChain",
            "image": "/assets/monerochain.png",
            "link": "http://monerochain.com",
            "description": my_dedent(
                """MoneroChain is a
                        block-explorer for the Monero Crypto Currency.
                        The app is an entirely client-side SPA, using a React/Redux stack. Data is
                        retrieved via CORS request to Nodes that have
                        implemented a compatible REST API. Additionally, the app offers a "node
                        input" tool, in which a custom node
                        can be created and selected. This allows users to specify their own node, or
                        a non-default node (which is especially useful
                        in the case of the default-node experiencing down-time)."""
            )
        },
        {
            "title": "CryptoIndex",
            "image": "/assets/cryptoindex.png",
            "link": "http://cryptoindex.com",
            "description": my_dedent(
                """CryptoIndex is a dashboard for viewing CryptoCurrency prices. It uses data from CoinMarketCap
                        retrieved via Web Scrapers and exposed via an API. The site is hosted on Google App Engine."""
            )
        }
    ]

    return render_template('projects.html', portfolio=portfolio_items)


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def page_not_found(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
