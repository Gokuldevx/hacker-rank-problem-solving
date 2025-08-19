from datetime import datetime
def timeConversion(s):
    # Write your code here
    convert = datetime.strptime(s, "%I:%M:%S%p").strftime("%H:%M:%S")
    return convert

if __name__ == '__main__':
  
    s = input()
    result = timeConversion(s)
    print(result)
