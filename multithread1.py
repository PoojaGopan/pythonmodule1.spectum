# from threading import Thread

# class A(Thread):
#     def run(self):
#         for i in range(5):
#             print("hi")

# class B(Thread):
#     def run(self):
#         for i in range(5):
#             print("hello")

# t1 = A()
# t2 = B()

# t1.start()
# t2.start()

# t1.join()
# t2.join()


# import threading
 
 
# def print_cube(num):
#     print("Cube: {}" .format(num * num * num))
 
 
# def print_square(num):
#     print("Square: {}" .format(num * num))
 
 
# if __name__ =="__main__":
#     t1 = threading.Thread(target=print_square, args=(10,))
#     t2 = threading.Thread(target=print_cube, args=(10,))
 
#     t1.start()
#     t2.start()
 
#     t1.join()
#     t2.join()
 
#     print("Done!")