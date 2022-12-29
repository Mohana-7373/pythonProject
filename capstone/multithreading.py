#single threading
import time
#start function is to count the starting time of first thread
start = time.perf_counter()
#defineing a method called calcutetime  it's function is to stop the thread for 5 seconds after one thread is executed
def CalculateTime():
    print("sleep for 5 seconds")
    time.sleep(5)
    print("completed sleep")
#calling the function to excute the code written in respective method
CalculateTime()
CalculateTime()
CalculateTime()
#finish work is to count the ending time of last thread
finish = time.perf_counter()
#print function is to show the total time taken by all threads to complete the execution
print(f'Finished in {finish - start} seconds')

import threading

start = time.perf_counter()


def CalculateTime():
    print("sleep for 5 seconds \n")
    time.sleep(5)
    print("completed sleep\n")

t1 = threading.Thread(target=CalculateTime)
t2 = threading.Thread(target=CalculateTime)
t3 = threading.Thread(target=CalculateTime)
t4 = threading.Thread(target=CalculateTime)

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

finish = time.perf_counter()

print(f'Finished in {finish - start} seconds')


#loop with threads
import time
import threading

start = time.perf_counter()

def CalculateTime(seconds):
    print(f"sleep for {seconds} second \n")
    time.sleep(5)
    print(f"completed {seconds} sleep \n")
threads = []

for _ in range(5):
    thread = threading.Thread(target=CalculateTime,args=[3])
    thread.start()
    threads.append(thread)

for t in threads:
    t.join()

finish = time.perf_counter()
print(threads)
print(f'Finished in {finish - start} seconds')

#WITH threads
import concurrent.futures
start = time.perf_counter()
def CalculateTime(seconds):
    print(f"sleep for {seconds} second \n")
    time.sleep(5)
    return f"completed {seconds} sleep \n"
list_a = [5, 10, 15, 20, 25]
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(CalculateTime,i)for i in list_a ]
    for r in concurrent.futures.as_completed(results):
        print(r.result())
finish = time.perf_counter()
print(f'Finished in {finish - start} seconds')









#######real world example
import requests
import time

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

t1 = time.perf_counter()

for img_url in img_urls:
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')

finish = time.perf_counter()

print(f'Finised in {finish - start} seconds')