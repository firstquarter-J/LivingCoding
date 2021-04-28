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
else:
    pageId = 'Welcome'
    description = 'Welcome'

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

        <p>{desc}</p>

        <a href="create.py">create</a>

        <form action="process_update.py" method="post">
            <input type="hidden" name="pageId" value="{form_default_title}">
            <p><input type="text" name="title" placeholder="title" value="{form_default_title}"></p>
            <p><textarea rows="4" name="description" placeholder="description">{form_default_description}</textarea></P>
            <p><input type="submit"></p>
        </form>

    </body>
</html>

'''.format(title=pageId, desc=description, listStr=view.getList(), form_default_title=pageId, form_default_description=description))
