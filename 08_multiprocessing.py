import multiprocessing
import time


def calculate_square(number: int) -> None:
    result = number ** 2
    print(f"Process {multiprocessing.current_process().name}: {number}² = {result}")


def main():

    numbers = [2, 4, 6, 8]

    processes = []

    start_time = time.perf_counter()

    for number in numbers:
        process = multiprocessing.Process(
            target=calculate_square,
            args=(number,)
        )

        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    end_time = time.perf_counter()

    print(f"\nExecution Time: {end_time - start_time:.4f} seconds")
    print("All processes completed.")


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
