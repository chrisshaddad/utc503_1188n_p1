from functools import reduce

class Etudiant:
    def __init__(self, numero, prenom, nom, niveau):
        self.numero = numero
        self.prenom = prenom
        self.nom = nom
        self.niveau = niveau

class Cours:
    def __init__(self, code, intitule, niveau):
        self.code = code
        self.intitule = intitule
        self.niveau = niveau

##On considere que l'indentifiant de Note est la combinaison du numero etudiant et du code cours (Comme join tables)
class Note:
    def __init__(self, numero, code, note):
        self.numero = numero
        self.code = code
        self.note = note

class BD:
    def __init__(self):
        self.etudiants = []
        self.cours = []
        self.notes = []

    def getindex(self, objecttype, indentifier1 = "", indentifier2 = ""):
        if(objecttype == "Etudiant"):
            for index, etudiant in enumerate(self.etudiants):
                if(etudiant.numero == indentifier1):
                    return index
        if(objecttype == "Cours"):
            for index, cours in enumerate(self.cours):
                if(cours.code == indentifier1):
                    return index
        if(objecttype == "Note"):
            for index, note in enumerate(self.notes):
                if(note.numero == indentifier1 and note.code == indentifier2):
                    return index
        return -1
    
    def ajouteretudiant(self, numero, prenom, nom, niveau):
        etudiantindex = self.getindex("Etudiant", numero)
        if(etudiantindex == -1):
            etudiantaajouter = Etudiant(numero, prenom, nom, niveau)
            self.etudiants.append(etudiantaajouter)
        else:
            print("Un etudiant ayant le numero " + str(numero) + " deja existe sur le systeme")

    def supprimeretudiant(self, numero):
        etudiantinddex = self.getindex("Etudiant", numero)
        if(etudiantinddex > -1):
            del self.etudiants[etudiantinddex]
        else:
            print("Il n'existe pas un etudiant ayant le numero " + str(numero))
    
    def editeretudiant(self, numero, prenom, nom, niveau):
        etudiantinddex = self.getindex("Etudiant", numero)
        if(etudiantinddex > -1):
            etudiantaediter = self.etudiants[etudiantinddex]
            etudiantaediter.prenom = prenom
            etudiantaediter.nom = nom
            etudiantaediter.niveau = niveau
            self.etudiants[etudiantinddex] = etudiantaediter
        else:
            print("Il n'existe pas un etudiant ayant le numero " + str(numero))

    def ajoutercours(self, code, intitule, niveau):
        coursindex = self.getindex("Cours", code)
        if(coursindex == -1):
            coursaajouter = Cours(code, intitule, niveau)
            self.cours.append(coursaajouter)
        else:
            print("Un cour ayant le code " + str(code) + " deja existe sur le systeme")

    def supprimercours(self, code):
        coursindex = self.getindex("Cours", code)
        if(coursindex > -1):
            del self.cours[coursindex]
        else:
            print("Il n'existe pas un etudiant ayant le code " + str(code))

    def editercours(self, code, intitule, niveau):
        coursindex = self.getindex("Cours", code)
        if(coursindex > -1):
            coursaediter = self.cours[coursindex]
            coursaediter.intitule = intitule
            coursaediter.niveau = niveau
        else:
            print("Il n'existe pas un etudiant ayant le code " + str(code))

    def ajouternote(self, numeroetudiant, codecours, note):
        etudiantindex = self.getindex("Etudiant", numeroetudiant)
        coursindex = self.getindex("Cours", codecours)
        if(etudiantindex > -1 and coursindex > -1):
            noteindex = self.getindex("Note", numeroetudiant, codecours)
            if(noteindex == -1):
                notesaajouter = Note(numeroetudiant, codecours, note)
                self.notes.append(notesaajouter)
            else:
                print("Un note deja existe pour cet etudiant dans ce cours")
        else:
            print("Ce cours ou etudiant n'existe pas")

    def supprimernote(self, numeroetudiant, codecours):
        noteindex = self.getindex("Note", numeroetudiant, codecours)
        if(noteindex > -1):
            del self.notes[noteindex]
        else:
            print("Cette note n'esist pas")

    def editernote(self, numeroetudiant, codecours, note):
        noteindex = self.getindex("Note", numeroetudiant, codecours)
        if(noteindex > -1):
            noteaediter = self.notes[noteindex]
            noteaediter.note = note
            self.notes[noteindex] = noteaediter
        else:
            print("Cette note n'esist pas")

    def moyenneclasse(self, codecours):
        notetotal = float(0)
        notecount = 0
        coursindex = self.getindex("Cours", codecours)
        if(coursindex > -1):
            for noteobject in self.notes:
                if(noteobject.code == codecours):
                    notetotal += noteobject.note
                    notecount += 1
            if(notecount > 0):
                print("Moyenne de la cours: " + codecours + " est: " + str(notetotal/notecount))
            else:
                print("Pas de note enrgistrer pour ce cours")
        else:
            print("Ce cours n'existe pas")

    def moyenneetudiant(self, numeroetudiant):
        notetotal = float(0)
        notecount = 0
        etudiantindex = self.getindex("Etudiant", numeroetudiant)
        if(etudiantindex > -1):
            for noteobject in self.notes:
                if(noteobject.numero == numeroetudiant):
                    notetotal += noteobject.note
                    notecount += 1
            if(notecount > 0):
                print("Moyenne de l'etudiant: " + str(numeroetudiant) + " est: " + str(notetotal/notecount))
            else:
                print("Pas de note enregistrer pour cet etudiant")
        else:
            print("Cet etudiant n'existe pas")

    def consulternoteclasse(self, codecours):
        coursindex = self.getindex("Cours", codecours)
        if(coursindex > -1):
            notelist = ""
            for noteobject in self.notes:
                if(noteobject.code == codecours):
                    notelist += "- Etudiant: " + str(noteobject.numero) + " Note: " + str(noteobject.note) + "\n"
            if(len(notelist) > 0):
                print(notelist)
            else:
                print("Pas de notes pour ce cours")
        else:
            print("Ce cours n'existe pas")
    
    def consulternoteetudiant(self, numeroetudiant):
        etudiantindex = self.getindex("Etudiant", numeroetudiant)
        if(etudiantindex > -1):
            notelist = ""
            for noteobject in self.notes:
                if(noteobject.numero == numeroetudiant):
                    notelist += "- Cours: " + str(noteobject.code) + " Note: " + str(noteobject.note) + "\n"
            if(len(notelist) > 0):
                print(notelist)
            else:
                print("Pas de notes pour cet etudiant")            
        else:
            print("Cet etudiant n'existe pas")
    
    def moyenneclasse2(self, codecours):
        coursindex = self.getindex("Cours", codecours)
        if(coursindex > -1):
            coursnotes = list(filter(lambda x: x.code == codecours, self.notes))
            if(len(coursnotes) > 0):
                notetotal = reduce(lambda x,y: x.note + y.note, coursnotes)
                print("Moyenne de la cours: " + codecours + " est: " + str(notetotal/len(coursnotes)))
            else:
                print("Pas de note enrgistrer pour ce cours")
        else:
            print("Ce cours n'existe pas")

    def moyenneetudiant2(self, numeroetudiant):
        etudiantindex = self.getindex("Etudiant", numeroetudiant)
        if(etudiantindex > -1):
            etudiantnotes = list(filter(lambda x: x.numero == numeroetudiant, self.notes))
            if(len(etudiantnotes) > 0):
                notetotal = reduce(lambda x,y: x.note + y.note, etudiantnotes)
                print("Moyenne de l'etudiant: " + str(numeroetudiant) + " est: " + str(notetotal/len(etudiantnotes)))
            else:
                print("Pas de note enrgistrer pour cet etudiant")
        else:
            print("Cet etudiant n'existe pas")

    def consulternoteclasse2(self, codecours):
        coursindex = self.getindex("Cours", codecours)
        if(coursindex > -1):
            coursnotes = list(filter(lambda x: x.code == codecours, self.notes))
            if(len(coursnotes) > 0):
                notelist = list(map(lambda x: "- Etudiant: " + str(x.numero) + " Note: " + str(x.note) + "\n", coursnotes))
                print(str.join("",notelist))
            else:
                print("Pas de notes pour ce cours")
        else:
            print("Ce cours n'existe pas")

    def consulternoteetudiant2(self, numeroetudiant):
        etudiantindex = self.getindex("Etudiant", numeroetudiant)
        if(etudiantindex > -1):
            etudiantnotes = list(filter(lambda x: x.numero == numeroetudiant, self.notes))
            if(len(etudiantnotes) > 0):
                notelist = list(map(lambda x: "- Cours: " + str(x.code) + " Note: " + str(x.note) + "\n", etudiantnotes))
                print(str.join("",notelist))
            else:
                print("Pas de notes pour cet etudiant")
        else:
            print("Cet etudiant n'existe pas")

basededonne = BD()

basededonne.ajouteretudiant(1, "Christophe", "Haddad", "A")
basededonne.ajouteretudiant(2, "Durant", "Dupont", "A")
basededonne.ajoutercours("NFA100", "DataBase", "A")
basededonne.ajoutercours("NFA101", "DataBase Avance", "A")

basededonne.ajouternote(1, "NFA100", 10)
basededonne.ajouternote(2, "NFA100", 11.32)
basededonne.ajouternote(1, "NFA101", 13)

basededonne.moyenneclasse("NFA100")
basededonne.moyenneclasse2("NFA100")

basededonne.consulternoteclasse2("NFA100")
basededonne.consulternoteetudiant(1)

input()