import random

class flashTerm (object):
    flashcards = {'mortgage': 'an agreement that allows you to borrow money from a bank by offering something of value, like a house',
    'interest': 'the money you own regulary on a loan, or the extra money you make when you invest',
    'taxes': 'money you must pay to the goverment off your income, business profits, or consumer goods',
    'equity': 'your value of ownership in a company or property. it belongs to you',
    'save': 'when you get money and you do not spend it',
    'marketing': 'when you tell and promote your products or services to people in order for them to buy it',
    'stock': 'the money raised by a business or corporation when they issue you shares',
    'diversification': 'investing in a variety of securities, so that you can avoid an economic slump',
    'risk': 'exposure to a chance of loss',
    'inflation': 'a rise in prices or a fall in the value of money',
    'leverage': 'the use of debt to acquire business',
    'liquidity': 'the ability or ease with which assets can be converted into cash',
    'illiquid': 'not readily covertible into cash',
    'capital': 'the wealth, whether in money or property, owned or employed in business by an individual, firm, corporation, etc.',
    'annuity': 'a sum of money or an investment that is paid at regular intervals',
    'future value': 'the amount that an investment will be worth at a future date if it is invested at a compounded interest rate',
    'investment': 'the investing of money or capital in order to gain profitable returns',
    'roi': 'return on investment',
    'bond': 'to place a debt on or secure a debt',
    'stock broker': 'someone employed by a member firm of a stock exchange, who buys and sells stocks and other securities for customers',
    'volatility': 'how much and how quickly the value of an investment, market, or market sector changes',
    'dividend': 'a sum of money paid to shareholders of a corporation out of earnings',
    'annual report': 'a required document that is made available to shareholders on a yearly basis. it discloses certain aspects of a funds operations and financial condition',
    'securities and exchange commission': 'a goverment commission created by congress to regulate the securities markets and protect investors',
    'mutual fund': 'an investment program funded by shareholders that trades in diversified holdings and is professionally managed',
    'investment club': 'a group of people who pool their money to make investments',
    'bull market': 'a market in which share prices are rising, encouraging buying',
    'bear market': 'a market in which prices are falling, encouraging selling',
    'cash': 'money in coins or bills',
    'loan': 'something that is borrowed especially a sum of money that is expected to be paid back with interest',
    'income': 'money you receive on regular basis for work or through investments',
    'invest': 'using money to receive a profit by putting it into the stock market through shares, or property like a house',
    'consumer': 'a person who buys goods and services for personal use',
    'producer': 'a person, conpany, or country that makes, grows, or supplies goods for sale',
    'stock market': 'a particular market where stocks and bonds are traded',
    'assets classes': 'a class of investments that have similar characteristics, including risk factors and how returns are created',
    'capital gain': 'profit from the sale of assets, as bonds or real estate'}
    flash_list = list(flashcards.keys())
    term = random.choice(flash_list)
    
