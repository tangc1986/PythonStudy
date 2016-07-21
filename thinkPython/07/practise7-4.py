def eval_loop():
    while True:
        string = raw_input('Input(done to quit): ')
        if string == 'done':
            print 'Done!!'
            break
        print eval(string)
        
eval_loop()
    