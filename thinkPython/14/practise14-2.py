def sed(pattern, replace, source_file, dest_file):
    try:
        fin = open(source_file)
        fout = open(dest_file, 'w')
        for line in fin:
            if pattern in line:
                line = line.replace(pattern, replace)
            fout.write(line)
        fin.close
        fout.close
    except:
        print 'Something went wrong.'
    