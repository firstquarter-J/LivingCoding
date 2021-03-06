#!python

print("content-type: text/html; charset=utf-8\n")
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

        <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-TQZXTCL6F4"></script>
        <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'G-TQZXTCL6F4');
        </script>

        <!-- 자바스크립트 링크 -->
        <script src="colors.js"></script>


        <!-- 밤, 낮 전환버튼 -->
        <input id="night_day" type="button" value="밤" onclick="
            NightDayHandler(this);
            // var target = document.querySelector('body');
            // if(this.value === '밤') {
            //     target.style.backgroundColor='black';
            //     target.style.color='white';
            //     this.value='낮';

            //     var alist = document.querySelectorAll('a');
            //     var i = 0;
            //     while(i < alist.length){
            //         alist[i].style.color = 'powderblue';
            //         i = i + 1;
            //     }
            // }
            // else {
            //     target.style.backgroundColor='white';
            //     target.style.color='black';
            //     this.value='밤';

            //     var alist = document.querySelectorAll('a');
            //     var i = 0;
            //     while(i < alist.length) {
            //         alist[i].style.color = 'blue';
            //         i = i + 1;
            //     }
            // }
        ">

    </head>

    <body>
        <h1><a href="index.html">Welcome</a></h1>
        <!-- <input type="text" onchange="alert('changed')"> -->
        <!-- <input type="text" onkeydown="alert('ket down!')"> -->

        <div id="grid">
            <ol> <!-- ol = Ordered List / ul = Unordered List -->
                <div class="ollink"><h2>Link</h2></div>
                <li><a href="https://www.youtube.com/channel/UCZbgw-o-kYIwYlqOWIXmH3Q">YouTube</a></li>
                <li><a href="https://velog.io/@firstquarter">Velog</a></li>
                <li><a href="https://github.com/firstquarter-J">GitHub</a></li>
                <li><a href="https://www.notion.so/85e0d5c12d42480fab1747aac48d333f">Profile</a></li>
            </ol>

        <!-- YouTube -->
            <div class="iframe">
                <iframe width="560" height="315" src="https://www.youtube.com/embed/DcY2oYWyN5k"
                    title="YouTube video player"
                    frameborder="0"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    allowfullscreen>
                </iframe>
            </div>
        </div>



        <!--
        <p><a href="https://www.w3.org/TR/html5/" target"_blank" // _blank는 뭐지?
            title="html5 specification">Hypertext Markup Language</a></p>
        -->



        <!-- <u>u tag</u> 유태그 -->

        <!-- <strong>strong tag</strong> 스트롱 태그-->
        <p>
            <!--Start of Tawk.to Script-->
            <script type="text/javascript">
                var Tawk_API=Tawk_API||{}, Tawk_LoadStart=new Date();
                (function(){
                    var s1=document.createElement("script"),s0=document.getElementsByTagName("script")[0];
                        s1.async=true;
                        s1.src='https://embed.tawk.to/607191f5067c2605c0c11d55/1f2tq49vp';
                        s1.charset='UTF-8';
                        s1.setAttribute('crossorigin','*');
                        s0.parentNode.insertBefore(s1,s0);
                })();
            </script>
            <!--End of Tawk.to Script-->
        </p>

        <p>
            <div id="disqus_thread"></div>
                <script>
            /**
            *  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
            *  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables    */
            /*
            var disqus_config = function () {
            this.page.url = PAGE_URL;  // Replace PAGE_URL with your page's canonical URL variable
            this.page.identifier = PAGE_IDENTIFIER; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
            };
            */
                    (function() { // DON'T EDIT BELOW THIS LINE
                    var d = document, s = d.createElement('script');
                    s.src = 'https://firstquarter.disqus.com/embed.js';
                    s.setAttribute('data-timestamp', +new Date());
                    (d.head || d.body).appendChild(s);
                    })();
                </script>
                <noscript>Please enable JavaScript to view the
                    <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a>
                </noscript>
        </p>



    </body>
</html>
''')
