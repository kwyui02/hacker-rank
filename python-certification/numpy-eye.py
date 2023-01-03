import numpy
numpy.set_printoptions(legacy="1.13")


def main(N, M):
    matrix = numpy.eye(N, M, k=0)
    print(matrix)


if __name__ == '__main__':
    input_list = input().split(" ")
    N = int(input_list[0])
    M = int(input_list[1])
    main(N, M)
