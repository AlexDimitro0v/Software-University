# Create a STOP sign
# 26th March 2016 - SoftUni exam question.


def stop_sign(n):
    # range_rows = 5*n
    underscore = 2*n + 1

    dots = n+1

    # UPPER Part
    print('.'*dots + '_'*underscore + '.'*dots)              # static line

    dots2 = n
    for rows in range(1, n+2):
        if rows == n+1:
            print("//"+"_"*((underscore+(dots*2) - (4+5))//2)+"STOP!"+'_'*((underscore+(dots*2) - (4+5)) // 2) + '\\\\')
        else:
            print("." * dots2 + "//" + "_" * (underscore+(dots*2) - ((dots2*2)+4)) + '\\\\' + "." * dots2)
            dots2 -= 1
    # LOWER Part
    print("\\\\" + '_'*(underscore + (dots*2)-4) + '//')     # static line

    dots3 = 1
    for rows in range(1, n):
        print('.'*dots3+'\\\\'+'_'*(underscore+(dots*2) - (dots3*2+4))+'//'+'.'*dots3)
        dots3 += 1


def main():
    n = int(input())
    stop_sign(n)


if __name__ == '__main__':
    main()
