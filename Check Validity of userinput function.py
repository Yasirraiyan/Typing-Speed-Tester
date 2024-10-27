def CheckValidityofinputsentence(choosingsentence):
    if(choosingsentence in sentences):
        print("The sentence is valid:")
        return 1;
    else:
        print("The sentence is invalid")
        return 0
