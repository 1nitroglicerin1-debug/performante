# -*- coding: utf-8 -*-
import io
s=io.open('index.html',encoding='utf-8').read()
i=s.find('<footer class="footer">')
j=s.find('</footer>')+9
head=s[:s.find('</head>')+7]
body='<body style="background:#0D0F12">'+s[i:j]+'</body></html>'
io.open('_footer_test.html','w',encoding='utf-8').write(head+body)
print('ok')
