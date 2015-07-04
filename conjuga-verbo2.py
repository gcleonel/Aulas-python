import sqlite3
db = sqlite3.connect("senac.db")
cursor = db.cursor()

pessoas = ['Eu', 'Tu', 'Ele', 'Nós', 'Vós', 'Eles']
conjuga_ar = ['o', 'as', 'a', 'amos', 'ais', 'am']
conjuga_er = ['o', 'es', 'e', 'emos', 'eis', 'em']
conjuga_ir = ['o', 'es', 'e', 'imos', 'is', 'em']

#a seguir, pedimos que o usuário informe o verbo
usuario = raw_input('Digite seu nome')
verbo = raw_input('Digite o infitivo de um verbo regular:')

#separa a terminação do verbo
termina_em = verbo[-2:]
#agora, de acordo com a terminação do verbo, conjuga apropriadamente
if termina_em == 'ar':
    for i in range(6): #repete seis vezes, percorrendo a lista
        print(pessoas[i]+ ' ' + verbo[:-2] + conjuga_ar[i])
elif termina_em == 'er':
    for i in range(6): #repete seis vezes, percorrendo a lista
        print(pessoas[i]+ ' ' + verbo[:-2] + conjuga_er[i])
elif termina_em == 'ir':
    for i in range(6): #repete seis vezes, percorrendo a lista
        print(pessoas[i]+ ' ' + verbo[:-2] + conjuga_ir[i])
    countador
else:
    print("Tem certeza que " +verbo.upper()+ " é um verbo regular?")
print()
cursor.execute("INSERT INTO usuario(nome, verbo, qnt) values ('"+str(usuario)+"', '"+str(verbo)+"', "+str(countador)+")")
db.commit()

cursor.execute("SELECT * FROM usuario")
usuarios = cursor.fetchall()
for u in usuarios:
    print(u)


