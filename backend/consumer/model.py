from flask_sqlalchemy import SQLAlchemy
from config import app
import json


db = SQLAlchemy(app)


  # Title
  # Tournament
  # Team
  # Match
  # Scores of a Team in a Match

class Title(db.Model):
    __tableName__ = "title"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    state = db.Column(db.Integer,nullable=False)

    @staticmethod
    def Insert(_Title,_state):
        _Title = _Title.strip()
        print(_Title)
        print(Title.query.filter_by(title=_Title).count())
        if Title.query.filter_by(title=_Title).count()==0:
            new_title = Title(title= _Title,state=_state)
            try:
                db.session.add(new_title)
                db.session.commit()
                print('add Title')
            except:
                return 'error'

class Tournament(db.Model):
    __tableName__ = "tournamet"
    id = db.Column(db.Integer, primary_key=True)
    tournament = db.Column(db.String(120), nullable=False)
    date_start_text = db.Column(db.String(120),nullable=False)
    # ForeignKey
    title = db.relationship('Title', backref='tournamet', lazy=True)
    title_id = db.Column(db.Integer, db.ForeignKey('title.id'))

    @staticmethod
    def Insert(_Tournament,_title,_date_start_text):
        _Tournament=_Tournament.strip()
        _title=_title.strip()
        if (Tournament.query.filter_by(Tournament=_Tournament).count==0):
            Title_id = Title.query.filter_by(title=_title).first().id
            new_tournaments = Tournament(tournament=_Tournament,title_id=Title_id,date_start_text=_date_start_text)
            try:
                db.session.add(new_tournaments)
                res = db.session.commit()
                print('add Tournament')
            except:
                return 'error'

class Team(db.Model):
    __tableName__ = "team"
    id = db.Column(db.Integer, primary_key=True)
    Team = db.Column(db.String(120), nullable=False)
    # Team_id = db.Column(db.Integer,nullable=False)

    @staticmethod
    def Insert(_Team_id,_Team):
        if (Team.query.filter_by(id=_Team_id).count==0):
            new_team = Team(id=_Team_id,Team=_Team)
            try:
                db.session.add(new_team)
                db.session.commit()
                print('add Team')
            except:
                return 'error'

class Matches(db.Model):
    __tableName__ = "matches"
    id = db.Column(db.Integer, primary_key=True)
     # ForeignKey
    tournament = db.relationship('Tournament', backref='tournamet', lazy=True)
    Tournament_id = db.Column(db.Integer, db.ForeignKey('tournament.id'))
     # ForeignKey
    Team1_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    Team2_id = db.Column(db.Integer, db.ForeignKey('team.id'))

    Team1 = db.relationship('Team', foreign_keys='team',backref='team1_id', lazy=True)
    Team2 = db.relationship('Team', foreign_keys='team',backref='team2_id', lazy=True)

# class Company(Base):
#     __tablename__ = 'company'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50), nullable=False)

# class Stakeholder(Base):
#     __tablename__ = 'stakeholder'
#     id = Column(Integer, primary_key=True)

#     company_id = Column(Integer, ForeignKey('company.id'), nullable=False)
#     stakeholder_id = Column(Integer, ForeignKey('company.id'), nullable=False)
#     company = relationship("Company", foreign_keys=[company_id])
#     stakeholder = relationship("Company", foreign_keys=[stakeholder_id])











# class Scores(db.Model):
#     __tableName__ = "scores"
#     team_id = db.Column(db.Integer, primary_key=True)
#     winner = db.Column(db.String(120), nullable=False)
#     Score = db.Column(db.String(120), nullable=False)




    # def json(self):
    #     return {
    #                                 'id': self.id, 
    #                                 'Title': self.Title, 
    #                                 'Tournament': self.Tournament,
    #                                 'Team': self.Team,
    #                                 'Match': self.Match,
    #                                  'Scores': self.Scores
    #                                 }

    # def __repr__(self):
    #     json_matches_table = {
    #                             'id': self.id, 
    #                             'Title': self.Title, 
    #                             'Tournament': self.Tournament,
    #                             'Team': self.Team,
    #                             'Match': self.Match,
    #                             'Scores': self.Scores
    #     }
    #     return json.dumps(json_matches_table)




