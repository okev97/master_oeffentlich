import pymongo
import json
import bson
from bson.codec_options import CodecOptions
import collections
import datetime
from pymongo import MongoClient

import certifi
ca = certifi.where()

client = pymongo.MongoClient("mongodb+srv://okev:1q2w3e4r@cluster0.cunvj.mongodb.net/myFirstDatabase?authSource=admin&retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")

cluster = MongoClient("mongodb+srv://okev:1q2w3e4r@cluster0.cunvj.mongodb.net/myFirstDatabase?authSource=admin&retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")

#testcollection
db = cluster["devices"]
collection = db["devices"]

#Collectionen für unterschiedliche Geräte
db2 = cluster["ArtTyp"]
collection2 = db["ArtTyp"]

#globale Zähler
countDevice = 1
countDevicePart = 1
countData = 1

daten={"ArtTyp":"test", "bezeichnung": "test", "Hersteller": "test", "seriennummer": 1234 }
collection2.insert_one(daten)

#Klassendefinitionen
class MedicalDevice(object):

    def __init__(self,id,artTyp):
        self.Id=id
        self.ArtTyp=artTyp
        daten={"id":id,"ArtTyp":artTyp}
        collection.insert_one(daten)

    def deleteDevice(self,id):
        if(id<0 or id>1000):
            print("Fehler: Fehlerhafte ID angegeben")
        else:
            query = {'id':id}
            collection.delete_one(query)
            return True
    def changeDevice(self,id,artTyp):
        if(self.ArtTyp==artTyp):
            print("Art/Typ ist bereits korrekt")
        else:
            self.ArtTyp=artTyp

class DeviceInformation(object):

    def __init__(self,artTyp,bezeichnung,hersteller,seriennummer):
        self.ArtTyp=artTyp
        self.Bezeichnung=bezeichnung
        self.Hersteller=hersteller
        self.seriennummer=seriennummer
        daten={"ArtTyp":artTyp, "bezeichnung": bezeichnung, "Hersteller": hersteller, "seriennummer": seriennummer }
        collection2.insert_one(daten)

    def change(self,bezeichnung,hersteller,seriennummer):
        self.Bezeichnung=bezeichnung
        self.Hersteller=hersteller
        self.seriennummer=seriennummer

class Component(object):

    def __init__(self, id, bezeichnungKomponente, bemerkung, artKomponente):
        self.BezeichnungKomponente=bezeichnungKomponente
        self.Bemerkung=bemerkung
        self.artKomponente=artKomponente
        
    def change(self,bezeichnungKomponente, bemerkung, artKomponente):
        self.BezeichnungKomponente=bezeichnungKomponente
        self.Bemerkung=bemerkung
        self.artKomponente=artKomponente


class Data(object):

    def __init__(self, bezeichnungData, messwerttyp, wert, einheit, id):
        self.BezeichnungData=bezeichnungData
        self.Messwerttyp=messwerttyp
        self.Wert=wert
        self.einheit=einheit
        self.Id=id
        self.Zeit=datetime

class Messwerttyp(enumerate):
    def __init__():
        pass

class Status(enumerate):
    def __init__():
        pass

#Abbruchvariable
verlassen = 1
while verlassen ==1:
    print("1-Neues Gerät anlegen")
    print("2-neue Komponente anlegen")
    print("3-Messwerte definieren")
    print("4-Status Enumeration bearbeiten")
    print("5-Einheit Enumeration bearbeiten")
    print("6-neuer Art Typ anlegen")
    print("0-Verlassen")
    
    zahl = int(input("Geben Sie eine Zahl ein: "))
    if zahl==1:
        TempDevice = str(input("Geben Sie einen Typ ein:"))
        if db.collection2.count_documents({"ArtTyp" : TempDevice})<1:
            print("Dieser Art/Typ exisitert nicht in der Datenbank, Sie müssen diesen Art/Typ anlegen")
        else:
            MedicalDevice(countDevice,TempDevice)
        countDevice = countDevice +1
    elif zahl==2:
        print("leere Funktion")
    elif zahl==3:
        print("leere Funktion")
    elif zahl==4:
        print("leere Funktion")
    elif zahl==5:
        print("leere Funktion")
    elif zahl==6:
        print("Ein neuer Art/Typ wird angelegt")
        TempArtTyp = str(input("Art/Typ:"))
        TempBezeichnung = str(input("Bezeichnung:"))
        TempHersteller = str(input("Hersteller:"))
        TempSeriennummer = int(input("Seriennummer:"))

        if db.collection2.count_documents({"ArtTyp" : TempArtTyp})>0:
            DeviceInformation(TempArtTyp,TempBezeichnung, TempHersteller, TempSeriennummer)
        else:
            print("Dieser Art/Typ exisitert bereits in der Datenbank, Sie können das Gerät einfach anlegen")
        print("leere Funktion")
    elif zahl==0:
        verlassen=0
        
#string anlegen

my_json_string = {
     "http://example.org/about": {
         "http://purl.org/dc/terms/title": [
             {"type": "literal", "value": "Anna's Homepage"}
          ]
      }
}

#python_json_obj = json.dumps(str(my_json_string))
#temp =bson.encode(python_json_obj)
#print(python_json_obj["Geraet"])
#collection2.insert_one(temp)



print("ende")

