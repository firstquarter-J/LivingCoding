#!python

print("content-type: text/html; charset=utf-8\n")
import sys
import codecs
import cgi, os, view

form = cgi.FieldStorage()
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r', encoding='UTF8').read()

    #보안 - javascript 꺽쇠처리 못하게~?
    description = description.replace('<', '&lt;')
    description = description.replace('>', '&gt;')


    update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
    delete_action = '''
        <form action="process_delete.py" method="post">
            <input type="hidden" name="pageId" value="{}">
            <input type="submit" value="delete">
        </form>
    '''.format(pageId)
else:
    pageId = 'Welcome'
    description = 'Welcome'
    update_link = ''
    delete_action = ''

print('''
<!DOCTYPE html>
<html>
    <head>
        <!-- 네이버 웹마스터 연동 -->
        <meta name="naver-site-verification" content="ccc5201fc3035c695ebb755c7dba402cf6de4e95" />

        <!-- CSS 파일 링크 -->
        <link href="index.css" rel="stylesheet">

        <!-- <meta charset="utf-8"> // 형식? 이렇게 읽어라? -->
        <meta charset="utf-8">

        <!-- jQuery -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>

        <!-- 타이틀 -->
        <title>장상현</title>

        <!-- 자바스크립트 링크 -->
        <script src="colors.js"></script>

        <!-- 밤, 낮 전환버튼 -->
        <input id="night_day" type="button" value="밤" onclick="
            NightDayHandler(this);
        ">

    </head>

    <body>
        <h1><a href="index.py">Welcome</a></h1>

        <div class="link">
            <ol> <!-- ol = Ordered List / ul = Unordered List -->
                {listStr}
            </ol>
        </div>

        <div>
            <h2>{title}</h2>
        </div>
        <p>
            {desc}
        </p>
        <a href="create.py">create</a>

        {update_link}
        {delete_action}


    </body>
</html>

'''.format(title=pageId,
        desc=description,
        listStr=view.getList(),
        update_link=update_link,
        delete_action=delete_action
        ))
