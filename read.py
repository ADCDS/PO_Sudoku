def read_instance():
    with open('instances/instance1.txt') as f:
        array = []
        for line in f: # read rest of lines
            array.append([int(x) for x in line.split()])
        return array
