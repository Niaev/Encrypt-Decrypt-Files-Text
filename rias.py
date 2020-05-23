# coding: utf-8

import getpass
import time
import sys

# Coded by KriptonWave
# Date: 15/05/2020

cript = {
"a": "I",
"b": "S",
"c": "N",
"d": "L",
"e": "B",
"f": "Q",
"g": "C",
"h": "R",
"i": "D",
"j": "T",
"k": "P",
"l": "E",
"m": "Z",
"n": "A",
"o": "G",
"p": "U",
"q": "Y",
"r": "K",
"s": "O",
"t": "X",
"u": "J",
"v": "W",
"w": "H",
"x": "M",
"y": "V",
"z": "F",
}
     
ownz = {
"I": "a",
"S": "b",
"N": "c",
"L": "d",
"B": "e",
"Q": "f",
"C": "g",
"R": "h",
"D": "i",
"T": "j",
"P": "k",
"E": "l",
"Z": "m",
"A": "n",
"G": "o",
"U": "p",
"Y": "q",
"K": "r",
"O": "s",
"X": "t",
"J": "u",
"W": "v",
"H": "w",
"M": "x",
"V": "y",
"F": "z",
} 

index = (r"""

 ██▀███   ██▓ ▄▄▄        ██████    
▓██ ▒ ██▒▓██▒▒████▄    ▒██    ▒    
▓██ ░▄█ ▒▒██▒▒██  ▀█▄  ░ ▓██▄      
▒██▀▀█▄  ░██░░██▄▄▄▄██   ▒   ██▒   
░██▓ ▒██▒░██░ ▓█   ▓██▒▒██████▒▒   
░ ▒▓ ░▒▓░░▓   ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░   
  ░▒ ░ ▒░ ▒ ░  ▒   ▒▒ ░░ ░▒  ░ ░   
  ░░   ░  ▒ ░  ░   ▒   ░  ░  ░     
   ░      ░        ░  ░      ░     

""")
user = getpass.getuser()
tempo = time.strftime("%H:%M:%S")
logs = []
unam = []

yes = {'yes','y', 'ye', ''}
no = {'no','n'}

print (index)
while True:
  s = str(input(user+' --> '))
  if "!help" in s:
     print("""
[#] Comandos:

!help = ajuda.
!quit = sair.
!contact = Autor Contato.
!banner = Ascii art.
!enc-file [FILE] = encriptar textos em arquivos.
!dec-file [FILE] = desencriptar textos em arquivos.
""")
  elif "!banner" in s:
       print(index)

  elif "!contact" in s: 
       print("[+] Twitter: @PlushSec\n[+] Discord: KriptonWave#9530\n")

  elif "!quit" in s:
       print("[!] Finalizado!!!")
       break

  elif s.find("!enc-file ") != -1:
       ss = s.split('!enc-file ')
       s2 = ss[1]
       with open(s2,'r') as ler:
            ler = ler.readlines()
            for pwn in ler:
                pwn = pwn.rstrip('\n')
                pwn = pwn.lower()
                for l in cript:
                    pwn = pwn.replace(l, cript[l])
                print("{}".format(pwn).lower())
                logs.append(pwn+'\n')
            op = str(input("\n[{} HORA] Deseja salvar? [Y/N]: ".format(tempo)))
            op = op.lower()
            if op in yes:
               save = str(input("[{} HORA] Nome do arquivo: ".format(tempo)))
               resul = open(save,'w')
               resul.writelines(logs)
               resul.close()
            elif op in no:
                 print("[{} HORA] Arquivo nao salvo!".format(tempo))
                 exit()
            else:
                 print("[{} HORA] Arquivo nao salvo!".format(tempo))
                 exit()

  elif s.find("!dec-file ") != -1:
       puta = s.split("!dec-file ")
       puta2 = puta[1]
       with open(puta2,'r') as btf:
            btf = btf.readlines()
            for brute in btf:
                brute = brute.rstrip('\n')
                brute = brute.upper()
                for j in ownz:
                    brute = brute.replace(j, ownz[j])
                print("{}".format(brute).lower())
                unam.append(brute+'\n')
            op = str(input("\n[{} HORA] Deseja salvar? [Y/N]: ".format(tempo)))
            op = op.lower()
            if op in yes:
               save = str(input("[{} HORA] Nome do arquivo: ".format(tempo)))
               names = open(save,'w')
               names.writelines(unam)
               names.close()
            elif op in no:
                 print("[{} HORA] Arquivo nao salvo!".format(tempo))

            else:
                 print("[{} HORA] Arquivo nao salvo!".format(tempo))
                 exit()

  else:
       print("[!] Comando invalido. Use !help.")




