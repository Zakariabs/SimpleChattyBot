# put your python code here

length = int(input())
width = int(input())
height = int(input())

sum_lengths_edges = 4*(length + width + height)
print(sum_lengths_edges)
surface_area = 2*(length * width + width * height + length * height)
print(surface_area)
volume = length * width * height
print(volume)


