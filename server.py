import  web

render = web.template.render('templates/')

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        data = web.input(name=None)
        return render.index(data.name)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()