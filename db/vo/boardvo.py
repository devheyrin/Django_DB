class BoardVO:
    def __init__(self,id,name,title,content,regdate):
        self.id = id;
        self.name = name;
        self.title = title;
        self.content = content;
        self.regdate = regdate;
    def __str__(self):
        return '%s, %s, %s, %s, %s' % (self.id,self.name,self.title,self.content,self.regdate);

    def getId(self):
        return self.id;

    def getName(self):
        return self.name;

    def getTitle(self):
        return self.title;

    def setTitle(self,title):
        self.title = title;

    def getContent(self):
        return self.content;

    def setContent(self, content):
        self.content;

    def getRegdate(self):
        return self.regdate;

