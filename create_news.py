import os

from app import db, News, Journalist

good_news = ['weather is fine', 'economics is stable']

j1 = Journalist(id=1, name='Ann', surname='Smith', email='smith@gmail.com')
j2 = Journalist(id=2, name='Bob', surname='Bin', email='bin@gmail.com')

n1 = News(id=1, news_text='weather is fine', journalist_id=j1.id)
n2 = News(id=2, news_text='economics is stable', journalist_id=j1.id)
n3 = News(id=3, news_text='salary growth', journalist_id=j2.id)

print(f'Journalist created with name {j1.name} surname {j1.surname} email {j1.email}')

if os.path.exists('myDB.db'):
    os.remove('myDB.db')

db.create_all()

db.session.add(j1)
db.session.add(j2)
db.session.add(n1)
db.session.add(n2)
db.session.add(n3)
try:
  db.session.commit()
except Exception:
  db.session.rollback()

db.session.close()
