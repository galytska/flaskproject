from app import db, News

good_news = ['weather is fine', 'economics is stable']

for news in good_news:
    db.session.add(News(news_text=news))
db.session.commit()
