import re
import datetime


def checkio(log_in):
    def getDomain(t):
        return re.findall('\w+\.\w{2,3}(?=[\n/ ]|$)', t)

    users = set(l.split(';;')[1].lower() for l in log_in.split())
    byUser = {u:{d:[] for d in set(getDomain(log_in))} for u in users}
    
    for line in log_in.split():
        (date, user), domain = line.split(';;')[:-1], getDomain(line)[0]
        user = user.lower()
        byUser[user][domain].append(date)
    
    log_out = []
    for u in byUser.keys():
        for dom in byUser[u].keys():
            nbConnections = len(byUser[u][dom])
            for i, stamp in enumerate(byUser[u][dom]):
                stamp = datetime.datetime(*map(int, stamp.split('-')))
                if i == 0:
                    start = stamp
                    length = 1
                    count = 1
                if i == nbConnections-1 or i > 0:
                    diff = int((stamp - start).total_seconds())
                    if diff > 1800:
                        log_out += [';;'.join(map(str,[u, dom, length, count]))]
                        length = 1
                        count = 1
                    else:
                        length += diff
                        if i > 0:
                            count += 1
                    if i == nbConnections-1:
                        log_out += [';;'.join(map(str,[u, dom, length, count]))]
                    else:
                        start = stamp
    log_out = sorted(log_out, key=lambda x: (x.split(';;')[0], x.split(';;')[1], 
                                             int(x.split(';;')[2]), 
                                             int(x.split(';;')[3])))
    return '''\n'''.join(log_out)
