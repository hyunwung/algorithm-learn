def solution(cacheSize, cities):
    cache = []
    time = 0
    for city in cities:
        city = city.lower()
        if cacheSize:
            if not city in cache:
                if len(cache) == cacheSize:
                    cache.pop(0)
                cache.append(city)
                time += 5
            else:
                cache.pop(cache.index(city))
                cache.append(city)
                time += 1
        else:
            print("여기")
            time += 5

    print(time)
    return time
solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])