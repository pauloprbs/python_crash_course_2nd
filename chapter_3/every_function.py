watched_series = ['wandinha', 'the good place', 'os aneis do poder', 'record of ragnarok', 'serie']

print(watched_series)

watched_series.append('serie para usar pop')
watched_series.insert(0, 'serie para dar del')

print(watched_series)

del watched_series[0]

print(watched_series)

watched_series.pop()

print(watched_series)

watched_series.remove('serie')

print(watched_series)

print(sorted(watched_series))

print(sorted(watched_series, reverse=True))

print(watched_series)

watched_series.sort()

print(watched_series)

watched_series.sort(reverse=True)

print(watched_series)

watched_series.reverse()

print(watched_series)

print(len(watched_series))
