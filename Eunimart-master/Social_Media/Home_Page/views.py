from django.shortcuts import render,redirect
import mysql.connector
from .forms import *
from django.http import HttpResponse


name=""
u_id=0
t_id=[]

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="raviajay.2003",
      database="user_details"
)
mycursor = mydb.cursor()

def home(request):
    return render(request,'home.html')

def login_signup(request):
    return render(request,'login_signup.html')

def get_hash(password):
    return password


def register(request):
    if(request.method=='POST'):
        form = user_cred(request.POST)
        if(form.is_valid()):
            first_name=form.cleaned_data['first_name']
            middle_name=form.cleaned_data['middle_name']
            last_name=form.cleaned_data['last_name']
            age=form.cleaned_data['age']
            phone_number=form.cleaned_data['phone_number']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            hash=get_hash(str(password))



    sql_query=("insert into user_credentials(first_name,middle_name,last_name,Age,phone_number,email,passwords)"
               "values(%s,%s,%s,%s,%s,%s,%s)")
    data=(first_name,middle_name,last_name,age,phone_number,email,str(password))


    mycursor.execute(sql_query,data)
    mydb.commit()

    mycursor.execute("SELECT * FROM user_credentials")


    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)


    return render(request,'home.html')

def dashboard(request):
    global u_id
    global name
    global t_id
    if(request.method=='POST'):
        #print("ju")
        validate=login_validate(request.POST or None)

        if(validate.is_valid()):
            email=validate.cleaned_data['emails']
            password=validate.cleaned_data['passwords']

            sql_query=("select user_id,first_name,email,passwords from user_credentials where email=%s and passwords=%s")
            data=(email,password)

            mycursor.execute(sql_query,data)
            myresult = mycursor.fetchall()
            print(myresult)
            

            if(len(myresult[0])==4):
                name=myresult[0][1]
                u_id=myresult[0][0]
                mycursor.execute("SELECT * FROM tweet_data")


                myresult = mycursor.fetchall()
                names=[]
                data=[]
                ids=[]
                for i in myresult:
                    t_id.append(i[0])
                    ids.append(i[1])
                    names.append(i[2])
                    data.append(i[3])
               
                return render(request,'tweet.html',{'user_id':u_id,'datas':zip(t_id,ids,names,data)})

                
            return HttpResponse("404")
    
    
def tweet(request):
    global u_id
    global name
    global t_id
    
    if(request.method=='POST'or None):
        form_tweet=post_tweet(request.POST)
        if(form_tweet.is_valid()):
            box=form_tweet.cleaned_data['user_tweet']
            sql_query=("insert into tweet_data(user_id,name,tweet_info)"
               "values(%s,%s,%s)")
            data=(u_id,name,box)
            mycursor.execute(sql_query,data)
            mydb.commit()
    
    mycursor.execute("SELECT * FROM tweet_data")


    myresult = mycursor.fetchall()
    names=[]
    data=[]
    ids=[]
    for i in myresult:
        t_id.append(i[0])
        ids.append(i[1])
        names.append(i[2])
        data.append(i[3])
    
               
    return render(request,'tweet.html',{'user_id':u_id,'datas':zip(t_id,ids,names,data)})
    
            
def delete_tweet(request,delete_id):
    
    sql_query=("delete from tweet_data where t_id=%s")
    data=(delete_id,)
    mycursor.execute(sql_query,data)
    mydb.commit()

    
               
    return render(request,'home.html')
       
    








