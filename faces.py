
def convert(string):
    new_string=string.replace(":)","🙂")
    new_string=new_string.replace(":(","🙁")
    return new_string

def main():
    string=input()
    print(convert(string))
main()
