from sqlalchemy import create_engine, ForeignKey, Column, Integer, String

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #to supress warnings
db = SQLAlchemy(app)

#declaring the Book model
class Vacature(db.Model):
    __tablename__ = 'vacatures'
    id = db.Column(db.Integer, primary_key = True) #primary key column, automatically generated IDs
    bedrijf_id = Column(Integer, ForeignKey('bedrijven.id'))
    title = db.Column(db.String(80), index = True, unique = True) # function title
    salary = db.Column(db.Integer, index = True, unique = False) #salary indication
    location = db.Column(db.String(20), index = True, unique = False) # job location
    description = db.Column(db.String(200), index = True, unique = False) #short job description
    
    #Get a nice printout for vacature objects
    def __repr__(self):
        return "{} in: {},{},{}".format(self.title, self.salary, self.location, self.description)
    
    #Een bedrijf kan meerdere vacatures hebben uitstaan, daarom willen we bedrijven aan vacatures koppelen en omgekeerd.
    
class Bedrijf(db.Model):
    __tablename__ = 'bedrijven'
    id = db.Column(db.Integer, primary_key = True) # primary key column for company
    name_bedrijf = db.Column(db.String(50), index = True, unique = False) #name of company
    contact_persoon_voornaam = db.Column(db.String(80), unique = False, index = True) # contact person first name
    contact_persoon_achter_naam = db.Column(db.String(80), unique = False, index = True) # contact person last name
    email = db.Column(db.String(120), unique = True, index = True) #email adres of contact person
    
    #add your relationship column here
    bedrijf = relationship("Bedrijf", backref="vacature") #klopt dit?
  
    #get a nice printout for bedrijf objects
    def __repr__(self):
        return "bedrijf: {}".format(self.email)
    
#   Deze moeten uiteindelijk in de DB:  
#    [
#     {'id' : 1,
#      'title' : 'Data Analyst',
#      'location' : ' Zevenhuizen, Zuid - Holland',
#      'salaris' : '5000 euro per maand'
#     },
#     {'id' : 2,
#      'title' : 'Medische analyst',
#      'location' : 'Gouda, Zuid - Holland',
#      'salaris' : '4000 euro per maand'
#     },
#     {'id' : 3,
#      'title' : 'Junior C# developer',
#      'location' : 'Brielle, Zuid - Holland',
#      'salaris' : '3500 euro per maand'
#     },
#     {'id' : 4,
#      'title' : 'Copywriter',
#      'location' : 'Rotterdam, Zuid - Holland',
#      'salaris' : '3000 euro per maand'
#     },   
#     {'id' : 5,
#      'title' : 'Python programmer',
#      'location' : 'Hybride',
#      'salaris' : '4800 euro per maand'
#     },
#     {'id' : 6,
#      'title' : 'Grafisch ontwerper',
#      'location' : 'Hybride',
#     },
#     {'id' : 5,
#      'title' : 'Python programmer',
#      'location' : 'Rotterdam, hybride',
#      'salaris' : '4800 euro per maand'
#     }
# ] 