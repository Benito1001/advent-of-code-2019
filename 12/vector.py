import math

class Vector3:
	def __init__(self, x=0, y=0, z=0):
		self.x = x
		self.y = y
		self.z = z

	def __len__(self):
		return 3

	def __getitem__(self, key):
		if key == 0:
			return self.x
		elif key == 1:
			return self.y
		elif key == 2:
			return self.z
		else:
			raise IndexError("Invalid subscript "+str(key)+" to Vec2d")

	def __setitem__(self, key, value):
		if key == 0:
			self.x = value
		elif key == 1:
			self.y = value
		elif key == 2:
			self.z = value
		else:
			raise IndexError("Invalid subscript "+str(key)+" to Vec2d")

	# String representaion (for debugging)
	def __repr__(self):
		return f"[{self.x}, {self.y}, {self.z}]"

	# Comparison
	def __eq__(self, other):
		if hasattr(other, "__getitem__") and len(other) == 3:
			return self.x == other[0] and self.y == other[1] and self.z == other[2]
		else:
			return False

	def __ne__(self, other):
		if hasattr(other, "__getitem__") and len(other) == 3:
			return self.x != other[0] or self.y != other[1] and self.z == other[2]
		else:
			return True

	# Addition
	def __add__(self, other):
		if isinstance(other, Vector3):
			return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
		elif hasattr(other, "__getitem__"):
			return Vector3(self.x + other[0], self.y + other[1], self.z + other[2])
		else:
			return Vector3(self.x + other, self.y + other, self.z + other)
	__radd__ = __add__

	# Subtraction
	def __sub__(self, other):
		if isinstance(other, Vector3):
			return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
		elif (hasattr(other, "__getitem__")):
			return Vector3(self.x - other[0], self.y - other[1], self.z - other[2])
		else:
			return Vector3(self.x - other, self.y - other, self.z - other)

	def __rsub__(self, other):
		if isinstance(other, Vector3):
			return Vector3(other.x - self.x, other.y - self.y, other.z - self.z)
		if (hasattr(other, "__getitem__")):
			return Vector3(other[0] - self.x, other[1] - self.y, other[2] - self.z)
		else:
			return Vector3(other - self.x, other - self.y, other - self.z)

	# Multiplication
	def __mul__(self, other):
		if isinstance(other, Vector3):
			return Vector3(self.x*other.x, self.y*other.y, self.z*other.z)
		if (hasattr(other, "__getitem__")):
			return Vector3(self.x*other[0], self.y*other[1], self.z*other[2])
		else:
			return Vector3(self.x*other, self.y*other, self.z*other)
	__rmul__ = __mul__

	# Unary operations
	def __neg__(self):
		return Vector3(operator.neg(self.x), operator.neg(self.y), operator.neg(self.z))

	def __pos__(self):
		return Vector3(operator.pos(self.x), operator.pos(self.y), operator.pos(self.z))

	def __abs__(self):
		return Vector3(abs(self.x), abs(self.y), abs(self.z))

	def __invert__(self):
		return Vector3(-self.x, -self.y, -self.z)

	# vectory functions
	def get_length_sqrd(self):
		return self.x**2 + self.y**2 + self.z**2

	def get_length(self):
		return math.sqrt(self.x**2 + self.y**2, + self.z**2)
	def __setlength(self, value):
		length = self.get_length()
		self.x *= value/length
		self.y *= value/length
		self.z *= value/length
	length = property(get_length, __setlength, None, "gets or sets the magnitude of the vector")

	def normalize(self):
		length = self.length
		if length != 0:
			return self*(1/length)
		return Vec2d(self)

	def to_tuple(self):
		return (self.x, self.y, self.z)
