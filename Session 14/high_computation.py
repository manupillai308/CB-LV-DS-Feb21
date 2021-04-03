def high_computation(i):
    # really computationally heavy algorithm
    result = 1000 * i
    return { "res":result, "id": 1233 }


result = high_computation(3)
open("result.txt", "w").write(result)
print("Result computed:", result)