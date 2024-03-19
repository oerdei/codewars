def say_hello(name, city, state):
    print(len(name))
    return f'Hello, {name[0]} {name[1]}! Welcome to {city}, {state}!'
    
    
print(say_hello(['John', 'Smith'], 'Phoenix', 'Arizona'))