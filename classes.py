from peewee import *
import os

arq = 'bd.db'
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db



class Item(BaseModel):

    nome = CharField()
    descricao = CharField()
    peso = FloatField()
    quantidade = IntegerField()  



    def __str__(self):

        return self.nome+" "+self.descricao+' '+ str(self.peso)+" "+ str(self.quantidade)+"||"     




class Inventario(BaseModel):

    peso_max = FloatField
    itens = ManyToManyField(Item)



    def __str__(self):

        lista_itens = ""
        for i in self.itens:
            lista_itens += str(i)

        return str(self.peso_max)+" "+ lista_itens+"||" 



class Arma(BaseModel):
    nome = CharField()
    peso = FloatField()
    dano = IntegerField()

    def __str__(self):

        return self.nome+" "+ str(self.peso)+" "+ str(self.dano)+"||"    




class Pocao(BaseModel):

    nome = CharField()
    efeito = CharField()
    duracao = FloatField()

    def __str__(self):

        return self.nome+" "+self.efeito+' '+ str(self.duracao)+"||" 


class Armadura(BaseModel):

    nome = CharField()
    peso = FloatField()
    protecao = IntegerField()



    def __str__(self):

        return self.nome+" "+str(self.peso)+" "+ str(self.protecao)+"||"  
    


class Npc(BaseModel):

    nome = CharField()
    reputacao = CharField()
    inventario = ForeignKeyField(Inventario)
    estado = CharField()


    def __str__(self):

        return self.nome+' '+ str(self.reputacao)+" "+ str(self.inventario)+" "+self.estado+"||"



class Classe(BaseModel):

    nome = CharField()
    habilidade = CharField()



    def __str__(self):

        return self.nome+' '+ self.habilidade+"||" 




class Magia(BaseModel):

    nome = CharField()
    descricao = CharField()
    efeito = CharField()



    def __str__(self):

        return self.nome+' '+ self.descricao+" "+ self.efeito+"||"   



class Jogador(BaseModel):

    nome = CharField()
    nivel = IntegerField()
    vida = IntegerField()
    arma = ForeignKeyField(Arma)
    magia = ForeignKeyField(Magia)
    armadura = ForeignKeyField(Armadura)
    classe = ForeignKeyField(Classe)
    inventario = ForeignKeyField(Inventario)
    estado = CharField()
    amizade = ForeignKeyField(Npc)
    

    def __str__(self):
        return self.nome+' '+ str(self.nivel)+" "+ str(self.vida)+' '+str(self.arma)+" "+str(self.armadura)+" "+str(self.inventario)+" "+ self.estado+" "+str(self.amizade)+"||"

class Inimigo(BaseModel):

    vida = IntegerField()
    arma = ForeignKeyField(Arma)
    armadura = ForeignKeyField(Armadura)
    xp = IntegerField()
    inventario = ForeignKeyField(Inventario)
    estado = CharField()

    def __str__(self):
        return str(self.vida)+" "+str(self.arma)+" "+str(self.armadura)+" "+str(self.xp)+' '+str(self.inventario)+" "+ self.estado+"||"






if __name__ == "__main__":
    if os.path.exists(arq):
        os.remove(arq)
    db.connect()

    db.create_tables([Item,Inventario,Inventario.itens.get_through_model(),Arma,Pocao,Armadura,Npc,Classe,Magia,Jogador,Inimigo])


    comida = Item.create(nome= "comida",descricao= "serve pra comer", peso = 1, quantidade = 1 )
    agua = Item.create(nome= "agua",descricao = "usada quando esta com sede", peso = 1, quantidade = 1)
    inventario1 = Inventario.create(peso_max = 200)
    inventario1.itens.add(agua)
    

    inventario2 = Inventario.create(peso_max = 50)
    inventario2.itens.add(comida)

    
    npc = Npc.create(nome = "João", reputacao = "Boa", inventario = inventario2, estado = "tranquilo")

    armadura1 = Armadura.create(nome = "leve", peso = 1, protecao = 11)
    arma1 = Arma.create(nome = "cajado",peso = 5, dano = 6)
    classe1 = Classe.create(nome = "Mago", habilidade = "conjura magia")
    magia1 = Magia.create(nome = "bola de fogo", descricao = "voce joga uma bola de fogo", efeito = "fogo")

    armadura2 = Armadura.create(nome = "pesada", peso = 10, protecao = 18)
    arma2 = Arma.create(nome = "machado",peso = 5, dano = 6)




    jogador =  Jogador.create(nome = "josé", nivel = 5,vida = 20, arma = arma1, magia = magia1, armadura = armadura1, classe = classe1, inventario = inventario1, estado = "Tranquilo", amizade = npc)
    inimigo = Inimigo.create(vida = 10, arma = arma2, armadura = armadura2, xp = 100, inventario = inventario2, estado = "agressivo")
 
    
    print (jogador)
    print()
    print (inimigo)
    print()
    print(inventario2)