from django.shortcuts import render

# Create your views here.
from db.vo.uservo import UserVO
from db.vo.itemvo import ItemVO
from db.frame.sqlitedao import SqliteDao
from db.dao.userdb import UserDB
from db.dao.itemdb import ItemDB

sqlitedao = SqliteDao('shop');
sqlitedao.makeTable();
udb = UserDB('shop');
idb = ItemDB('shop');

def home(request):
    return render(request, 'base.html')

def html5(request):
    context = {
        'section':'html5.html'
    };
    return render(request, 'base.html',context);
def css3(request):
    context = {
        'section': 'css3.html'
    };
    return render(request, 'base.html',context);
def javascript(request):
    context = {
        'section': 'javascript.html'
    };
    return render(request, 'base.html',context);
def jquery(request):
    context = {
        'section': 'jquery.html'
    };
    return render(request, 'base.html',context);
def ajax(request):
    context = {
        'section': 'ajax.html'
    };
    return render(request, 'base.html',context);

def login(request):
    context = {
        'section': 'login.html'
    };
    return render(request, 'base.html',context);

def loginimpl(request):
    id = request.POST['id'];
    pwd = request.POST['pwd'];
    context = {};
    try:
        dbuser = udb.select(id);
        print(dbuser);
        if pwd == dbuser.getPwd():
            # session 에 사용자 정보를 넣는다.
            request.session['sessionid'] = id;
            # section 영역에 loginok.html 화면을 넣는다.
            context['section'] = 'loginok.html';
            context['loginuser'] = dbuser;

        else:
            raise Exception;
    except:
        # section 영역에 loginfail.html  화면을 넣는다.
        context['section'] = 'loginfail.html';
        print('Error....');

    return render(request, 'base.html', context);



    # 입력한 ID가 회원가입된 ID인지 검사
    # 입력한 PWD가 회원 가입시 입력한 PWD와 동일한지 검사
    # if id == 'qq' and pwd == '11':
    #     request.session['sessionid'] = id;
    #     context['section'] = 'loginok.html';
    #     context['loginid'] = 'qq';
    # else:
    #     context['section'] = 'loginfail.html';
    # 로그인 정상 처리
    # 로그인 실패 처리
    #return render(request, 'base.html', context);

def logout(request):
    if request.session['sessionid'] != None:
        del request.session['sessionid'];
    return render(request, 'base.html');

def register(request):
    context = {
        'section': 'register.html'
    };
    return render(request, 'base.html',context);

def userdetail(request):
    # 요청하는 id 값을 추츨
    id = request.GET['id'];
    # 요청한 id 정보의 상세 정보를 조회
    user = udb.select(id);
    # 상세 화면으로 이동
    context = {
        'section': 'userdetail.html',
        'userdata': user
    };
    return render(request, 'base.html',context);



def registerimpl(request):
    id = request.GET['id'];
    pwd = request.GET['pwd'];
    name = request.GET['name'];

    user = UserVO(id, pwd, name);
    udb.insert(user);
    print(id, pwd, name);
    # 회원 정보를 DB에 저장한다.
    context = {
        'section':'registerok.html',
        'rname':name,
    }

    return render(request, 'base.html',context);

def userlist(request):
    users = udb.selectall()
    context = {
        'section': 'userlist.html',
        'userlist': users
    };
    return render(request, 'base.html',context);

def additem(request):

    context = {
        'section': 'additem.html'
    };
    return render(request, 'base.html',context);

def additemimpl(request):
    name = request.GET['name'];
    price = request.GET['price'];

    item = ItemVO('', name, price, '');
    idb.insert(item);

    context = {
        'section': 'additemok.html',
        'item': item

    };
    return render(request, 'base.html',context);



def itemlist(request):
    items = idb.selectall();
    context = {
        'section': 'itemlist.html',
        'itemlist': items
    };
    return render(request, 'base.html',context);


def itemdetail(request):
    # 요청하는 id 값을 추츨
    id = request.GET['id'];
    # 요청한 id 정보의 상세 정보를 조회
    item = idb.select(id);
    # 상세 화면으로 이동
    context = {
        'section': 'itemdetail.html',
        'itemdata': item
    };
    return render(request, 'base.html',context);

def boards(request):
    context = {
        'section': 'boards.html',
    };
    return render(request, 'base.html', context);

