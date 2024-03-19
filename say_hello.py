def say_hello(name, city, state):
    print(len(name))
    #a = name[0]
    #for x in range(len(name)):
    #   new_name = a.join(name[x])
    x = 1
    new_name = name[0]
    while x < len(name):
        new_name = new_name + " " + name[x]
        x = x + 1
    return f'Hello, {new_name}! Welcome to {city}, {state}!'
    
    
print(say_hello(['Franklin','Delano','Roosevelt','Otto'], 'Phoenix', 'Arizona'))