# Write a program to ask the user which browser he wants to run automation

browser_name = input("Enter the name of the browser\n")
browser_name = browser_name.lower()
match browser_name:
    case "firefox":
        print("Execute the firefox")
    case "chrome":
        print("execute the chrome ")
    case "edge":
        print("execute the edge")