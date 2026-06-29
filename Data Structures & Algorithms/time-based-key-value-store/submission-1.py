class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timemap:
            self.timemap[key].append((timestamp, value))
        else:
            self.timemap[key] = []
            self.timemap[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""

        else:
            values = self.timemap[key]
            l = 0
            r = len(values) -1

            while l <= r:
                mid = (l + r) // 2
                if values[mid][0] == timestamp:
                    return values[mid][1]
                
                elif values[mid][0] < timestamp:
                    l = mid + 1
                else:
                    r = mid -1
            if r != -1:
                return values[r][1]
            else:
                return ""
