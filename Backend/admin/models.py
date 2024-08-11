from app import app
from flask_admin import Admin,BaseView, expose

admin = Admin(app, name='microblog', template_mode='bootstrap3')

class CreateView(BaseView):
    @expose('/admin')
    def index(self):
        return self.render('model/create.html')
admin.add_view(CreateView(name='create', endpoint='create'))