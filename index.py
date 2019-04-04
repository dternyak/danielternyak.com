import datetime
import json
import logging
import textwrap

from flask import Flask, render_template, redirect, request
from google.appengine.api import urlfetch

app = Flask(__name__, template_folder="templates")
app.url_map.strict_slashes = False


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
def home():
    projects = [

        {
            "title": "MoneroChain",
            "link": "http://monerochain.com",
            "description": my_dedent(
                """A blockchain explorer for the Monero cryptocurrency."""
            )
        },
        {
            "title": "react-redux-flask",
            "link": "http://github.com/dternyak/react-redux-flask",
            "description": my_dedent(
                """Full-stack seed that helped to ramp up more than 10,000 projects."""
            )
        },
        # {
        #     "title": "MoneroWallet",
        #     "link": "http://monerowallet.com",
        #     "description": my_dedent(
        #         """A wallet for the Monero cryptocurrency (who'da guessed)."""
        #     )
        # },
        {
            "title": "eth-priv-to-addr",
            "link": "https://github.com/dternyak/eth-priv-to-addr",
            "description": my_dedent(
                """A dead-simple docker utility for converting Ethereum private keys to addresses."""
            )
        }
    ]
    additional_posts, articles = get_articles()

    return render_template('index.html',
                           articles=articles,
                           projects=projects,
                           additional={
                               "additional": bool(additional_posts),
                               "link": additional_posts
                           })


def get_articles():
    additional_posts = False
    articles = []
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
                    articles.append({
                        "author": "dternyak",
                        "title": title,
                        "updatedAt": updated_at_proper,
                        "subtitle": subtitle,
                        "link": full_link,
                        "firstPublishedAt": firstPublishedAt
                    })
                articles.sort(key=lambda e: e['firstPublishedAt'], reverse=True)
                for each in articles:
                    each["firstPublishedAt"] = datetime.datetime.utcfromtimestamp(
                        each["firstPublishedAt"] / 1000).strftime('%B %-d, %Y')
                additional_posts = len(articles) < (json_result['payload']['userMeta']["numberOfPostsPublished"])
                if additional_posts:
                    additional_posts = url


        else:
            print result.status_code
    except urlfetch.Error:
        logging.exception('Caught exception fetching url')

    return additional_posts, articles


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def page_not_found(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
