# App 5: Weather client app

![image](app-5.png)

Key concepts showcased
=================

**Python Package Index (PyPI)**

[https://pypi.python.org/pypi](https://pypi.python.org/pypi)

**pip**

    pip3 list
    pip3 install requests

**Requests package**

Quick start: [http://docs.python-requests.org/en/master/user/quickstart/](http://docs.python-requests.org/en/master/user/quickstart/)

**Beautiful soup package**

Quick start: [http://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start](http://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start)

**tuples**

    # Create a tuple
    m = (22.5, 44.234, 19.02, 'strong')

    temp = m[0]      # 22.5
    quality = m[3]   # 'strong'

    print(m) # (22.5, 44.234, 19.02, 'strong')

    # tuple unpacking
    t, la, lo, q = m

**namedtuples**

    import collections
    
    # Define a named tuple 'type'
    Measurement = collections.namedtuple('Measurement', 
    'temp, lat, long, quality')
 
    # Create an instance of that type of named tuple
    m = Measurement(22.5, 44.234, 19.02, 'strong')

    temp = m[0]          # old skool
    temp = m.temp        # new hotness
    quality = m.quality  # new hotness

    print(m)
    # Measurement(temp=22.5, lat=44.234, 
        long=19.02, quality='strong')
