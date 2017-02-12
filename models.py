from google.appengine.ext import ndb


class BlogPost(ndb.Model):
    time = ndb.StringProperty()
    title = ndb.StringProperty()
    body = ndb.StringProperty()
    author = ndb.StringProperty()
