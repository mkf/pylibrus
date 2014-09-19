#!/usr/bin/python
# -*- coding: utf-8 -*-

import mechanize
import getpass
import argparse
import re
import datetime
import time
waitinga = 2

def czekanko(waiting):
	print "Czekanie %4d s na załadowanie strony (jeżeli coś się zcrashuje, oznacza to że wybrany czas czekanie może być za krótki)..." % waiting
	for waitinglive in range(0,waiting):
		time.sleep(1)
		print "       %5d..." % waitinglive


class corobienie:
    def __init__(self,br,polecenia):
        self.polecenia = polecenia
        corobic = self.zdobadzpolecenie('Wpisz polecenie: ',polecenia)
        if corobic == 'plan':
            self.plan(br, "n")
        elif corobic == 'conowego':
            self.conowego(br)
        elif corobic == 'dzisiaj':
            self.dzisiaj(br)
        elif corobic == 'jutro':
            self.jutro(br)
        elif corobic == 'oceny':
            self.oceny(br)
        elif corobic == 'nieobec':
            self.nieobec(br)
        elif corobic == 'terminarz':
            self.terminarz(br,"n","n")
        #tutaj będzie elif że jeśli corobic to "terminarz YYYY-MM", to on wtedy odpala terminarz dla tego miesiaca, i/lub lepiej, może być terminarzwyb czy coś takiego, że będzie trochę interaktywny, podpolecenia tj. wybór daty w zasadzie wyłącznie, albo potem nawet od do hurtowe czytanie, co do tak wgl podpolecen wszystkich, to będzie trza dla każdego polecenia z podpoleceniami zrobic podpolecenie pomoc
	elif corobic == 'terminarzwyb':
	    self.terminarzwyb(br)	
	elif corobic == 'ogloszenia':
       	    self.ogloszenia(br)
        elif corobic == 'szczesliwynr':
            self.szczesliwynr(br)
        elif corobic == 'pomoc':
       	    print wytlumaczeniepolecen
        elif corobic == 'wyjdz':
            quit()
        else:
            print u'Błąd w kwestii informacji co robić'
            quit()
    def zdobadzpolecenie(self,pytanie,komendki):
        print 'Dostępne polecenia: '
        print komendki
        polec = raw_input(pytanie)
        try:
            polecenia.index(polec)
            run = polec
            return run
        except:
            print 'Nie znaleziono polecenia: %s' % polec
            runu = zdobadzpolecenie()
            return runu
    def plan(self,br,dajreada):
        szasowilasjkdfg = time.time()
    def conowego(self,br):
        czasik = time.time()
    def dzisiaj(self,br):
        czasik = time.time()
    def jutro(self,br):
        czasik = time.time()
    def oceny(self,br):
        czasik = time.time()
    def nieobec(self,br):
        czasik = time.time()
    def terminarz(self,br,wybtermclpocz,wybtermclkonc):
        terazmc = '2014-09' #tu będzie z datetime.timetuple przerabiane na string w tym stylu
        if wybtermclpocz == "n":
            wtcpocz = terazmc
        else:
            wtcpocz = wybtermclpocz
        if wybtermclkonc == "n":
            wtckonc = terazmc
        else:
            wtckonc = wybtermclkonc
        #tu będzie przerabianie tych datowych stringów na daty ładne numeryczne, raczej nie na obiekty datetime
    def terminarzwyb(self,br):
        print u"Wybierz miesiące, które mają być zparsowane, licząc włącznie"
        rpocz = raw_input('Podaj rok miesiąca początkowego:  ')
        mpocz = raw_input('Podaj miesiąc początkowy:  ')
        dpocz = str('%4d-%2d' % (rpocz,mpocz))
        print "Wybrano datę początkową: %4d-%2d" % (rpocz, mpocz)
        rkonc = raw_input('Podaj rok miesiąca końcowego:  ')
        mkonc = raw_input('Podaj miesiąc końcowy:  ')
        dkonc = str('%4d-%2d' % (rkonc,mkonc))
        print "Wybrano datę końcową: %s" % dkonc
        self.terminarz(br, dpocz, dkonc)
    def ogloszenia(self,br):
        czasik = time.time()
    def szczesliwynr(self,br):
        czasik = time.time()

polecenia = ('plan', 'conowego', 'dzisiaj', 'jutro', 'oceny', 'nieobec', 'terminarz', 'terminarzwyb', 'ogloszenia', 'szczesliwynr', 'pomoc', 'wyjdz')
br = mechanize.Browser()
#br.open('https://dziennik.librus.pl/loguj/przenies/uczen_index')
br.open('https://m.dziennik.librus.pl/module/Common/action/Login') #tymczasowo przestawiamy się na wersję mobilną — desktopowej chyba nie da się zbyt łatwo
czekanko(waitinga)
try:
    br.select_form(name='logowanie')
except:
    br.select_form(nr=0)
uzyszk = raw_input('Wpisz nazwę użytkownika:  ')
br['login'] = uzyszk
haselo = getpass.getpass('Wpisz hasło (zabezp. przed pokazaniem na ekr. znaków hasła: OK):  ')
br['passwd'] = haselo
odpoa = br.submit()
def restarcik(br, uzyszkn, haselon):
	br.select_form(name='logowanie')
	br['login'] = uzyszkn
	br['passwd'] = haselon
	czekanko(waitinga)
	odpoah = br.submit()
	return odpoah

assert br.viewing_html()
print br.title()
print odpoa.geturl()
#print odpoa.info() #d
readzikdebugu = odpoa.read()
try:
    if len(re.findall("Do zalogowania się wymagane jest dodatkowo wpisanie kodu z obrazka", readzikdebugu)):
        print "Przerąbane. Że niby za dużo logowań, blablabla, CAPTCHA. Tego jeszcze nie obsługuję. Wychodzimy! (albo jednak nie)"
        #quit()
        odpoag = restarcik(br,uzyszk,haselo)
        assert br.viewing_html()
        print br.title()
        print odpoag.geturl()
        print odpoag.info()
        print odpoag.read()
    if len(re.findall("Zaloguj się aby przejść do wybranej strony.", readzikdebugu)):
        odpoah = restarcik(br,uzyszk,haselo)
        assert br.viewing_html()
        print br.title()
        print odpoah.geturl()
        print odpoah.info()
        print odpoah.read()
    else:
        print odpoa.read()
except:
    #print odpoa.read()
    print readzikdebugu



while True:
	corobienie(br,polecenia)


