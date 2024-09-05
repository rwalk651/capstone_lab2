from dataclasses import dataclass

@dataclass
class Students:
    name: str
    id: str
    gpa: float

def main():
    sam = Students('sam', 'eie3', 3.4)
    alex = Students('alex', '1234', 3.8)
    print(sam)
    print(alex)

if __name__ == '__main__':
    main()

# dataclass is more human readable, less typing
# be aware of how dataclass will generate string for each statement