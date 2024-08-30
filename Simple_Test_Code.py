import webbrowser

def search_code(url):
    print("Your searching :", search_item)
    print(" ")
    webbrowser.open(url)



print("**************************************")
print("------------ Search Web --------------")
print("**************************************")

print(" ")
print("       Select searching option")
print(" ")
print(" Enter 01 for Google Search Engine")
print(" Enter 02 for Youtube Search")
print(" Enter 03 for Go to Chat GPT")
print(" ")

search_option = int(input("Enter Searching Option Number :"))
print(" ")

while True:
    if (search_option == 1):
        search_item = input("Type Here : ")
        url = "https://www.google.com/search?q=" + search_item
        search_code(url)
        continue

    elif (search_option == 2):
        search_item = input("Type Here : ")
        url = "https://www.youtube.com/results?search_query=" + search_item
        search_code(url)
        continue

    elif (search_option == 3):
        url = "https://www.chatgpt.com/"
        webbrowser.open(url)
        break

    else:
        print("Please re check your searching option number is corect")
        break
