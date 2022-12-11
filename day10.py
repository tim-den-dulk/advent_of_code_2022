from get_inputs import GetInputs


class RayTube:
    def __init__(self, data):
        self.cycle = 0
        self.x = 1
        self.value = 0
        self.data = data
        self.monitor=""

    def update_cycle(self, addx):
        self.cycle += 1
        if self.cycle % 40 == 20 and self.cycle < 221:
            self.value += self.cycle * self.x
        self.draw_pixel()
        self.x += int(addx)

    def draw_pixel(self):
        if (self.cycle-1)%40 in range(self.x-1,self.x+2):
            self.monitor+="#"
        else:
            self.monitor+="."
        if self.cycle%40==0:
            self.monitor+="\n"

    def run(self):
        for line in self.data:
            if line == "noop":
                self.update_cycle(0)
            else:
                addx = line.split()[1]
                self.update_cycle(0)
                self.update_cycle(addx)


data = GetInputs(10).lines()
raytube = RayTube(data)
raytube.run()
print(raytube.value)
print(raytube.monitor)
