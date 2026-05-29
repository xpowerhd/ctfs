import itertools
import string
import multiprocessing

def try_keys(start, step, cipher_text, charset):

    for index, combo in enumerate(itertools.product(charset, repeat=5)):

		# Only process combos where index % step == start (to split work)
        if index % step != start:
            continue

        xored = ""
        rand_str = ''.join(combo) * 16

        for i in range(len(cipher_text)):
            xored += chr(ord(cipher_text[i]) ^ ord(rand_str[i % len(rand_str)]))

        if "THM{" in xored and "}" in xored:
            print(f"Found candidate: {xored}")
            answer = input("Is that right? (YES to confirm): ")
            if answer.strip().upper() == "YES":
                return xored
    return None

if __name__ == "__main__":
    cipher_text = "67222c4334020b0d56307612157930475e0253277204130b255f26185011411e18083141122e4a39"
    charset = string.ascii_lowercase + string.ascii_uppercase + string.digits

    num_processes = multiprocessing.cpu_count()
    print(f"Using {num_processes} processes")

    pool = multiprocessing.Pool(processes=num_processes)

    # Each process gets a different starting index in the keyspace
    results = [pool.apply_async(try_keys, args=(i, num_processes, cipher_text, charset)) for i in range(num_processes)]

    pool.close()

    # Wait for processes and check for successful result
    for r in results:
        xored = r.get()
        if xored is not None:
            print("Decryption confirmed:", xored)
            pool.terminate()  # Stop other processes
            break

    pool.join()
