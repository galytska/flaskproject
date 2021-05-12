import os

from app import db
from models import Journalist, News

j1 = Journalist(id=1, name='Ann', surname='Smith', email='smith@gmail.com')
j2 = Journalist(id=2, name='Bob', surname='Bin', email='bin@gmail.com')

n1 = News(id=1,
          title='fine weather',
          text='Weather is driven by air pressure, temperature, '
               'and moisture differences between one place and another. '
               'These differences can occur due to the Sun\'s angle at any particular spot, '
               'which varies with latitude. The strong temperature contrast between polar and '
               'tropical air gives rise to the largest scale atmospheric circulations: '
               'the Hadley cell, the Ferrel cell, the polar cell, and the jet stream.',

          journalist_id=j1.id)
n2 = News(id=2,
          title='stable economics',
          text='Economics focuses on the behaviour and interactions of economic agents and how economies work. '
               'Microeconomics analyzes basic elements in the economy, including individual agents and markets, '
               'their interactions, and the outcomes of interactions. Individual agents may include, for example, '
               'households, firms, buyers, and sellers.',

          journalist_id=j1.id)
n3 = News(id=3,
          title='salary growth',
          text='A salary is a form of payment from an employer to an employee, which may be specified in an '
               'employment contract. It is contrasted with piece wages, where each job, hour, or other unit is paid '
               'separately, rather than on a periodic basis. From the point of view of running a business, '
               'salary can also be viewed as the cost of acquiring and retaining human resources for running '
               'operations, and is then termed personnel expense or salary expense. In accounting, salaries are '
               'recorded on payroll accounts.',

          journalist_id=j2.id)

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
