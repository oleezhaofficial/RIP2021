data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]


def main():
    result = sorted(data, key=abs, reverse=True)
    print(result)
    
    result_with_lambda = (lambda mass : sorted(mass, key=abs, reverse=True))(data)
    print (result_with_lambda)

if __name__ == "__main__":
    main()