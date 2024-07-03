lang = input("qual sua lingagem de programação favorita? ")

match lang:
    case "javascript":
        print ("voce pode se tornar um desenvolvedor web")
    case "python":
        print ("voce pode se tornar um cientista de dados")
    case "php":
        print ("voce pode se tornar um desenvolvedor back-end")
    case "solidity":
        print ("voce pode se tornar um desenvolvedor blockchain")
    case "java":
        print ("voce pode se tornar um desenvolvedor de aplicativos mobile")
    case _:
        print ("a linguagem não interessa, o que interessa é resolver problemas")