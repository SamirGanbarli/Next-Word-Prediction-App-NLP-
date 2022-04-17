import os
import re
import nltk
import string
import nltk.corpus
import nltk, re, pprint
from nltk import word_tokenize
from nltk.util import ngrams
from nltk import bigrams
import csv
import random
import time
import array as arr
from django.shortcuts import redirect
from nltk import FreqDist
from nltk.corpus import brown
from django.shortcuts import render, redirect
from .models import Todo



class gram:
    def __init__(self):
        todo = Todo.objects.all()
        f = open(r"C:\Users\User\Desktop\korpus.txt", "r", encoding='utf-8')
        content = f.read()
        content = re.sub('<.*>', '', content)
        content = re.sub('ENDOFARTICLE.', '', content)
        tokenized = word_tokenize(content)
        tokenized = [i.lower() for i in tokenized]
        words = [word for word in tokenized]
        n_gram = ngrams(words, 1)
        n_gram2= ngrams(words, 2)
        n_gram3= ngrams(words, 3)
        n_gram4= ngrams(words, 4)
        n_gram5= ngrams(words, 5)
        fdist = nltk.FreqDist(n_gram)  
        fdist2 = nltk.FreqDist(n_gram2)
        fdist3 = nltk.FreqDist(n_gram3)
        fdist4 = nltk.FreqDist(n_gram4)
        fdist5 = nltk.FreqDist(n_gram5)
        self.todo = todo
        self.fdist = fdist 
        self.fdist2 = fdist2
        self.fdist3 = fdist3
        self.fdist4 = fdist4
        self.fdist5 = fdist5
        
    


      
global gram1
gram1 = gram()

def first(request):
    return render(request, 'first.html')


def choose(request):
    return render(request, 'choose.html')


def index(request):
    
    if request.method == 'POST':

        new_todo = Todo(
            title = request.POST['title']
        )
        counter = 0
        for x in gram1.fdist3:
            
            if (x[0]+' '+x[1]) == new_todo.title:
                a = gram1.fdist3[(x[0]),(x[1]),(x[2]),]
                max = x[2]
                new_todo.title = new_todo.title + ' ' + max
                counter = counter + 1
                break  
            
           
        new_todo.save()
        return render(request, 'index.html', {'todos': Todo.objects.all()})

    return render(request, 'index.html', {'todos': gram1.todo})




#######################-------------------------------------------
def index3(request):
    if request.method == 'POST':

        new_todo = Todo(
            title = request.POST['title']
        )
        for x in gram1.fdist2:
            if x[0] == new_todo.title:
        
                c = gram1.fdist2[(x[0]),(x[1]),]  

                max = x[1]

                value = x[0] + ' ' + x[1]

                new_todo.title = new_todo.title + ' ' + max
        
                break
        
        

        for z in gram1.fdist3:
            if(z[0] + ' ' + z[1]) == value:

                b = gram1.fdist3[(z[0]), (z[1]), (z[2]),]

                value3 = z[0] + ' ' + z[1] + ' ' + z[2]

                new_todo.title = new_todo.title + ' ' + z[2]

                break

        

        for x in range(100):
            for x in gram1.fdist4:

                if(x[0]+' '+x[1]+' '+x[2]) == value3:

                    a4 = gram1.fdist4[(x[0]),(x[1]),(x[2]),(x[3]),]

                    max = x[3]

                    value3 = x[1]+' '+x[2]+' '+x[3]

                    new_todo.title = new_todo.title + ' ' + max

                    break

            if x[3] == '.':
                break
                  
        new_todo.save()
        
        return render(request, 'index3.html', {'todos': Todo.objects.all()})
    
    return render(request, 'index3.html', {'todos': gram1.todo})

#####-----------------------------------------######--------------#######---------------

def index2(request):

    if request.method == 'POST':

        new_todo = Todo(
            title = request.POST['title']
        )
        counter = 0
        for x in gram1.fdist2:
            if x[0] == new_todo.title:
        
                a = gram1.fdist2[(x[0]),(x[1]),]
     
                max = x[1]

                new_todo.title = new_todo.title + ' ' + max
        
        
                break
              
           
        new_todo.save()
        return render(request, 'index2.html', {'todos': Todo.objects.all()})

    return render(request, 'index2.html', {'todos': gram1.todo})


def delete(request, pk):
    gram1.todo = Todo.objects.get(id=pk)
    gram1.todo.delete()

    return redirect('/')