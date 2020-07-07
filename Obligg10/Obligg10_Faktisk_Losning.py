import tkinter
import time
import math


class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Object:
    def __init__(self, owner):
        self.owner = owner
        self.tags = []


class Transform:
    def __init__(self, position):
        self.position = position

    def translate(self, translation):
        self.position.x += translation.x
        self.position.y += translation.y


class Physics:
    def __init__(self, velocity, linear_resistance, quadratic_resistance):
        self.owner.physics_objects.append(self)
        self.velocity = velocity
        self.linear_resistance = linear_resistance
        self.quadratic_resistance = quadratic_resistance

    def __del__(self):
        self.owner.physics_objects.remove(self)
        self.owner.graphics_objects.remove(self)

    def speed(self):
        return math.sqrt(self.velocity.x ** 2 + self.velocity.y ** 2)

    def air_resistance(self, var, power):
        resistance = power
        if var == 1:
            resistance = resistance * 0.01
        else:
            resistance = 0
        return resistance

    def update(self, timestep, air_res, power):
        if self.speed() <= 3:
            self.__del__()
        self.velocity.x -= (self.velocity.x * self.linear_resistance + \
                            self.velocity.x * self.speed() * self.quadratic_resistance) * timestep
        self.velocity.x -= self.air_resistance(air_res, self.velocity.x)

        self.velocity.y -= (self.velocity.y * self.linear_resistance - 9.81 + \
                            self.velocity.y * self.speed() * self.quadratic_resistance) * timestep
        self.velocity.y -= self.air_resistance(air_res, self.velocity.y)

        self.translate(self.velocity)

    def velocity_react(self, force):
        sx = 1
        sy = 1
        if force.x != 0:
            sx = -1
        if force.y != 0:
            sy = -1

        self.velocity.x = self.velocity.x * sx * 0.5
        self.velocity.y = self.velocity.y * sy * 0.5


# Interface for collider. Depends on having a transform
class ColliderAABB:
    def __init__(self, upper_left_offset, lower_right_offset, parent):
        self.parent = parent
        self.upper_left_offset = upper_left_offset
        self.lower_right_offset = lower_right_offset

    # Returns True if the bounding box intersects with the other bounding box
    def check(self, other):
        if self.upper_left.x > other.lower_right.x:
            return False
        if self.upper_left.y > other.lower_right.y:
            return False
        if self.lower_right.x < other.upper_left.x:
            return False
        if self.lower_right.y < other.upper_left.y:
            return False
        return True

    # Returns the world space coordinate of the upper left corner
    @property
    def upper_left(self):
        return Vec2(self.parent.position.x + self.upper_left_offset.x, \
                    self.parent.position.y + self.upper_left_offset.y)

    # Returns the world space coordinate of the lower right corner
    @property
    def lower_right(self):
        return Vec2(self.parent.position.x + self.lower_right_offset.x, \
                    self.parent.position.y + self.lower_right_offset.y)


class Collision:
    def __init__(self, upper_left_offset, lower_right_offset):
        self.owner.collision_objects.append(self)
        self.collider = ColliderAABB(upper_left_offset, lower_right_offset, self)

    def __del__(self):
        self.owner.collision_objects.remove(self)

    def collides(self, other):
        if self.collider.check(other.collider):
            self.on_collision(other)

    def on_collision(self, other):
        pass


class Graphics:
    def __init__(self):
        self.owner.graphics_objects.append(self)

        print("Created graphics object")

    def __del__(self):
        self.owner.graphics_objects.remove(self)

    def draw(self):
        pass


class Ball(Physics, Collision, Transform, Object, Graphics):
    def __init__(self, position, velocity, radius, owner):
        Object.__init__(self, owner)
        Collision.__init__(self, Vec2(-radius, -radius), Vec2(radius, radius))
        Transform.__init__(self, position)
        Physics.__init__(self, velocity, 0, 0)
        Graphics.__init__(self)
        self.components = ["Transform", "Physics", "Collision", "Graphics", "Object"]
        self.radius = radius
        self.tags = ["projectile"]

    def on_collision(self, other):
        if "terrain" in other.tags:
            dx = 0
            dy = 0
            if self.collider.upper_left.x < other.collider.lower_right.x:
                dx = other.collider.lower_right.x - self.collider.upper_left.x

            if self.collider.upper_left.y < other.collider.lower_right.y:
                dy = other.collider.lower_right.y - self.collider.upper_left.y

            if self.collider.lower_right.x > other.collider.upper_left.x:
                dx = other.collider.upper_left.x - self.collider.lower_right.x

            if self.collider.lower_right.y > other.collider.upper_left.y:
                dy = other.collider.upper_left.y - self.collider.lower_right.y

            self.translate(Vec2(-self.velocity.x, -self.velocity.y))
            self.velocity_react(Vec2(dx, dy))

    def draw(self):
        self.owner.canvas.create_oval(self.position.x - self.radius, self.position.y - self.radius, \
                                      self.position.x + self.radius, self.position.y + self.radius, fill="red")


class Rectangle(Collision, Transform, Object, Graphics):
    def __init__(self, position, size, owner):
        Object.__init__(self, owner)
        Collision.__init__(self, Vec2(-size.x / 2, -size.y / 2), Vec2(size.x / 2, size.y / 2))
        Transform.__init__(self, position)
        Graphics.__init__(self)
        self.components = ["Transform", "Collision", "Graphics", "Object"]
        self.tags = ["terrain"]
        self.size = size

    def draw(self):
        self.owner.canvas.create_rectangle(self.position.x - self.size.x / 2, self.position.y - self.size.y / 2, \
                                           self.position.x + self.size.x / 2, self.position.y + self.size.y / 2,
                                           fill="blue")


class Application:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.main_window, \
                                     width=800, height=600, \
                                     borderwidth=0, highlightthickness=0, bg="black")
        self.canvas.grid(row=0, column=0, columnspan=5, rowspan=5)

        self.physics_objects = []
        self.collision_objects = []
        self.graphics_objects = []

        self.slider_power = tkinter.Scale(self.main_window, from_=1, to=100, orient=tkinter.HORIZONTAL,
                                          label="POWER!!!")
        self.slider_angle = tkinter.Scale(self.main_window, from_=1, to=45, orient=tkinter.HORIZONTAL, label="Angle")
        self.activate_button = tkinter.Button(self.main_window, text="Skyt!", command=self.start)

        self.var = tkinter.IntVar()
        self.checkbox = tkinter.Checkbutton(self.main_window, text="Air Resistance", variable=self.var).grid(row=5,
                                                                                                             column=4)

        self.slider_power.set(25)
        self.slider_angle.set(25)

        self.slider_power.grid(row=5, column=1)
        self.slider_angle.grid(row=5, column=2)
        self.activate_button.grid(row=5, column=3)

        o = Ball(Vec2(200, 475), Vec2(-self.slider_power.get(), self.slider_angle.get()), 5, self)
        obstical = Rectangle(Vec2(350, 470), Vec2(10, 80), self)
        mark = Rectangle(Vec2(600, 470), Vec2(30, 30), self)
        r = Rectangle(Vec2(400, 500), Vec2(800, 30), self)
        self.canvas.create_rectangle(0, 0, 800, 600, fill="white")

        for obj in self.graphics_objects:
            obj.draw()

        self.main_window.update()

        self.main_window.mainloop()

    def start(self):

        self.main_window.update()
        # Spawn canon

        o = Ball(Vec2(200, 475), Vec2(-self.slider_power.get(), self.slider_angle.get()), 5, self)
        self.loop()

    def loop(self):

        previous_time = time.time()
        while True:
            self.canvas.delete("all")
            self.canvas.create_rectangle(0, 0, 800, 600, fill="white")
            new_time = time.time()
            for obj in self.physics_objects:
                obj.update((new_time - previous_time), self.var.get(), self.slider_power.get())

            for i in range(len(self.collision_objects)):
                for j in range(len(self.collision_objects)):
                    obj1 = self.collision_objects[i]
                    obj2 = self.collision_objects[j]
                    obj1.collides(obj2)

            for obj in self.graphics_objects:
                obj.draw()

            previous_time = new_time

            self.main_window.update()
            self.main_window.update_idletasks()
            time.sleep(0.0165)

if __name__ == "__main__":
    app = Application()
