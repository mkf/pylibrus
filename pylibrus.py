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
			corobic = self.zdobadzpolecenie()
			if corobic == 'plan':
				self.plan(br, "n")
			elif corobic == 'costam':
				self.costam(br)
			else:
				print u'Błąd w kwestii informacji co robić'
				quit()
	def zdobadzpolecenie(self):
		print 'Dostępne polecenia: '
		print polecenia
		polec = raw_input('Wpisz polecenie: ')
		try:
			polecenia.index(polec)
			run = polec
			return run
		except:
			print 'Nie znaleziono polecenia: %s' % polec
			runu = zdobadzpolecenie()
			return runu
	def plan(self,br,dajreada):
		czasik = time.time()
	def costam(self,br):
		czasik = time.time()
polecenia = ('plan', 'costam')
br = mechanize.Browser()
#br.open('https://dziennik.librus.pl/loguj/przenies/uczen_index')
br.open('https://m.dziennik.librus.pl/module/Common/action/Login') #tymczasowo przestawiamy się na wersję mobilną — desktopowej chyba nie da się
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
    print odpoa.read()
while True:
	corobienie(br,polecenia)
