# 2014.06.24 13:44:54 EDT
import os
import urllib
from google.appengine.api import users
from google.appengine.ext import ndb
import jinja2
import webapp2
JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)), extensions=['jinja2.ext.autoescape'], autoescape=True)
MAIN_PAGE_FOOTER_TEMPLATE = '    <form action="/LessonMaker?%s" method="post">\n      <div><textarea name="content" rows="3" cols="60"></textarea></div>\n      <div><input type="submit" value="Sign Lessonplan"></div>\n    </form>\n\n    <hr>\n\n    <form>Lessonplan name:\n      <input value="%s" name="lessonplan_name">\n      <input type="submit" value="switch">\n    </form>\n\n    <a href="%s">%s</a>\n\n  </body>\n</html>\n'
DEFAULT_LESSONPLAN_NAME = 'default_lessonplan'

def lesson_key(lessonplan_name = DEFAULT_LESSONPLAN_NAME):
    """Constructs a Datastore key for a Lesson entity with Lesson_name."""
    return ndb.Key('Lesson', lessonplan_name)



class Lesson(ndb.Model):
    """Models an individual Lessonplan entry with author, content, and date."""

    author = ndb.UserProperty()
    init = ndb.StringProperty(indexed=False)
    instruct = ndb.StringProperty(indexed=False)
    final = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)


class MainPage(webapp2.RequestHandler):

    def get(self):
        lessonplan_name = self.request.get('lessonplan_name', DEFAULT_LESSONPLAN_NAME)
        lessonplans_query = Lesson.query(ancestor=lesson_key(lessonplan_name))
        lesson = lessonplans_query.fetch(1)
        if not lesson:
            print '\n\nEmpty\n\n'
            initCode = 'None'
            instructCode = 'None'
            finalCode = 'None'
        else:
            initCode = lesson[0].init
            instructCode = lesson[0].instruct
            finalCode = lesson[0].final
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
        template_values = {'lesson': lesson,
         'init_code': initCode,
         'final_code': finalCode,
         'instruct_code': instructCode,
         'lessonplan_name': urllib.quote_plus(lessonplan_name),
         'url': url,
         'url_linktext': url_linktext}
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))




class Lessonplan(webapp2.RequestHandler):

    def get(self):
        lessonplan_name = self.request.get('lessonplan_name', DEFAULT_LESSONPLAN_NAME)
        lessonplans_query = Lesson.query(ancestor=lesson_key(lessonplan_name))
        lesson = lessonplans_query.fetch(1)
        if not lesson:
            print '\n\nEmpty\n\n'
            initCode = 'None'
            instructCode = 'None'
            finalCode = 'None'
        else:
            initCode = lesson[0].init
            instructCode = lesson[0].instruct
            finalCode = lesson[0].final
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
        template_values = {'lesson': lesson,
         'init_code': initCode,
         'final_code': finalCode,
         'instruct_code': instructCode,
         'lessonplan_name': urllib.quote_plus(lessonplan_name),
         'url': url,
         'url_linktext': url_linktext}
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))



    def post(self):
        lessonplan_name = self.request.get('lessonplan_name', DEFAULT_LESSONPLAN_NAME)
        if Lesson.get_by_id(lessonplan_name) is None:
            lessonplan = Lesson(id=lessonplan_name)
        else:
            lessonplan = Lesson.get_by_id(lessonplan_name)
        print lessonplan.instruct
        if users.get_current_user():
            lessonplan.author = users.get_current_user()
        if self.request.get('init') != '':
            lessonplan.init = self.request.get('init')
        if self.request.get('instruct') != '':
            lessonplan.instruct = self.request.get('instruct')
        if self.request.get('final') != '':
            lessonplan.final = self.request.get('final')
        print '\n\n\n',
        print lessonplan_name,
        print '\n\n\n'
        lessonplan.put()
        query_params = {'lessonplan_name': lessonplan_name}
        self.redirect('/LessonMaker?' + urllib.urlencode(query_params))



application = webapp2.WSGIApplication([('/LessonMaker', Lessonplan)], debug=True)

