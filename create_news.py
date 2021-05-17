"""
Fill Data Base with initial test data
All Previous data will be deleted!
"""
import logging
import os

from app import db
from models import Journalist, News
from tests.test_data import journalist1, journalist2

filename = os.path.splitext(__file__)[0]
logging.basicConfig(filename=f'{filename}.log',
                    format='%(asctime)s,%(msecs)d '
                           '%(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    filemode='w',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.info("Start create DB data")


j1 = Journalist(id=1, name='Ann', surname='Smith', email='smith@gmail.com', password_hash=hash)
j1.set_password(journalist1['password'])
j2 = Journalist(id=2, name='Bob', surname='Bin', email='bin@gmail.com')
j2.set_password(journalist2['password'])
n1 = News(id=1,
          title='fine weather',
          text='Weather is driven by air pressure, '
               'temperature, '
               'and moisture differences between '
               'one place and another. '
               'These differences can occur due to the Sun\'s angle '
               'at any particular spot, '
               'which varies with latitude. '
               'The strong temperature contrast between polar and '
               'tropical air gives rise to '
               'the largest scale atmospheric circulations: '
               'the Hadley cell, the Ferrel cell, '
               'the polar cell, and the jet stream.',

          journalist_id=j1.id)
n2 = News(id=2,
          title='stable economics',
          text='Economics focuses on the behaviour and interactions '
               'of economic agents and how economies work. '
               'Microeconomics analyzes basic elements in the economy, '
               'including individual agents and markets, '
               'their interactions, and the outcomes of interactions. '
               'Individual agents may include, for example, '
               'households, firms, buyers, and sellers.',

          journalist_id=j1.id)
n3 = News(id=3,
          title='salary growth',
          text='A salary is a form of payment from an employer '
               'to an employee, which may be specified in an '
               'employment contract. It is contrasted with piece wages, '
               'where each job, hour, or other unit is paid '
               'separately, rather than on a periodic basis. '
               'From the point of view of running a business, '
               'salary can also be viewed as the cost of acquiring '
               'and retaining human resources for running '
               'operations, and is then termed personnel expense '
               'or salary expense. In accounting, salaries are '
               'recorded on payroll accounts.',

          journalist_id=j2.id)

if os.path.exists('myDB.db'):
    os.remove('myDB.db')
    logger.warning('Previous DB was deleted')

db.create_all()

db.session.add(j1)
logger.info(
    f'Journalist created with name "{j1.name}" '
    f'surname "{j1.surname}" email "{j1.email}"')
db.session.add(j2)
logger.info(
    f'Journalist created with name "{j2.name}" '
    f'surname "{j2.surname}" email "{j2.email}"')
db.session.add(n1)
logger.info(f'News was added with title "{n1.title}"')
db.session.add(n2)
logger.info(f'News was added with title "{n2.title}"')
db.session.add(n3)
logger.info(f'News was added with title "{n3.title}"')
try:
    db.session.commit()
    logger.info('new DB was created')
except Exception as e:
    db.session.rollback()
    logger.error(e)

db.session.close()
