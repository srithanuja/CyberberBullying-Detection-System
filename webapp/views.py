

from django.shortcuts import render
from django.http import HttpResponse, request
from .models import *

import matplotlib.pyplot as plt;
import numpy as np
import numpy
from django.shortcuts import render, redirect
from PIL import ImageTk, Image
from .Prediction import NN
from .Prediction2 import RF2



def homepage(request):
	return render(request, 'index.html')

def signuppage(request):
	if request.method=='POST':
		e_mail=request.POST['mail']

		d=usertab.objects.filter(e_mail__exact=e_mail).count()
		if d>0:
			return render(request, 'signup.html',{'msg':"e_mail Already Registered"})
		else:
			
			pass_word=request.POST['pass_word']
			phone=request.POST['phone']
			n_a_m_e=request.POST['n_a_m_e']
			gen=request.POST['gen']
			picture=request.POST['picture']
		
			d=usertab(n_a_m_e=n_a_m_e,e_mail=e_mail,pass_word=pass_word,phone=phone,gender=gen,picture=picture)
			d.save()

			return render(request, 'signup.html',{'msg':"Register Success, You can Login.."})
	else:
		return render(request, 'signup.html')


	
def userloginaction(request):
	if request.method=='POST':
		uid=request.POST['mail']
		pass_word=request.POST['pass_word']
		d=usertab.objects.filter(e_mail__exact=uid).filter(pass_word__exact=pass_word).count()
		
		if d>0:
			d=usertab.objects.filter(e_mail__exact=uid)
			request.session['e_mail']=uid
			request.session['n_a_m_e']=d[0].n_a_m_e
			fc=frequest.objects.filter(to_e_mail__exact=uid).filter(stz__exact='request').count()	
			if fc>0:
				fc=str(fc)+str(" new")
			else:
				fc=""

			return render(request, 'user_home.html',{'data': d[0],'fc':fc})

		else:
			return render(request, 'user.html',{'msg':"Login Fail"})

	else:
		return render(request, 'user.html')

def adminloginaction(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        pwd = request.POST['pwd']

        if uid == 'admin' and pwd == 'admin':
            request.session['adminid'] = 'admin'
            return render(request, 'admin_home.html')

        else:
            return render(request, 'admin.html', {'msg': "Login Fail"})

    else:
        return render(request, 'admin.html')



def adminhomedef(request):
    if "adminid" in request.session:
        uid = request.session["adminid"]
        return render(request, 'admin_home.html')

    else:
        return render(request, 'admin.html')

def training(request):
    if "adminid" in request.session:
        uid = request.session["adminid"]
        return render(request, 'training.html')

    else:
        return render(request, 'admin.html')

def testing(request):
    if "adminid" in request.session:
        uid = request.session["adminid"]
        return render(request, 'testing.html')

    else:
        return render(request, 'admin.html')

def adminlogoutdef(request):
    try:
        del request.session['adminid']
    except:
        pass
    return render(request, 'admin.html')



def userlogoutaction(request):
	try:
		del request.session['e_mail']
	except:
		pass
	return render(request, 'user.html')



def userhomepage(request):
	if "e_mail" in request.session:
		e_mail=request.session["e_mail"]
		d=usertab.objects.filter(e_mail__exact=e_mail)

		fc=frequest.objects.filter(to_e_mail__exact=e_mail).filter(stz__exact='request').count()	
		print('..........',fc)
		if fc>0:
			fc=str(fc)+str(" new")
		else:
			fc=""

		return render(request, 'user_home.html',{'data': d[0],'fc':fc})

	else:
		return redirect('n_userlogout')

		
def viewprofilepage(request):
	if "e_mail" in request.session:
		uid=request.session["e_mail"]
		d=usertab.objects.filter(e_mail__exact=uid)
		return render(request, 'viewpprofile.html',{'data': d[0]})

	else:
		return render(request, 'user.html')


def fsearch(request):
	if "e_mail" in request.session:
		uid=request.session["e_mail"]
		fe_mail=request.POST['e_mail']
		d=usertab.objects.filter(e_mail__exact=fe_mail)
		if len(d)>0:
			return render(request, 'fsearch.html',{'data': d[0]})
		else:
			return render(request, 'msg.html',{'msg': "No Details Available"})


	else:
		return render(request, 'user.html')


def freqsend(request):
	if "e_mail" in request.session:
		uid=request.session["e_mail"]
		un_a_m_e=request.session["n_a_m_e"]
		fe_mail=request.POST['e_mail']
		fn_a_m_e=request.POST['n_a_m_e']
		
		d=frequest.objects.filter(fe_mail__exact=uid).filter(to_e_mail__exact=fe_mail).count()
		
		if d>0:

			d=usertab.objects.filter(e_mail__exact=uid)
			return render(request, 'user_home.html',{'data': d[0],'msg':'Already sent friend request'})

		else:
			d=frequest(fn_a_m_e=un_a_m_e,fe_mail=uid,to_e_mail=fe_mail,stz='request')
			d.save()
					
			d=usertab.objects.filter(e_mail__exact=uid)
			return render(request, 'user_home.html',{'data': d[0],'msg':'Friend Request Sent Successfully'})

		
	else:
		return render(request, 'user.html')


def viewfreq(request):
	uid=request.session["e_mail"]
	un_a_m_e=request.session["n_a_m_e"]
	if request.method=='POST':
		
		fe_mail=request.POST['e_mail']
		fn_a_m_e=request.POST['n_a_m_e']
		
		d=friends.objects.filter(e_mail__exact=uid).filter(frnd_e__exact=fe_mail).count()
		if d>0:
			return render(request, 'user_home.html',{'data': d[0],'msg':'Your Already Friends'})
		else:
			

			d=friends(e_mail=uid,frnd_e=fe_mail,frnd_n=fn_a_m_e)
			d.save()
			d=friends(e_mail=fe_mail,frnd_e=uid,frnd_n=un_a_m_e)
			d.save()
			frequest.objects.filter(to_e_mail = uid).filter(fe_mail = fe_mail).update(stz = 'accepted')
			d=usertab.objects.filter(e_mail__exact=uid)
			return render(request, 'user_home.html',{'data': d[0],'msg':'Updated !!'})
	else:
		d=frequest.objects.filter(to_e_mail__exact=uid).filter(stz__exact="request")
		return render(request, 'viewfreq.html',{'data': d})

def reqreject(request):

	uid=request.session["e_mail"]
	fe_mail=request.POST['e_mail']
	frequest.objects.filter(to_e_mail = uid).filter(fe_mail = fe_mail).update(stz = 'rejected')
	d=usertab.objects.filter(e_mail__exact=uid)
	return render(request, 'user_home.html',{'data': d[0],'msg':'Updated !!'})

def viewfrds(request):
	if "e_mail" in request.session:
		uid=request.session["e_mail"]
		d=friends.objects.filter(e_mail__exact=uid)
		return render(request, 'viewfrds.html',{'data': d})
	else:
		return render(request, 'user.html')



def writepost(request):
	if request.method=='POST':
		import random
		
		msg=request.POST['msg']
		n_a_m_e=request.session["n_a_m_e"]
		e_mail=request.session["e_mail"]
		picture=request.POST['picture']

		rs=NN.detecting(msg)
		print('..........', rs)
		if rs=='Non-offensive':
			d=posts(n_a_m_e=n_a_m_e,e_mail=e_mail,msg=msg,picture=picture,stz='non',stz2='False')
			d.save()
		else:
			rs=RF2.detecting(msg)
			d=posts(n_a_m_e=n_a_m_e,e_mail=e_mail,msg=msg,picture=picture,stz=rs, stz2="True")
			d.save()

		return render(request, 'writepost.html',{'msg':"Post shared.."})
	
	else:
		return render(request, 'writepost.html')



def writepost2(request):
	if request.method=='POST':
		import random
		
		msg=request.POST['msg']
		n_a_m_e=request.session["n_a_m_e"]
		e_mail=request.session["e_mail"]
		picture='non'

		rs=NN.detecting(msg)
		print('..........', rs)
		if rs=='Non-offensive':
			d=posts(n_a_m_e=n_a_m_e,e_mail=e_mail,msg=msg,picture=picture,stz='non',stz2='False')
			d.save()
		else:
			rs=RF2.detecting(msg)
			d=posts(n_a_m_e=n_a_m_e,e_mail=e_mail,msg=msg,picture=picture,stz=rs, stz2="True")
			d.save()

		return render(request, 'writepost.html',{'msg':"Post shared.."})
	
	else:
		return render(request, 'writepost.html')



def ownwall(request):
	if "e_mail" in request.session:
		uid=request.session["e_mail"]
		d=posts.objects.filter(e_mail__exact=uid).order_by('-id')

		return render(request, 'ownwall.html',{'data': d})
	else:
		return render(request, 'user.html')



def viewwall(request):
	if "e_mail" in request.session:
		uid=request.session["e_mail"]
		
		d=posts.objects.all().order_by('-id')

		r=[]
		pp=True
		for d1 in d:
			pp=True
			if d1.picture=='non':
				pp=False
			d3=friends.objects.filter(e_mail__exact=uid).filter(frnd_e__exact=d1.e_mail).count()
			if d3>0:
				ss=None
				if d1.stz2=='True':
					ss=True
					ss2=False
				else:
					ss=False
					ss2=True

				print('>>>>>>>>>>',bool(d1.stz2))
				r.append({'n':d1.n_a_m_e,'p':d1.picture,'m':d1.msg,'stz1':d1.stz,'stz2':ss,'stz3':ss2,'pstz':pp})
		
		return render(request, 'viewwall.html',{'data': r})

	else:
		return render(request, 'user.html')





def d1svmdef(request):
    
    from .D1SVM import model
    model()

    return render(request, 'training.html', {'msg': "SVM Classifier Training Completed Successfully"})
 

def d1nbdef(request):
    
    from .D1NB import model
    model()

    return render(request, 'training.html', {'msg': "Naive Bayees Classifier Training Completed Successfully"})
 


def d1nndef(request):
    
    from .D1NN import model
    model()

    return render(request, 'training.html', {'msg': "Neural Network Classifier Training Completed Successfully"})
 



def d1rfdef(request):
    
    from .D1RF import model
    model()

    return render(request, 'training.html', {'msg': "Random Forest Classifier Training Completed Successfully"})
 



def d2rfdef(request):
    
    from .D2RF import model
    model()

    return render(request, 'training.html', {'msg': "Random Forest Classifier Training Completed Successfully"})
 


def d2svmdef(request):
    
    from .D2SVM import model
    model()

    return render(request, 'training.html', {'msg': "SVM Classifier Training Completed Successfully"})
 

def d2nbdef(request):
    
    from .D2NB import model
    model()

    return render(request, 'training.html', {'msg': "Naive Bayees Classifier Training Completed Successfully"})
 


def d2nndef(request):
    
    from .D2NN import model
    model()

    return render(request, 'training.html', {'msg': "Neural Network Classifier Training Completed Successfully"})
 


def d1testingdef(request):
    
    from .D1Testing import D1Testing
    D1Testing.main()

    return render(request, 'testing.html', {'msg': "Testing of dataset1 completed.."})
 


def d2testingdef(request):
    
    from .D2Testing import D2Testing
    D2Testing.main()
    return render(request, 'testing.html', {'msg': "Testing of dataset2 completed.."})
 
def results(request):
    if "adminid" in request.session:
        d = performance.objects.all()

        return render(request, 'viewaccuracy.html', {'data': d})

    else:
        return render(request, 'admin.html')


def viewgraph(request, cat):
    if "adminid" in request.session:
        algorithms = ['NB D1','SV M D1','NN D1','RF D1', 'NB D2','SV M D2','NN D2','RF D2']
        plt.cla()
        plt.clf()

        row = performance.objects.all()
        rlist = []
        for r in row:

            if cat == 'acc_v':
                rlist.append(float(r.acc))
                plt.title('Accuracy Measure')
            elif cat == 'pre_v':
                rlist.append(float(r.prec))
                plt.title('Precision Measure')
            elif cat == 'rec_v':
                rlist.append(float(r.recall))
                plt.title('Recall Measure')
            elif cat == 'f1_v':
                rlist.append(float(r.f1))
                plt.title('F1-Score Measure')

        try:

            height = rlist
            print(height,',, ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,')
            baars = algorithms
            y_pos = np.arange(len(baars))
            # plt.bar(baars, height, color=['green', 'orange', 'cyan'])
            plt.bar(baars, height, color=['green', 'orange', 'cyan','purple','green', 'orange', 'cyan','purple' ])
            # plt.plot( baars, height )
            plt.xlabel('')
            plt.ylabel('Algorithms ')
            from PIL import Image

            plt.savefig(str(cat)+'.jpg')
        except Exception as e:
            print(e)

        from PIL import Image
        print("+str(cat)+"+".jpg",'<<<<<<<<<<<<<<<<<<')
        im = Image.open(str(cat)+".jpg")
        im.show()

        return redirect('results')

