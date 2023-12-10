class Map:
    def __init__(self):
        self.map = {}

    def push(self, key,value):
        # Add child
        self.map[key] = value

    def get(self,key):
        value = None
        try:
            value = self.map[key]
        except KeyError as ke:
            print(f"Key not found : {key}")
            
        return value

# Example usage:
if __name__ == "__main__":
    map = Map()

    map.push("one","one")
    map.push("two","two")

    print(map.get("one"))
    print(map.get("three"))
