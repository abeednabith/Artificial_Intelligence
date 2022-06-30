def main():
    x1 = [117, 120, 145, 129, 132, 130, 110, 163, 136, 115, 118, 132, 111, 112]

    print("max: ", max(x1))
    print("min: ", min(x1))
    print("range: ", max(x1)-min(x1))
    sum = 0
    rng = max(x1)-min(x1)
    for i in range(len(x1)):
        sum += x1[i]
    print("sum: ", sum)
    aver = sum/len(x1)
    print("mean = ", aver)
    x2s = [0]*len(x1)
    for i in range(len(x1)):
        devation = float(x1[i]-aver)
        x2s[i] = devation/rng
    X2s = ["%.3f" % elem for elem in x2s]
    print("X2s", X2s)


if __name__ == "__main__":
    main()
