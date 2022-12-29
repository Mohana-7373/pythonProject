import os
import concurrent.futures
import time
start = time.perf_counter()
def find_files(filename, search_path):
    result = []

    # Walking top-down from the root
    for root, dir, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root, filename))
    return result
Drives=["C:","D:","E:","F:"]
input_file='Empty_File.txt'
with concurrent.futures.ThreadPoolExecutor() as executor:
    results=[executor.submit(find_files,input_file,drive) for drive in Drives]

    for r in concurrent.futures.as_completed(results):
        print(r.result())

finish = time.perf_counter()

print(f'Finished in {finish - start} seconds')



#print(find_files("Text document.txt")