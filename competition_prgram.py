from tornado import web,ioloop,httpserver
login_infomation={}
diction_item=[]
seen=set()
duplicated=set()


http_server=''
username='muggle'
password='1264381274'
search=''

class login_table(web.RequestHandler):
    def post(self,*args,**kwargs):
        username = self.get_argument("username_login")
        password = self.get_argument("password_login")
        flag = 0
        for usernames in login_infomation:
            if usernames==username:
                search=login_infomation[username]
                flag = 1
        if flag == 0:
            login_infomation[username]=password
        self.write(username+'#')
        self.write(password+'#')

    def get(self): 
        for usernames in login_infomation:
            self.write(usernames + '#')
            self.write(login_infomation[usernames] + '#')
        
application = web.Application([
        (r'/',login_table)
    ])

if __name__ == '__main__':
    http_server=httpserver.HTTPServer(application)
    http_server.listen('8787')
    ioloop.IOLoop.current().start()