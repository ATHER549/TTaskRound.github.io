from django.shortcuts import render
import mysql.connector as sql
un = ''
em = ''
ph = ''
msg = ''
# Create your views here.


def contactaction(request):
    global un, em, ph, msg
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root",
                        passwd="MySQL@1234", database='website')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "name":
                un = value
            if key == "email":
                em = value
            if key == "phone":
                ph = value
            if key == "message":
                msg = value

        c = "insert into contacts Values('{}','{}','{}','{}','{}')".format(
            un, em, ph, msg)
        cursor.execute(c)
        m.commit()
    return render(request, 'contactus_page.html')
