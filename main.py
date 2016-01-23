# 2016-01-22
# - Added Guesbook
# - Added login

from google.appengine.api import users

import webapp2




# ========== ========== ==========
# 2016-01-22: Created Class
class MainPage(webapp2.RequestHandler):
    
    # When a web GET request is made
    def get(self):
        # Checks for active Google account session
        user = users.get_current_user()

        if user:
            self.response.headers['Content-Type'] = 'text/html; charset=utf-8'
            self.response.write('Dude, ' + user.nickname())
        else:
            self.redirect(users.create_login_url(self.request.uri))
# ========== ========== ==========



# ========== ========== ==========
class ContactPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')
    def post(self):
        self.response.write('Hello, World!')
# ========== ========== ==========



# ========== ========== ==========
# 
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/contact.php', ContactPage),
], debug=True)
# ========== ========== ==========
