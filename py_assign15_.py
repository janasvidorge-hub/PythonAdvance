
import gc

# Display initial garbage collection status
print("Automatic GC Enabled:", gc.isenabled())

# Display garbage collection thresholds
print("GC Thresholds:", gc.get_threshold())

# Create a class
class Demo:
    def __init__(self, name):
        self.name = name

# Disable automatic garbage collection
gc.disable()
print("\nAutomatic Garbage Collection Disabled")

# Create circular references
obj1 = Demo("Object 1")
obj2 = Demo("Object 2")

obj1.ref = obj2
obj2.ref = obj1

print("Objects with circular references created.")

# Delete external references
del obj1
del obj2

print("External references deleted.")

# Perform manual garbage collection
collected = gc.collect()

print("Garbage Collection Completed.")
print("Objects Collected:", collected)

# Display garbage collection count
print("GC Count:", gc.get_count())

# Enable automatic garbage collection again
gc.enable()

print("\nAutomatic GC Enabled:", gc.isenabled())
